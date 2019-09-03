from talk import *
from tkinter import *
import threading 
import sqlite3  as dbapi

#important link
#https://stackoverflow.com/questions/50175555/how-to-change-tkinter-label-while-another-process-is-running        

def drop():
        cur.execute('drop table data')
        
def insert():
        print(alphaId.get())
        cur.execute('create table data(WolfAlpha TEXT, micIndex INTEGER)')
        cur.execute('insert into data values(?,?)',(alphaId.get(),mic_index.get()))
        con.commit()
        window2.destroy()

def setting():
    
    label = Label(window2,text="Enter your Wolfram Alpha Id",font=('arial',15,),fg="blue").pack(pady=10)
    wolfAlplaName = Entry(window2,textvariable=alphaId,font=('arial',15)).pack(pady=10,ipadx=100,ipady=10)

    label = Label(window2,text="Enter Microphone Index ",font=('arial',15,),fg="blue").pack(pady=10)
    wolfAlplaName = Entry(window2,textvariable=mic_index,font=('arial',15)).pack(pady=10,ipadx=100,ipady=10)
    
    b = Button(window2,text="ok",font=('arial',15),fg="red",command=insert).pack()
    frame=Frame(window2)
    
    label2=Label(frame,text=" a Siddhant shah production ",pady=1,font=0.00005).pack(side='bottom')
    frame.pack(side="bottom")
    mainloop()

try:
    con=dbapi.connect('talkData.db')
    cur = con.cursor()
    cur.execute('select * from data')
    t=(cur.fetchall())
    m=t[0][1]
    w=t[0][0]
    try:
        window = Tk()
        window.config(bg = "orange")
        window.geometry('500x300+%d+%d' %(int(500/1.5),int(300/1.5)))
        t = voicePrint()
        var =StringVar()
        var.set(" ")
        
        def call():
            print(var.get())
            #check audio is given or not
            if(var.get() != " "):
                button.config(text = "ok you typed")
                #then take a file of entry
                result=var.get()
        
            else:
                
                t.set_Microphone(m)
                button.config(text = "listening")
                t.mic_Listen()
                try:
                    result = t.display()
                except:
                    button.config(text = "opsss")
                    t.playaudio("sorry i dot understand please speak again i am listening")
                    button.config(text = "Click me")
                #var is a entry box variable
                var.set(result)
           
            try:
                #dntXWH3RH-KE5EVL4W5Q
                button.config(text = "Thinking")
                result=t.wolframalphaCon(w,result)
                #m.forget()
                button.config(text = "Speaking")
                t.playaudio(result)
        
            except:
                
                button.config(text = "Thinking")
                result = t.wiki(result)
                button.config(text = "Speaking")
                t.playaudio(result)
            var.set(" ")    
            button.config(text = "Click me")
    

        def thread(): # NEW
            threading.Thread(target=call).start() # NEW

        window.title('your personal assistant')
        entry = Entry(window,textvariable=var,font=('arial',15)).pack(pady=10,ipadx=100,ipady=10)
        #button image and button

        button = Button(window,border="0",font=('arial',35),fg="red",bg="orange",text='Click me',command= thread)
        button.pack(ipady=25)

        
        button2 = Button(window,text='Setting',bg="orange",fg="orange",command=drop).pack(side="right")
        
        frame=Frame(window)
        label2=Label(frame,text="       a Siddhant shah production",pady=1,font=0.005,fg='black',bg="orange").pack(side='bottom')
        frame.pack(side="bottom")

        
        mainloop()

    except:
            print(error)
except:
    window2=Tk()
    window2.geometry('500x350+%d+%d' %(int(500/1.5),int(300/1.5)))
    alphaId = StringVar()
    mic_index=IntVar() 
    setting()
               
