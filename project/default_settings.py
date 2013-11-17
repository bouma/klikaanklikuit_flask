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
