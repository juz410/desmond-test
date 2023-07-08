import os

heheBoi = os.path.join(os.path.expanduser("~"), "Desktop")

i = 1

for i in range(10):
    virus = "Virus"+str(i)
    myHackingLocation = os.path.join(heheBoi, virus)
    os.mkdir(myHackingLocation)