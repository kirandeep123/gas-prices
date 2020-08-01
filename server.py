import http.server

class GasPriceHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("go get ")
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
if __name__=='__main__':
    httpd = http.server.HTTPServer(('127.0.01',5000),GasPriceHandler)
    print('server running on port 5000')
