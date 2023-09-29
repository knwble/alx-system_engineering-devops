# Project: Processes and Signals
## In this project we will learn how processes work and signals are handled if they can.
- Task 0: Write a Bash script that displays its own PID.
- Task 1: Write a Bash script that displays a list of currently running processes.
- Task 2: Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
- Task 3: Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
- Task 4: Write a Bash script that displays To infinity and beyond indefinitely.
- Task 5: We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this. Write a Bash script that kills 4-to_infinity_and_beyond process.
- Task 6: Write a Bash script that kills 4-to_infinity_and_beyond process.
- Task 7: Write a Bash script that displays: To infinity and beyond indefinitely, With a sleep 2 in between each iteration, I am invincible!!! when receiving a SIGTERM signal
- Task 8: Write a Bash script that kills the process 7-highlander.
- Advanced Task 9:
Creates the file /var/run/holbertonscript.pid containing its PID.
Displays To infinity and beyond indefinitely.
Displays I hate the kill command when receiving a SIGTERM signal.
Displays Y U no love me?! when receiving a SIGINT signal.
Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal.
- Advanced Task 10: Write a manage_my_process Bash script that: Indefinitely writes I am alive! to the file /tmp/my_process. In between every I am alive! message, the program should pause for 2 seconds. Also write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)
- Advanced Task 11: Write a C program that creates 5 zombie processes.
- Advanced Task 12: Create a screencast where you live-code/demo something related to Unix signals.
