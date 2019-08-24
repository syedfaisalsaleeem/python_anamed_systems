from tkinter import *
import time
from PIL import Image, ImageTk
import os
import threading
from scrollable_7 import ScrollFrame
from scrollable_8 import ScrollFrame1
from toggle_button_1 import Toggle
import sqlite3
import socket
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import random
from datetime import date
from pandas import DataFrame
def raise_frame(frame):
    frame.tkraise()
temp="notempty"
s11=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s11.bind((socket.gethostname(),1234))
s11.listen(5)
clientsocket,address=s11.accept()
clientsocket.send(bytes("Close!","utf-8"))
with open('hello.txt') as my_file:
     my_file.seek(0, os.SEEK_END) # go to end of file
     if my_file.tell(): # if current position is truish (i.e != 0)
         my_file.seek(0) # rewind the file for later use 
     else:
         print ("file is empty")
         temp="empty"
if temp=="empty":
    import done_screen_1_end
    

else:
    #import video_work
    def on_configure(event):

        canvas.configure(scrollregion=canvas.bbox('all'))



    root = Tk()
    root.geometry('1024x600+0+0')
    list_set=['False']
##    s11=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##    s11.bind((socket.gethostname(),1234))
##    s11.listen(5)
##    clientsocket,address=s11.accept()
##    clientsocket.send(bytes("Open1!","utf-8"))

    list_stop=['open']
    l_f_hrs=[0]
    l_f_mins=[0]


    imagePath=PhotoImage(file="header.png")
    widgetf=Label(root,image=imagePath)
    widgetf.place(x=0,y=0)

    with open("hello.txt",'r') as f:
        read_file=f.read()
        read_file=str(read_file)

    q_1_s=0


            
        

    check_temperature=['False']
    l_cool=['Timer is going to start when temperature reached the setpoint']
    def read_every_second():

        global q_1_s,clientsocket,address,s,list_set,check_temperature,l_cool
        global e5,e6,check_temperature,l_cool,list_set,list_stop

        t=time.localtime()
##        current_time_1=time.strftime("%H:%M:%S",t)
##
##        entry_time=Entry(root)
##        entry_time.config(bg='#efeeef',fg='black', font=('Arial', 15,'bold'),relief=GROOVE,borderwidth=0)
##        entry_time.place(x=850,y=50,width=150)
##        entry_time.insert(0,current_time_1)
##        x_temperature = random.randint(49,50)
##
##        entry_temperature=Entry(root)
##        entry_temperature.config(bg='#efeeef',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
##        entry_temperature.place(x=270,y=50,width=500)
##        
##        degree_sign=u'\u00B0'
##        entry_temperature.insert(0,str(x_temperature)+degree_sign+"C")
##        if list_set[-1]=="True":
##                test=Entry(root)
##                test.config(bg='#efeeef',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0)
##                test.place(x=350,y=10,width=400)
##                test.insert(0,'Current Temperature')
##                entry_temperature=Entry(root)
##                entry_temperature.config(bg='#efeeef',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0)
##                entry_temperature.place(x=640,y=10,width=120)
##                #entry_temperature.insert(0,'80 C')
##                degree_sign=u'\u00B0'
##                entry_temperature.insert(0,str(x_temperature)+degree_sign+"C")
##                timer1=Entry(root)
##                timer1.config(bg='#efeeef',fg='black', font=('Arial', 16,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
##                timer1.place(x=270,y=55,width=500,height=35)
##                #timer1.insert(0,'                                                     ')
##                timer1.insert(0,l_cool[-1])
##                if (len(list_set)>2):
##                    list_set.clear()
##                    list_set.append('True')
##
##                
##
##        if list_set[-1]=="False":
##                test=Entry(root)
##                test.config(bg='#efeeef',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
##                test.place(x=300,y=10,width=400)
##                test.insert(0,'Current Temperature')     
##                entry_temperature=Entry(root)
##                entry_temperature.config(bg='#efeeef',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
##                entry_temperature.place(x=270,y=50,width=500)
##                
##                degree_sign=u'\u00B0'
##                entry_temperature.insert(0,str(x_temperature)+degree_sign+"C")
##                
##                if (len(list_set)>2):
##                    list_set.clear()
##                    list_set.append('False')


        q_1_s+=1
            
            

        if q_1_s>200:
    #        graph1.draw_axes()
            q_1_s=0
        root.after(200, read_every_second)



    #read_every_second()
    threadtime = threading.Thread(target = read_every_second(), args = ())
    threadtime.start()
    q_1_s_faisal=0

    def read_every_second_faisal():
        global q_1_s_faisal
        today = date.today()
