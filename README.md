# kasa_smart_plug_control
Detect and control Kasa smart plugs by name or IP address from python or windows command prompt.  
  
### Get the released Windows executable here:    
   https://github.com/rkinnett/kasa_smart_plug_control/releases
  
  Syntax:  
    kasa_smart_plug_control discover  
    kasa_smart_plug_control 192.xxx.xxx.xxx info  
    kasa_smart_plug_control 192.xxx.xxx.xxx on  
    kasa_smart_plug_control 192.xxx.xxx.xxx off  
    kasa_smart_plug_control MyPlug1 on  
  
  Compiled with pyinstaller:
	py -3 -m PyInstaller --noconfirm --onefile --console --name "kasa_smart_plug_control" --icon "kasa_plug_icon.ico" "kasa_smart_plug_control.py" --clean
  
  
### Or run from python:  
  Requires python-kasa:  
    pip install python-kasa  
  
  Syntax:  
    python kasa_smart_plug_control.py discover  
    python kasa_smart_plug_control.py 192.xxx.xxx.xxx info  
    python kasa_smart_plug_control.py 192.xxx.xxx.xxx on  
    python kasa_smart_plug_control.py 192.xxx.xxx.xxx off  
    python kasa_smart_plug_control.py MyPlug1 on  