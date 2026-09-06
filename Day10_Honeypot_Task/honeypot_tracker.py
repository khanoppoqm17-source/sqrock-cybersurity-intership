from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

LOG = []

class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = {
            "time": str(datetime.datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "agent": self.headers.get("User-Agent", "?"),
        }
        LOG.append(entry)
        print(json.dumps(entry, indent=2))
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting!")
    
    def log_message(self, *args):
        pass  # suppress default server logs

if __name__ == "__main__":
    print("\n=== Honeypot Link Tracker ===")
    print("Server running at http://localhost:8080")
    print("Open this link in a browser tab, then check this console.\n")
    print("Press Ctrl+C to stop and see the full log.\n")
    
    try:
        HTTPServer(("", 8080), HoneyHandler).serve_forever()
    except KeyboardInterrupt:
        print("\n\n=== Captured Log ===")
        for entry in LOG:
            print(json.dumps(entry, indent=2))