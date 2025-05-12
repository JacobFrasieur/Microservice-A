import zmq
import time
import json

#Will print the message sent back. Can be changed if you dont want printed immediately
#ASSUMPTIONS MADE:
#1: JSON File is in expected format
#2: JSON FIle in same dir as micro
#3: User follows this order:
#       - Connect to socket
#       - Tell micro to start
#       - Grab finished string from micro

def motivation_msg():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #Tell micro to start, wait for ready
    socket.send_string("start")
    time.sleep(1)

    motiv = socket.recv_string()
    print(motiv)

#Use whenever you want your motivational message. Microservice must be running
motivation_msg()