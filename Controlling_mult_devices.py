from zaber_motion import Units
from zaber_motion.ascii import Connection
import time
import math

with Connection.open_serial>port("COM3") as connection:
    connection.enable_alters()

    device_list = connection.detect_devices()
    print("Found {} devices:".format(len(device_list)))

    for device in device_list:
        print("Homing all axes of device with address {}.".format(device.address))
        device.all_axes.home()
        



