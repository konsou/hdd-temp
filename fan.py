from time import sleep

import smbus
from i2c_pkg.emc2301_pkg import emc2301
from i2c_pkg.emc2301_pkg import fan_type


def fan_testing():
    bus = smbus.SMBus(10)
    address = 0x2f

    sensor = emc2301.EMC2301(address=0x2f,
                             busnum=10)

    print('Running sensor self test...')
    self_test_status = 'PASS' if sensor.self_test() == 0 else 'FAIL'
    print(f'Status: {self_test_status}')
    print(f'Product id: {sensor.productid()}')
    print(f'Manufacturer id: {sensor.manufid()}')
    print(f'Revision id: {sensor.revisionid()}')
    print(f'Register list:')
    print(emc2301.conf_register_list())
    print('Set fan speed to 0')
    sensor.write_register(register='FAN_SETTING', value=0)
    for i in range(10):
        print(f'Fan speed: {sensor.speed()[0]}')
        sleep(1)
    sensor.write_register(register='FAN_SETTING', value=255)
    for i in range(10):
        print(f'Fan speed: {sensor.speed()[0]}')
        sleep(1)
    sensor.write_register(register='FAN_SETTING', value=100)


if __name__ == '__main__':
    fan_testing()
