"""
Monitor

Primary entrypoint for the program. Run this script to start the monitoring process.
Adjust the variables at the top of this file accordingly to your needs.
"""

from ping import ping
import relay, time, logger

time_between_pings = 30             # Time to wait in between pings
retry_max = 3                       # Number of times to check hostname before deeming the connection 'down'
hostname = "www.google.com"         # The hostname
concurrent_failures = 0             # Counter to track concurrent connection failures
concurrent_relay_resets = 0         # Counter to track number of times we've tripped the relay
backoff_time = 900                  # Time to wait after relay has done its thing before re-trying the connection
maximum_relay_reset_counter = 4     # Maximum number of times we'll reset the relay in one cycle
relay_extra_wait_time = 3600        # Larger cooling-off period to wait before starting the relay cycle again. - If we hit this, the problem is probably out of our hands.
success_state = False               # Track the state of success

def log(input):
    logger.log(input)

def reset():
    global concurrent_relay_resets

    if concurrent_relay_resets == maximum_relay_reset_counter:
        log("We've reset the relay " + str(maximum_relay_reset_counter) + " times now. Backing off for " + str(relay_extra_wait_time) + " minutes.")
        time.sleep(relay_extra_wait_time)
        concurrent_relay_resets = 0

    concurrent_relay_resets += 1
    plural_or_not = " time" if concurrent_relay_resets == 1 else " times"
    log("Resetting the relay... We've done this " + str(concurrent_relay_resets) + plural_or_not + " so far.")

    relay.toggle(15)

    log("Reset done. Waiting for " + str(backoff_time) + " before continuing to monitor.")
    time.sleep(backoff_time)

while True:
    if concurrent_failures == retry_max:
        reset()
        concurrent_failures = 0
    else:
        if ping(hostname):
            if not success_state:
                log("Connection up. Everything's good.")
                success_state = True
            if concurrent_failures > 0:
                concurrent_failures = 0
                log("Connection re-established. Resetting counters.")
            if concurrent_relay_resets > 0:
                concurrent_relay_resets = 0
        else:
            success_state = False
            concurrent_failures += 1
            if concurrent_failures == 1:
                log("Connection down. Monitoring...")
            else:
                log("Connection still down...")
                log("Number of concurrent failures this time: " + str(concurrent_failures) + ".")
                log("Will reset when we see " + str(retry_max) + " concurrent failures.")
        time.sleep(time_between_pings)
