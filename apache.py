import os, time, threading, io


print("Smp_A")

os.system('service nginx stop')
time.sleep(3)
os.system('a2enmod php7')
time.sleep(3)
os.system('service apache2 start')

print("servicios corriendo")
