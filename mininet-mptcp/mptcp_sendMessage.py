#!/usr/bin/env python
# -*- coding: latin-1 -*-xyer

import socket

def send_rtcm_data(filename,host,port):
    # Create  socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set MPTCP options
    sock.setsockopt(socket.SOL_TCP, 42, 1)
    
    #  Connect the IP address and port number of the receiving end 
    sock.connect((host, port))
    
    # Send data
    with open(filename, 'rb') as file:
        data = file.read()
    #Send binary data
    sock.sendall(data)
    
    # Close sock
    sock.close()

if __name__ == '__main__':
    file_to_send = "generate_rtcm.bin" 
    server_host = "10.0.0.1"  
    port=5001
    send_rtcm_data(file_to_send ,server_host,port)
    #h2



