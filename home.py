from base64 import encode
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

ReadFile = open('file.html','r')
NewFile = ReadFile.read()

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print('inside class')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        bytReturn = self.wfile.write(bytes(NewFile, "utf-8"))
        
        print(bytReturn)


       
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        print('hey')
        webServer.serve_forever()
        print('hello')
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