##        d1 = today.strftime("%d-%B-%Y")
##        entry_d1=Entry(root)
##        entry_d1.config(bg='#efeeef',fg='black', font=('Arial', 15,'bold'),relief=GROOVE,borderwidth=0)
##        entry_d1.place(x=850,y=13,width=150)
##        entry_d1.insert(0,d1)
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open!","utf-8"))

        q_1_s_faisal+=1

        if q_1_s_faisal>70:

            q_1_s_faisal=0
        root.after(70, read_every_second_faisal)



    
    thread3 = threading.Thread(target = read_every_second_faisal(), args = ())
    thread3.start()


    
    label_temp = Label(root, text="Current Temperature",bg='#efeeef',fg='#231f1e', font=('Arial', 18,'bold'))
    label_temp.place(x=400,y=10,width=300)

    f1 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f1.configure(bg='#f7f7ff')

    f2 = Frame(root,height=500,width=1022,relief='raised',borderwidth=1)
    f2.configure(bg='#f7f7ff')
    f3 = Frame(root,height=500,width=1022,relief='raised',borderwidth=1)
    f3.configure(bg='#f7f7ff')
    f4=Frame(root,height=500,width=1022,relief='raised',borderwidth=1)
    f4.scrollFrame=ScrollFrame(f4)
    f4.configure(bg='#f7f7ff')
    f5 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f5.configure(bg='#f7f7ff')
    f6 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f6.configure(bg='#f7f7ff')
    f7 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f7.configure(bg='#f7f7ff')
    f8 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f8.configure(bg='#f7f7ff')
    f_addnewuser = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_addnewuser.configure(bg='#f7f7ff')
    f_setting = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_setting.configure(bg='#f7f7ff')
    f_ins_setting = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_ins_setting.configure(bg='#f7f7ff')
    f_servicemode = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_servicemode.configure(bg='#f7f7ff')
    f_servicemode1 = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_servicemode1.scrollFrame=ScrollFrame1(f_servicemode1)
    f_servicemode1.configure(bg='#f7f7ff')
    f_about = Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_about.scrollFrame=ScrollFrame1(f_about)
    f_about.scrollFrame.pack(fill='both',expand=True)
    f_graph=Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_graph.configure(bg='#f7f7ff')
    fcontact=Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    fcontact.configure(bg='#f7f7ff')
    f_result=Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_result.configure(bg='#f7f7ff')
    f_result_data=Frame(root,height=500,width=1024,relief='raised',borderwidth=1)
    f_result_data.configure(bg='#f7f7ff')
    f_result_data.scrollFrame=ScrollFrame(f_result_data)
    f_result_data.configure(bg='#f7f7ff')


    for frame in (f1, f2, f3, f4,f5,f6,f7,f8,f_addnewuser,f_setting,f_ins_setting,f_servicemode,f_servicemode1,f_about,f_graph,fcontact,f_result,f_result_data):

        
        frame.grid(row=1,column=0,sticky='news',pady=100)
        frame.pack_propagate(0)
        f4.scrollFrame.pack(side="top", fill="both", expand=True)
        

        

    raise_frame(f1)

    l_entry_call_name=['None']
    l_entry_call_designation,l_entry_call_contact,l_entry_call_employeid=['None'],['None'],['None']
    l_entry=['None']
    l_entry_password=['None']
   
    l_entry_e4,l_entry_e5,l_entry_e6,l_entry_e7=['None'],['None'],['None'],['None']
    
    l_e4=[0]
    current=200
    current_1=200
    dict_1={}
    
    
    
    OptionList1 = [
    '                            ',
    "Slow",
    "Medium",
    "Fast",
    ]
    OptionList = [
    '                            ',
    "OFF",
    "25 %",
    "50 %",
    "75 %",
    "100 %"
    ]
    OptionList2 = [
    "                            ",
    "faisal"

    ]
    lena="drop.png"
    def settings():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Close!","utf-8"))
        raise_frame(f_setting)
    def back_new():
        global lena,OptionList2,variable2
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8"))
        clientsocket.send(bytes("Open1!","utf-8"))
        OptionList2.clear()
  
        print(OptionList2)
        print(dict_1)
        OptionList2.append("                            ")
        for new11 in dict_1.keys():
            OptionList2.append(dict_1[new11][0])
            print(dict_1[new11][0])
            print(OptionList2)
        raise_frame(f1)
        variable2 = StringVar(f5)
        variable2.set(OptionList2[0])
        opt2 = OptionMenu(f5, variable2, *OptionList2)
        opt2.config(bg='white',font=('Arial', 18),relief=GROOVE,borderwidth=0,activeforeground = "#00afef",activebackground = "white",highlightbackground='white')
        opt2['menu'].config(bg='white',font=('Arial',18),activeforeground = "white",activebackground = "#00afef")
        opt2.place(x=690,y=324,width=270,height=38)

        img = Image.open("drop.png")
        filename = ImageTk.PhotoImage(img)
        canvas = Canvas(f5,height=42,width=35)
        
        canvas.image = filename  # <--- keep reference of your image
        canvas.create_image(0,0,anchor='nw',image=filename)
        #canvas.grid(row=508,column=8005)
        canvas.place(x=927,y=322)
        #canvas.pack(side=RIGHT)
        
        


    def limitSizeDay1(*args):
        value = dayValue1.get()
        if(l_e4[-1]=="call_designation"):
                   
            ha_2=e2.get()
            ha_2=str(ha_2)
            if len(value) > 14: dayValue1.set(value[:14])
        if(l_e4[-1]=="call_name"):
                   
            ha_2=e2.get()

            ha_2=str(ha_2)



            if len(value) > 14: dayValue1.set(value[:14])
        if(l_e4[-1]=="call_employeid"):
                   
            ha_2=e2.get()

            ha_2=str(ha_2)
            if len(value) > 14: dayValue1.set(value[:14])

    x_faisal_meter=0

    def read_every_second_meter():
            global x_faisal_meter


            x_faisal_meter+=1    
            if x_faisal_meter>100:
        #        graph1.draw_axes()
                x_faisal_meter=0
            f_graph.after(100, read_every_second_meter)



    read_every_second_meter()






    dayValue1 = StringVar()
    dayValue1.trace('w', limitSizeDay1)
    
    imagePath_k_b_1=PhotoImage(file="DA_1217key.png")
    widgetf=Label(f3,image=imagePath_k_b_1)
    widgetf.place(x=0,y=0)

    e3 = Entry(f3)
    e3.config(justify=LEFT,font=('arial',21),takefocus='on',textvariable=dayValue1)
    e3.place(x=48,y=13,height=85,width=930)
    
    
    imagePath_f_1=PhotoImage(file="screens2.png")
    widgetf_1=Label(f5,image=imagePath_f_1)
    widgetf_1.place(x=0,y=0)

    
    

    

    def change_start_screen():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Close!","utf-8"))

        raise_frame(f5)
    def change_about():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Close!","utf-8"))

        raise_frame(f_about)

        #pass
    def add_user4():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Close!","utf-8"))
        raise_frame(f4)
    def back():
        global s11
        raise_frame(f1)
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8"))
    def call_1(event):
        global l_entry_e4,l_e4
        
        print('entry')
        e2.delete(0,END)
        f5.focus()
        e2.focus()

        if l_entry_e4[-1] =='None':
            e2.insert(0,'')
        else:
            e2.delete(0,END)
            e2.insert(0,l_entry_e4[-1])
            l_entry_e4.clear()

        if(len(l_e4)>2):
            del l_e4[0]
        
        l_e4.append('e4')
        raise_frame(f2)
        #change_1()


    def call_2(event):
        global l_entry_e5,l_e4
        print('entry')
        e5.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='black')
    
        e9.delete(0,END)
        f5.focus()
        e9.focus()
        if l_entry_e5[-1] =='None':
            e9.insert(0,'')
        elif l_entry_e5[-1]=='infinity':
            e9.delete(0,END)
            e9.insert(0,'')
            
            e5.delete(0,END)
            
        else:
            e9.delete(0,END)
            e9.insert(0,l_entry_e5[-1])
            l_entry_e5.clear()
        #e2.delete(0,END)
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('e5')
        raise_frame(f8)

    def call_3(event):
        global l_entry_e6,l_e4
        e6.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='black')
        print('entry')
        e9.delete(0,END)
        f5.focus()
        e9.focus()
        if l_entry_e6[-1] =='None':
            e9.insert(0,'')

        elif l_entry_e6[-1]=='infinity':
            e9.delete(0,END)
            e9.insert(0,'')
            
            e6.delete(0,END)
        else:
            e9.delete(0,END)
            e9.insert(0,l_entry_e6[-1])
            l_entry.clear()
        #e2.delete(0,END)
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('e6')
        raise_frame(f8)

    def call_4(event):
        global l_entry,l_e4
        print('entry')
        e3.delete(0,END)
        f5.focus()
        if l_entry_e7[-1] =='None':
            e3.insert(0,'')
        else:
            e3.delete(0,END)
            e3.insert(0,l_entry_e7[-1])
            l_entry.clear()

        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('e7')
        raise_frame(f3)
    def registration():
        pass

    def call_name(event):
        global l_entry,l_e4,l_entry_call_name
        print('entry')
        e3.delete(0,END)
        t=e_name.get()
        if(len(l_entry_call_name)>2):
            del l_entry_call_name[0]
        l_entry_call_name.append(t)

        e3.config(font=('arial',21),takefocus='off',borderwidth='2')
        f_addnewuser.focus()
        if l_entry_call_name[-1] =='None':
            e3.insert(0,'')
        else:
            #e3.delete(0,END)
            e3.insert(0,l_entry_call_name[-1])
            l_entry.clear()
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('call_name')
        raise_frame(f3)


    def call_designation(event):
        global l_entry,l_e4,l_entry_call_designation
        print('entry')
        e3.delete(0,END)
        t=e_designation.get()
        if(len(l_entry_call_designation)>2):
            del l_entry_call_designation[0]
        l_entry_call_designation.append(t)
        e3.config(font=('arial',21),takefocus='off',borderwidth='2')
        f_addnewuser.focus()
        if l_entry_call_designation[-1] =='None':
            e3.insert(0,'')
        else:
            #e3.delete(0,END)
            e3.insert(0,l_entry_call_designation[-1])
            l_entry.clear()
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('call_designation')
        raise_frame(f3)

    def call_contact(event):
        global l_entry,l_e4,l_entry_call_contact
        print('entry')
        ec.delete(0,END)
        f_addnewuser.focus()
        t=e_contact.get()
        l_entry_call_contact.append(t)

        
        ec.focus()
        if l_entry_call_contact[-1] =='None':
            ec.insert(0,'')
        else:
            #e2.delete(0,END)
            ec.insert(0,l_entry_call_contact[-1])
            l_entry.clear()
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('call_contact')
        raise_frame(fcontact)
    def call_employeid(event):
        global l_entry,l_e4,l_entry_call_employeid
        print('entry')
        e3.delete(0,END)
        e3.config(font=('arial',21),takefocus='off',borderwidth='2')
        t=e_employeid.get()
        l_entry_call_employeid.append(t)
        f_addnewuser.focus()
        if l_entry_call_employeid[-1] =='None':
            e3.insert(0,'')
        else:
            #e3.delete(0,END)
            e3.insert(0,l_entry_call_employeid[-1])
            l_entry.clear()
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('call_employeid')
        raise_frame(f3)
    def click():
       global variable1,variable1,variable2,e4,e5,e6,OptionList2,list_set
       print(e5.get())
       print(len(variable1.get()),len(variable.get()),len(variable2.get()),len(e4.get()),e5.get(),e6.get()),list_set
       if((len(e4.get())!=0 and len(e5.get()) !=0 and len(e6.get()) !=0 and len(variable1.get()) != 28 and len(variable.get()) !=28 and len(variable2.get())!=28)):
           clientsocket,address=s11.accept()
           clientsocket.send(bytes("Open2!","utf-8"))
           
           raise_frame(f_graph)
           if(len(list_set)>2):
            del list_set[0]
           list_set.append('True')
           reading_graph()
           
       elif(len(e4.get())!=0 and len(variable1.get()) != 28 and len(variable.get()) !=28 and len(variable2.get())!=28 and (e5.get()!="Hrs") and (e6.get()!="Min")):
           clientsocket,address=s11.accept()
           clientsocket.send(bytes("Open2!","utf-8"))
           
           raise_frame(f_graph)
           if(len(list_set)>2):
                del list_set[0]
           list_set.append('True')
           reading_graph()
           
       else:
            import popup_6
    def edit():

        pass


    key_1=0
    def add_user():
        global current,current_1,dict_1,key_1,list_faisal
        
        list_xqq=[]
        def edit_user(q_edit):
            global dict_1,current_1,dict_1,list_faisal
            #raise_frame(f4)
            list_xqqq=[]
            for new1 in dict_1.keys():
                xa=dict_1[new1][0]
                xa.lower()
                xb=e_name.get()
                xb.lower()
                if dict_1[new1][0] ==dict_1[q_edit][0]:
                    continue

                
                elif xa.lower() ==xb.lower():
                    import popup_name

            
            if(len(e_name.get())!=0 and len(e_employeid.get()) !=0) :
                for widget in f4.winfo_children():
                    widget.destroy()
                t_name=e_name.get()
                t_designation=e_designation.get()
                t_contact=e_contact.get()
                t_employeid=e_employeid.get()
                
                dict_1[q_edit]=[t_name,t_employeid,t_contact,t_designation]
                print(dict_1)
                if(len(list_xqqq)>2):
                        del list_xqqq[0]
                for xqqq in dict_1.keys():
                    list_xqqq.append(xqqq)
                list_xqqq.sort(reverse=True)
                f4.scrollFrame=ScrollFrame(f4)
                for row in range(len(dict_1)+1):
                    a = row
                    Label(f4.scrollFrame.viewPort, text=" ", width=150,height=150, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)

                f4.scrollFrame.pack(side="top", fill="both", expand=True)
                l=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Add New User",font=('Arial', 16,'bold'), command=lambda:raise_frame(f_addnewuser)).place(x=12,y=70,width=200,height=45)
                l_1=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_new).place(x=805,y=70,width=150,height=45)
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='Users',font=('Arial',18,'bold')).place(x=470,y=10)
                Label(f4.scrollFrame.viewPort,fg='black',bg='white',relief='raised',borderwidth=2, text='Name',font=('Arial',15,'bold')).place(x=1,y=150,width=200,height=50)
                Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Employer ID',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=201,y=150,width=200,height=50)
                Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Contact',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=401,y=150,width=200,height=50)
                Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Designation',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=601,y=150,width=200,height=50)
                Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Actions',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=801,y=150,width=200,height=50)




                            
                if (len(list_xqqq)==0):
                    current=200
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised', text='',font=('Arial',15,'bold')).place(x=1,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=201,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=401,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=601,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=801,y=current,width=200,height=70)
                    
                else:    
                    print(list_xqqq[0])
                    c_current=200
                    for fz2 in list_xqqq:
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised', text=dict_1[fz2][0],font=('Arial',15,'bold')).place(x=1,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][1],relief='raised',font=('Arial',15,'bold')).place(x=201,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][2],relief='raised',font=('Arial',15,'bold')).place(x=401,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][3],relief='raised',font=('Arial',15,'bold')).place(x=601,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=801,y=c_current,width=200,height=70)
                        c_current=c_current+70
                current_1=210
                for last_1 in list_xqqq:
                        a=last_1
                        Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Delete",font=('Arial',15,'bold'), command=lambda x=a: delete_1(x)).place(x=815, y=current_1,width=75,height=50)
                        Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Edit",font=('Arial',15,'bold'), command=lambda x=a: edit_1(x)).place(x=910, y=current_1,width=75,height=50)
                        print(list_faisal)
                        if(len(list_faisal)>2):
                            del list_faisal[0]
                        list_faisal.append(current_1)
                        current_1=current_1+70
                        print(list_faisal)

                Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Add User",font=('Arial', 16,'bold'), command=add_user).place(x=605,y=347,width=150,height=45)
                raise_frame(f4)
                e_name.delete(0,END)
                e_designation.delete(0,END)
                e_contact.delete(0,END)
                e_employeid.delete(0,END)
                
            else:
                import popup_6
        def back_edit():
                    Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Add User",font=('Arial', 16,'bold'), command=add_user).place(x=605,y=347,width=150,height=45)
                    e3.delete(0,END)
                    e_name.delete(0,END)
                    e_designation.delete(0,END)
                    e_contact.delete(0,END)
                    e_employeid.delete(0,END)
                    
                    raise_frame(f4)

            

            
        def edit_1(q_2):
            global dict_1,current
            current=250
            edit_dict=dict_1.keys()
            print(dict_1[q_2])
            e_name.delete(0,END)
            e_designation.delete(0,END)
            e_contact.delete(0,END)
            e_employeid.delete(0,END)
            e_name.insert(0,dict_1[q_2][0])
            e_designation.insert(0,dict_1[q_2][3])
            e_contact.insert(0,dict_1[q_2][2])
            e_employeid.insert(0,dict_1[q_2][1])
            Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Save",font=('Arial', 16,'bold'), command=lambda x=q_2: edit_user(x)).place(x=605,y=347,width=150,height=45)
            #Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Back1",font=('Arial', 16,'bold'), command=back_edit).place(x=805,y=70,width=150,height=45)

            raise_frame(f_addnewuser)



        def delete_1(q_1):
            
            #print('delete')
            def delete_2(q_1):
                    global dict_1,current

                     
                    current=250
                    list_xq=[]
                    cf_1=dict_1.keys()
                    print(len(dict_1))
                    print(cf_1)
                    print(q_1)
                    del dict_1[q_1]
                    for widget in f4.winfo_children():
                        widget.destroy()

                    print(dict_1)
                    print(dict_1.keys())
                    if(len(list_xq)>2):
                        del list_xq[0]


                    for xq in dict_1.keys():
                        list_xq.append(xq)
                    list_xq.sort(reverse=True)
                    f4.scrollFrame=ScrollFrame(f4)
                    for row in range (len(dict_1)+1):
                        a = row
                        Label(f4.scrollFrame.viewPort, text=" ", width=150,height=150, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)
                    f4.scrollFrame.pack(side="top", fill="both", expand=True)
                    l=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Add New User",font=('Arial', 16,'bold'), command=lambda:raise_frame(f_addnewuser)).place(x=12,y=70,width=200,height=45)
                    l_1=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_new).place(x=805,y=70,width=150,height=45)


                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='Users',font=('Arial',18,'bold')).place(x=470,y=10)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='white',relief='raised',borderwidth=2, text='Name',font=('Arial',15,'bold')).place(x=1,y=150,width=200,height=50)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Employer ID',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=201,y=150,width=200,height=50)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Contact',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=401,y=150,width=200,height=50)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Designation',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=601,y=150,width=200,height=50)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Actions',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=801,y=150,width=200,height=50)


                    
                    
                    if (len(list_xq)==0):
                        c_current=200
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text='',font=('Arial',14,'bold')).place(x=1,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=201,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=401,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=601,y=c_current,width=200,height=70)
                        Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=801,y=c_current,width=200,height=70)
                        
                    else:    
                        print(list_xq[0])
                        c_current=200
                        for fz1 in list_xq:
                            Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text=dict_1[fz1][0],font=('Arial',14,'bold')).place(x=1,y=c_current,width=200,height=70)
                            Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz1][1],relief='raised',font=('Arial',14,'bold')).place(x=201,y=c_current,width=200,height=70)
                            Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz1][2],relief='raised',font=('Arial',14,'bold')).place(x=401,y=c_current,width=200,height=70)
                            Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz1][3],relief='raised',font=('Arial',14,'bold')).place(x=601,y=c_current,width=200,height=70)
                            Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=801,y=c_current,width=200,height=70)
                            c_current=c_current+70
                        current_1=210
                        list_faisal=[]
                        for last_1 in list_xq:
                            a=last_1
                            Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Delete",font=('Arial',15,'bold'),command=lambda x=a: delete_1(x)).place(x=815, y=current_1,width=75,height=50)
                            Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Edit",font=('Arial',15,'bold'), command=lambda x=a: edit_1(x)).place(x=910, y=current_1,width=75,height=50)
                            print(list_faisal)
                            if(len(list_faisal)>2):
                                del list_faisal[0]
                            list_faisal.append(current_1)
                            current_1=current_1+70
                            print(list_faisal)

                        

                        

            
            
            with open('delete.txt','w') as ra:
                    ra.write('Close')
                    
                    
            def delete_3():
                import popup_delete

                print('delete faisal')

                        
                        
                        


                

                    
            clientsocket,address=s11.accept()
            clientsocket.send(bytes("Close!","utf-8"))
            thread1 = threading.Thread(target = delete_3, args = ())
            thread1.start()
            
            while True:
                with open('delete.txt','r') as f:
                        line=f.readline()
                        print(line,'line')
                if line=='Yes':
                    thread2 = threading.Thread(target = delete_2(q_1), args = (q_1,))
                    thread2.start()
                    break
                    print('delete')
                if line=='No':
                    break
                    print('Not delete')
 
            
 


        conn=sqlite3.connect('new1.db')
        c=conn.cursor()
        def create_table():
            c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT ,designation TEXT,contact TEXT,employeid TEXT)')

        def data_entry():
            t_name=e_name.get()
            t_designation=e_designation.get()
            t_contact=e_contact.get()
            t_employeid=e_employeid.get()
            
            c.execute("INSERT INTO stuffTOPlot(name,designation,contact,employeid) VALUES(?,?,?,?)",(t_name,t_designation,t_contact,t_employeid))
            conn.commit()
            c.close()
            conn.close()
        create_table()
        data_entry()
        for new1 in dict_1.keys():
            xa=dict_1[new1][0]
            xa.lower()
            xb=e_name.get()
            xb.lower()
            if xa.lower() ==xb.lower():
                import popup_name

        if(len(e_name.get())!=0 and len(e_employeid.get()) !=0) :
            t_name=e_name.get()
            t_designation=e_designation.get()
            t_contact=e_contact.get()
            t_employeid=e_employeid.get()
            #e_name.delete(0,END)
            dict_1[key_1]=[t_name,t_employeid,t_contact,t_designation]
            if(len(list_xqq)>2):
                        del list_xqq[0]
            for xqq in dict_1.keys():
                list_xqq.append(xqq)
            list_xqq.sort(reverse=True)

                        
            if (len(list_xqq)==0):
                current=200
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text='',font=('Arial',14,'bold')).place(x=1,y=c_current,width=200,height=70)
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=201,y=c_current,width=200,height=70)
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=401,y=c_current,width=200,height=70)
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=601,y=c_current,width=200,height=70)
                Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=801,y=c_current,width=200,height=70)
                
            else:    
                print(list_xqq[0])
                current=200
                for fz2 in list_xqq:
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text=dict_1[fz2][0],font=('Arial',14,'bold')).place(x=1,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][1],relief='raised',font=('Arial',14,'bold')).place(x=201,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][2],relief='raised',font=('Arial',14,'bold')).place(x=401,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text=dict_1[fz2][3],relief='raised',font=('Arial',14,'bold')).place(x=601,y=current,width=200,height=70)
                    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',14,'bold')).place(x=801,y=current,width=200,height=70)
                    current=current+70

            current_1=210
            list_faisal=[]
            unix=u'\u270E'       

            #uni=str(uni)
            #sorted(dict_1.keys(),reverse=True)
            for last_1 in list_xqq:
                a=last_1
                Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Delete",font=('Arial',15,'bold'), command=lambda x=a: delete_1(x)).place(x=815, y=current_1,width=75,height=50)
                Button(f4.scrollFrame.viewPort,bg='#4299ff', fg='white', text="Edit",font=('Arial',15,'bold'), command=lambda x=a: edit_1(x)).place(x=910, y=current_1,width=75,height=50)
                print(list_faisal)
                if(len(list_faisal)>2):
                    del list_faisal[0]
                list_faisal.append(current_1)
                current_1=current_1+70
                print(list_faisal)
            #x=Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Edit",font=('Arial', 16,'bold'), command=edit).place(x=805,y=current_1,width=20,height=45)
            #x1=Button(f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Delete",font=('Arial', 16,'bold'), command=delete_1).place(x=850,y=current_1,width=20,height=45)
            key_1=key_1+1
            print(dict_1)

            raise_frame(f4)
            e_name.delete(0,END)
            e_designation.delete(0,END)
            e_contact.delete(0,END)
            e_employeid.delete(0,END)
            current= current+50
            current_1=current_1+50

        else:
            import popup_6
    for row in range(len(dict_1)+1):
            a = row
            Label(f4.scrollFrame.viewPort, text='', width=150,height=150, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)
            
            



    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='Users',font=('Arial',18,'bold')).place(x=470,y=10)
    Label(f4.scrollFrame.viewPort,fg='black',bg='white',relief='raised',borderwidth=2, text='Name',font=('Arial',15,'bold')).place(x=1,y=150,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Employer ID',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=201,y=150,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Contact',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=401,y=150,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Designation',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=601,y=150,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='white', text='Actions',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=801,y=150,width=200,height=50)


    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text='',font=('Arial',15,'bold')).place(x=1,y=200,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=201,y=200,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=401,y=200,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=601,y=200,width=200,height=50)
    Label(f4.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=801,y=200,width=200,height=50)
    #Button(f4, text='Add New User',font=('Arial',10), command=lambda:raise_frame(f7)).place(x=15,y=127,width=100,height=10)
    l=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Add New User",font=('Arial', 16,'bold'), command=lambda:raise_frame(f_addnewuser)).place(x=12,y=70,width=200,height=45)
    l_1=Button(master=f4.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_new).place(x=805,y=70,width=150,height=45)

    def back_f4():
        Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Add User",font=('Arial', 16,'bold'), command=add_user).place(x=605,y=347,width=150,height=45)
        e_name.delete(0,END)
        e_designation.delete(0,END)
        e_contact.delete(0,END)
        e_employeid.delete(0,END)

            
        raise_frame(f4)
