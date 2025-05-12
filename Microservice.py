import zmq
import random
import datetime
import json
import os

#Socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#File processing
def process(received):
    name = received["user"]
    current_date = str(datetime.datetime.now().date())
    highest_priority = None

    #Find task with the highest priority
    for task in received["tasks"]:
        #Always grabs first highest priority
        if task["priority"] == "high" and task["due_date"] == current_date:
            highest_priority = task["title"]
            break

        elif task["priority"] == "medium" and task["due_date"] == current_date:
            highest_priority = task["title"]

        elif task["priority"] == "low" and task["due_date"] == current_date:
            highest_priority = task["title"]

    if highest_priority:
        rand = random.randint(1, 10)
        match rand:
            case 1:
                msg = f"Hey, {name}! Make sure you get {highest_priority} done today!"
            case 2:
                msg = f"You need to finish {highest_priority} today, good luck {name}!"
            case 3:
                msg = f"You're doing great so far {name}! Just make sure you get {highest_priority} done today!"
            case 4:
                msg = f"Success is built on working hard. Make sure you work hard on {highest_priority} today {name}!"
            case 5:
                msg = f"You've faced bigger challenges before {name}! Time to face {highest_priority}!"
            case 6:
                msg = f"Almost done for the week {name}! Just make sure you get {highest_priority} done today!"
            case 7:
                msg = f"Make today count {name}! Time to get {highest_priority} done today!"
            case 8:
                msg = f"{highest_priority} wont do itself, you got this {name}!"
            case 9:
                msg = f"{highest_priority} is next, you got this {name}!"
            case 10:
                msg = f"Time to get {highest_priority} finished, the ball is in your court {name}!"

        return msg
    # If no items with high/med/low priority today
    else:
        return "Nothing to do today!"


#Running code
while True:
    try:
        #If we receive a message asking us if we are ready
        message = socket.recv_string()
        if message == "start":

            #Try to open json file in same dir, else raise error
            if os.path.exists("tasklist.json"):
                with open('tasklist.json', 'r') as file:
                    file_received = json.load(file)
            else:
                raise FileNotFoundError

            #Process file, send it back when done
            if file_received:
                socket.send_string(process(file_received))
    #No file sent
    except FileNotFoundError:
        socket.send_string("File not found")



