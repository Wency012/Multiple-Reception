#!/usr/bin/env python
# -*- coding: latin-1 -*-xyer

import socket
import time
#import threading

#Define global variables to mark the current scheduler
current_scheduler="redundant"

#Switch scheduler
#def switch_scheduler():
 #   global current_scheduler
 #   if current_scheduler== "default":
  #      current_scheduler="redundant"
  #  else:
  #      current_scheduler== "redundant"
   #     current_scheduler="default"

#Timer Functions
#def scheduler_time():
#    while True:
 #       switch_scheduler()
 #       time.sleep(30)

# Receive data
def receive_data(filename, port):
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)

    # Receive Connection

    conn, addr = s.accept()
    
    #Initialize throughput test parameters
    start_time = time.time()
    received_bytes = 0
    throughput_values = []

    #Start Timer Thread
    #timer_thread = threading.Thread(target=scheduler_time)
   # timer_thread.daemon = True #Set as a guardian thread, so that the thread also exits when the program exits

    #timer_thread.start()

    # Receive Data

    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)

            #Measure time intervals and calculate throughput

            received_bytes += len(data)
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 1.0: # Calculate throughput once per second
                throughput = received_bytes / (elapsed_time * 1024)  
                throughput_values.append(throughput)
                start_time = current_time
                received_bytes = 0
    #Save throughput to file
    with open("throughput.txt", "w") as throughput_file:
        for value in throughput_values:
            throughput_file.write(str(value) + "\n")
    
    # Save throughput to file

    conn.close()
    s.close()

if __name__ == '__main__':
    received_file = "received_file.bin"
    server_port = 5001
    receive_data(received_file, server_port)
    #h1