###########################################RESULT SCREEN###########################################################
    for row in range(1):
            a = row
            Label(f_result_data.scrollFrame.viewPort, text='', width=150,height=150, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)
    f_result_data.scrollFrame.pack(side="top", fill="both", expand=True)

    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='Users',font=('Arial',18,'bold')).place(x=470,y=10)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='white',relief='raised',borderwidth=2, text='Name',font=('Arial',15,'bold')).place(x=1,y=150,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='white', text='Employer ID',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=201,y=150,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='white', text='Contact',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=401,y=150,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='white', text='Designation',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=601,y=150,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='white', text='Actions',borderwidth=2,relief='raised',font=('Arial',15,'bold')).place(x=801,y=150,width=200,height=50)


    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff',relief='raised',borderwidth=2, text='',font=('Arial',15,'bold')).place(x=1,y=200,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=201,y=200,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=401,y=200,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=601,y=200,width=200,height=50)
    Label(f_result_data.scrollFrame.viewPort,fg='black',bg='#f7f7ff', text='',relief='raised',font=('Arial',15,'bold')).place(x=801,y=200,width=200,height=50)
    
    l_1=Button(master=f_result_data.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command='').place(x=805,y=70,width=150,height=45)


########################################### USER SCREEN ##########################################################


    imagePath_userscreen=PhotoImage(file="userscreen.png")
    widgetf_userscreen=Label(f_addnewuser,image=imagePath_userscreen)
    widgetf_userscreen.place(x=0,y=0)

    Label(f_addnewuser,fg='black',bg='white', text='Add User',font=('Arial',18,'bold')).place(x=470,y=17)


    e_name = Entry(f_addnewuser)
    e_name.config(font=('arial',21),bg='white',takefocus='off',relief="groove",borderwidth=0,justify=CENTER)
    e_name.place(x=471,y=103,height=41,width=493)
    e_name.bind("<FocusIn>",call_name)

    Label(f_addnewuser,fg='black',bg='white', text='Enter Name',font=('Arial',15,'bold')).place(x=70,y=120)


    e_designation = Entry(f_addnewuser)
    e_designation.config(font=('arial',21),bg='white',takefocus='off',relief="groove",borderwidth=0,justify=CENTER)
    e_designation.place(x=471,y=268,height=41,width=492)
    e_designation.bind("<FocusIn>",call_designation)

    Label(f_addnewuser,fg='black',bg='white', text='Enter Employee ID',font=('Arial',15,'bold')).place(x=70,y=174)
    
    e_contact = Entry(f_addnewuser)
    e_contact.config(font=('arial',21),bg='white',takefocus='off',relief="groove",borderwidth=0,justify=CENTER)
    e_contact.place(x=471,y=215,height=41,width=493)
    e_contact.bind("<FocusIn>",call_contact)

    Label(f_addnewuser,fg='black',bg='white', text='Enter Contact',font=('Arial',15,'bold')).place(x=70,y=228)

    e_employeid = Entry(f_addnewuser)
    e_employeid.config(font=('arial',21),bg='white',takefocus='off',relief="groove",borderwidth=0,justify=CENTER)
    e_employeid.place(x=471,y=161,height=41,width=492)
    e_employeid.bind("<FocusIn>",call_employeid)

    Label(f_addnewuser,fg='black',bg='white', text='Enter Designation',font=('Arial',15,'bold')).place(x=70,y=280)



    Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_f4).place(x=805,y=347,width=150,height=45)
    Button(master=f_addnewuser,bg='#4299ff',fg='white', text="Add User",font=('Arial', 16,'bold'), command=add_user).place(x=605,y=347,width=150,height=45)
    




        





####    button1 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="Start Test",font=('Arial', 10,'bold'), command=registration).place(x=150,y=123)
####    button2 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="Settings",font=('Arial', 10,'bold'), command=registration).place(x=150,y=250)
####    button3 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="User",font=('Arial', 10,'bold'), command=registration).place(x=150,y=377)
####    button4 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="Results",font=('Arial', 10,'bold'), command=registration).place(x=420,y=90)
####    button5 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="Damper Setting",font=('Arial', 10,'bold'), command=registration).place(x=420,y=220)
####    button6 = Button(master=f1,width=43,height=5,bg='white',fg='black', text="About",font=('Arial', 10,'bold'), command=registration).place(x=420,y=350)
####    imagePath_main=PhotoImage(file="main_screen.png")
####    widgetmain=Label(f1,image=imagePath_main)
####    widgetmain.place(x=0,y=0)
    label_welcome="Welcome to " + read_file
    label_device = Label(f1, text=label_welcome,bg='#f7f7ff',fg='#231f1e', font=('Arial', 18,'bold'))
    label_device.place(x=400,y=20)



    imagePath_start=PhotoImage(file="start.png")
    widgetstart=Button(f1,borderwidth=1,image=imagePath_start,command=change_start_screen)
    widgetstart.place(x=50,y=90)

    #imagePath_start_test=PhotoImage(file="buttons_start_test.png")
####    widgetstart=Button(f1,relief="groove",borderwidth=0,text="Start Test",font=('Arial',25,'bold'),command=change_start_screen)
####    widgetstart.place(x=85,y=110,width=200,height=90)
    
    imagePath_start_test_1=PhotoImage(file="setting.png")
    widgetstart_1=Button(f1,borderwidth=1,image=imagePath_start_test_1,command=settings)
    widgetstart_1.place(x=50,y=220)
    imagePath_start_test_2=PhotoImage(file="user.png")
    widgetstart_2=Button(f1,image=imagePath_start_test_2,command=add_user4)
    widgetstart_2.place(x=50,y=350)
    imagePath_results=PhotoImage(file="Result.png")
    widgetstart_results=Button(f1,image=imagePath_results,command=lambda:raise_frame(f_result_data))
    widgetstart_results.place(x=340,y=90)
    imagePath_damper=PhotoImage(file="about.png")
    widgetstart_damper=Button(f1,borderwidth=1,image=imagePath_damper,command=change_about)
    widgetstart_damper.place(x=340,y=220)
    imagePath_about=PhotoImage(file="damper.png")
    widgetstart_about=Button(f1,image=imagePath_about)
    widgetstart_about.place(x=340,y=350)
    label_start=Button(master=f1,text="Start Test",font=('Arial',22,'bold'),fg='black',relief='flat',borderwidth=0,command=change_start_screen).place(x=125,y=114)
    label_setting=Button(master=f1,text="Settings",font=('Arial',22,'bold'),fg='black',relief='raised',borderwidth=0,command=settings).place(x=125,y=244)
    label_user=Button(master=f1,text="User",font=('Arial',22,'bold'),fg='black',relief='raised',borderwidth=0,command=add_user4).place(x=125,y=374)
    label_results=Button(master=f1,text="Results",font=('Arial',22,'bold'),fg='black',relief='raised',borderwidth=0).place(x=420,y=114)
    label_about=Button(master=f1,text="About",font=('Arial',22,'bold'),fg='black',relief='raised',borderwidth=0,command=change_about).place(x=420,y=244)
    label_damper=Button(master=f1,text="Damper",font=('Arial',22,'bold'),fg='black',relief='raised',borderwidth=0).place(x=420,y=374)
    Label(master=f5,bg='#00afef',fg='white', text="C",font=('Arial', 16,'bold')).place(x=935,y=109)
    e4 = Entry(f5)
    e4.config(font=('arial',21),takefocus='off',justify=CENTER,relief="groove",borderwidth=0)
    e4.place(x=687,y=103,height=41,width=238)
    e4.bind("<FocusIn>",call_1)
##
    e5 = Entry(f5)##hours entry widget
    e5.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='gray')
    e5.place(x=687,y=161,height=41,width=110)
    e5.insert(0,"Hrs")
    e5.bind("<FocusIn>",call_2)
##
    e6 = Entry(f5) ## minutes entry widget
    e6.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='gray')
    e6.place(x=815,y=161,height=41,width=110)
    e6.insert(0,"Min")
    e6.bind("<FocusIn>",call_3)
    variable1 = StringVar(f5)
    variable1.set(OptionList1[3])
    #s.configure("TMenubutton",background='red')

    opt1 = OptionMenu(f5, variable1, *OptionList1)
    opt1.config(bg='white',font=('Arial', 18),relief=GROOVE,borderwidth=0,activeforeground = "#00afef",activebackground = "white",highlightbackground='white')
    opt1['menu'].config(bg='white',font=('Arial',18),activeforeground = "white",activebackground = "#00afef")
    opt1.place(x=687,y=217,width=270,height=38)

    imagePath_drop=PhotoImage(file="drop.png")
    widgetdrop=Label(f5,borderwidth=0,image=imagePath_drop)
    widgetdrop.place(x=925,y=214)

    variable = StringVar(f5)
    variable.set(OptionList[5])
    #s.configure("TMenubutton",background='red')

    opt = OptionMenu(f5, variable, *OptionList)
    opt.config(bg='white',font=('Arial', 18),relief=GROOVE,borderwidth=0,activeforeground = "#00afef",activebackground = "white",highlightbackground='white')
    opt['menu'].config(bg='white',font=('Arial',18),activeforeground = "white",activebackground = "#00afef")
    opt.place(x=687,y=269,width=270,height=38)

    imagePath_drop1=PhotoImage(file="drop.png")
    widgetdrop1=Label(f5,borderwidth=0,image=imagePath_drop1)
    widgetdrop1.place(x=925,y=267)


    variable2 = StringVar(f5)
    variable2.set(OptionList2[0])
    #s.configure("TMenubutton",background='red')

    opt2 = OptionMenu(f5, variable2, *OptionList2)
    opt2.config(bg='white',font=('Arial', 18),relief=GROOVE,borderwidth=0,activeforeground = "#00afef",activebackground = "white",highlightbackground='white')
    opt2['menu'].config(bg='white',font=('Arial',18),activeforeground = "white",activebackground = "#00afef")
    opt2.place(x=687,y=324,width=270,height=38)

    imagePath_drop2=PhotoImage(file="drop.png")
    widgetdrop2=Label(f5,borderwidth=0,image=imagePath_drop2)
    widgetdrop2.place(x=925,y=322)

    label_set_parameters = Label(f5, text="Set Parameters",bg='white',fg='#231f1e', font=('Arial', 17,'bold'))
    label_set_parameters.place(x=400,y=20)
    label_set_parameters = Label(f5, text="Set Temperature",bg='white',fg='#231f1e', font=('Arial', 15,'bold'))
    label_set_parameters.place(x=95,y=120)
    label_set_parameters = Label(f5, text="Set Timer/Infinity Mode",bg='white',fg='#231f1e', font=('Arial', 15,'bold'))
    label_set_parameters.place(x=95,y=175)
    label_set_parameters = Label(f5, text="Level",bg='white',fg='#231f1e', font=('Arial', 15,'bold'))
    label_set_parameters.place(x=95,y=230)
    label_set_parameters = Label(f5, text="Fan Speed",bg='white',fg='#231f1e', font=('Arial', 15,'bold'))
    label_set_parameters.place(x=95,y=285)
    label_set_parameters = Label(f5, text="Set User",bg='white',fg='#231f1e', font=('Arial', 15,'bold'))
    label_set_parameters.place(x=95,y=335)


#######################################################SETTINGS#######################################################################################
    def back_setting():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8"))
        raise_frame(f1)


    def instrument_setting():
        #time.sleep(2)
        raise_frame(f_ins_setting)
        def read_every_second_faisal_12():
            q_1_s_faisal_1=0

            def read_every_second_faisal_1():
                q_1_s_faisal_1=0
                label_temp = Label(root, text='80 C',bg='#efeeef',fg='#231f1e', font=('Arial', 18,'bold'))
                label_temp.place(x=470,y=52)
                print('current toggle value is {}.'.format(bool(vartime.get())))
                print(vartime.get())
                #Label(master=f_ins_setting,width=2,height=0,bg='white',fg='black', text="C",font=('Arial', 16,'bold')).place(x=270,y=390)
                if vartime.get()==True:
                    print('tr')
                    #Label(master=f_ins_setting,width=2,height=0,bg='white',fg='black', text="C",font=('Arial', 16,'bold')).place(x=270,y=390)

                if vartime.get()==False:
                    #Label(master=f_ins_setting,width=2,height=0,bg='white',fg='black', text="F",font=('Arial', 16,'bold')).place(x=270,y=390)
                    print('fal')
            
                    


                q_1_s_faisal_1+=1
                    
                    

                if q_1_s_faisal_1>2000:


            #        graph1.draw_axes()
                    q_1_s_faisal_1=0
                root.after(2000, read_every_second_faisal_1)
            
            read_every_second_faisal_1()
    imagePath_back_setting=PhotoImage(file="screens_ins_setting.png")
    widget_back_setting=Label(f_setting,borderwidth=1,image=imagePath_back_setting)
    widget_back_setting.place(x=0,y=0)


    imagePath_setting=PhotoImage(file="setting.png")
    widgetsetting=Button(f_setting,borderwidth=1,image=imagePath_setting,command=lambda:raise_frame(f_servicemode))
    widgetsetting.place(x=400,y=100)

    imagePath_setting_1=PhotoImage(file="setting.png")
    widgetsetting_1=Button(f_setting,borderwidth=1,image=imagePath_setting_1,command=lambda:raise_frame(f_servicemode))
    widgetsetting_1.place(x=400,y=240)

    Button(master=f_setting,borderwidth='0',relief='flat',fg='black', text="Instrument",font=('Arial', 18,'bold'),command=lambda:raise_frame(f_ins_setting)).place(x=468,y=126)
    Button(master=f_setting,borderwidth='0',relief='flat',fg='black', text="Service",font=('Arial', 18,'bold'),command=lambda:raise_frame(f_servicemode)).place(x=468,y=268)

    
    button1 = Button(master=f_setting,width=10,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_setting).place(x=450,y=385)
    Label(master=f_setting,width=10,height=1,bg='white',fg='black', text="Settings",font=('Arial', 18,'bold')).place(x=450,y=17)



    button1 = Button(master=f5,width=10,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back).place(x=780,y=385)
    button2 = Button(master=f5,width=22,height=2,bg='#f7f7f7',fg='green', text="Start To Run A Test",activeforeground = "#75f07a",activebackground = "black",font=('Arial', 16,'bold'),command=click).place(x=670,y=21)
