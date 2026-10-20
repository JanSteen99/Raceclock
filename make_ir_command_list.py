# Create a CommandSet for the raceclock using the remote control
# Based on https://github.com/kentwait/ircodec
# Created 23-8-2026 by Jan

# Input
emitterpin = 12
receiverpin = 17
filename = "raceclockcommandos_v1"

# Script
from ircodec.command import CommandSet
controller = CommandSet(name='Raceclock', emitter_gpio=12, receiver_gpio=17, description='Raceclock v1')
record = True

while record:
    # Add the requested key
    commandname = input("Enter the name of the command to record, exit to stop: ")
    if commandname == "exit":
        record=False
        print("Stopping command inputs, saving list...")
        controller.save_as(filename+".json")
    else:
        controller.add(commandname)
        # Connected to pigpio
        # Detecting IR command...
        # Received.

# # Send the volume up command
# controller.emit('volume_up')

# # Remove the volume up command
# controller.remove('volume_up')

# # Examine the contents of the CommandSet
# controller
# # CommandSet(emitter=22, receiver=23, description="TV remote")
# # {}

# Save to JSON


# # Load from JSON
# new_controller = CommandSet.load('another_tv.json')
