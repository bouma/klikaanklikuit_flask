from maxcube.cube import MaxCube
from maxcube.connection import MaxCubeConnection
from maxcube.device import \
    MAX_THERMOSTAT, \
    MAX_THERMOSTAT_PLUS, \
    MAX_WINDOW_SHUTTER, \
    MAX_WALL_THERMOSTAT, \
    MAX_DEVICE_MODE_AUTOMATIC, \
    MAX_DEVICE_MODE_MANUAL, \
    MAX_DEVICE_MODE_VACATION, \
    MAX_DEVICE_MODE_BOOST
import logging
import signal
import sys

'''
LET OP: connection timeout als de Max!Cube applicatie op de laptop draait.
ip-adres nu is 192.168.1.186, maar ligt waarschijnlijk nog niet vast
port number: 62910 Dat lijkt de standaard te zijn voor Max!Cube

'''

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


class CubeCtrl(object):

    '''
    Wat gaan we doen:
    - haal kamers (naam, id) op
    - haal thermostaat per kamer op (naam, actual_temperature, target_temperature, valve_position)
    - 
    - target temp
    '''

    cube = None

    def __init__(self):
        self.cube = MaxCube(MaxCubeConnection('192.168.1.186', 62910))

        print "rooms:"
        for room in self.cube.get_rooms():
            print "%s (%d)" % (room.name, room.id)

    def get_info(self):

        room = self.cube.room_by_id(1)
        print("Room(1): " + room.name)

        for device in self.cube.devices_by_room(room):

            self.get_device_info(device)

    def set_temperature(self, room_id=1, temp=10.5):
        room = self.cube.room_by_id(1)
        for device in self.cube.devices_by_room(room):
            print(device)
            if self.cube.is_wallthermostat(device) or self.cube.is_thermostat(device):
                print("Setting temp to %s" % str(temp))
                self.cube.set_target_temperature(device, temp)
            else:
                print("No Thermostat")

    def set_device_mode(self, device):
        print(device)
        if self.cube.is_wallthermostat(device):
            print("Setting mode")
            self.cube.set_mode(device, MAX_DEVICE_MODE_MANUAL)
        else:
            print("No Wall Thermostat") 

    def get_device_info(self, device):

        print("Device: " + device.name)
        if device.type == MAX_THERMOSTAT:
            type = "MAX_THERMOSTAT"
        elif device.type == MAX_THERMOSTAT_PLUS:
            type = "MAX_THERMOSTAT_PLUS"
        elif device.type == MAX_WINDOW_SHUTTER:
            type = "MAX_WINDOW_SHUTTER"
        elif device.type == MAX_WALL_THERMOSTAT:
            type = "MAX_WALL_THERMOSTAT"
        print("Type:   " + type)
        print("RF:     " + device.rf_address)
        print("Room ID:" + str(device.room_id))
        print("Room:   " + self.cube.room_by_id(device.room_id).name)
        print("Name:   " + device.name)
        print("Serial: " + device.serial)

        if device.type == MAX_THERMOSTAT:
            print("MaxSetP:" + str(device.max_temperature))
            print("MinSetP:" + str(device.min_temperature))
            if device.mode == MAX_DEVICE_MODE_AUTOMATIC:
                mode = "AUTO"
            elif device.mode == MAX_DEVICE_MODE_MANUAL:
                mode = "MANUAL"
            print("Mode:   " + mode)
            print("Valve: " + str(device.valve_position))
            print("Actual: " + str(device.actual_temperature))
            print("Target: " + str(device.target_temperature))

        if device.type == MAX_WALL_THERMOSTAT:
            print("MaxSetP:" + str(device.max_temperature))
            print("MinSetP:" + str(device.min_temperature))
            if device.mode == MAX_DEVICE_MODE_AUTOMATIC:
                mode = "AUTO"
            elif device.mode == MAX_DEVICE_MODE_MANUAL:
                mode = "MANUAL"
            print("Mode:   " + mode)
            print("Actual: " + str(device.actual_temperature))
            print("Target: " + str(device.target_temperature))

        if device.type == MAX_WINDOW_SHUTTER:
            print("IsOpen: " + str(device.is_open))

        print("")

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)
    # print 'Press Ctrl+C to exit'

    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--h', '--help']:
        print "Get details from Max! thermostat or set temperature"
        print "set temperature: python %s <temp as float>" % sys.argv[0]
        sys.exit()

    # BEGIN logging config
    import logging
    logger = logging.getLogger('maxcube')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    # END logging config

    cubectrl = CubeCtrl()

    cubectrl.get_info()

    print sys.argv
    if len(sys.argv) > 1 :

        print "setting temp"
        cubectrl.set_temperature(temp=float(sys.argv[1]))

    # import pdb; pdb.set_trace()


#for room in cube.rooms:
#    print("Room: " + room.name)
#    for device in cube.devices_by_room(room):
#        print("Device: " + device.name)
#
#print("")


