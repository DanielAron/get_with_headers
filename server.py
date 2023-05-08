import http.server
import socketserver
from http.client import HTTPSConnection
from urllib.parse import urlparse

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Open URL in New Tab</title>
            </head>
            <body>
                <button id="openUrlBtn">Open URL in New Tab</button>
                <script>
                    document.getElementById('openUrlBtn').addEventListener('click', function () {
                        window.location.href = "/redirect";
                    });
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
        elif self.path == "/redirect":
            url = "https://tstdrv2456091.app.netsuite.com/app/login/oauth2/authorize.nl?client_id=c6e22d0ee5b5f769bc32c99a80ad85a1d05df2d41ef42e5a0bdfd60166e08b9f&redirect_uri=https%3A%2F%2Fplatform.panoply.io%2Fsources%2Fcallback.html&response_type=code&scope=rest_webservices&state=Gb50fW4HU2q9gpOH"
            parsed_url = urlparse(url)
            conn = HTTPSConnection(parsed_url.netloc)
            conn.request("GET", parsed_url.path + "?" + parsed_url.query)
            response = conn.getresponse()
            
            if response.status == 200:
                self.send_response(302)
                self.send_header("Location", url)
                self.end_headers()
            else:
                self.send_response(500)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Error")
        else:
            self.send_error(404)

handler = CustomHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Serving on port {PORT}")
httpd.serve_forever()
