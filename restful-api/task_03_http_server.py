#!/usr/bin/python3
"""A simple HTTP server implementation using http.server"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handler for our simple API server"""

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Helper method to set HTTP headers"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _send_json_response(self, data, status_code=200):
        """Helper method to send JSON response"""
        self._set_headers(status_code, 'application/json')
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            # Root endpoint
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        
        elif self.path == '/data':
            # Data endpoint - return sample JSON data
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(sample_data)
        
        elif self.path == '/status':
            # Status endpoint
            self._set_headers()
            self.wfile.write("OK".encode())
        
        else:
            # Handle undefined endpoints
            error_message = {"error": "Endpoint not found"}
            self._send_json_response(error_message, 404)


def run_server(port=8000):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server() 