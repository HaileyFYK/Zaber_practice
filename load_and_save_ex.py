from zaber_motion import Units
from zaber_motion.ascii import Connection

# -----------------------
# Save function
# -----------------------
def save_state(axis):
    state = axis.get_state()

    with open("axis1_backup.json", "w") as file:
        file.write(state)

    print("State saved!")

# -----------------------
# Load function
# -----------------------
def load_state(axis):
    with open("axis1_backup.json", "r") as file:
        state = file.read()

    axis.set_state(state)

    print("State restored!")


with Connection.open_serial_port("COM3") as connection:

    connection.enable_alerts()

    device = connection.detect_devices()[0]
    axis = device.get_axis(1)

    # Change something
    axis.settings.set(
        "maxspeed",
        50,
        Units.VELOCITY_MILLIMETRES_PER_SECOND
    )

    # Save it
    save_state(axis)

    # Change it again
    axis.settings.set(
        "maxspeed",
        10,
        Units.VELOCITY_MILLIMETRES_PER_SECOND
    )

    # Restore the old settings
    load_state(axis)