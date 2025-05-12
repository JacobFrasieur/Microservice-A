<h1>Communication Contract</h1>
<h2>Programmatically request Data:</h2>
      To request data, follow these steps<br><br>
      1. Import zmq. <br><br>
      2. Initialize it using zmq.Context()<br><br>
      3. Create a REQ socket using context.socket(zmq.REQ)<br><br>
      4. Connect to the microservices socket using its port (5555). This should look like socket.connect("tcp://localhost:5555")<br><br>
      5. Send a string to that socket saying "start". This is how the microservice knows when to start working<br><br>
      Example Call:
      
          context = zmq.Context()
          socket = context.socket(zmq.REQ)
          socket.connect("tcp://localhost:5555")
          socket.send_string("start")

<h2>Programmatically recieve data</h2>
      To recieve data, follow the steps for requesting first, then follow these steps<br><br>
      1. Sleep, allowing the microservice to perform its work<br><br>
      2. Set a variable to the string the microservice will be sending, this should look like motivation = socket.recv_string()<br><br>
      Example Call:
      
            time.sleep(1)
            motiv = socket.recv_string()
<h2>UML Diagram</h2>

![UML](https://github.com/user-attachments/assets/4c87b313-e801-4fbd-96bc-fa0d9534917f)
