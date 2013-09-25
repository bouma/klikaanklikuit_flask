#!../venv/bin/python
import os
from flask import Flask
from flask import render_template
import time
from datetime import datetime

app = Flask(__name__)
app.config.from_object(os.getenv('RASP_PYSETTINGS', 'default_settings'))
app.debug = app.config.get('DEBUG', False)

@app.route('/')
def index():
    '''
    Knoppen scherm
    '''
    ctx = {'now': datetime.now()}
    return render_template('index.html', switches=app.config['SWITCHES'], ctx=ctx)


@app.route('/lamp/<address>/<aan_uit>/')
def lamp_aanuit(address, aan_uit='on'):
    configured_addresses = [ sw[1] for sw in app.config['SWITCHES']]
    if address not in configured_addresses:
        app.logger.warn("Illegal attempt to switch %s" % address)
        return "ERROR"
    cmnd_file = app.config['CMND_FILE']
    if os.path.isfile(cmnd_file):
        cmnd = "%s %s %s" % (cmnd_file, address, aan_uit)
        app.logger.debug(cmnd)
        os.system(cmnd)
    else:
        time.sleep(2)
    app.logger.info("switched %s %s" % (address, aan_uit))
    return "lamp is nu: %s" % aan_uit


@app.route('/all/<aan_uit>/')
def all_aanuit(aan_uit='on'):
    cmnd_file = app.config['CMND_FILE']
    for name, switch_addr in app.config['SWITCHES']:
        cmnd = "%s %s %s" % (cmnd_file, switch_addr, aan_uit)
        if os.path.isfile(cmnd_file):
            os.system(cmnd)
        app.logger.info("switched %s %s" % (switch_addr, aan_uit))
    return "switched all %s" % aan_uit


if __name__ == '__main__':
    app.run(debug = app.debug, host=app.config['HOST'])
