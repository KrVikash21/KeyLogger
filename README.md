# KeyLogger
Basic keylogger program
###
1. We are creating a log file in the first line of the code. We will be storing the logs in this file.
2. We have created a function to write the key to the log file. We are converting the key to string and writing it to the log file.
3. We have created a function to read the key. We are checking if the key is pressed. If the key pressed is the escape key, we are returning False. If the key pressed is not the escape key, we are calling the function to write the key to the log file.
4. We are starting the listener. We are listening to the keys pressed by the user. If the user presses the escape key, we are stopping the listener. If the user presses any other key, we are calling the function to read the key.
5. We are joining the listener.
6. We are closing the log file.
###
