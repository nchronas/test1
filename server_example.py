#!/usr/bin/env python
 
import logging
import logging.handlers 

import socket
import SocketServer
import SimpleHTTPServer
import sys
import os
from time import sleep
from urlparse import urlparse, parse_qs
import signal
import time
import syslog

syslog.syslog('Mpu server started')


 
def signal_handler(signal, frame):
    httpd.shutdown
    print('You pressed Ctrl+C!')
    sys.exit(0)
	

PORT = 8000



    
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        print self.path  
        syslog.syslog('Mpu server request')

        if self.path[0:9]=='/logfiles':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('''
<!DOCTYPE HTML>
<html lang="en-US">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=index">
        <script type="text/javascript">
            window.location.href = "index"
        </script>
        <title>Page Redirection</title>
    </head>
    <body>
        <!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
        If you are not redirected automatically, follow the <a href='index'>link to example</a>
    </body>
</html>''')
            return        
            
        else:
        #serve files, and directory listings by following self.path from
        #current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    

signal.signal(signal.SIGINT, signal_handler)

httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()

    
