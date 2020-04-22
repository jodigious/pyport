import socket
import subprocess
import sys
from datetime import datetime

def pyport():

    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input from the user
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print banner with information on host
    print("-"*120)
    print("\tPlease wait, scanning remote host, {}".format(remoteServerIP))
    print("-"*120)

    # Check time of start scan
    time1 = datetime.now()

    # Now we scan between ports 1 and 1024
    # Include error handling

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}  \t Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        print("You hit Cntl+C\n")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved\n")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server\n")
        sys.exit()

    # Checking timestamp again
    time2 = datetime.now()

    # Calculate the diff in time to find runtime.
    time_run = time2 - time1

    # Print the runtime.
    print("\nRunetime: {}".format(time_run))

pyport()
