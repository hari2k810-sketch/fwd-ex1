# EX01 Developing a Simple Webserver
## Date:15-10-2026
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
    <title>Computer Network Protocols</title>
</head>
<body>
    <h1>List of Computer Network Protocols</h1>

    <ol>
        <li>HTTP - Hypertext Transfer Protocol</li>
        <li>HTTPS - Hypertext Transfer Protocol Secure</li>
        <li>FTP - File Transfer Protocol</li>
        <li>TCP - Transmission Control Protocol</li>
        <li>IP - Internet Protocol</li>
        <li>UDP - User Datagram Protocol</li>
        <li>DNS - Domain Name System</li>
        <li>SMTP - Simple Mail Transfer Protocol</li>
        <li>POP3 - Post Office Protocol</li>
        <li>SSH - Secure Shell</li>
    </ol>
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