#######################################################INSTRUMENT SETTING #############################################################################

    def save_time():
       x=vartime.get()
       pass
       if(x==True):
           Label(master=f5,bg='#00afef',fg='white', text="C",font=('Arial', 16,'bold')).place(x=935,y=109)
       if(x==False):
           Label(master=f5,bg='#00afef',fg='white', text="F",font=('Arial', 16,'bold')).place(x=935,y=109)
    
           

    imagePath_ins_setting=PhotoImage(file="screens_ins_setting.png")
    widget_ins_setting=Label(f_ins_setting,borderwidth=1,image=imagePath_ins_setting)
    widget_ins_setting.place(x=0,y=0)
    
    button1 = Button(master=f_ins_setting,width=10,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=lambda:raise_frame(f_setting)).place(x=830,y=30)
    Label(master=f_ins_setting,width=19,height=1,bg='white',fg='black', text="Instrument Settings",font=('Arial', 18,'bold')).place(x=70,y=19)
    Label(master=f_ins_setting,width=19,height=0,bg='white',fg='black', text="Company Detail",font=('Arial', 14,'bold')).place(x=70,y=69)
    
    Label(master=f_ins_setting,width=19,height=1,bg='white',fg='black', text="Company Name",font=('Arial', 12)).place(x=90,y=119)
    e_com_name = Entry(f_ins_setting)
    e_com_name.config(font=('arial',21),takefocus='off',borderwidth='2')
    e_com_name.place(x=120,y=150,height=35,width=320)
    Label(master=f_ins_setting,width=19,height=1,bg='white',fg='black', text="Telephone Number",font=('Arial', 12)).place(x=470,y=119)
    e_tele_no = Entry(f_ins_setting)
    e_tele_no.config(font=('arial',21),takefocus='off',borderwidth='2')
    e_tele_no.place(x=490,y=150,height=35,width=320)
    #e7.bind("<FocusIn>",call_4)
    Button(master=f_ins_setting,width=10,height=1,bg='#4299ff',fg='white', text="Save",font=('Arial', 14,'bold'), command='').place(x=830,y=145)
    Button(master=f_ins_setting,width=10,height=1,bg='#4299ff',fg='white', text="Save",font=('Arial', 14,'bold'), command='').place(x=830,y=250)
    Button(master=f_ins_setting,width=10,height=1,bg='#4299ff',fg='white', text="Save",font=('Arial', 14,'bold'), command=save_time).place(x=830,y=370)
    
    Label(master=f_ins_setting,width=19,height=0,bg='white',fg='black', text="Time",font=('Arial', 15,'bold')).place(x=50,y=209)
    toggle = Toggle(f_ins_setting)
    toggle.configure(bg='white')
    toggle.place(x=120,y=250,height=75)
 

    Label(master=f_ins_setting,width=19,height=0,bg='white',fg='black', text="Temperature Setting",font=('Arial', 15,'bold')).place(x=90,y=329)
    vartime=BooleanVar()
    toggle1 = Toggle(f_ins_setting,variable=vartime)
    toggle1.configure(bg='white')
    toggle1.place(x=120,y=370,height=75)  
    

##################################################Service mode###############################################################################################
    
    def call_password(event):
        global l_entry,l_e4,l_entry_password
        print('entry')
        e3.delete(0,END)
        e3.config(font=('arial',21),takefocus='off',borderwidth='2',show='*')
        e8.config(font=('arial',21),takefocus='off',borderwidth='2',show='*')
        f_addnewuser.focus()
        if l_entry_password[-1] =='None':
            e3.insert(0,'')
        else:
            e3.delete(0,END)
            #e3.insert(0,l_entry_call_designation[-1])
            l_entry.clear()
        if(len(l_e4)>2):
            del l_e4[0]
        l_e4.append('entry_password')
        raise_frame(f3)
    def checking_password():
        global l_entry,l_e4,l_entry_password
        unique=l_entry_password[-1]
        x=unique.lower()
        if x=="faisal":
            raise_frame(f_servicemode1)
            e_password.delete(0,END)
            l_entry_password.clear()
            l_entry_password.append('a')
            print("access granted")
        else:
            import popup_password

    Label(master=f_servicemode,width=19,height=1,bg='#f7f7ff',fg='black', text="Service Mode",font=('Arial', 18,'bold')).place(x=380,y=19)

    e_password = Entry(f_servicemode)
    e_password.config(font=('arial',21),takefocus='off',borderwidth='2',show='*')
    e_password.place(x=380,y=140,height=35,width=320)
    e_password.bind("<FocusIn>",call_password)
    Button(master=f_servicemode,width=26,height=2,bg='#4299ff',fg='white', text="Enter Password",font=('Arial', 14,'bold'), command=checking_password).place(x=380,y=200)
    Button(master=f_servicemode,width=26,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 14,'bold'), command=lambda:raise_frame(f_setting)).place(x=380,y=320)


