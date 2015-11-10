# ubuntu-brightness-fix

This is intended to be a quick workaround for those having brightness shortcut key problem such as ubuntu not recognizing `FN`+`Whatever your brightness key is`. 

I have tried many solutions such as adding something to the grub file, or adding a config file under X11 directory. Both didn't work for me. And the [Brightness-Indicator](https://launchpad.net/indicator-brightness) also didn't. So I had to figure out a way. 

After searching the web, I found out a file called 'brightness' under `/sys/class/backlight/intel_backlight`. It keep track of the current brightness level and it directly effect the system brightness. So I just had to change the value inside the file. And then I developed this script to make it easier for all of us. 

# To do
1. Set the read write permission `sudo chmod 775 /sys/class/backlight/intel_backlight/brightness`
2. Change the ownership of the file `sudo chown $USER /sys/class/backlight/intel_backlight/brightness`
3. Check `/sys/class/backlight/intel_backlight/max_brightness` file and `/sys/class/backlight/intel_backlight/brightness` file to determine your system's maximum brightness and current one to decide how much you want to step up when you press your hot key. My computer's max_brightness is 973 so that means the range is between 0 to 973. And so I choose 100 to be the step, thus there would be 9 levels between total darkness and max brightness. **You need to change it accordingly, not all system are going to be the same.**
4. Download the brightness.py file or download the whole repo, unzip somewhere and place it somewhere (example: /home/user/programs), and open the file to tweak the setting.
5. Setup SymLink by executing `sudo ln -s /path/to/brightness.py /usr/bin/brightness`
6. Go to Dash, type `keyboard` or go to system settings -> Keyboard -> Shortcuts, Go to custom shortcuts, create new shortcut, name it "Brightness UP" and type `brightness +` in command, another one naming "Brightness DOWN" and type `brightness -` in command. Set custom shortcut keys for both of them. I used `Ctrl+Up Arrow` for Pumping up brightness and `Ctrl+Down Arrow` for dimming the brightness.