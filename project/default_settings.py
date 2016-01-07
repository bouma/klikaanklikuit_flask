HOST='192.168.1.61'
CMND_FILE='/home/pi/extralibs/lights/kaku'
DRY_RUN=False
DEBUG=True

SWITCHES = (('Linker lamp', 'G 12'),
            ('TV en Ziggo', 'G 13'),
            ('Boekenkast licht', 'G 14'),
            ('Hanglamp', 'G 15'))

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0,2,3]
ALL = range(0, len(SWITCHES))

SPARK_DEVICE_ID = "48ff70065067555057352287"
SPARK_ACCESS_TOKEN = "b66240ea89175ab476b6942115d74a3740bb7043"
