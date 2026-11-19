from tkinter import*
from PIL import  Image ,ImageTk
import os
import speech_to_text
import action
root=Tk()
root.title("AI Assistant")
root.geometry("550x675")  
root.resizable(False,False)
root.config(bg="#73f07b")
#ask fn
def ask():
     user_val=speech_to_text.speech_to_text()
     bot_val=action.Action(user_val)
     text.insert(END,"You : "+user_val+"\n")
     if bot_val !=None:
         text.insert(END,"Bot : "+bot_val+"\n")
     if bot_val=="Ok sir.":
         root.destroy()

def send():
    send=entry.get()
    bot=action.Action(send)
    text.insert(END,"You : "+send+"\n")
    if bot !=None:
        text.insert(END,"Bot : "+bot+"\n")  
    if bot=="Ok sir.":
        root.destroy()    
def delete():
    text.delete(1.0,END)
# center
root.grid_columnconfigure(0, weight=1)


#frame
frame=LabelFrame(root,padx=20,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#73f07b")
frame.grid(row=0,column=0,padx=55,pady=10)
#taxe label

text_label=Label(frame,text="AI Assistant", font=("comic Sans ms",14,"bold"),bg="#73f07b")

text_label.grid(row=0,column=0,padx=20,pady=10)
#Image
img=Image.open(os.path.join("image","AI Assistant.png"))
img=img.resize((300,270),Image.Resampling.LANCZOS)
image=ImageTk.PhotoImage(img)


image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)
  
  
#Adding some text
text=Text(root ,font=("courier",10, "bold") ,bg="#9aced9") 
text.grid(row=2,column=0)
text.place(x=100 ,y=350,width=350,height=100)


#Entry box
entry=Entry(root,justify="center")
entry.place(x=100 ,y=500,width=350,height=30)
  #button
Button1=Button(root,text="ASK" ,bg="#a3b8da",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=50,y=575)
  #button2
Button2=Button(root,text="SEND" ,bg="#a3b8da",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=210,y=575)  
  
   #button2
Button3=Button(root,text="Delete" ,bg="#a3b8da",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
Button3.place(x=370,y=575)  
   
  
  
  
root.mainloop()