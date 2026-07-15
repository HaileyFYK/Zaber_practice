from zaber_motion import Units, Mesurement, wait_all
from zaber_motion.ascii import Connection, AxisGroup

with Connection.open_serial_port("COM3") as connection:
    connection.enable_alters()

    device_list = connection.detect_devices()
    print("Found {} devices:".format(len(device_list)))

    device = device_list[0]
    x_axis = device.get_axis(1)
    y_axis = device.get_axis(2)

    if not x_axis.is_homed():
        x_axis.home()
    if not y_axis.is_homed():
        y_axis.home()

    # Move both axes simultaneously to (100, 100) mm
    x_axis.move_absolute(100, Units.LENGTH_MILLIMETRES, wait_until_idle = False)
    y_axis.move_absolute(100, Units.LENGTH_MILLIMETRES, wait_until_idle = False)

    # Wait for both movements to complete
    x_axis.wait_until_idle()
    y_axis.wait_until_idle()

    # from zaber_motion.ascii import Connection, AxisGroup  
    # from zaber_motion import Measurement
    group = AxisGroup([device.get_axis(1), device.get_axis(2)])
    group.move_absolute(Measurement(1, 'cm'), Measurement(2, 'cm')) #Allow the axex to move simultaneously to (1, 2) cm

    # from zaber_motion.ascii import Connection
    # from zaber_motion import Units, wait_all
    
