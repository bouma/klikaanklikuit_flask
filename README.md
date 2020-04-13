klikaanklikuit_flask
====================

smartphone/tablet control for your wireless 'klik aan klik uit ' light switches using Flask running on Raspberry Pi

Find details about hardware and configuration in [this blog](http://blog.egoactive.com/klikaanklikuit-met-smartphone-via-raspberrypi.html)


Build a virtualenv
```
   virtualenv --no-site-packages venv
```

and activate it:
```
   . ./venv/bin/activate
```

install requirements with pip
```
   pip install -r requirements.txt
```

go into the project folder and edit default_settings.py
or select your own settings by:
```
   export RASP_PYSETTINGS=<myown>_settings
```

Finally startup the app for testing:
```
   ./app.py
```
and point your browser at ```http://<ip-in-your-settings>:5000/```


Depends on pilight

BEWARE: if you need to edit /etc/pilight/config.json, MAKE SURE TO STOP THE DEAMON FIRST
```
   sudo /etc/init.d/pilight stop
   - do editting work
   sudo /etc/init.d/pilight start
```
