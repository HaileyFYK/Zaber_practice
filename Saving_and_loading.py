from zaber_motion import Units
from zaber_motion.ascii import Connection

# Save the state of a device to a file
def save_state(device: Device):
    state = device.get_state()
    with open('save.json', 'w', encoding='utf-8') as save_file:
        save_file.write(state)

# Load the state of a device from a file
def load_state(device: Device):
    with open('save.json', 'r', encoding='utf-8') as save_file:
        state = save_file.read()
    device.set_state(state)

device = connection.get_device(1)
device.identify()

#Save the current state of the device
MM_S = Units.VELOCITY_MILLIMETRES_PER_SECOND
initial_maxspeed = device.settings.get('max_speed', MM_S)
save_state(device)

# Change the max speed of the device
device.settings.set('max_speed', 1.5, MM_S)
assert device.settings.get('max_speed', MM_S) != initial_maxspeed

# Load the previous state of the device
load_state(device)
assert device.settings.get('max_speed', MM_S) == initial_maxspeed