from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
```html
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
```
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()