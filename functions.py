import requests
import time
import os
import sys
import socket

def downRate():
    #list of HTTP GET URLs to be tested
    #HTTP
    url = 'http://i.4cdn.org/wsg/1519131696905.webm'
    #url = 'http://speedtest.ftp.otenet.gr/files/test100k.db'
    #url = 'http://mirror.filearena.net/pub/speed/SpeedTest_16MB.dat'
    #url = 'http://skse.silverlock.org/beta/skse_1_07_03_installer.exe'
    #url = 'http://www.bluej.org/download/files/BlueJ-windows-412.msi'
    #url = 'http://ttyplus.com/download/mtputty.zip'

    #HTTPS
    #url = 'http://ipv4.download.thinkbroadband.com/10MB.zip'
    #url = 'https://www.thinkbroadband.com/assets/images/download-files/iconDownload-5MB.png'
    #url = 'https://s3.amazonaws.com/blstudio/Stud.io.exe'
    #url = 'https://go.microsoft.com/fwlink/?Linkid=852157'
    #url = 'https://the.earth.li/~sgtatham/putty/latest/w32/putty-0.70-installer.msi'
    #url = 'https://discordapp.com/api/download?platform=win'
    #url = "https://github.com/jp9000/obs-studio/releases/download/21.0.1/OBS-Studio-21.0.1-Full-Installer.exe"
    
    #do an http GET and time it
    start = time.time()
    file = requests.get(url)
    end = time.time()

    #get file size in Mb
    headers = file.headers
    file_size = int(headers['Content-Length'])*8
    file_size = file_size/1000000
    
    #print data and return download speed
    print("size of file downloaded(Mb): ", file_size)
    dt = end - start
    print("time taken for download(Sec):", dt)
    rate = file_size/dt
    return rate

def upRate(uploop):

    dummy_file = 'dummy.txt'
    
    #list of post urls
    
    #original post url from stackexchange
    #post_url = 'http://httpbin.org/post'
    
    #ucsb http post bin
    post_url = 'http://ucsb.edu/post'

    #write a bunch of dummy text into a text file
    with open(dummy_file, 'wb') as dummy:
        for i in range (int(uploop)):
            dummy.write(str.encode('This is a dummy text. Its sole purpose is being uploaded to a server.'))
        dummy.close()
    
    #get dummy file size
    file_size = os.path.getsize('dummy.txt')*8/1000000

    #send the dummy.txt using HTTP post and time it
    files = open(dummy_file, 'rb')
    start = time.time()
    request = requests.post(post_url, data=files)
    end = time.time()
    dt = end-start
    headers = request.headers

    #print data and return upload speed
    print("upload file size(Mb)", file_size)
    print("upload time(sec): ", dt)
    rate = file_size/dt
    return rate


def pingTest(IP):
    #pretty simple, just use UNIX for 4 ping requests
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pingo = os.system('ping -c4 ' + IP)
    sock.close()
    return


