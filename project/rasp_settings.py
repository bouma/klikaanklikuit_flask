HOST='192.168.6.203'
CMND_FILE='/home/pi/extralibs/lights/kaku'
DRY_RUN=True
DEBUG=True

SWITCHES = (('Links', 'G 12'),
            ('TV Ziggo', 'G 13'),
            ('Achterlicht', 'G 14'),
            ('Hanglamp', 'G 15'))

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0,2,3]
ALL = range(0, len(SWITCHES))
