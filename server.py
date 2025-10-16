import http.server
import socketserver
import os

PORT = 4173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = super().translate_path(path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(DIRECTORY, relpath)
        return fullpath

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    print(f"Serving from {DIRECTORY} on port {PORT}...")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
