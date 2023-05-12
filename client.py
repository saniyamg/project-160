import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


window=Tk()
window.title('music window')
window.geometry('300x300')
window.configure(bg='LightSkyBlue')




PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None




# Boilerplate Code
def receiveMessage():
    global SERVER
    global BUFFER_SIZE

    while True:
        chunk = SERVER.recv(BUFFER_SIZE)
        try:
            if("tiul" in chunk.decode() and "1.0," not in chunk.decode()):
                letter_list = chunk.decode().split(",")
                listbox.insert(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
                print(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
            else:
                textarea.insert(END,"\n"+chunk.decode('ascii'))
                textarea.see("end")
                print(chunk.decode('ascii'))
        except:
            pass

# Teacher Activity
def showClientsList():
    pass

# Prevoius class code
# Here we ended the last class
def connectToServer():
    global SERVER
    global name
    global sending_file
    cname = name.get()
    SERVER.send(cname.encode())


def openChatWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here


    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    selectlabel=Label(window,text='select song', bg='LightSkyBlue',font=('calibri',8))
    selectlabel.place(x=2,y=1)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playbutton=Button(window,text='play', bg='SkyBlue',font=('calibri',8))
    playbutton.place(x=30,y=200)

    stop=Button(window,text='stop', bg='SkyBlue',font=('calibri',8))
    stop.place(x=200,y=200)

    upload=Button(window,text='upload', bg='SkyBlue',font=('calibri',8))
    upload.place(x=30,y=250)

    download=Button(window,text='download', bg='SkyBlue',font=('calibri',8))
    download.place(x=200,y=250)

    infolabel=Button(window,text='', bg='SkyBlue',font=('calibri',8))
    infolabel.place(x=4,y=200)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Boilerlate Code
    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    openChatWindow()

setup()
