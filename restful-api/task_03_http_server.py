#!/usr/bin/env python3
"""
Module to implement a simple HTTP server using Python's http.server module.
"""
import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler.
    """
    def do_GET(self):
        """
        Handle GET requests.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


if __name__ == '__main__':
    from http.server import HTTPServer
    server_address = ('', 8000)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("HTTP server on port 8000...")
    httpd.serve_forever()
