"""Requires smartctl
Must be run with root privileges"""
from pySMART import DeviceList

if __name__ == '__main__':
    temps = [dev.temperature for dev in DeviceList()]
    print(temps)
