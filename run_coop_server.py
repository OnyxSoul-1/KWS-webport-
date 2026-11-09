
import http.server, socketserver, os
class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()
    def translate_path(self, path):
        # Serve index.html for directories
        path = super().translate_path(path)
        if os.path.isdir(path): return os.path.join(path, 'index.html')
        return path
PORT = 8080
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving with COOP/COEP headers at http://localhost:{PORT}")
    httpd.serve_forever()
