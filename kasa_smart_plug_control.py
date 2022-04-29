import asyncio
import time
import sys
import re
from kasa import SmartPlug, Discover

# KASA API:
# https://python-kasa.readthedocs.io/en/latest/index.html


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

command = None
target = None


async def main():    
    target_ip = None
    target_name = None
    devices = None
    operation = None
    plug = None
    
    for arg in sys.argv[1:]:
        if arg.lower() in ('discover', 'on', 'off', 'info'):
            print('Requested operation: %s' % arg)
            operation = arg
        elif re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', arg):
            target_ip = arg
        else:
            print('Unrecognized arg "%s", maybe switch name' % arg)
            target_name = arg
            devices = await discover()

    if operation in (None, 'discover'):
        devices = await discover()
        return

    if target_ip:
        plug = SmartPlug(target_ip)
    elif target_name:
        assert devices is not None and len(devices.items()) > 0, 'Error, no kasa smar plugs detected'
        for addr, device in devices.items():
            if device.alias.lower() == target_name.lower():
                print('found match')
                plug = device
                break
        assert plug is not None, 'failed to identify plug "%s"' % target_name
        
    await plug.update()
    
    if operation == 'on':
        if device.is_on:
            print('Plug "%s" is already on' % device.alias)
        else:
            print('Turning on plug "%s"' % device.alias)
            await plug.turn_on()
    elif operation == 'off':
        if device.is_on:
            print('Turning off plug "%s"' % device.alias)
            await plug.turn_off()
        else:
            print('Plug "%s" is already off' % device.alias)
    elif operation == 'info':
        print(plug)





async def discover():
    print('Detecting kasa smart plugs...')
    devices = await Discover.discover()
    for addr, dev in devices.items():
        await dev.update()
        print(f"{addr} >> {dev}")
    print('(done)')
    return devices




asyncio.run(main())

