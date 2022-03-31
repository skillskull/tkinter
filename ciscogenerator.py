#
#Cisco Code Generator
#Powered by: Rodrigo Noriega
#V 1.0
#09-December-2020
#
#

import os
import re
import socket
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Getting current Directory
current_direct = os.getcwd()

#Generating a list to validate a subnetmask            
netmask = ["128.0.0.0","192.0.0.0","224.0.0.0","240.0.0.0",
           "248.0.0.0","252.0.0.0","254.0.0.0","255.0.0.0",
           "255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0",
           "255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0",
           "255.255.128.0","255.255.192.0","255.255.224.0","255.255.240.0",
           "255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0",
           "255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240",
           "255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255"
           ]

# Define a function for validate an Ip addess 
def checkIP():  

    checkIP = dataIn_IPAdd.get()
    try:
        socket.inet_aton(checkIP)
        print("Valid IP")
    except socket.error:
        print("Invalid IP")

#Define a function for validate a Subnet Mask
def checkMask():
    
    checkMask = dataIn_IPMask.get()

    for x in netmask:
        if (x == checkMask):
            print("Valid Subnet Mask")
   
def GetData_Frame1():
    #Se define una concatenación del widget con la variable
    my_frame1.gettingData1 = dataIn_hostname.get()
    print(my_frame1.gettingData1)
    my_frame1.gettingData2 = dataIn_lineconepass.get()
    print(my_frame1.gettingData2)
    my_frame1.gettingData3 = dataIn_Execpass.get()
    print(my_frame1.gettingData3)
    my_frame1.gettingData4 = dataIn_linevtypass.get()
    print(my_frame1.gettingData4)
    my_frame1.gettingData5 = dataIn_bannerod.get()
    print(my_frame1.gettingData5)
    my_frame1.gettingData6 = dataIn_scriptname.get()
    print(my_frame1.gettingData6)
    archivo = open(my_frame1.gettingData6 + '.txt', 'w')
    archivo.write('!\nenable\n')
    archivo.write('configure terminal\n')
    archivo.write('hostname ' + my_frame1.gettingData1 + '\n!\n')
    archivo.write('line console 0\npassword ' + my_frame1.gettingData2 + '\nlogin\nexit\n!\n')
    archivo.write('enable secret ' + my_frame1.gettingData3 + '\n!\n')
    archivo.write('line vty 0 15\npassword ' + my_frame1.gettingData4 + '\nlogin\nexit\n!\n')
    archivo.write('banner motd #' + my_frame1.gettingData5 + '#\n!\n')
    archivo.close()
    messagebox.showinfo("Info", "Code generated successfully\n\nYou can find your file configuration at:\n\n" + current_direct)
    
def GetData_Frame2():
    checkIP()
    checkMask()
    messagebox.showinfo("Info", "Code generated successfully\n\nYou can find your file configuration at:\n\n" + current_direct)

def GetData_Frame3():
    messagebox.showinfo("Info", "Code generated successfully\n\nYou can find your file configuration at:\n\n" + current_direct)
    
root = Tk()
root.geometry("370x350")
root.resizable(0,0)

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook, width=345, height=410, bg="white", pady=10)
my_frame2 = Frame(my_notebook, width=345, height=410, bg="white", pady=10)
my_frame3 = Frame(my_notebook, width=345, height=410, bg="white", pady=10)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)
my_frame3.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Basic.conf")
my_notebook.add(my_frame2, text="L2")
my_notebook.add(my_frame3, text="L3")

generateButton_Frame1 = Button(my_frame1, text="Generate Code!", command=GetData_Frame1)
generateButton_Frame2 = Button(my_frame2, text="Generate Code!", command=GetData_Frame2)
generateButton_Frame3 = Button(my_frame3, text="Generate Code!", command=GetData_Frame3)

#Cretaing for frame1

Label_hostname = Label(my_frame1, text="Hostname", bg="white").grid(row=1, column=0, pady=5, padx=10)
dataIn_hostname = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)
Label_lineconepass = Label(my_frame1, text="line console 0 password", bg="white").grid(row=2, column=0, pady=5, padx=20)
dataIn_lineconepass = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)
Label_Execepass = Label(my_frame1, text="EXEC access password", bg="white").grid(row=3, column=0, pady=5, padx=20)
dataIn_Execpass = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)
Label_linevtypass = Label(my_frame1, text="Line vty 0 15 password", bg="white").grid(row=4, column=0, pady=5, padx=20)
dataIn_linevtypass = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)
Label_bannerod = Label(my_frame1, text="Banner of the day", bg="white").grid(row=5, column=0, pady=5, padx=20)
dataIn_bannerod = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)
Label_scriptname = Label(my_frame1, text="Configuration file name", bg="white").grid(row=6, column=0, pady=5, padx=20)
dataIn_scriptname = Entry(my_frame1, width=25, selectborderwidth=2, bd=2)

#Creating into frame2

Label_SVIconf = Label(my_frame2, text = "SVI Configuration", bg = "white").grid(row = 0 , column = 0, columnspan = 2)
Label_ifvVLAN = Label(my_frame2, text = "number of VLAN", bg="white").grid(row = 1, column = 0, pady = 5, padx = 10)
dataIn_ifVLAN = Entry(my_frame2, width=25, selectborderwidth=2, bd=2)
Label_IPAdd = Label(my_frame2, text = "IPv4 Address", bg="white").grid(row = 2, column = 0, pady = 5, padx = 10)
dataIn_IPAdd = Entry(my_frame2, width=25, selectborderwidth=2, bd=2)
Label_IPMask = Label(my_frame2, text = "IPv4 Subnet Mask", bg="white").grid(row = 3, column = 0, pady = 5, padx = 10)
dataIn_IPMask = Entry(my_frame2, width=25, selectborderwidth=2, bd=2)
Label_IPGate = Label(my_frame2, text = "IPv4 Default Gateway", bg="white").grid(row = 4, column = 0, pady = 5, padx = 10)
dataIn_IPGate = Entry(my_frame2, width=25, selectborderwidth=2, bd=2)

#Creating into frame3

Label_ifvVLAN = Label(my_frame3, text = "Test", bg="white").grid(row = 1, column = 0, pady = 5, padx = 10)
dataIn_test = Entry(my_frame3, width=25, selectborderwidth=2, bd=2)

#Shoving into frame1

dataIn_hostname.grid(row=1, column=1, padx=10)
dataIn_lineconepass.grid(row=2, column=1, padx=10)
dataIn_Execpass.grid(row=3, column=1, padx=10)
dataIn_linevtypass.grid(row=4, column=1, padx=10)
dataIn_bannerod.grid(row=5, column=1, padx=10)
dataIn_scriptname.grid(row=6, column=1, padx=10)
generateButton_Frame1.grid(row=7, column=1, pady=20)

#Shoving into frame2

dataIn_ifVLAN.grid(row = 1, column = 1, padx = 10)
dataIn_IPAdd.grid(row = 2, column = 1, padx = 10)
dataIn_IPMask.grid(row = 3, column = 1, padx = 10)
dataIn_IPGate.grid(row = 4, column = 1, padx = 10)
generateButton_Frame2.grid(row = 7, column = 1)

#Shoving into frame 3
dataIn_test.grid(row = 1, column = 1, padx = 10)
generateButton_Frame3.grid(row = 7, column = 1)

#Shoving into root
closeButton = Button(root, text="Close", width=10, command=root.destroy).pack(side=RIGHT, padx=10)

root.mainloop()