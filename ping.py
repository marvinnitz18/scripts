import os
import time
import sys

args = sys.argv[1:]


def ping(hostname):
	response = os.system("ping -c 1 " + hostname+"> /dev/null")
	if response == 0: print(hostname, 'is up!')
	else: print(hostname, 'is down!')

while __name__ == '__main__':
    ping(args[0])
    os.system("date")
    time.sleep(5)
    os.system("clear")

if args[1] == "1":
	ping(args[0])
	os.system("date")

else: print("2nd Argument needs to be forever")
