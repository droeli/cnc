import argparse
import mouse
import os
import time


non_move_wait = None

if os.path.exists('config.ini'):
    with open('config.ini') as conff:
        for line in conff:
            if 'non_move_wait' in line:
                non_move_wait = float(line.split('=')[1].strip())

parser = argparse.ArgumentParser(description="CNC (can not click), will click for you after you did not move your mouse for a specific time (default 1s)")
parser.add_argument('-w', type=float, default=None, help='Amount of seconds to wait for no movement before click for ex: 0.2; Can also be set in config.ini (same dir as exe)')
args = parser.parse_args()

if non_move_wait is None and args.w is None:
    non_move_wait = 1
    print('Using default of ' + str(non_move_wait) + ' seconds before clicking')
elif args.w is not None:
    non_move_wait = args.w
    print('Using ' + str(non_move_wait) + ' seconds before clicking you supplied as command line argument')
else:
    print('Using ' + str(non_move_wait) + ' seconds before clicking you supplied in config.ini')

current_position = None
last_position = None

try:
    while True:
        current_position = mouse.get_position()
        if current_position == last_position:
            mouse.click()
            print('I clicked for you')
        else:
            print('You moved your mouse')
        last_position = current_position
        time.sleep(non_move_wait)
except KeyboardInterrupt as ki:
    pass