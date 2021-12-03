from tkinter import *
import xml.etree.ElementTree as ET
from graph import *
from parseur import *
from table import *
from count import *
from tkinter.ttk import *
from collections import Counter

import lxml.etree
#paquet installés:
#C:\Users\Alex\AppData\Local\Programs\Python\Python310\python.exe -m pip install --upgrade pip
#lxml==4.6.3
#matplotlib==3.4.3
#pyparsing==2.4.7
#pyttk==0.3.2

#fonction créer la base du tableau 

def refresh(self):
    self.destroy()

def Refresh():
    list = root.grid_slaves()
    for l in list:
        l.destroy()

def swap():
    general2()

def ram():
     general()


def menu():
    menubar = Menu(root)
    root.config(menu=menubar)
    countlxml_Server_ram=count()
    countlxml_Server_swap=count2()
    tab_Server=parse_Server()

    menufichier = Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_command(label="Ouvrir ")
    menufichier.add_command(label="Enregistrer")
    menufichier.add_command(label="Quitter", command = Close)

    Client1= Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
    menubar.add_cascade(label="Client1", menu=Client1)
    Client1_Trier = Menu(menubar, tearoff=0)
    Client1_Trier.add_command(label="RAM", command = general_trier_ram_client1)
    Client1_Trier.add_command(label="SWAP", command = general_trier_swap_client1)
    Client1.add_cascade(label="Trier", underline=0, menu=Client1_Trier)
    Client1.add_separator()
    Client1_graphiques = Menu(menubar, tearoff=0)
    Client1_graphiques.add_command(label="RAM", command = app)
    Client1_graphiques.add_command(label="SWAP", command = app2)
    Client1.add_cascade(label="Graphiques", underline=0, menu=Client1_graphiques)
    Client1.add_separator()
    
    Client2= Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
    menubar.add_cascade(label="Client2", menu=Client2)
    Client2_Trier = Menu(menubar, tearoff=0)
    Client2_Trier.add_command(label="RAM", command = general_trier_ram_client2)
    Client2_Trier.add_command(label="SWAP", command = general_trier_swap_client2)
    Client2.add_cascade(label="Trier", underline=0, menu=Client2_Trier)
    Client2.add_separator()
    Client2_graphiques = Menu(menubar, tearoff=0)
    Client2_graphiques.add_command(label="RAM", command = app3)
    Client2_graphiques.add_command(label="SWAP", command = app4)
    Client2.add_cascade(label="Graphiques", underline=0, menu=Client2_graphiques)

    Clients= Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
    menubar.add_cascade(label="Tous les Clients", menu=Clients)
    Clients.add_command(label="RAM", command = general)
    Clients.add_command(label="SWAP", command = general2)
    Client2.add_separator()

    refresh = Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='green',activeborderwidth=0,font=("Verdana", 12))
    menubar.add_cascade(label="Refresh", command = Refresh)


def general():
    lst=create_table()
    countlxml_TotalRam=count()
    total_rows = countlxml_TotalRam
    total_columns = 5
    for i in range(total_rows):        
        for j in range(total_columns):
            #widget Entry                   
            entry = Entry(root, width=30,font=('Arial',12,'bold'))
            #grid()méthode à laquelle nous pouvons passer des positions de ligne et de colonne
            entry.grid(row=i, column=j)
            entry.insert(END, lst[i][j])

def general2(): 
    lst_swap=create_table2()
    countlxml_SwapSize=count2()
    total_rows_swap = countlxml_SwapSize
    total_columns_swap = 4  
    for y in range(total_rows_swap):        
        for z in range(total_columns_swap):                   
            entry2 = Entry(root, width=30,font=('Arial',12,'bold')) 
            entry2.grid(row=y, column=z)
            entry2.insert(END, lst_swap[y][z]) 

def general_trier_ram_client1():
    lst_ram_client1=create_table_client1_ram()
    #print('lst_swap_client1',lst_swap_client1)
    countlxml_ramUsage_client1=count_client1_ram()
    #count_rows_trier_ram=create_table_trier_ram()
    total_rows_client1_ram=countlxml_ramUsage_client1
    #print('total_rows_client1_swap',total_rows_client1_swap)
    #total_rows = taille_tab_Server_client1
    total_columns = 5
    for c in range(total_rows_client1_ram):  
        for d in range(total_columns):                  
            entry_ram_client1 = Entry(root, width=30,font=('Arial',12,'bold'))
            entry_ram_client1.grid(row=c, column=d)
            entry_ram_client1.insert(END, lst_ram_client1[c][d])

def general_trier_swap_client1():
    lst_swap_client1=create_table_client1_swap()
    #print('lst_swap_client1',lst_swap_client1)
    countlxml_SwapUsage_client1=count_client1_swap()
    #count_rows_trier_ram=create_table_trier_ram()
    total_rows_client1_swap=countlxml_SwapUsage_client1
    #print('total_rows_client1_swap',total_rows_client1_swap)
    #total_rows = taille_tab_Server_client1
    total_columns = 4
    for a in range(total_rows_client1_swap):  
        for b in range(total_columns):                  
            entry_swap_client1 = Entry(root, width=30,font=('Arial',12,'bold'))
            entry_swap_client1.grid(row=a, column=b)
            entry_swap_client1.insert(END, lst_swap_client1[a][b])


def general_trier_ram_client2():
    lst_ram_client2=create_table_client2_ram()
    #print('lst_swap_client2',lst_swap_client2)
    countlxml_ramUsage_client2=count_client2_ram()
    #count_rows_trier_ram=create_table_trier_ram()
    total_rows_client2_ram=countlxml_ramUsage_client2
    #print('total_rows_client2_swap',total_rows_client2_swap)
    #total_rows = taille_tab_Server_client2
    total_columns = 5
    for c in range(total_rows_client2_ram):  
        for d in range(total_columns):                  
            entry_ram_client2 = Entry(root, width=30,font=('Arial',12,'bold'))
            entry_ram_client2.grid(row=c, column=d)
            entry_ram_client2.insert(END, lst_ram_client2[c][d])

def general_trier_swap_client2():
    lst_swap_client2=create_table_client2_swap()
    #print('lst_swap_client2',lst_swap_client2)
    countlxml_SwapUsage_client2=count_client2_swap()
    #count_rows_trier_ram=create_table_trier_ram()
    total_rows_client2_swap=countlxml_SwapUsage_client2
    #print('total_rows_client2_swap',total_rows_client2_swap)
    #total_rows = taille_tab_Server_client2
    total_columns = 4
    for a in range(total_rows_client2_swap):  
        for b in range(total_columns):                  
            entry_swap_client2 = Entry(root, width=30,font=('Arial',12,'bold'))
            entry_swap_client2.grid(row=a, column=b)
            entry_swap_client2.insert(END, lst_swap_client2[a][b])
###########fonction pour le bouton quitter###########
def Close():
    root.destroy()
###########fonction pour le bouton quitter###########
##############################graphiques##############################

root = Tk()
root.title('αMonitoring ADMIN')
menu()
general()
#general_trier_ram()
#general2()
#general2()
root.mainloop()
