HOST='192.168.1.13'
WEMOS_BASE_URL='http://192.168.1.14'
CMND_FILE='/usr/local/bin/pilight-control'
DRY_RUN=False
DEBUG=True

SWITCHES = (('Linker lamp', '-d LinksBoven -s'),
            ('TV en Horizon', '-d TVHorizonBoven -s'),
            ('Boekenkast licht', '-d BoekenkastBoven -s'),
            ('Hanglamp Boven', '-d HanglampBoven -s'),
            ('TV Beneden', '-d TVBeneden -s'),
            ('Lotek Beneden', '-d BankBeneden -s'),
            ('Ventilator Zolder', '-d VentilatorZolder -s'),
            ('Losse schakelaar', '-d LosseSchakelaar -s'),
            ('Buitenlamp', '-d BuitenLamp -s'),
            ('Stopcontact buiten', '-d BuitenStopcontact -s'),
           )

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0, 2, 3]
BOVENONLY = [0, 1, 2, 3]
BENEDENONLY = [4, 5]
ALL = range(0, len(SWITCHES))

