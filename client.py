import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path
import time
from tkinter import filedialog
from pathlib import Path
import ftplib
from ftplib import FTP 
import os 
import time
import ntpath
from path import Path



from playsound import playsound
import pygame
from pygame import mixer

for file in os.listdir('shared_files'):
    filename=os.fsdecode(file)
    listbox.insert(song_counter,filename)
    song_counter=song_counter+1

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected) 
    mixer.music.play()
    if(song_selected !=""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")     

PlayButton=Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font=("Callibri",10),command=play)
PlayButton.place(x=30,y=200)


def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")




def browseFiles():
    global listbox
    global song_counter
    global filePathLabel

    try:
        filename=filedialog.askopenfilename()
        HOSTNAME="127.0.0.1"
        USERNAME="lftpd"
        PASSWORD="lftpd"
         
        ftp_server=FTP(HOSTNAME,USERNAME,PASSWORD)
        ftp_server.encoding="utf-8"
        ftp_server.cwd('shared_files')
        fname=ntpath.basename(filename) 
        with open(filename,'rb')as file:
            ftp_server.storbinary(f"STOR{fname}",file)
        ftp_server.dir()
        ftp_server.quit()

        listbox.insert(song_counter,fname)
        song_counter=song_counter+1  

    except FileNotFoundError:
        print("Cancel Button Pressed")
        

def download():
    #textarea.insert(END,"\n"+"\nPlease wait file is downloading.....")
    #textarea.see("end")

    song_to_download=listbox.get(ANCHOR)
    infoLabel.configure(text="Downloading"+song_to_download)
    HOSTNAME="127.0.0.1"
    USERNAME="lftpd"
    PASSWORD="lftpd"
    home=str(Path.home())
    download_path=home+"/Downloads"
    ftp_server=ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)
    ftp_server.encoding="utf-8"
    ftp_server.cwd('shared_files')
    local_filename=os.path.join(download_path,song_to_download)
    file=open(local_filename,'wb')
    ftp_server.retrbinary('RETR'+song_to_download,file.write)
    ftp_server.dir()
    file.close()
    ftp_server.quit()
    infoLabel.configure(text="Downloading Completed")
    time.sleep(1)
    if(song_selected !=""):
        infolabel.configure(text="Now Playing"+song_selected)
    else:
        infolabel.configure(text="")    


stop=Button(window,text="Stop",width=10,bd=1,bg='SkyBlue',font=("Callibri",10),command=stop)
stop.place(x=200,y=200)

ResumeButton=Button(window,text="Resume",width=10,bd=1,bg='SkyBlue',font=("Callibri",10),command=resume)
ResumeButton.place(x=30,y=250)

PauseButton=Button(window,text="Pause",width=10,bd=1,bg='SkyBlue',font=("Calibri",10),command=pause)
PauseButton.place(x=200,y=250)

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()


       
