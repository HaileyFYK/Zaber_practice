from zaber_motion import Units
from zaber_motion.ascii import Connection

# Connect to the Zaber device
with Connection.open_usb() as connection:
    # Identify all devices
    device_list = connection.detect_devices()
    print(f"Found {len(device_list)} devices.")

    # Select the first rotation stage
    device = device_list[0]
    axis = device.get_axis(1)

    axis.home()

    axis.move_absolute(90, Units.ANGLE_DEGREES)

    axis.move_relative(45, Units.ANGLE_DEGREES)
    