from os import system
from platform import machine
print('Checking For Update...')
system('git pull')
if machine()=='aarch64':
    system('curl -L https://raw.githubusercontent.com/Nil500/gox/main/run.py')
else:
    system('curl -L  https://raw.githubusercontent.com/Nil500/gox/main/run.py')
