#importing
from main import maincam, maincamtrigger
#just some prints
print('welcome!')
print('select the operating mode')
mode = int(input('triggermode(1) or maincameramode(2):')) #selection mode
if mode == 1:
   maincamtrigger()
if mode == 2:
   maincam()
