"""
Relay

Utilises gpiozero library to interface with the GPIO on the Pi.
Change the 'relay_pin' value accordingly to meet your needs.
"""

import gpiozero, time

relay_pin = 17
relay = gpiozero.OutputDevice(relay_pin, active_high=False, initial_value=False)

def toggle(delay):
    relay.toggle()
    time.sleep(delay)
    relay.toggle()
