import asyncio
import time
import sys
import re
from kasa import SmartPlug, Discover, SmartDeviceException
'''
KASA Smart Plug Controller

(c) Ryan Kinnett, 2022
https://github.com/rkinnett/kasa_smart_plug_control

Requires python-kasa:
  pip install python-kasa

KASA API:  https://python-kasa.readthedocs.io/en/latest/index.html


'''

help_info = '''
Kasa Smart Plug Controller

(c) Ryan Kinnett, 2022
https://github.com/rkinnett/kasa_smart_plug_control

Syntax:
  kasa_smart_plug_control discover
  kasa_smart_plug_control 192.xxx.xxx.xxx info
  kasa_smart_plug_control MySmartPlug1 on
  kasa_smart_plug_control MySmartPlug1 off
'''

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():    
    target_ip = None
    target_name = None
    devices = None
    operation = None
    plug = None
    
    if len(sys.argv)<=1:
        print(help_info)
        time.sleep(5)
        return
        
    for arg in sys.argv[1:]:
        if re.match(r'^-*[hH](elp)?$', arg) or arg=='/?':
            print(help_info)
            time.sleep(5)
            return
        elif arg.lower() in ('discover', 'list', 'on', 'off', 'info'):
            print('Requested operation: %s' % arg)
            operation = arg
        elif re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', arg):
            target_ip = arg
        else:
            print('Unrecognized arg "%s", maybe switch name' % arg)
            target_name = arg
            devices = await discover()

    if operation in (None, 'discover', 'list'):
        devices = await discover()
        return

    if target_ip:
        plug = SmartPlug(target_ip)
    elif target_name:
        if not devices or len(devices.items()) == 0:
            print('Error, no kasa smar plugs detected')
            return
        for addr, device in devices.items():
            if device.alias.lower() == target_name.lower():
                print('found match')
                plug = device
                break
        if plug is None:
            print('failed to identify plug "%s"' % target_name)
            return
        
    try:
        await plug.update()
    except SmartDeviceException as e:
        print(e)
        return
    
    if operation == 'on':
        if plug.is_on:
            print('Plug "%s" is already on' % plug.alias)
        else:
            print('Turning on plug "%s"' % plug.alias)
            await plug.turn_on()
    elif operation == 'off':
        if plug.is_on:
            print('Turning off plug "%s"' % plug.alias)
            await plug.turn_off()
        else:
            print('Plug "%s" is already off' % plug.alias)
    elif operation == 'info':
        print(plug)



async def discover():
    print('Detecting kasa smart plugs...')
    devices = await Discover.discover()
    for addr, dev in devices.items():
        await dev.update()
        print('  "%s", plug type %s at %s' % (dev.alias, dev.model, addr))        
    return devices


asyncio.run(main())