###################################################################Service Mode Inside ##########################################################################
    for row in range(1):
                a = row
                Label(f_servicemode1.scrollFrame.viewPort, text='', width=150,height=43, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)

    f_servicemode1.scrollFrame.pack(side="top", fill="both", expand=True)
    screen_service=PhotoImage(file="screens_service_mode.png")
    screen_service_1=Label(master=f_servicemode1.scrollFrame.viewPort,image=screen_service)
    screen_service_1.place(x=0,y=0)

    e_server = Entry(f_servicemode1.scrollFrame.viewPort) ## minutes entry widget
    e_server.config(font=('arial',21),fg='gray',takefocus='off',relief="groove",borderwidth=2,justify=CENTER)
    e_server.place(x=200,y=220,height=41,width=611)

    e_server.insert(0,"Enter Admin Server Address")
    #e_server.bind("<FocusIn>",call_3)

    varlang=['                                                                              ','English','Spanish','Arabic','Urdu']
    lang = StringVar(f_servicemode1.scrollFrame.viewPort)
    lang.set(varlang[1])
        #s.configure("TMenubutton",background='red')

    opt2 = OptionMenu(f_servicemode1.scrollFrame.viewPort, lang, *varlang)
    opt2.config(bg='white',font=('Arial', 18),relief=GROOVE,borderwidth=1,activeforeground = "#00afef",activebackground = "white",highlightbackground='white')
    opt2['menu'].config(bg='white',font=('Arial',18),activeforeground = "white",activebackground = "#00afef")
    opt2.place(x=200,y=110,width=611,height=38)

    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Service Mode",font=('Arial', 18,'bold')).place(x=70,y=30,width=161,height=21)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Language",font=('Arial', 14,'bold')).place(x=107,y=70,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Admin Panel",font=('Arial', 14,'bold')).place(x=120,y=170,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Factory Reset",font=('Arial', 14,'bold')).place(x=120,y=280,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Performance",font=('Arial', 14,'bold')).place(x=120,y=420,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Total Performed Test",font=('Arial', 14,'bold')).place(x=120,y=460,width=201,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Total Test Perform",font=('Arial', 12)).place(x=120,y=490,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Total Test Aborted",font=('Arial', 12)).place(x=120,y=530,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="Total Test Printed",font=('Arial', 12)).place(x=120,y=570,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="80",font=('Arial', 12)).place(x=350,y=490,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="20",font=('Arial', 12)).place(x=350,y=530,width=131,height=31)
    Label(master=f_servicemode1.scrollFrame.viewPort,bg='white',fg='black', text="3",font=('Arial', 12)).place(x=350,y=570,width=131,height=31)


    #Button(master=f_servicemode1,bg='#4299ff',fg='white', text="EDIT",font=('Arial',10,'bold'), command='').place(x=900, y=current_1,width=70,height=50)

    Button(master=f_servicemode1.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Save",font=('Arial', 16,'bold'), command='').place(x=860,y=110,width=100,height=41)
    Button(master=f_servicemode1.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Save",font=('Arial', 16,'bold'), command='').place(x=860,y=220,width=100,height=41)
    Button(master=f_servicemode1.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Reset Factory Setting",font=('Arial', 16,'bold'), command='').place(x=160,y=320,width=230,height=45)
    Button(master=f_servicemode1.scrollFrame.viewPort,width=10,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=lambda: raise_frame(f_setting)).place(x=830,y=570)
###################################################################About Us ###########################################################################################        
    def back_about():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8"))
        raise_frame(f1)

    for row in range(1):
                a = row
                Label(f_about.scrollFrame.viewPort, text='', width=150,height=43, borderwidth="0",bg='#f7f7ff').grid(row=row, column=0)


    screen_about=PhotoImage(file="screens_service_mode.png")
    screen_about_1=Label(master=f_about.scrollFrame.viewPort,image=screen_about)
    screen_about_1.place(x=0,y=0)
    Label(master=f_about.scrollFrame.viewPort,bg='white',fg='black', text="About us",font=('Arial', 25,'bold')).place(x=420,y=50)
    e_server = Text(f_about.scrollFrame.viewPort) 
    e_server.config(font=('arial',21),fg='black',relief="groove",borderwidth=2)
    quote = """Lorem Ipsum is simply dummy text of the printing and typesetting
industry. Lorem Ipsum has been the industry's standard dummy text
ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem IpsumContrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance."""
    e_server.insert(END, quote)
    e_server.place(x=70,y=120,height=481,width=901)
    e_server.config(font=('arial',21),fg='black',relief="groove",borderwidth=2,state=DISABLED)





    Button(master=f_about.scrollFrame.viewPort,width=10,height=1,bg='#4299ff',fg='white', text="Back",font=('Arial', 16,'bold'), command=back_about).place(x=830,y=50)






    key=0
    def ddash():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '_')
        key=key+1
    def  show():
            global key
            mq=e2.get()
            mq_1=len(mq)
            cursor_position_1=e2.index(INSERT)
            print(cursor_position_1)
            #print(l_type)
            print(key)
            e2.insert(cursor_position_1, '0')
            key=key+1
            




    def  show1():
                global key
                mq=e2.get()
                mq_1=len(mq)
                cursor_position_1=e2.index(INSERT)
                print(cursor_position_1)
                #print(l_type)
                print(key)
                e2.insert(cursor_position_1, '1')
                key = key + 1




    def show2():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '2')
        key=key+1
    def show3():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '3')
        key=key+1

    def show4():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '4')
        key=key+1

    def show5():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '5')
        key=key+1

    def show6():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '6')
        key=key+1

    def show7():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '7')
        key=key+1

    def show8():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '8')
        key=key+1

    def show9():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '9')
        key=key+1
    def cursor_right():
        cursor_position_1=e2.index(INSERT)
        e2.icursor(cursor_position_1+1)
        
    def cursor_left():
        cursor_position_1=e2.index(INSERT)
        e2.icursor(cursor_position_1-1)
        
    def clear():
        global key
        print (key)
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        #e2.insert(cursor_position_1, '5')
        #mm=e2.index()
        #print(mm)
        e2.delete(cursor_position_1-1,cursor_position_1)
        key=key-1
        if (key<=0):
            key=0
    def enter():
        global l_entry_e4,l_entry_e5,l_entry_e6,l_e4,l_e5
        #e1.delete(0,END)
        y=e2.get()
        y=str(y)
        #e1.insert(0,y)
        
        l_entry.append(y)
        
        #raise_frame(f1)
        if l_e4[-1]=="e4":
            e4.delete(0,END)
            y=e2.get()
            y=str(y)
            if len(e2.get())!=0:
                co_1=float(y)
            else:
                co_1=26
            l_entry_e4.append(y)
            print(l_entry_e4)
            e4.insert(0,y)
            if(co_1>300 or co_1<25):
                import popup_4
                
            else:
                raise_frame(f5)

        elif l_e4[-1]=="e5":
            e5.delete(0,END)
            y=e2.get()
            y=str(y)
            l_entry_e5.append(y)
            print(l_entry_e4)
            e5.insert(0,y)
            raise_frame(f5)

        elif l_e4[-1]=="e6":
            e6.delete(0,END)
            y=e2.get()
            y=str(y)
            l_entry_e6.append(y)
            print(l_entry_e4)
            e6.insert(0,y)
            raise_frame(f5)
        elif l_e4[-1]=="call_contact":
            e_contact.delete(0,END)
            y=e2.get()
            y=str(y)
            l_entry_call_contact.append(y)
            print(l_entry_call_contact)
            e_contact.insert(0,y)
            raise_frame(f_addnewuser)


    def point_1():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, '.')
        key=key+1
        
    def close():
        e1.delete(0,END)
        raise_frame(f1)
    def space():
        global key
        mq=e2.get()
        mq_1=len(mq)
        cursor_position_1=e2.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e2.insert(cursor_position_1, ' ')
        key=key+1
    def change():
        global key
        cursor_position=e2.index(INSERT)
        e3.delete(0,END)
        f_e_3=e2.get()
        f_e_3=str(f_e_3)
        e3.insert(0,f_e_3)
        e3.icursor(cursor_position)
    ##    l_type.append(key)
    ##    print(l_type)

        raise_frame(f3)
        
    def ddash_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '_')
        key=key+1
    def  show_f6():
        
            global key
            mq=e8.get()
            mq_1=len(mq)
            cursor_position_1=e8.index(INSERT)
            print(cursor_position_1)
            #print(l_type)
            print(key)
            e8.insert(cursor_position_1, '0')
            key=key+1
            




    def  show1_f6():
                global key
                mq=e8.get()
                mq_1=len(mq)
                cursor_position_1=e8.index(INSERT)
                print(cursor_position_1)
                #print(l_type)
                print(key)
                e8.insert(cursor_position_1, '1')
                key = key + 1




    def show2_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '2')
        key=key+1
    def show3_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '3')
        key=key+1

    def show4_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '4')
        key=key+1

    def show5_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '5')
        key=key+1

    def show6_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '6')
        key=key+1

    def show7_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '7')
        key=key+1

    def show8_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '8')
        key=key+1

    def show9_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '9')
        key=key+1
    def clear_f6():
        global key
        print (key)
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        #e2.insert(cursor_position_1, '5')
        #mm=e2.index()
        #print(mm)
        e8.delete(cursor_position_1-1,cursor_position_1)
        key=key-1
        if (key<=0):
            key=0
    def enter_f6():
        global l_entry_e4,l_entry_e5,l_entry_e6,l_e4,l_e5,l_entry_call_name,l_entry_call_designation,l_entry_call_contact,l_entry_call_employeid
        #e1.delete(0,END)
        y=e8.get()
        y=str(y)
        #e1.insert(0,y)
        
        l_entry.append(y)
        
        #raise_frame(f1)
        if l_e4[-1]=="e4":
            e4.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_e4.append(y)
            print(l_entry_e4)
            e4.insert(0,y)
            raise_frame(f5)

        elif l_e4[-1]=="e5":
            e5.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_e5.append(y)
            print(l_entry_e4)
            e5.insert(0,y)
            raise_frame(f5)
        elif l_e4[-1]=="e6":
            e6.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_e6.append(y)
            print(l_entry_e4)
            e6.insert(0,y)
            raise_frame(f5)
        elif l_e4[-1]=="e7":
            e7.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_e7.append(y)
            print(l_entry_e7)
            e7.insert(0,y)
            raise_frame(f5)
        elif l_e4[-1]=="call_name":
            e_name.delete(0,END)
            y=e8.get()
            y=str(y)
            if(len(l_entry_call_name)>2):
                del l_entry_call_name[0]
            print(l_entry_call_name)
            l_entry_call_name.append(y)
            print(l_entry_call_name)
            e_name.insert(0,y)
            
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="call_designation":
            e_designation.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_call_designation.append(y)
            print(l_entry_call_designation)
            e_designation.insert(0,y)
            raise_frame(f_addnewuser)

        elif l_e4[-1]=="call_contact":
            e_contact.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_call_contact.append(y)
            print(l_entry_call_contact)
            e_contact.insert(0,y)
            raise_frame(f_addnewuser)

        elif l_e4[-1]=="call_employeid":
            e_employeid.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_call_employeid.append(y)
            print(l_entry_call_employeid)
            e_employeid.insert(0,y)
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="entry_password":
            e_password.delete(0,END)
            y=e8.get()
            y=str(y)
            l_entry_password.append(y)
            print(l_entry_password)
            e_password.insert(0,y)
            e8.config(font=('arial',21),takefocus='off',borderwidth='2',show='')
            e3.config(font=('arial',21),takefocus='off',borderwidth='2',show='')
            raise_frame(f_servicemode)
            
            
            

    def point_1_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, '.')
        key=key+1
        
    def close_f6():
        e8.delete(0,END)
        raise_frame(f1)
    def space_f6():
        global key
        mq=e8.get()
        mq_1=len(mq)
        cursor_position_1=e8.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e8.insert(cursor_position_1, ' ')
        key=key+1
    def change_f6():
        global key
        cursor_position=e8.index(INSERT)
        e3.delete(0,END)
        f_e_3=e8.get()
        f_e_3=str(f_e_3)
        e3.insert(0,f_e_3)
        e3.icursor(cursor_position)


        raise_frame(f3)
    def ddash_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '_')
        key=key+1
    def  show_f8():
        
            global key
            mq=e9.get()
            mq_1=len(mq)
            cursor_position_1=e9.index(INSERT)
            print(cursor_position_1)
            #print(l_type)
            print(key)
            e9.insert(cursor_position_1, '0')
            key=key+1
            




    def  show1_f8():
                global key
                mq=e9.get()
                mq_1=len(mq)
                cursor_position_1=e9.index(INSERT)
                print(cursor_position_1)
                #print(l_type)
                print(key)
                e9.insert(cursor_position_1, '1')
                key = key + 1




    def show2_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '2')
        key=key+1
    def show3_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '3')
        key=key+1

    def show4_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '4')
        key=key+1

    def show5_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '5')
        key=key+1

    def show6_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '6')
        key=key+1

    def show7_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '7')
        key=key+1

    def show8_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '8')
        key=key+1

    def show9_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '9')
        key=key+1
    def clear_f8():
        global key
        print (key)
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        #e2.insert(cursor_position_1, '5')
        #mm=e2.index()
        #print(mm)
        e9.delete(cursor_position_1-1,cursor_position_1)
        key=key-1
        if (key<=0):
            key=0
    def enter_f8():
        ###########################################################################enter entry9##################################################
        global l_entry_e4,l_entry_e5,l_entry_e6,l_e4,l_e5
        #e1.delete(0,END)
        y=e9.get()
        y=str(y)
        #e1.insert(0,y)
        
        l_entry.append(y)
        
        #raise_frame(f1)
        if l_e4[-1]=="e4":
            e4.delete(0,END)
            
            y=e9.get()
            y=str(y)
            l_entry_e4.append(y)
            print(l_entry_e4)
            e4.insert(0,y)
            raise_frame(f5)

        elif l_e4[-1]=="e5":




            ##############
            e5.delete(0,END)
            #e6.delete(0,END)
            #e6.insert(0,"Min")
            y=e9.get()
            y=str(y)
            if len(e9.get())!=0:
                co_2=float(y)
            elif len(e9.get())==0:
                co_2=1
                e5.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='gray')
                e5.delete(0,END)
                e5.insert(0,"Hrs")
                e6.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='gray')
                e6.delete(0,END)
                e6.insert(0,"Min")
                l_entry_e6.append('')
                
            else:
                co_2=1
            l_entry_e5.append(y)
            print(l_entry_e5)
            e5.insert(0,y)
            if(co_2>99 or co_2<0):
                import popup_7
            else:
                raise_frame(f5)

                
        elif l_e4[-1]=="e6":

                        ##############
            e6.delete(0,END)
            y=e9.get()
            y=str(y)
            if len(e9.get())!=0:
                co_3=float(y)
            elif len(e9.get())==0:
                co_3=1
                e6.config(font=('arial',21),takefocus='off',relief="groove",borderwidth=0,justify=CENTER,fg='gray')
                e6.delete(0,END)
                e6.insert(0,"Min")
            else:
                co_3=1
            l_entry_e6.append(y)
            print(l_entry_e6)
            e6.insert(0,y)
            if(co_3>59 or co_3<0):
                import popup_8
            else:
                raise_frame(f5)
        elif l_e4[-1]=="e7":
            e7.delete(0,END)
            y=e9.get()
            y=str(y)
            l_entry_e7.append(y)
            print(l_entry_e7)
            e7.insert(0,y)
            raise_frame(f5)
            

    def point_1_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, '.')
        key=key+1
        
    def close_f8():
        e9.delete(0,END)
        raise_frame(f1)
    def space_f8():
        global key
        mq=e9.get()
        mq_1=len(mq)
        cursor_position_1=e9.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        e9.insert(cursor_position_1, ' ')
        key=key+1
    def cursor_right_f8():
        cursor_position_1=e9.index(INSERT)
        e9.icursor(cursor_position_1+1)
        
    def cursor_left_f8():
        cursor_position_1=e9.index(INSERT)
        e9.icursor(cursor_position_1-1)

    def infinte():
        global l_entry_e4,l_entry_e5,l_entry_e6,l_e4,l_e5
        
        if l_e4[-1]=="e5" or l_e4[-1]=="e6":
            e5.delete(0,END)
            print(l_entry_e4)
            e5.insert(0,'infinity')
            e6.delete(0,END)
            l_entry_e5.append('infinity')
            l_entry_e6.append('infinity')
            print(l_entry_e5)
            e6.insert(0,'infinity')
            raise_frame(f5)
            

            

    def limitSizeDay(*args):
        global l_e4
        value = dayValue.get()

        ha_1=e2.get()
        if len(e2.get()) !=0:
            ha_1=float(ha_1)
        else:
            ha_1=0

        if (ha_1<100 and ha_1>0):
            if len(value) > 4: dayValue.set(value[:4])
        else:    
            if len(value) > 5: dayValue.set(value[:5])


    def limitSizeDayc(*args):
        global l_e4
        valuec = dayValuec.get()
        if(l_e4[-1]=="call_contact"):
                   
            ha_2c=ec.get()
           
            ha_2c=str(ha_2c)

            if len(valuec) > 13: dayValuec.set(valuec[:13])


    dayValuec = StringVar()
    dayValuec.trace('w', limitSizeDayc)
    dayValue = StringVar()
    dayValue.trace('w', limitSizeDay)
    imagePath_numeric=PhotoImage(file="numeric1.png")
    widgetnumeric=Label(f2,image=imagePath_numeric)
    widgetnumeric.place(x=0,y=0)
    e2 = Entry(f2) #############################################################################entry2#########################################################
    
    e2.config(justify=LEFT,font=('arial',21),takefocus='on',textvariable=dayValue)
    e2.place(x=44,y=13,height=84,width=940)
    imagePath_numericc=PhotoImage(file="numeric1.png")
    widgetnumericc=Label(fcontact,image=imagePath_numericc)
    widgetnumericc.place(x=0,y=0)

    ec = Entry(fcontact) #############################################################################entry2#########################################################
    
    ec.config(justify=LEFT,font=('arial',21),takefocus='on',textvariable=dayValuec)
    ec.place(x=44,y=13,height=84,width=940)
    
    


    imagePath_numeric_f6=PhotoImage(file="numeric1.png")
    widgetnumeric_f6=Label(f6,image=imagePath_numeric_f6)
    widgetnumeric_f6.place(x=0,y=0)

    def limitSizeDay2(*args):
        global l_e4
        value = dayValue2.get()
        if(l_e4[-1]=="call_designation" or l_e4[-1]=="call_name" or l_e4[-1]=="call_employeid"):
            ha_2=e8.get()
            ha_2=str(ha_2)

            if len(value) > 14: dayValue2.set(value[:14])



    dayValue2 = StringVar()
    dayValue2.trace('w', limitSizeDay2)

    e8 = Entry(f6)
    e8.config(justify=LEFT,font=('arial',21),takefocus='on',textvariable=dayValue2)
    e8.place(x=44,y=13,height=84,width=940)

    imagePath_numeric_f8=PhotoImage(file="numeric1.png")
    widgetnumeric_f8=Label(f8,image=imagePath_numeric_f8)
    widgetnumeric_f8.place(x=0,y=0)
    def limitSizeDay4(*args):
        global l_e4
        value4 = dayValue4.get()

        if(l_e4[-1]=="e5" or l_e4[-1]=="e6"):
                   
            ha_3=e9.get()
            if len(e9.get()) !=0:
                ha_3=float(ha_3)
            else:
                ha_3=0

            if (ha_3>0):
                if len(value4) > 3: dayValue4.set(value4[:3])


    dayValue4 = StringVar()
    dayValue4.trace('w', limitSizeDay4)
    e9 = Entry(f8)
    e9.config(justify=LEFT,font=('arial',21),takefocus='on',textvariable=dayValue4)
    e9.place(x=44,y=13,height=84,width=90)




    def  showc():
            global key
            mq=ec.get()
            mq_1=len(mq)
            cursor_position_1=ec.index(INSERT)
            print(cursor_position_1)
            #print(l_type)
            print(key)
            ec.insert(cursor_position_1, '0')
            key=key+1
            




    def  show1c():
                global key
                mq=ec.get()
                mq_1=len(mq)
                cursor_position_1=ec.index(INSERT)
                print(cursor_position_1)
                #print(l_type)
                print(key)
                ec.insert(cursor_position_1, '1')
                key = key + 1

    def  point_1c():
                global key
                mq=ec.get()
                mq_1=len(mq)
                cursor_position_1=ec.index(INSERT)
                print(cursor_position_1)
                #print(l_type)
                print(key)
                ec.insert(cursor_position_1, '+')
                key = key + 1



    def show2c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '2')
        key=key+1
    def show3c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '3')
        key=key+1

    def show4c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '4')
        key=key+1

    def show5c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '5')
        key=key+1

    def show6c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '6')
        key=key+1

    def show7c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '7')
        key=key+1

    def show8c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '8')
        key=key+1

    def show9c():
        global key
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        ec.insert(cursor_position_1, '9')
        key=key+1
    def cursor_rightc():
        cursor_position_1=ec.index(INSERT)
        ec.icursor(cursor_position_1+1)
        
    def cursor_leftc():
        cursor_position_1=ec.index(INSERT)
        ec.icursor(cursor_position_1-1)
        
    def clearc():
        global key
        print (key)
        mq=ec.get()
        mq_1=len(mq)
        cursor_position_1=ec.index(INSERT)
        print(cursor_position_1)
        #print(l_type)
        print(key)
        #e2.insert(cursor_position_1, '5')
        #mm=e2.index()
        #print(mm)
        ec.delete(cursor_position_1-1,cursor_position_1)
        key=key-1
        if (key<=0):
            key=0
    def enterc():
        global l_entry_e4,l_entry_e5,l_entry_e6,l_e4,l_e5
        #e1.delete(0,END)
        y=ec.get()
        y=str(y)
        #e1.insert(0,y)
        
        l_entry.append(y)
        
        #raise_frame(f1)
        if l_e4[-1]=="e4":
            e4.delete(0,END)
            y=ec.get()
            y=str(y)
            if len(ec.get())!=0:
                co_1=float(y)
            else:
                co_1=26
            l_entry_e4.append(y)
            print(l_entry_e4)
            e4.insert(0,y)
            if(co_1>300 or co_1<25):
                import popup_4
                
            else:
                raise_frame(f5)

        elif l_e4[-1]=="e5":
            e5.delete(0,END)
            y=ec.get()
            y=str(y)
            l_entry_e5.append(y)
            print(l_entry_e4)
            e5.insert(0,y)
            raise_frame(f5)

        elif l_e4[-1]=="e6":
            e6.delete(0,END)
            y=ec.get()
            y=str(y)
            l_entry_e6.append(y)
            print(l_entry_e4)
            e6.insert(0,y)
            raise_frame(f5)
        elif l_e4[-1]=="call_contact":
            e_contact.delete(0,END)
            y=ec.get()
            y=str(y)
            l_entry_call_contact.append(y)
            print(l_entry_call_contact)
            e_contact.insert(0,y)
            raise_frame(f_addnewuser)


    
    button1 = Button(master=fcontact,bg='white',fg='black', text="1",font=('Arial', 24,'bold'),borderwidth=1, command=show1c).place(x=47,y=113,width=295,height=63)
    button2 =Button(master=fcontact,bg='white',fg='black', text="2",font=('Arial', 24,'bold'),borderwidth=1, command=show2c).place(x=360,y=113,width=295,height=63)
    button3 = Button(master=fcontact,bg='white',fg='black', text="3",font=('Arial', 24,'bold'),borderwidth=1, command=show3c).place(x=672,y=113,width=295,height=63)
    button4 = Button(master=fcontact,bg='white',fg='black', text="4",font=('Arial', 24,'bold'),borderwidth=1, command=show4c).place(x=47,y=187,width=295,height=63)
    button5 = Button(master=fcontact,bg='white',fg='black', text="5",font=('Arial', 24,'bold'),borderwidth=1, command=show5c).place(x=360,y=187,width=295,height=63)
    button6 = Button(master=fcontact,bg='white',fg='black', text="6",font=('Arial', 24,'bold'),borderwidth=1, command=show6c).place(x=672,y=187,width=295,height=63)
    button7 = Button(master=fcontact,bg='white',fg='black', text="7",font=('Arial', 24,'bold'),borderwidth=1, command=show7c).place(x=47,y=264,width=295,height=63)
    button8 = Button(master=fcontact,bg='white',fg='black', text="8",font=('Arial', 24,'bold'),borderwidth=1, command=show8c).place(x=360,y=264,width=295,height=63)
    button9 = Button(master=fcontact,bg='white',fg='black', text="9",font=('Arial', 24,'bold'),borderwidth=1, command=show9c).place(x=672,y=264,width=295,height=63)
    button10 = Button(master=fcontact,bg='white',fg='black', text="clear",font=('Arial', 24,'bold'),borderwidth=1, command=clearc).place(x=47,y=338,width=295,height=63)
    button11 = Button(master=fcontact,bg='white',fg='black', text="0",font=('Arial', 24,'bold'),borderwidth=1, command=showc).place(x=360,y=338,width=295,height=63)
    button12 = Button(master=fcontact,bg='white',fg='black', text="+",font=('Arial', 24,'bold'),borderwidth=1, command=point_1c).place(x=672,y=338,width=295,height=63)
    button13 = Button(master=fcontact,bg='white',fg='black', text="<",font=('Arial', 25,'bold'),borderwidth=1, command=cursor_leftc).place(x=47,y=413,width=295,height=63)
    button14 = Button(master=fcontact,bg='white',fg='black', text="enter",font=('Arial', 24,'bold'),borderwidth=1, command=enterc).place(x=360,y=413,width=295,height=63)
    button15 = Button(master=fcontact,bg='white',fg='black', text=">",font=('Arial', 25,'bold'),borderwidth=1, command=cursor_rightc).place(x=672,y=413,width=295,height=63)


    button1 = Button(master=f2,bg='white',fg='black', text="1",font=('Arial', 24,'bold'),borderwidth=1, command=show1).place(x=47,y=113,width=295,height=63)
    button2 =Button(master=f2,bg='white',fg='black', text="2",font=('Arial', 24,'bold'),borderwidth=1, command=show2).place(x=360,y=113,width=295,height=63)
    button3 = Button(master=f2,bg='white',fg='black', text="3",font=('Arial', 24,'bold'),borderwidth=1, command=show3).place(x=672,y=113,width=295,height=63)
    button4 = Button(master=f2,bg='white',fg='black', text="4",font=('Arial', 24,'bold'),borderwidth=1, command=show4).place(x=47,y=187,width=295,height=63)
    button5 = Button(master=f2,bg='white',fg='black', text="5",font=('Arial', 24,'bold'),borderwidth=1, command=show5).place(x=360,y=187,width=295,height=63)
    button6 = Button(master=f2,bg='white',fg='black', text="6",font=('Arial', 24,'bold'),borderwidth=1, command=show6).place(x=672,y=187,width=295,height=63)
    button7 = Button(master=f2,bg='white',fg='black', text="7",font=('Arial', 24,'bold'),borderwidth=1, command=show7).place(x=47,y=264,width=295,height=63)
    button8 = Button(master=f2,bg='white',fg='black', text="8",font=('Arial', 24,'bold'),borderwidth=1, command=show8).place(x=360,y=264,width=295,height=63)
    button9 = Button(master=f2,bg='white',fg='black', text="9",font=('Arial', 24,'bold'),borderwidth=1, command=show9).place(x=672,y=264,width=295,height=63)
    button10 = Button(master=f2,bg='white',fg='black', text="clear",font=('Arial', 24,'bold'),borderwidth=1, command=clear).place(x=47,y=338,width=295,height=63)
    button11 = Button(master=f2,bg='white',fg='black', text="0",font=('Arial', 24,'bold'),borderwidth=1, command=show).place(x=360,y=338,width=295,height=63)
    button12 = Button(master=f2,bg='white',fg='black', text=".",font=('Arial', 24,'bold'),borderwidth=1, command=point_1).place(x=672,y=338,width=295,height=63)
    button13 = Button(master=f2,bg='white',fg='black', text="<",font=('Arial', 25,'bold'),borderwidth=1, command=cursor_left).place(x=47,y=413,width=295,height=63)
    button14 = Button(master=f2,bg='white',fg='black', text="enter",font=('Arial', 24,'bold'),borderwidth=1, command=enter).place(x=360,y=413,width=295,height=63)
    button15 = Button(master=f2,bg='white',fg='black', text=">",font=('Arial', 25,'bold'),borderwidth=1, command=cursor_right).place(x=672,y=413,width=295,height=63)
          


   # change_1()
    def change_1_f6():
        
        button1 = Button(master=f6,bg='white',fg='black', text="1",font=('Arial', 24,'bold'),borderwidth=1, command=show1_f6).place(x=47,y=113,width=295,height=63)
        button2 =Button(master=f6,bg='white',fg='black', text="2",font=('Arial', 24,'bold'),borderwidth=1, command=show2_f6).place(x=360,y=113,width=295,height=63)
        button3 = Button(master=f6,bg='white',fg='black', text="3",font=('Arial', 24,'bold'),borderwidth=1, command=show3_f6).place(x=672,y=113,width=295,height=63)
        button4 = Button(master=f6,bg='white',fg='black', text="4",font=('Arial', 24,'bold'),borderwidth=1, command=show4_f6).place(x=47,y=187,width=295,height=63)
        button5 = Button(master=f6,bg='white',fg='black', text="5",font=('Arial', 24,'bold'),borderwidth=1, command=show5_f6).place(x=360,y=187,width=295,height=63)
        button6 = Button(master=f6,bg='white',fg='black', text="6",font=('Arial', 24,'bold'),borderwidth=1, command=show6_f6).place(x=672,y=187,width=295,height=63)
        button7 = Button(master=f6,bg='white',fg='black', text="7",font=('Arial', 24,'bold'),borderwidth=1, command=show7_f6).place(x=47,y=264,width=295,height=63)
        button8 = Button(master=f6,bg='white',fg='black', text="8",font=('Arial', 24,'bold'),borderwidth=1, command=show8_f6).place(x=360,y=264,width=295,height=63)
        button9 = Button(master=f6,bg='white',fg='black', text="9",font=('Arial', 24,'bold'),borderwidth=1, command=show9_f6).place(x=672,y=264,width=295,height=63)
        button10 = Button(master=f6,bg='white',fg='black', text="clear",font=('Arial', 24,'bold'),borderwidth=1, command=clear_f6).place(x=47,y=338,width=295,height=63)
        button11 = Button(master=f6,bg='white',fg='black', text="0",font=('Arial', 24,'bold'),borderwidth=1, command=show_f6).place(x=360,y=338,width=295,height=63)
        button12 = Button(master=f6,bg='white',fg='black', text=".",font=('Arial', 24,'bold'),borderwidth=1, command=point_1_f6).place(x=672,y=338,width=295,height=63)
        button13 = Button(master=f6,bg='white',fg='black', text="abc",font=('Arial', 24,'bold'),borderwidth=1, command=change_f6).place(x=47,y=413,width=295,height=63)
        button14 = Button(master=f6,bg='white',fg='black', text="space",font=('Arial', 24,'bold'),borderwidth=1, command=space_f6).place(x=360,y=413,width=295,height=63)
        button15 = Button(master=f6,bg='white',fg='black', text="enter",font=('Arial', 24,'bold'),borderwidth=1, command=enter_f6).place(x=672,y=413,width=295,height=63)


    change_1_f6()
    def change_time():
        
        button1 = Button(master=f8,bg='white',fg='black', text="1",font=('Arial', 24,'bold'),borderwidth=1, command=show1_f8).place(x=47,y=113,width=295,height=63)
        button2 =Button(master=f8,bg='white',fg='black', text="2",font=('Arial', 24,'bold'),borderwidth=1, command=show2_f8).place(x=360,y=113,width=295,height=63)
        button3 = Button(master=f8,bg='white',fg='black', text="3",font=('Arial', 24,'bold'),borderwidth=1, command=show3_f8).place(x=672,y=113,width=295,height=63)
        button4 = Button(master=f8,bg='white',fg='black', text="4",font=('Arial', 24,'bold'),borderwidth=1, command=show4_f8).place(x=47,y=187,width=295,height=63)
        button5 = Button(master=f8,bg='white',fg='black', text="5",font=('Arial', 24,'bold'),borderwidth=1, command=show5_f8).place(x=360,y=187,width=295,height=63)
        button6 = Button(master=f8,bg='white',fg='black', text="6",font=('Arial', 24,'bold'),borderwidth=1, command=show6_f8).place(x=672,y=187,width=295,height=63)
        button7 = Button(master=f8,bg='white',fg='black', text="7",font=('Arial', 24,'bold'),borderwidth=1, command=show7_f8).place(x=47,y=264,width=295,height=63)
        button8 = Button(master=f8,bg='white',fg='black', text="8",font=('Arial', 24,'bold'),borderwidth=1, command=show8_f8).place(x=360,y=264,width=295,height=63)
        button9 = Button(master=f8,bg='white',fg='black', text="9",font=('Arial', 24,'bold'),borderwidth=1, command=show9_f8).place(x=672,y=264,width=295,height=63)
        button10 = Button(master=f8,bg='white',fg='black', text="clear",font=('Arial', 24,'bold'),borderwidth=1, command=clear_f8).place(x=47,y=338,width=295,height=63)
        button11 = Button(master=f8,bg='white',fg='black', text="0",font=('Arial', 24,'bold'),borderwidth=1, command=show_f8).place(x=360,y=338,width=295,height=63)
        button12 = Button(master=f8,bg='white',fg='black', text="infinity",font=('Arial', 24,'bold'),borderwidth=1, command=infinte).place(x=672,y=338,width=295,height=63)
        button13 = Button(master=f8,bg='white',fg='black', text="<",font=('Arial', 24,'bold'),borderwidth=1, command=cursor_left_f8).place(x=47,y=413,width=295,height=63)
        button14 = Button(master=f8,bg='white',fg='black', text="enter",font=('Arial', 24,'bold'),borderwidth=1, command=enter_f8).place(x=360,y=413,width=295,height=63)
        button15 = Button(master=f8,bg='white',fg='black', text=">",font=('Arial', 24,'bold'),borderwidth=1, command=cursor_right_f8).place(x=672,y=413,width=295,height=63)


    change_time()


    
    #Label(f3, text='FRAME 3').pack(side='left')

    key_1=0
    def  a():
            global key_1,key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position,'a')
            key=key+1
    def  b():
                global key
                mm=e3.get()
                mm_1=len(mm)
                cursor_position=e3.index(INSERT)
                print(cursor_position)
                #print(l_type)
                print(key)
                e3.insert(cursor_position, 'b')
                key = key + 1
    def c():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'c')
        key=key+1
    def d():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'd')
        key=key+1
    def e():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position,'e')
        key=key+1
    def f():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position,'f')
        key=key+1

    def g():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'g')
        key=key+1

    def h():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'h')
        key=key+1

    def i():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'i')
        key=key+1

    def j():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'j')
        key=key+1



    def  k():
            global key_1,key
            #print(l_type)
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            print(key)
            e3.insert(cursor_position,'k')
            key=key+1
    def  l():
                global key
                mm=e3.get()
                mm_1=len(mm)
                cursor_position=e3.index(INSERT)
                print(cursor_position)
                #print(l_type)
                print(key)
                e3.insert(cursor_position, 'l')
                key = key + 1
    def m():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'm')

        key=key+1
    def n():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'n')
        
        key=key+1
    def o():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'o')
        key=key+1
    def p():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'p')
        key=key+1

    def q():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'q')
        key=key+1

    def r():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'r')
        key=key+1

    def s():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 's')
        key=key+1

    def t():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 't')
        key=key+1



    def u():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'u')
        key=key+1

    def v():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'v')
        key=key+1



    def  w():
            global key_1,key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'w')
            key=key+1
    def  x():
                global key
                mm=e3.get()
                mm_1=len(mm)
                cursor_position=e3.index(INSERT)
                print(cursor_position)
                #print(l_type)
                print(key)
                e3.insert(cursor_position, 'x')
                key = key + 1
    def y():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'y')
        key=key+1
    def z():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, 'z')
        key=key+1
    def point():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, '.')
        key=key+1
    def dash():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        #print(l_type)
        print(key)
        e3.insert(cursor_position, '-')
        key=key+1

    def shift():

        def  A():
            global key_1,key
            #print(l_type)
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'A')
            key=key+1
        def  B():
                    global key
                    mm=e3.get()
                    mm_1=len(mm)
                    cursor_position=e3.index(INSERT)
                    print(cursor_position)
                    #print(l_type)
                    print(key)
                    e3.insert(cursor_position, 'B')
                    key = key + 1
        def C():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'C')
            key=key+1
        def D():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'D')
            key=key+1
        def E():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'E')
            key=key+1
        def F():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'F')
            key=key+1

        def G():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'G')
            key=key+1

        def H():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'H')
            key=key+1

        def I():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'I')
            key=key+1

        def J():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'J')
            key=key+1



        def  K():
                global key_1,key
                mm=e3.get()
                mm_1=len(mm)
                cursor_position=e3.index(INSERT)
                print(cursor_position)
                #print(l_type)
                print(key)
                e3.insert(cursor_position, 'K')
                key=key+1
        def  L():
                    global key
                    mm=e3.get()
                    mm_1=len(mm)
                    cursor_position=e3.index(INSERT)
                    print(cursor_position)
                    #print(l_type)
                    print(key)
                    e3.insert(cursor_position, 'L')
                    key = key + 1
        def M():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'M')
            key=key+1
        def N():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'N')
            key=key+1
        def O():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'O')
            key=key+1
        def P():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            #print(l_type)
            print(key)
            e3.insert(cursor_position, 'P')
            key=key+1

        def Q():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
           
            print(key)
            e3.insert(cursor_position, 'Q')
            key=key+1

        def R():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'R')
            key=key+1

        def S():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'S')
            key=key+1

        def T():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'T')
            key=key+1



        def U():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
           
            print(key)
            e3.insert(cursor_position, 'U')
            key=key+1

        def V():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'V')
            key=key+1



        def  W():
                global key_1,key
                mm=e3.get()
                mm_1=len(mm)
                cursor_position=e3.index(INSERT)
                print(cursor_position)
                #print(l_type)
                print(key)
                e3.insert(cursor_position, 'W')
                key=key+1
        def  X():
                    global key
                    mm=e3.get()
                    mm_1=len(mm)
                    cursor_position=e3.index(INSERT)
                    print(cursor_position)
                    #print(l_type)
                    print(key)
                    e3.insert(cursor_position, 'X')
                    key = key + 1
        def Y():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'Y')
            key=key+1
        def Z():
            global key
            mm=e3.get()
            mm_1=len(mm)
            cursor_position=e3.index(INSERT)
            print(cursor_position)
            
            print(key)
            e3.insert(cursor_position, 'Z')
            key=key+1
            
        buttonQ = Button(master=f3,bg='white',fg='black', text="Q",font=('Arial', 28), borderwidth=1,command=Q).place(x=60,y=111,width=80)
        buttonW = Button(master=f3,bg='white',fg='black', text="W",font=('Arial', 28),borderwidth=1, command=W).place(x=151,y=111,width=80)
        buttonE = Button(master=f3,bg='white',fg='black', text="E",font=('Arial', 28),borderwidth=1, command=E).place(x=242,y=111,width=80)
        buttonR = Button(master=f3,bg='white',fg='black', text="R",font=('Arial', 28),borderwidth=1, command=R).place(x=333,y=111,width=80)
        buttonT = Button(master=f3,bg='white',fg='black', text="T",font=('Arial', 28),borderwidth=1, command=T).place(x=424,y=111,width=80)
        buttonY = Button(master=f3,bg='white',fg='black', text="Y",font=('Arial', 28),borderwidth=1, command=Y).place(x=515,y=111,width=80)
        buttonU = Button(master=f3,bg='white',fg='black', text="U",font=('Arial', 28),borderwidth=1, command=U).place(x=606,y=111,width=80)
        buttonI = Button(master=f3,bg='white',fg='black', text="I",font=('Arial', 28),borderwidth=1, command=I).place(x=697,y=111,width=80)
        buttonO = Button(master=f3,bg='white',fg='black', text="O",font=('Arial', 28),borderwidth=1, command=O).place(x=788,y=111,width=80)
        buttonP = Button(master=f3,bg='white',fg='black', text="P",font=('Arial', 28),borderwidth=1, command=P).place(x=879,y=111,width=80)
        buttonA = Button(master=f3,bg='white',fg='black', text="A",font=('Arial', 28),borderwidth=1, command=A).place(x=60,y=212,width=80)
        buttonS = Button(master=f3,bg='white',fg='black', text="S",font=('Arial', 28),borderwidth=1, command=S).place(x=151,y=212,width=80)
        buttonD = Button(master=f3,bg='white',fg='black', text="D",font=('Arial', 28),borderwidth=1, command=D).place(x=242,y=212,width=80)
        buttonF = Button(master=f3,bg='white',fg='black', text="F",font=('Arial', 28),borderwidth=1, command=F).place(x=333,y=212,width=80)
        buttonG = Button(master=f3,bg='white',fg='black', text="G",font=('Arial', 28),borderwidth=1, command=G).place(x=424,y=212,width=80)
        buttonH = Button(master=f3,bg='white',fg='black', text="H",font=('Arial', 28),borderwidth=1, command=H).place(x=515,y=212,width=80)
        buttonJ = Button(master=f3,bg='white',fg='black', text="J",font=('Arial', 28),borderwidth=1, command=J).place(x=606,y=212,width=80)
        buttonK = Button(master=f3,bg='white',fg='black', text="K",font=('Arial', 28),borderwidth=1, command=K).place(x=697,y=212,width=80)
        buttonL = Button(master=f3,bg='white',fg='black', text="L",font=('Arial', 28),borderwidth=1, command=L).place(x=788,y=212,width=80)

        buttoncolon = Button(master=f3,bg='white',fg='black', text=":",font=('Arial', 28),borderwidth=1, command=colon).place(x=879,y=212,width=80)
        qq=u'\u2B06'
        qq=str(qq)
        buttonshift = Button(master=f3,bg='white',fg='black', text=qq,font=('Arial', 28),borderwidth=1, command=shift_1).place(x=60,y=313,width=80)
        buttonZ = Button(master=f3,bg='white',fg='black', text="Z",font=('Arial', 28),borderwidth=1, command=Z).place(x=151,y=313,width=80)
        buttonX = Button(master=f3,bg='white',fg='black', text="X",font=('Arial', 28),borderwidth=1, command=X).place(x=242,y=313,width=80)
        buttonC = Button(master=f3,bg='white',fg='black', text="C",font=('Arial', 28),borderwidth=1, command=C).place(x=333,y=313,width=80)
        buttonV = Button(master=f3,bg='white',fg='black', text="V",font=('Arial', 28),borderwidth=1, command=V).place(x=424,y=313,width=80)
        buttonB = Button(master=f3,bg='white',fg='black', text="B",font=('Arial', 28),borderwidth=1, command=B).place(x=515,y=313,width=80)
        buttonN = Button(master=f3,bg='white',fg='black', text="N",font=('Arial', 28),borderwidth=1, command=N).place(x=606,y=313,width=80)
        buttonM = Button(master=f3,bg='white',fg='black', text="M",font=('Arial', 28),borderwidth=1, command=M).place(x=697,y=313,width=80)
        buttonpoint = Button(master=f3,bg='white',fg='black', text=".",font=('Arial', 28),borderwidth=1, command=point).place(x=788,y=313,width=80)
        buttonclear = Button(master=f3,bg='white',fg='black', text="clear",font=('Arial', 28),borderwidth=1, command=clear).place(x=879,y=313,width=82)
        button123 = Button(master=f3,bg='white',fg='black', text="123",font=('Arial', 28),borderwidth=1, command=change_2).place(x=60,y=404,width=180)
        buttondash = Button(master=f3,bg='white',fg='black', text="-",font=('Arial', 28),borderwidth=1, command=dash).place(x=255,y=404,width=125)
        buttonspace = Button(master=f3,bg='white',fg='black', text="space",font=('Arial', 28),borderwidth=1, command=space).place(x=390,y=404,width=338)
        buttonenter = Button(master=f3,bg='white',fg='black', text="enter",font=('Arial', 28),borderwidth=1, command=enter).place(x=740,y=404,width=230)
        


    def enter():

        global l_entry,l_e4

        y_1=e3.get()
        y_1=str(y_1)

        l_entry.append(y_1)

        if l_e4[-1]=="e7":
            e7.delete(0,END)
            y=e3.get()
            y=str(y)
            l_entry_e7.append(y)
            print(l_entry_e7)
            e7.insert(0,y)
            raise_frame(f5)

        if l_e4[-1]=="call_name":
            e_name.delete(0,END)
            y=e3.get()
            y=str(y)
            if(len(l_entry_call_name)>2):
                del l_entry_call_name[0]
            l_entry_call_name.append(y)
            e_name.insert(0,y)
            e3.config(font=('arial',21),takefocus='off',borderwidth='2')
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="call_designation":
            e_designation.delete(0,END)
            y=e3.get()
            y=str(y)
            l_entry_call_designation.append(y)
            print(l_entry_call_designation)
            e_designation.insert(0,y)
            e3.config(font=('arial',21),takefocus='off',borderwidth='2')
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="call_contact":
            e_contact.delete(0,END)
            y=e3.get()
            y=str(y)
            l_entry_call_contact.append(y)
            print(l_entry_call_contact)
            e_contact.insert(0,y)
            e3.config(font=('arial',21),takefocus='off',borderwidth='2')
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="call_employeid":
            e_employeid.delete(0,END)
            y=e3.get()
            y=str(y)
            l_entry_call_employeid.append(y)
            print(l_entry_call_employeid)
            e_employeid.insert(0,y)
            e3.config(font=('arial',21),takefocus='off',borderwidth='2')
            raise_frame(f_addnewuser)
        elif l_e4[-1]=="entry_password":
            e_password.delete(0,END)
            y=e3.get()
            y=str(y)
            l_entry_password.append(y)
            print(l_entry_password)
            e_password.insert(0,y)
            e3.config(font=('arial',21),takefocus='off',borderwidth='2',show='')
            e8.config(font=('arial',21),takefocus='off',borderwidth='2',show='')
            raise_frame(f_servicemode)
        

    def close():
        e1.delete(0,END)
        raise_frame(f1)
    def space():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        print(key)
        e3.insert(cursor_position, ' ')

        key=key+1
        

    def colon():
        global key
        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)

        print(key)
        e3.insert(cursor_position, ':')
        key=key+1
    def clear():
        global key

        mm=e3.get()
        mm_1=len(mm)
        cursor_position=e3.index(INSERT)
        print(cursor_position)
        e3.delete(cursor_position-1,cursor_position)
        key=key-1
        if (key<=0):
            key=0



    def change_2():
        global key

        cursor_position=e3.index(INSERT)
        print(cursor_position)
        e8.delete(0,END)
        f_e_2=e3.get()
        f_e_2=str(f_e_2)
        e8.insert(0,f_e_2)
        
        e8.icursor(cursor_position)
        raise_frame(f6)

    def shift_1():

        buttonq = Button(master=f3,bg='white',fg='black', text="q",font=('Arial', 28), borderwidth=1,command=q).place(x=60,y=111,width=80)
        buttonw = Button(master=f3,bg='white',fg='black', text="w",font=('Arial', 28),borderwidth=1, command=w).place(x=151,y=111,width=80)
        buttone = Button(master=f3,bg='white',fg='black', text="e",font=('Arial', 28),borderwidth=1, command=e).place(x=242,y=111,width=80)
        buttonr = Button(master=f3,bg='white',fg='black', text="r",font=('Arial', 28),borderwidth=1, command=r).place(x=333,y=111,width=80)
        buttont = Button(master=f3,bg='white',fg='black', text="t",font=('Arial', 28),borderwidth=1, command=t).place(x=424,y=111,width=80)
        buttony = Button(master=f3,bg='white',fg='black', text="y",font=('Arial', 28),borderwidth=1, command=y).place(x=515,y=111,width=80)
        buttonu = Button(master=f3,bg='white',fg='black', text="u",font=('Arial', 28),borderwidth=1, command=u).place(x=606,y=111,width=80)
        buttoni = Button(master=f3,bg='white',fg='black', text="i",font=('Arial', 28),borderwidth=1, command=i).place(x=697,y=111,width=80)
        buttono = Button(master=f3,bg='white',fg='black', text="o",font=('Arial', 28),borderwidth=1, command=o).place(x=788,y=111,width=80)
        buttonp = Button(master=f3,bg='white',fg='black', text="p",font=('Arial', 28),borderwidth=1, command=p).place(x=879,y=111,width=80)
        buttona = Button(master=f3,bg='white',fg='black', text="a",font=('Arial', 28),borderwidth=1, command=a).place(x=60,y=212,width=80)
        buttons = Button(master=f3,bg='white',fg='black', text="s",font=('Arial', 28),borderwidth=1, command=s).place(x=151,y=212,width=80)
        buttond = Button(master=f3,bg='white',fg='black', text="d",font=('Arial', 28),borderwidth=1, command=d).place(x=242,y=212,width=80)
        buttonf = Button(master=f3,bg='white',fg='black', text="f",font=('Arial', 28),borderwidth=1, command=f).place(x=333,y=212,width=80)
        buttong = Button(master=f3,bg='white',fg='black', text="g",font=('Arial', 28),borderwidth=1, command=g).place(x=424,y=212,width=80)
        buttonh = Button(master=f3,bg='white',fg='black', text="h",font=('Arial', 28),borderwidth=1, command=h).place(x=515,y=212,width=80)
        buttonj = Button(master=f3,bg='white',fg='black', text="j",font=('Arial', 28),borderwidth=1, command=j).place(x=606,y=212,width=80)
        buttonk = Button(master=f3,bg='white',fg='black', text="k",font=('Arial', 28),borderwidth=1, command=k).place(x=697,y=212,width=80)
        buttonl = Button(master=f3,bg='white',fg='black', text="l",font=('Arial', 28),borderwidth=1, command=l).place(x=788,y=212,width=80)

        buttoncolon = Button(master=f3,bg='white',fg='black', text=":",font=('Arial', 28),borderwidth=1, command=colon).place(x=879,y=212,width=80)
        qq=u'\u2B06'
        qq=str(qq)
        buttonshift = Button(master=f3,bg='white',fg='black', text=qq,font=('Arial', 28),borderwidth=1, command=shift).place(x=60,y=313,width=80)
        buttonz = Button(master=f3,bg='white',fg='black', text="z",font=('Arial', 28),borderwidth=1, command=z).place(x=151,y=313,width=80)
        buttonx = Button(master=f3,bg='white',fg='black', text="x",font=('Arial', 28),borderwidth=1, command=x).place(x=242,y=313,width=80)
        buttonc = Button(master=f3,bg='white',fg='black', text="c",font=('Arial', 28),borderwidth=1, command=c).place(x=333,y=313,width=80)
        buttonv = Button(master=f3,bg='white',fg='black', text="v",font=('Arial', 28),borderwidth=1, command=v).place(x=424,y=313,width=80)
        buttonb = Button(master=f3,bg='white',fg='black', text="b",font=('Arial', 28),borderwidth=1, command=b).place(x=515,y=313,width=80)
        buttonn = Button(master=f3,bg='white',fg='black', text="n",font=('Arial', 28),borderwidth=1, command=n).place(x=606,y=313,width=80)
        buttonm = Button(master=f3,bg='white',fg='black', text="m",font=('Arial', 28),borderwidth=1, command=m).place(x=697,y=313,width=80)
        buttonpoint = Button(master=f3,bg='white',fg='black', text=".",font=('Arial', 28),borderwidth=1, command=point).place(x=788,y=313,width=80)
        buttonclear = Button(master=f3,bg='white',fg='black', text="clear",font=('Arial', 28),borderwidth=1, command=clear).place(x=879,y=313,width=82)
        button123 = Button(master=f3,bg='white',fg='black', text="123",font=('Arial', 28),borderwidth=1, command=change_2).place(x=60,y=404,width=180)
        buttondash = Button(master=f3,bg='white',fg='black', text="-",font=('Arial', 28),borderwidth=1, command=dash).place(x=255,y=404,width=125)
        buttonspace = Button(master=f3,bg='white',fg='black', text="space",font=('Arial', 28),borderwidth=1, command=space).place(x=390,y=404,width=338)
        buttonenter = Button(master=f3,bg='white',fg='black', text="enter",font=('Arial', 28),borderwidth=1, command=enter).place(x=740,y=404,width=230)

    shift_1()

    def cannotenter():
        import popup_6



    

    q_1_s_1=0


