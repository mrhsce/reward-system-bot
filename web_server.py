#!/usr/bin/env python

# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.

import socket
import re
import shared

# Standard socket stuff:
host = '' # do we need socket.gethostname() ?
port = 34494
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests


def start_server():
    # Loop forever, listening for requests:
    while True:
        csock, caddr = sock.accept()
        print "Connection from: " + `caddr`
        req = csock.recv(1024) # get the request, 1kB max
        print req

        match_add = re.match('GET /add\?type=([a-zA-Z]+)\?v=(\d+\.\d{1,2}|\d+)\s', req)
        match_subtract = re.match('GET /subtract\?type=([a-zA-Z]+)\?v=(\d+\.\d{1,2}|\d+)\s', req)
        match_getfun = re.match('GET /getfun', req)

        if match_add:
           shared.update_hours(match_add.group(1), float(match_add.group(2)))
           print(match_add.group(1) + " " + match_add.group(2))
        if match_subtract:
           shared.update_hours(match_subtract.group(1), float(match_subtract.group(2)))
           print(match_subtract.group(1) + " " + match_subtract.group(2))
        if match_getfun:
           print(match_getfun.group(1) + " " + match_getfun.group(2))
    #
    #            # Look in the first line of the request for a move command
    #     # A move command should be e.g. 'http://server/move?a=90'
    #     match = re.match('GET /move\?a=(\d+)\sHTTP/1', req)
    #     if match:
    #         angle = match.group(1)
    #         print "ANGLE: " + angle + "\n"
    #         csock.sendall("""HTTP/1.0 200 OK
    # Content-Type: text/html
    #
    # <html>
    # <head>
    # <title>Success</title>
    # </head>
    # <body>
    # Boo!
    # </body>
    # </html>
    # """)
    #     else:
    #         # If there was no recognised command then return a 404 (page not found)
    #         print "Returning 404"
    #         csock.sendall("HTTP/1.0 404 Not Found\r\n")
        csock.close()