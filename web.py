from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lyrics Search</title>
</head>
<body>
    <h1>Lyrics Search</h1>
    <input type="text" id="song" placeholder="Enter song name">
    <button onclick="searchLyrics()">Search</button>
    <div id="lyrics"></div>
    
    <script>
        function searchLyrics() {
            document.getElementById('lyrics').innerHTML = "Lyrics will appear here.";
        }
    </script>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()