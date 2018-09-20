#!/usr/bin/env python

# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.

import socket
import re
import shared
import requests

# Standard socket stuff:
host = ''  # do we need socket.gethostname() ?
port = 34492
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests


def start_server():
    # Loop forever, listening for requests:
    while True:
        csock, caddr = sock.accept()
        print "Connection from: " + `caddr`
        req = csock.recv(1024)  # get the request, 1kB max
        print req

        match_activity = re.match('GET /activity\?type=([a-zA-Z]+)\s', req)
        match_add = re.match('GET /add\?type=([a-zA-Z]+)\?v=(\d+\.\d{1,2}|\d+)\s', req)
        match_subtract = re.match('GET /subtract\?type=([a-zA-Z]+)\?v=(\d+\.\d{1,2}|\d+)\s', req)
        match_getfun = re.match('GET /getfun\s', req)

        if match_activity:
            shared.update_hours_activity(match_activity.group(1))
            print(match_activity.group(1))
        if match_add:
            shared.update_hours(match_add.group(1), float(match_add.group(2)))
            print(match_add.group(1) + " " + match_add.group(2))
        if match_subtract:
            shared.update_hours(match_subtract.group(1), float(match_subtract.group(2)))
            print(match_subtract.group(1) + " " + match_subtract.group(2))
        if match_getfun:
            print("Get fun invoked")
            informFunTime()
        csock.close()


def informFunTime():
    session = requests.session()
    session.proxies['http'] = 'socks5h://ir124484:08740874@go.socadd.com:443'
    session.proxies['https'] = 'socks5h://ir124484:08740874@go.socadd.com:443'
    r = session.post("https://maker.ifttt.com/trigger/get_fun_time/with/key/b1_hFEHX3mCBV2sHH7Hr5N",
                      data={'value1': shared.get_fun_hours()})
    print("Get fun time request response status: " + str(r.status_code))
