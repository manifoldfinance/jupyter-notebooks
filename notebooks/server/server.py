from http.server import HTTPServer, BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "test/html")
        self.end_headers()
        self.wfile.write("Test message".encode())


def main():
    PORT = 8000
    server = HTTPServer(("", PORT), handler)
    print("Sever is running on port %s" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()
