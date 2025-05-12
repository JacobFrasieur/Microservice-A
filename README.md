<h1>Communication Contract</h1>
A: Programmatically request Data:<br>
      To request data, follow these steps<br>
      1. Import zmq. <br>
      2. Initialize it using zmq.Context()<br>
      3. Create a REQ socket using context.socket(zmq.REQ)<br>
      4. Connect to the microservices socket using its port (5555). This should look like socket.connect("tcp://localhost:5555")<br>
      5. Send a string to that socket saying "start". This is how the microservice knows when to start working<br>
      
      Example Call:
          context = zmq.Context()
          socket = context.socket(zmq.REQ)
          socket.connect("tcp://localhost:5555")
          socket.send_string("start")

B: Programmatically recieve data<br>
      To recieve data, follow the steps for requesting first, then follow these steps<br>
      1. Sleep, allowing the microservice to perform its work<br>
      2. Set a variable to the string the microservice will be sending, this should look like motivation = socket.recv_string()<br>

      Example Call:
            time.sleep(1)
            motiv = socket.recv_string()
