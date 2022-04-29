# kasa_smart_plug_control
Detect and control Kasa smart plugs from python or windows command prompt.

Get the released Windows executable here:  TODO

  Syntax:
    kasa_smart_plug_control discover
	kasa_smart_plug_control 192.xxx.xxx.xxx info
	kasa_smart_plug_control 192.xxx.xxx.xxx on
	kasa_smart_plug_control 192.xxx.xxx.xxx off
	kasa_smart_plug_control MyPlug1 on
	
  Compiled with pyinstaller:
    pyinstaller --noconfirm --onefile --console --icon "kasa_plug_icon.ico"  "kasa_smart_plug_control.py"

Or run from python:
  Requires python-kasa:
    pip install python-kasa
	
  Syntax:
    python kasa_smart_plug_control discover
	python kasa_smart_plug_control 192.xxx.xxx.xxx info
	python kasa_smart_plug_control 192.xxx.xxx.xxx on
	python kasa_smart_plug_control 192.xxx.xxx.xxx off
	python kasa_smart_plug_control MyPlug1 on