#############################################tkinter_graph######################
    list_names=[]
    def data_store():
        global l_1,l_2,list_names
        t=time.localtime()
        current_time_1=time.strftime("%H%M%S",t)
        today = date.today()
        d1 = today.strftime("%d-%B-%Y")
        name=current_time_1+d1
        Value={'Time':l_1 , 'Temperature':l_2}
        df1=DataFrame(Value,columns=['Time','Temperature'])
        export_csv=df1.to_csv(r'an'+name+'.csv',index=None,header=True)
        list_names.append('an'+name+'.csv')
        
    def change_graph():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open2!","utf-8"))
        raise_frame(f_graph)

    def back4():
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8"))
        label_start=Button(master=f1,text="View Running Test",font=('Arial',19,'bold'),fg='black',relief='flat',borderwidth=0,command=change_graph).place(x=59,y=114)
   
        raise_frame(f1)

    def stop_test():
        global list_set,l_1,l_2,list_stop,halt_timer,gfg1

        data_store()
        if(len(list_set)>2):
            del list_set[0]

        list_set.append('False')
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Close!","utf-8"))
        
        graph_result_show()

        list_stop.append('close')
        if(len(list_stop)>2):
            list_stop.clear()
            list_stop.append('close')
        halt_timer=False
        gfg1=1
        raise_frame(f_result)
        l_1.clear()
        l_2.clear()


    g_value=0
    x=0
    l_1=[]
    l_2=[]
    list_temperature=[]
    list_date=[]
    gfg1=0
    def temp():
        global list_temperature,list_time,list_set
        l_1=[]
        t=time.localtime()
        current_time=time.strftime("%H%M%S",t)

        x_temperature = random.randint(42,43)
        
        tempC=float(x_temperature)
        tempC=round(tempC,2)
        list_temperature.append(tempC)
        timer = threading.Timer(1, gfg) 
        timer.start()
        if(list_set[-1]=='False'):
            timer.cancel()

        return tempC
    rt=1
    def animate(i):
        global l_1,l_2,list_date,rt,list_set,check_temperature
        
        ax1.clear()

        ax1.set_facecolor('white')
        ax1.set_title('Temperature Chart')
        ax1.set_ylabel('Temperature')

        ax1.grid(axis='y')
        ax1.autoscale(enable=True,axis='both')
        if(list_set[-1]=='False'):
                check_temperature.append('False')
                if (len(check_temperature))>2:
                    check_temperature.clear()
                    check_temperature.append('False')
        if(list_set[-1]=='True'):

            t=time.localtime()
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            list_date.append(d1)
            current_time=time.strftime("%H%M%S",t)
            current_time_1=time.strftime("%H%M%S",t)
            y=temp()
            l_1.append(y)
            print(y)
            l_2.append(current_time)

            if(l_1[-1] < l_1[0]+10):
                ax1.set_ylim(l_1[0]-5, l_1[0]+10)

            else:
                ax1.autoscale(enable=True,axis='y')
                

            if(len(l_2)>11):
         

                 ax1.set_xticks(np.arange(0, len(l_2), (len(l_2)/8)+rt))
                 rt=rt+0.1
                

            check_temperature.append('True')
            if (len(check_temperature))>2:
                check_temperature.clear()
                check_temperature.append('True')

                



            ax1.plot(l_2,l_1,color='red',linewidth=2.5,antialiased=True,solid_capstyle='round',solid_joinstyle='round')


    img1 = Image.open("graph_screen.png")
    filename1 = ImageTk.PhotoImage(img1)
    canvas1 = Canvas(f_graph,height=500,width=1024)
        
    canvas1.image = filename1  # <--- keep reference of your image
    canvas1.create_image(0,0,anchor='nw',image=filename1)
        #canvas.grid(row=508,column=8005)
    canvas1.place(x=0,y=0)


    fig = Figure(figsize=(6.5, 2.8), dpi=100)
    fig.patch.set_facecolor('white')

    ax1=fig.add_subplot(1,1,1)

    canvas = FigureCanvasTkAgg(fig, master=f_graph)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().place(x=50,y=10)
    ani=animation.FuncAnimation(fig,animate,interval=1000)
    Label(f_graph,text="Time",font=('Arial',12),bg='white').place(x=350,y=280)
    Button(f_graph,text="Home",bg='#4299ff',fg='white',font=('Arial',16),command=back4).place(x=80,y=430)
    Button(f_graph,text="Stop Test",bg='#4299ff',fg='white',font=('Arial',16),command=stop_test).place(x=580,y=430)





    def reading_graph():
        global list_stop,gfg1,l_f_hrs,l_f_mins
        list_stop.append('open')
        if(len(list_stop)>2):
            list_stop.clear()
        gfg1=0
        entry_temperature1=e4.get()
        entry_time1=e5.get()
        entry_time2=e6.get()


        if(e5.get()=='infinity' and e6.get()=='infinity'):
            e_temperature=Entry(f_graph)
            e_temperature.config(bg='white',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
            e_temperature.place(x=310,y=362,width=200)

            degree_sign=u'\u00B0'
            e_temperature.insert(0,entry_temperature1+degree_sign+"C")
            e_time1=Entry(f_graph)
            e_time1.config(bg='white',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
            e_time1.place(x=790,y=362,width=60)
            e_time1.insert(0,"infinity")

            
        else:
            e_temperature=Entry(f_graph)
            e_temperature.config(bg='white',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
            e_temperature.place(x=310,y=362,width=100)
                #entry_temperature.insert(0,'80 C')
            degree_sign=u'\u00B0'
            e_temperature.insert(0,entry_temperature1+degree_sign+"C")
            e_time1=Entry(f_graph)
            e_time1.config(bg='white',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
            e_time1.place(x=790,y=362,width=60)
            e_time1.insert(0,entry_time1+"Hrs")
            e_time2=Entry(f_graph)
            e_time2.config(bg='white',fg='black', font=('Arial', 20,'bold'),relief=GROOVE,borderwidth=0,justify=CENTER)
            e_time2.place(x=860,y=362,width=60)
            e_time2.insert(0,entry_time2+"Min")
            l_f_hrs.append(entry_time1)
            l_f_mins.append(entry_time2)



    Label(f_graph,text="Set Temperature",font=('Arial',16,'bold'),bg='white',fg='black').place(x=85,y=360)
    Label(f_graph,text="Set Timer",font=('Arial',16,'bold'),bg='white',fg='black').place(x=600,y=360)
   # Label(f_graph,text=entry_time1,font=('Arial',12),bg='white',fg='black').place(x=850,y=370)
    
    
    




##################################################################result screen#######################################
    def user_show(qt):
        hh_temp=[]
        gfg=qt
        df=pd.read_csv(gfg)
        

        figresult = Figure(figsize=(3.87, 3.1), dpi=100)
        figresult.patch.set_facecolor('white')

        ax2=figresult.add_subplot(1,1,1)


        count=len(open(list_names[-1]).readlines()) 

        df2=pd.read_csv(list_names[-1], skiprows=range(2,count-1), header=0)

        print(df2,'dataframe')
        for xq in df2['Time']:
            hh_temp.append(xq)

        print(hh_temp[-1],'tempad')
        print(hh_temp[0],'tempad')
        if(hh_temp[-1] < hh_temp[0]+10):
                ax2.set_ylim(hh_temp[0]-5, hh_temp[0]+10)


        ax2.set_title('Temperature Chart')
        ax2.set_ylabel('Temperature')
        
        ax2.grid(axis='y')
        
        ax2.plot(df['Temperature'],df['Time'],color='red',linewidth=2.5,antialiased=True,solid_capstyle='round',solid_joinstyle='round')

        canvasresult1 = FigureCanvasTkAgg(figresult, master=f_result)  # A tk.DrawingArea.
        canvasresult1.draw()
        canvasresult1.get_tk_widget().place(x=560,y=52)
        Label(f_result,text='Time',bg='white',fg='black',font=('Arial',11)).place(x=735,y=355,height=11)
        if(len(hh_temp)>2):
            del hh_temp[0]


        raise_frame(f_result)
        print(gfg)
    def back5():
        global s11
        clientsocket,address=s11.accept()
        clientsocket.send(bytes("Open1!","utf-8")) 
        raise_frame(f1)



    imgresult = Image.open("resultscreen.png")
    filenameresult = ImageTk.PhotoImage(imgresult)
    canvasresult = Canvas(f_result,height=500,width=1024)
        
    canvasresult.image = filenameresult  # <--- keep reference of your image
    canvasresult.create_image(0,0,anchor='nw',image=filenameresult)

    canvasresult.place(x=0,y=0)





    Button(f_result,text="Back",bg='#4299ff',fg='white',font=('Arial',15),command=back5).place(x=60,y=430,width=150)
    Button(f_result,text="Home",bg='#4299ff',fg='white',font=('Arial',15),command='').place(x=550,y=430,width=150)
    Button(f_result,text="Print",bg='#4299ff',fg='white',font=('Arial',15),command='').place(x=800,y=430,width=150)
    Label(f_result,text="Set User",bg='white',fg='black',font=('Arial',15,'bold')).place(x=80,y=292)
    Label(f_result,text="Set Temperature",bg='white',fg='black',font=('Arial',15,'bold')).place(x=80,y=93)
    Label(f_result,text="Set Timer",bg='white',fg='black',font=('Arial',15,'bold')).place(x=80,y=192)
    Label(f_result,text="Test Details",bg='white',fg='black',font=('Arial',18,'bold')).place(x=76,y=12)


    def graph_result_show():
        global l_f_hrs,l_f_mins,variable2,list_names
        hh_temp=[]
        x1=e4.get()
        x2=e5.get()
        x3=e6.get()
        x4=variable2.get()
        print(x4)
        degree_sign=u'\u00B0'
        Label(f_result,text=x1+degree_sign+"C",bg='white',fg='black',font=('Arial',15,'bold')).place(x=390,y=95)
        Label(f_result,text=x2+"Hrs"+x3+"Mins",bg='white',fg='black',font=('Arial',15,'bold')).place(x=390,y=192)
        Label(f_result,text=x4,bg='white',fg='black',font=('Arial',15,'bold')).place(x=390,y=292,width=100)
        df=pd.read_csv(list_names[-1])
        

        figresult = Figure(figsize=(3.87, 3.1), dpi=100)
        figresult.patch.set_facecolor('white')

        ax2=figresult.add_subplot(1,1,1)


        count=len(open(list_names[-1]).readlines()) 

        df2=pd.read_csv(list_names[-1], skiprows=range(2,count-1), header=0)

        print(df2,'dataframe')
        for xq in df2['Time']:
            hh_temp.append(xq)

        print(hh_temp[-1],'tempad')
        print(hh_temp[0],'tempad')
        if(hh_temp[-1] < hh_temp[0]+10):
                ax2.set_ylim(hh_temp[0]-5, hh_temp[0]+10)


        ax2.set_title('Temperature Chart')
        ax2.set_ylabel('Temperature')
        
        ax2.grid(axis='y')
        
        ax2.plot(df['Temperature'],df['Time'],color='red',linewidth=2.5,antialiased=True,solid_capstyle='round',solid_joinstyle='round')

        canvasresult1 = FigureCanvasTkAgg(figresult, master=f_result)  # A tk.DrawingArea.
        canvasresult1.draw()
        canvasresult1.get_tk_widget().place(x=560,y=52)
        Label(f_result,text='Time',bg='white',fg='black',font=('Arial',11)).place(x=735,y=355,height=11)
        if(len(hh_temp)>2):
            del hh_temp[0]


        imgstart = Image.open("start.png")
        filenamestart = ImageTk.PhotoImage(imgstart)
        canvasstart = Canvas(f1,width=265,height=101)
            
        canvasstart.image = filenamestart  # <--- keep reference of your image
        canvasstart.create_image(2,2,anchor='nw',image=filenamestart)
        canvasstart.configure(borderwidth=0)

        canvasstart.place(x=50,y=90)

        label_start=Button(master=f1,font=('Arial',22,'bold'),fg='black',relief='raised',image=filenamestart,borderwidth=1,command=change_start_screen).place(x=50,y=90)
        Button(master=f1,text="Start Test",font=('Arial',22,'bold'),fg='black',relief='flat',borderwidth=0,command=change_start_screen).place(x=125,y=114)

        current_1=210
        list_faisal=[]
        unix=u'\u270E'       
        print(list_names)
        for last_1 in list_names:
            a=last_1
            Button(f_result_data.scrollFrame.viewPort,bg='#4299ff',fg='white', text="Show Result",font=('Arial',15,'bold'), command=lambda x=a:user_show(x)).place(x=815, y=current_1,width=75,height=50)
            print(list_faisal)
            if(len(list_faisal)>2):
                del list_faisal[0]
            list_faisal.append(current_1)
            current_1=current_1+70
            print(list_faisal)
    






    halt_timer=True

    def gfg(): 
            global e5,e6,check_temperature,gfg1,l_cool,list_set,list_stop,halt_timer,e_time1,l_f_hrs,l_f_mins
            print(check_temperature)
            try:
                if (check_temperature[-1]=='True'):
                    hours=l_f_hrs[-1]
                    print(hours)
                    hours=int(hours)
                    minutes=l_f_mins[-1]
                    minutes=int(minutes)
                    print(minutes)
                    print("1231")
                    print(gfg1)
                    if hours!='infinity' and minutes!='infinity' and gfg1==0:
                        gfg1=1
                    
                        for h in range( hours):
                            for m in range(minutes):
                                for z in range(61):
                                    if(len(l_cool)>2):
                                        del l_cool[0]
                                    print(str(hours)+'hours'+str(minutes-1)+'minutes'+str(60-z)+'seconds')
                                    uuu=str(str(hours)+'hours'+str(minutes-1)+'minutes'+str(60-z)+'seconds')
                                    l_cool.append(uuu)

                                    time.sleep(1)
                                    if(list_stop[-1]=='close'):
                                        gfg1=1
                                        break

                                minutes=minutes-1
                                if(list_stop[-1]=='close'):
                                    gfg1=1
                                    break
                            if(list_stop[-1]=='close'):
                                gfg1=1
                                break
                                


                                
                        for h in range(hours):  
                            for m in range(61):
                                    for z in range(61):
                                        if(len(l_cool)>2):
                                            del l_cool[0]
                                        print(str(hours-1)+'hours'+str(60-m)+'minutes'+str(60-z)+'seconds')
                                        uuu=str(str(hours-1)+'hours'+str(60-m)+'minutes'+str(60-z)+'seconds')
                                        l_cool.append(uuu)
                                        time.sleep(1)
                                        if(list_stop[-1]=='close'):
                                            gfg1=1
                                            break


                                    minutes=minutes-1
                                    if(list_stop[-1]=='close'):
                                        gfg1=1
                                        break
                                    
                            hours=hours-1
                            if(list_stop[-1]=='close'):
                                    gfg1=1
                                    break


                        


                else:
                    print('cool')

            except:
                print("error")
            


  


    clientsocket,address=s11.accept()
    clientsocket.send(bytes("Open1!","utf-8"))

    root.mainloop()

