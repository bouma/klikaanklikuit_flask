HOST='0.0.0.0'
WEMOS_BASE_URL='http://192.168.1.123'
CMND_FILE='/home/pi/extralibs/lights/kaku'
DRY_RUN=True
DEBUG=True

SWITCHES = [('Linker lamp', 'G 12'),
            ('TV en Ziggo', 'G 13'),
            ('Boekenkast licht', 'G 14'),
            ('Hanglamp', 'G 15')]

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0,2,3]
ALL = range(0, len(SWITCHES))

SPARK_DEVICE_ID = "<my own sparticle-core id>"
SPARK_ACCESS_TOKEN = "<the secret access token>"
