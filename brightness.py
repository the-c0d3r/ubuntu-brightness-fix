#!/usr/bin/env python


file_path = "/sys/class/backlight/intel_backlight/brightness"

def change(arg):

    curbri = int(open(file_path).read().strip('\n'))
    if arg == '+':
        setbri(int(curbri+100))
    elif arg == '-':
        setbri(int(curbri-100))

def setbri(per):
    try:
        cmd = open(file_path,'w')
        cmd.write(str(per))
        cmd.close()
    except IOError:
        print("[!] Permission error occured")
        print("[!] Try chmod and chown to the brightness file")

if __name__ == "__main__":
    usage = """
Usage : brightness +
        brightness - 
"""
    import sys
    if len(sys.argv) == 1:
        print usage
    elif len(sys.argv) == 2:
        if sys.argv[1] == '+':
            change('+')
        elif sys.argv[1] == '-':
            change('-')
        else:
            print usage