#!python3.10

import os,platform

mamunXten=platform.architecture()[0]

os.system('git pull')

if mamunXten=="32bit":
    print('Your Device Architecture is Unsupported..!')

elif mamunXten=="64bit":
    __import__("Xsafe").ONOFF()


