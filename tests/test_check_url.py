from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from servercheck.core import check_url


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ok":
            code = 200
            body = b"OK"
        elif self.path == "/fail":
            code = 500
            body = b"ALERT"
        else:
            code = 404
            body = b"404 Not Found"
        self.send_response(code)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def test_check_url():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    port = server.server_address[1]
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        assert check_url(f"http://127.0.0.1:{port}/ok", 0.5) == ("OK", 200)
        assert check_url(f"http://127.0.0.1:{port}/fail", 0.5) == ("ALERT", 500)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
