HOST='0.0.0.0'
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

SPARK_DEVICE_ID = "48ff70065067555057352287"
SPARK_ACCESS_TOKEN = "ed33d6d63db5b2bb1f11d11ec767b5ccebf6ac18"
