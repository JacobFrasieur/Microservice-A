import zmq
import random
import datetime
import json
import os
import time

#Socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#File processing
def high_priority(received):
    name = received.get("user", "friend")
    current_date = str(datetime.datetime.now().date())
    highest_priority = None

    #Find task with the highest priority
    for task in received["tasks"]:
        #Always grabs first highest priority
        if task["priority"] == "high" and task["dueDate"] == current_date:
            highest_priority = task["title"]
            break

        elif task["priority"] == "medium" and task["dueDate"] == current_date:
            highest_priority = task["title"]

        elif task["priority"] == "low" and task["dueDate"] == current_date:
            highest_priority = task["title"]

    if highest_priority:
        return random_motivation(name,highest_priority)

    else:
        return "Nothing to do today!"


def random_motivation(name, highest_priority):
        rand_int = random.randint(1, 10)
        match rand_int:
            case 1:
                motiv_msg = f"Hey, {name}! Make sure you get {highest_priority} done today!"
            case 2:
                motiv_msg = f"You need to finish {highest_priority} today, good luck {name}!"
            case 3:
                motiv_msg = f"You're doing great so far {name}! Just make sure you get {highest_priority} done today!"
            case 4:
                motiv_msg = f"Success is built on working hard. Make sure you work hard on {highest_priority} today {name}!"
            case 5:
                motiv_msg = f"You've faced bigger challenges before {name}! Time to face {highest_priority}!"
            case 6:
                motiv_msg = f"Almost done for the week {name}! Just make sure you get {highest_priority} done today!"
            case 7:
                motiv_msg = f"Make today count {name}! Time to get {highest_priority} done today!"
            case 8:
                motiv_msg = f"{highest_priority} wont do itself, you got this {name}!"
            case 9:
                motiv_msg = f"{highest_priority} is next, you got this {name}!"
            case 10:
                motiv_msg = f"Time to get {highest_priority} finished, the ball is in your court {name}!"

        return motiv_msg
    # If no items with high/med/low priority today


#Running code
while True:
    try:
        #If we receive a message asking us if we are ready
        message = socket.recv_string()
        if message == "start":
            print("Received message to start, grabbing tasks and generating message...")
            #Request JSON file
            socket.send_string("json")
            #Recieve JSON file
            file = socket.recv_json()
            file_path = file.get("file", "tasklist.json")

            #Process file, send it back when done
            if file_path:
                print("Generating message...")
                time.sleep(5)
                socket.send_string(high_priority(file))
    #No file sent
    except FileNotFoundError:
        socket.send_string("File not found")



