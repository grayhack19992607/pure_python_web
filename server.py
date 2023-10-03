import http.server
import socketserver

# Specify the port you want to use
port = 8000

# Create a simple HTTP server to serve the HTML file
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
