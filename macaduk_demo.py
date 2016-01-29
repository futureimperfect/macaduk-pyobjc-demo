#!/usr/bin/env python

import curses
import time

from Cocoa import CWInterface


def get_color(val):
    '''Get color from val.
    1: Magenta
    2: Red
    3: Blue
    4: Yellow
    '''
    if val < -80:
        return 4
    elif val < -70:
        return 3
    elif val < -60:
        return 2
    return 1


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    interface = CWInterface.interface()
    interface_name = interface.interfaceName()

    try:
        while True:
            rssi = interface.rssiValue()
            noise = interface.noiseMeasurement()
            tx_rate = interface.transmitRate()
            channel = interface.channel()
            color_number = get_color(rssi)
            stdscr.addstr(0, 0, '# WiFi Info')
            stdscr.addstr(1, 0, '')
            stdscr.addstr(2, 0, 'RSSI: %s dBm' % rssi,
                          curses.color_pair(color_number))
            stdscr.addstr(3, 0, 'Noise: %s dBm' % noise)
            stdscr.addstr(4, 0, 'Interface Name: %s' % interface_name)
            stdscr.addstr(5, 0, 'Tx Rate: %s Mbps' % tx_rate)
            stdscr.addstr(6, 0, 'Channel: %s' % channel)
            stdscr.refresh()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == '__main__':
    main()
