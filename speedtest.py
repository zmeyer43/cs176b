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
    #url = 'https://cf-media.sndcdn.com/Oq9TrcvNGT3E.128.mp3?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vT3E5VHJjdk5HVDNFLjEyOC5tcDMiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1MjA5OTMwMzd9fX1dfQ__&Signature=YkBgiqzKj8NTYXVMG0HnA36JV0bZDirdMAOFJ62kAMkDCCzTje6I9aIHiT3AaaqFSBLVo38rhfVnJsmZDZeXJmS3ZW9eEJR5deRsrOrq~vIH6HDFjmWiOtPIHXHp3XJ9cna7D3a58~1OV81UQKrAN8Wr8xZNwntCPZACgB7JhAMfjRu3pz6oT2jRasveZjimHpfG2k~SUDu3uxuBiTvth3~hK8i-57D1tZu9p3YwFJqACTS7TuQzHowpXMcVdiwQ4iw2f2fMiAHbNAarXRV9LLAJX5BlJ0mZyhaQ3FEc810RxKaCCDgHQk0Suc8ManW6vU3ofXK2XToaC~LnlH-xSQ__&Key-Pair-Id=APKAJAGZ7VMH2PFPW6UQ'
    
    #url = 'http://mirror.filearena.net/pub/speed/SpeedTest_16MB.dat'
    #url = 'https://cf-media.sndcdn.com/Oz3ATVtF0fbu.128.mp3?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiKjovL2NmLW1lZGlhLnNuZGNkbi5jb20vT3ozQVRWdEYwZmJ1LjEyOC5tcDMiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1MjA5OTAxNjZ9fX1dfQ__&Signature=ZfCJLK-S5JeKgByheXcFWLMrtbIKw6-~NDB7pOhF6LNkney94Kf70u80nGancQdoXZCVcBcdC3nQq~46HMx4pqswu4y56RceurNnyR8xXyacI3DDHyF1erO-bZVUfL~qQMauzlaDPlT7O-6TyTLLAwsnXxScpxsOnL7-nV6-Iw5yQPQnsKGkfENW7Oh9lkjSZsLiLjEU2H3y893jMB-3-7DjzQNJKujCwU0DsMXuygdta6gHh4z4wl7XNFqbuREfk~pMSmvn66~QnIShZPe~BDD~1iSgjFA77Ak-atwcc8DoJbE6~dUeUmCKZ16xasBnQzj81x2OKBHTHfTEJ8ezlA__&Key-Pair-Id=APKAJAGZ7VMH2PFPW6UQ'
    #2.9 Mb
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
    
    #CCleaner filehippo DL 27.68 Mb
    #url = "https://filehippo.com/download/file/afb38ae6a4524b8f97972a5d3798d11f9d62d7eee5811e2d68c509aec049eb36/"

    #OBS STUDIO 836.8 Mb
    #url = "https://github.com/jp9000/obs-studio/releases/download/21.0.1/OBS-Studio-21.0.1-Full-Installer.exe"
    
    #do an http GET and time it
    start = time.time()
    file = requests.get(url)
    end = time.time()
    


    headers = file.headers
    file_size = int(headers['Content-Length'])*8
    file_size = file_size/1000000
    print("size of file downloaded(Mb): ", file_size)
    dt = end - start
    print("time taken for download(Sec):", dt)
    rate = file_size/dt
    return rate

def upRate():
    
    dummy_file = 'dummy.txt'
    #original post url from stackexchange
    #post_url = 'http://httpbin.org/post'

    #ucsb http post bin
    post_url = 'http://ucsb.edu/post'
    
    #write a bunch of dummy text into a text file
    with open(dummy_file, 'wb') as dummy:
        for i in range (int(uploop)):
            dummy.write(str.encode('This is a dummy text. Its sole purpose is being uploaded to a server.'))
        dummy.close()
    file_size = os.path.getsize('dummy.txt')*8/1000000
    
    #send the dummy.txt using HTTP post
    files = open(dummy_file, 'rb')
    start = time.time()
    request = requests.post(post_url, data=files)
    end = time.time()
    dt = end-start
    headers = request.headers
    
    
    print("upload file size(Mb)", file_size)
    print("upload time(sec): ", dt)
    rate = file_size/dt
    return rate


def pingTest(IP):
    #pretty simple, just use UNIX for 4 ping requests
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start = time.time()
    pingo = os.system('ping -c4 ' + IP)
    end = time.time()
    dt = end - start
    dtms = dt*1000
    sock.close()
    return






while(1):
    cmd = input('\ninput 0, 1, or 2 for downspeed, upspeed, or ping test (or q for quit)\n')
    if(cmd == '0'):
        tmp = downRate()
        print("downspeed(Mbps): ", tmp)
    elif(cmd == '1'):
        uploop = input('input number of times to write the string:\n')
        tmp = upRate()
        print("upspeed(Mbps): ", tmp)
    elif(cmd == '2'):
        pingplace = input('input pingplace: ')
        pingTest(pingplace)
    elif(cmd == 'q'):
        break
    else:
        print('please enter a valid input next time')


