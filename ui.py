    # -*- coding: utf-8 -*-
    """
    Created on Sun Sep 15 00:08:38 2019
    @author: bhavanisathish
    """
    
    
    import mysql.connector
    from tkinter import *
    from datetime import date
    from googletrans import Translator
    from gtts import gTTS
   
    import os
    from tkinter import *
    from tkinter import filedialog
    import speech_recognition as sr 
    root=Tk()
    root.title("personal diary")
    root.geometry('400x400')
    db_cur=mysql.connector.connect(host='localhost',user='root',passwd='',database='personaldiary')
    db=db_cur.cursor()
    
    def login():
        import tkinter.messagebox
        root.destroy()
        #from tkinter import *
        root1=Tk()
        root1.title("Login Page")
        root1.geometry('400x400')
        def log():
            username=textt.get()
            passwordss=textt1.get()
            print(username)
            print(passwordss)
            db.execute("select *from pd where name='%s' and password='%s'"%(username,passwordss))
            l=db.fetchone()
            if(l):
                    root1.destroy()
                    db_cur.commit()
                    root5=Tk()
                    menub=Menu(root5)
                    root5.config(menu=menub)
                    global text
                    text=Text(root5,width=100,height=20)
                    
                    text.pack()
                    fname1="C:/Users/bhavanisathish/sathish/"+str(date.today())+".txt"
                    
                    fname=filedialog.askopenfile(initialfile=fname1)
                    print(fname)
                    tt1 = fname.read()
                    if tt1 != None:
                         text.delete(1.0, END)
                         text.insert(1.0,tt1)
                    
                    def record():
                        while True:
                        # get audio from the microphone                                                                       
                            r = sr.Recognizer()                                                                                   
                            with sr.Microphone() as source:                                                                       
                                print("Speak:")  
                                try:                                                                              
                                    audio = r.listen(source)
                                    print("recorded")
                                    speech= r.recognize_google(audio)
                                    if(speech=="stop"):
                                        print("stoppped")
                                        break
                                    else:
                                        print(speech)
                                        global text
                                        text.insert(END,speech)
                                   
                                    
                                except sr.UnknownValueError:
                                    print("Could not understand audio")
                                except sr.RequestError as e:
                                    print("Could not request results; {0}".format(e))
                    def open():
                       global text
                       fin = filedialog.askopenfile()
                       print(fin)
                       tt = fin.read()
                       if tt != None:
                                text.delete(1.0, END)
                                text.insert(1.0,tt)
                              
                    
                    def save():#save the file
                       ###now=datetime.datetime.now()
                       fn=str(date.today())+".txt"
                       db.execute("select dname from pd where name='%s' and password='%s'"%(username,passwordss))
                       dn=db.fetchone()
                       
                      ### saveFilePath=filedialog.asksaveasfilename(title = fn,filetypes = ((".txt"),("all files","*.*")))
                       filename=filedialog.asksaveasfile(initialdir =dn ,initialfile=fn,defaultextension=".txt")
                       print(filename)
                       if filename:
                            #with open(filename, "w") as file:
                                ###file=open(filename)#,encoding="UTF-8")
                                #open("1.txt","r")
                                alltext=text.get(1.0, END)
                                filename.write(alltext)
                                #root.title(os.path.basename(filename))
                                filename.close()
                       """"   
                       
                       
                       filename=fn   
                       if filename:
                            ##file=open(filename,'w')
                            alltext=text.get(1.0, END)
                            filename.write(alltext)
                            #root.title(os.path.basename(filename))
                            file.close()"""
                    def show():
                        
                       ### mixer.init()
                    
                        translator = Translator()
                        destlang='ta'
                        alltext=text.get(1.0, END)
                        translated = translator.translate(alltext,  dest=destlang)
                        print(translated.text)
                        s=gTTS(text=translated.text,lang='ta',slow=False)
                        s.save("latest1.mp3")
                        os.system("latest1.mp3")
                        
                    
                    def stop():
                        mixer.music.stop()
                        os.remove("latest1.mp3")
                      
                    
                    fmenu=Menu(menub,tearoff=0)
                    menub.add_cascade(label="File",menu=fmenu)
                    fmenu.add_command(label="Open",command=open)
                    fmenu.add_command(label="Save",command=save)
                    fmenu.add_command(label="Exit",command=root5.destroy)
                    but=Button(root5,command=record,text="record me")
                    but.pack()
                    butt=Button(root5,command=show,text="here me")
                    butt.pack()
                    
                    butto=Button(root5,command=stop,)
                    butto.pack()
                    root5.mainloop()
            else:
                tkinter.messagebox.showinfo("error","Invaild username or password")
        laa=Label(root1,text='LOGIN PAGE')
        laa.pack(padx=10,pady=20)
        username=StringVar()
        passwords=StringVar()
        lf=Frame(root1)
        lf.pack(padx=10,pady=30)
        la=Label(lf,text='name')
        la.grid(row=5,column=5,padx=15,pady=20)
        textt=Entry(lf)
        textt.grid(row=5,column=7,padx=15,pady=20)
        la1=Label(lf,text='password')
        la1.grid(row=7,column=5,padx=15,pady=20)
        textt1=Entry(lf)
        textt1.grid(row=7,column=7,padx=15,pady=20)
        but=Button(lf,text='LOGIN',command=log)
        but.grid(row=8,column=7,padx=15,pady=20)
    
    
    def reg():
        import tkinter.messagebox
        root2=Tk()
        root2.title("Register Page")
        root2.geometry('400x400')
        def clicked():
            #sql="insert into pd(name,password,dname,language) values(%s,%s,%s,%s)"
            #val=(str(uname),str(password),str(dn),str(lang))
            uname=text.get()
            password=text1.get()
            dn=text2.get()
            lang=text3.get()
            if(uname =="" or password == "" or dn == "" or lang=="" ):
                tkinter.messagebox.showerror("Info","fill are the details")    
             
            else:
                try:
                    db.execute("insert into pd(name,password,dname,language) values('%s','%s','%s','%s')"%(uname,password,dn,lang));
                    db_cur.commit()
                    root2.destroy()
                    login()
                except:
                    tkinter.messagebox.showerror("Info","Diary name already exists.Please give another name")
            
        laa=Label(root2,text='REGISTRATION PAGE')
        laa.pack(padx=10,pady=20)
        lf=Frame(root2)
        uname=StringVar()
        password=StringVar()
        dn=StringVar()
        lang=StringVar()
        lf.pack(padx=30,pady=30)
        la=Label(lf,text='name')
        la.grid(row=5,column=5,padx=15,pady=20)
        text=Entry(lf)
        text.grid(row=5,column=7,padx=15,pady=20)
        la1=Label(lf,text='password')
        la1.grid(row=7,column=5,padx=15,pady=20)
        text1=Entry(lf,show='*')
        text1.grid(row=7,column=7,padx=15,pady=20)
        la2=Label(lf,text='Diary name')
        la2.grid(row=8,column=5,padx=15,pady=20)
        text2=Entry(lf)
        text2.grid(row=8,column=7,padx=15,pady=20)
        la3=Label(lf,text='Language')
        la3.grid(row=9,column=5,padx=15,pady=20)
        text3=Entry(lf)
        text3.grid(row=9,column=7,padx=15,pady=20)
        but=Button(lf,text='REGISTER',command=clicked)
        but.grid(row=10,column=7,padx=15,pady=20)   
        
    
    pa=Frame(root)
    pa.pack(padx=120,pady=10)
    button=Button(pa,text='Login',command=login)
    button.grid(row=0,column=5,padx=3)
    button1=Button(pa,text='Register',command=reg)
    button1.grid(row=0,column=6,padx=3)
    laa=Label(root,text='PERSONAL DIARY')
    laa.pack(padx=80,pady=60)
    root.mainloop()
