import json
import ftplib
import os
import time

dir_files = ""
ftp_host = ""
ftp_port = ""
ftp_user = ""
ftp_pass = ""
delay = ""
cyclic = ""
ftp = ""

def loadSettings():
  if os.path.exists('ftpclient.settings'):
    with open('ftpclient.settings') as json_file:
      data = json.load(json_file)
      global dir_files
      dir_files = data['dir_files']
      global ftp_host
      ftp_host = data['ftp_host']
      global ftp_port
      ftp_port = data['ftp_port']
      global ftp_user
      ftp_user = data['ftp_user']
      global ftp_pass
      ftp_pass = data['ftp_pass']
      global delay
      delay = data['delay']
      global cyclic
      cyclic = data['cyclic']
    return True
  else:
    return False

def connectToFtpServer():
  global ftp
  ftp = ftplib.FTP()
  ftp.connect(ftp_host, ftp_port)
  ftp.login(ftp_user, ftp_pass)
  return True

def sendFiles():
  while True:
    entries = os.listdir(dir_files)
    for entry in entries:
      ftp.storbinary("STOR " + entry, open(dir_files+"/"+entry, "rb"), 1024)
      time.sleep(delay)
    if not cyclic:
      break

if loadSettings():
  if connectToFtpServer():
    sendFiles()
  else:
    print("Error connect to FTP Server")
else:
  print("The file ftpclient.settings was not found.")

