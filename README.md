# EX01 Developing a Simple Webserver
## Date:15-06-2026
## REG NO : 26009013

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~


from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
    <title>My First Website</title>
</head>
<body>
    <h1>Welcome to My Website!</h1>
    <p>This is my first web page using Python.</p>

    <h2>About Me</h2>
    <p>I am learning web development.</p>

    <h2>My Skills</h2>
    <ul>
        <li>Python</li>
        <li>HTML</li>
        <li>CSS</li>
    </ul>

    <h2>Contact</h2>
    <p>Email: student@example.com</p>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header(
            'Content-type', 'text/html; charset=utf-8'
        )
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 880)
httpd = HTTPServer(server_address, myhandler)

print("My web server is running...")
httpd.serve_forever()

~~~

## OUTPUT:
![alt text](<Screenshot 2026-11-14 132729.png>)
![alt text](<exp 1.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

