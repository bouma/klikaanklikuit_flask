HOST='192.168.1.61'
CMND_FILE='/usr/local/bin/pilight-control'
DRY_RUN=False
DEBUG=True

SWITCHES = (('Linker lamp', '-d LinksBoven -s'),
            ('TV en Horizon', '-d TVHorizonBoven -s'),
            ('Boekenkast licht', '-d BoekenkastBoven -s'),
            ('Hanglamp Boven', '-d HanglampBoven -s'),
            ('TV Beneden', '-d TVBeneden -s'),
            ('Lotek Beneden', '-d BankBeneden -s'))

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0,2,3]
ALL = range(0, len(SWITCHES))

SPARK_DEVICE_ID = "48ff70065067555057352287"
SPARK_ACCESS_TOKEN = "b66240ea89175ab476b6942115d74a3740bb7043"
