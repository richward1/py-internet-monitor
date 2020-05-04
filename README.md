# Py Internet Monitor
Python-based internet connection monitor, that can automatically power-cycle a relay when the connection
drops.

## Introduction
This project was built to control the power to a router that regularly hangs. Rather than
manually resetting the router every few days, I decided to automate it.

The project uses the `gpiozero` library, and is intended to be used with just one relay. The 
relay used for this can be found [here](https://www.amazon.co.uk/Waycreat-Channel-Optocoupler-Arduino-Raspberry/dp/B07RNWLXJM/ref=sr_1_20?dchild=1&keywords=pi+5v+relay+board&qid=1588587912&s=electronics&sr=1-20).
The general idea behind this is: 
- Regularly ping a host with excellent reliability (I used Google)
- If successful, do nothing until the next ping
- If no response, start counting the number of failures
- If the number of failures reaches a certain point, open and close the relay - cutting the 
power enough to power-cycle the device
- Wait for an allotted 'back-off' time before we try the internet connection again

## Getting Started
1. Clone this repo
    ```shell script
    git clone https://github.com/richward1/py-internet-monitor.git
    ``` 

2. Run the `monitor.py` script
    ```shell script
    python monitor.py
    ```

## Usage
### Changing values
All values for timings can be adjusted in `monitor.py`.
The relay GPIO pin can be adjusted in `relay.py`. 

### Running the script in the background
Currently, you can run the script with `python monitor.py`, which will run in your current
shell session, taking over your shell and stopping when the shell is closed.

To run the script in the background:
```shell script
python monitor.py &
```

To run the script in the background and stay running when the shell is closed:
```shell script
nohup python monitor.py &
```

Take note of the PID that is printed in your shell when you start the script, as you'll need
it if you want to kill the process.
Alternatively, you can find the process by running `top -u $whoami`, which will return
all processes running under your user. Find the PID of the python process and kill it with
`kill [PID-HERE]`.

### Logs
The logger will automatically keep a rotating log file in `./logs`. This can be changed
in `logger.py`.

## Contributing
Please submit a PR if you'd like to contribute to this project. I'm more than happy to review
and accept changes, but this isn't my full-time job, so I can't guarantee a speedy response.

## License
Please see [License.md](https://github.com/richward1/py-internet-monitor/LICENSE)