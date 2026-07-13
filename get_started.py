from zaber_motion import Units
from zaber_motion.ascil import Connection

with Connection.open_serial_port("COM3")as connection:
    connection.enable_alters()

    device_list = connection.detect_devices()
    print("Found {} devices:".format(len(device_list)))

    device = device_list[0]
    
    axis = device.get_axis(1)
    if not axis.is_homed():
        axis.home()


    axis.move_absolute(Units.LENGTH_MILLIMETRES, 10)

    axis.move_relative(Units.LENGTH_MILLIMETRES, 5)