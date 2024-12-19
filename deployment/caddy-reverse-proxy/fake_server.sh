#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send response headers
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        # Send hello response
        response = {
            "message": "hello",
            "path": self.path
        }
        self.wfile.write(json.dumps(response, indent=2).encode())

    # Handle POST the same way as GET
    def do_POST(self):
        self.do_GET()

# Create server
server_address = ('0.0.0.0', 3000)
httpd = HTTPServer(server_address, HelloHandler)

print('Starting server on port 3000...')
httpd.serve_forever()
