import sys
import time

f = None
try :
    f = open("poem.txt")
    # Our usual file reading idiom
    while True :
        line = f.readline()
        if len(line) == 0 :
            break
        print(line, end="")
        sys.stdout.flush()
        print("Please ctrl+c now")
        # To make sure that it runs for a while
        time.sleep(2)
except IOError:
    print("Couldn't find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file")
finally:
    if f:
        f.close()
    print("Cleaning up: Closed the file")