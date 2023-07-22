HOST='192.168.1.13'
WEMOS_BASE_URL='http://192.168.1.14'
CMND_FILE='/usr/local/bin/pilight-control'
DRY_RUN=False
DEBUG=True

SWITCHES = (
            ('Boekenkast licht', '-d BoekenkastBoven -s'),
            ('Linker lamp', '-d LinksBoven -s'),
            ('Op kastenblok', '-d VentilatorZolder -s'),
            ('TV en Horizon', '-d TVHorizonBoven -s'),
            ('Hanglamp Boven', '-d HanglampBoven -s'),
            ('Kerstboom', '-d KerstBoom -s'),
            ('Lotek Beneden', '-d TVBeneden -s'),
            ('Gardena buiten', '-d Gardena -s'),
            ('Bank Beneden', '-d BankBeneden -s'),
            ('Losse schakelaar', '-d LosseSchakelaar -s'),
            ('Buitenlamp', '-d BuitenLamp -s'),
            ('Stopcontact buiten', '-d BuitenStopcontact -s'),
           )

# switch subsets (point to the indexes of the SWITCHES array)
LIGHTSONLY = [0, 1, 2, 4, 5]
BOVENONLY = [0, 1, 2, 3, 4, 5]
BENEDENONLY = [6, 7]
BUITENONLY = [8, 9, 10]
ALL = range(0, len(SWITCHES))

