from zaber_motion.gcode import Translator
from zaber_motion.ascii import Connection

with Connection.open_serial_port("COM3") as connection:
    connection.enable_alters()

    device_list = connection.detect_devices()
    print("Found {} devices:".format(len(device_list)))

    device = device_list[0]
    
    stream = device.stream.get_stream(1)
    stream = setup_live(1, 2)

    translator = Translator.setup(stream)

    translator.translate("G28") #axis.home()
    translator.translate("G0 X100") #x_axis.move_absolute(Units.LENGTH_MILLIMETRES,100)
    translator.translate("G0 Y100") #y_axis.move_absolute(Units.LENGTH_MILLIMETRES,100)
    translator.translate("G0 X0 Y0") #x_axis.move_absolute(Units.LENGTH_MILLIMETRES,0), y_axis.move_absolute(Units.LENGTH_MILLIMETRES,0)

    translator.flush()
    stream.disable()