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


def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)


class CubeCtrl(object):

    cube = None

    def __init__(self):
        self.cube = MaxCube(MaxCubeConnection('192.168.1.186', 62910))


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
        sys.exit()

    cubectrl = CubeCtrl()
    cubectrl.get_info()

    print sys.argv
    if len(sys.argv) > 1 :

        print "setting temp"
        cubectrl.set_temperature(temp=float(sys.argv[1]))



#for room in cube.rooms:
#    print("Room: " + room.name)
#    for device in cube.devices_by_room(room):
#        print("Device: " + device.name)
#
#print("")


