klikaanklikuit_flask
====================

smartphone/tablet control for your wireless 'klik aan klik uit ' light switches using Flask running on Raspberry Pi

**A pointer to setup-description of hardware and native packages on the Raspberry Pi will follow here shortly.**
Meanwhile, this app can be tried out on your local machine.

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


