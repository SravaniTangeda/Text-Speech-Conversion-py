#importing required module
from tkinter import *
import pyttsx3
# module to convert text to speech
window = Tk()
# create tkinter window
window.title("text_to_speech_convertor")
# title of window
window.geometry("650x550+350+400")
frame1 = Frame(window,bg = "lightpink",height = "150") # styling the frame
frame1.pack(fill = X)
# place the widget
frame2 = Frame(window,bg = "lightgreen",height = "500")
frame2.pack(fill=X)
label = Label(frame1, text = "Text to Speech",font = "bold, 36",bg = "lightpink")
# styling thelabel which shows text
label.place(x = 180, y = 70)
def talk():
# function which helps to set speech properties and convert text Speech
engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('volume',1)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say(enter_txt.get())
engine.runAndWait()
enter_txt = Entry(frame2, width = 45,bd = 4, font = 14)
# entry is used to enter text
enter_txt.place(x = 130, y = 52)
enter_txt.insert(0, "")
button = Button(frame2, text = "SUBMIT",width = "15", pady = 10,font = "bold, 15",command =talk, bg='lightyellow')
# create button which holds talk function using
command
button.place(x = 250,y = 130)
window.mainloop()
#Start the GUI

