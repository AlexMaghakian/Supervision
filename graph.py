
from table import *
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure 
import time 
import threading 
from datetime import datetime
import matplotlib.dates as mdates


##############################graphiques##############################

continuePlotting = False 

def change_state(): 
    global continuePlotting 
    if continuePlotting == True: 
        continuePlotting = False 
    else: 
        continuePlotting = True 

##############################CLIENT 1 graph##############################
#####Graph client 1 ram-date
def data_points_client1_ram(): 

    f = open("./graph/ram_client1.txt", "r") 
    ram_file = f.readlines() 
    f.close() 
    client1_ram = []

    for i in range(len(ram_file)): 
        client1_ram.append(int(ram_file[i].rstrip("\n")))
    return client1_ram

def data_points_client1_date_ram():
    file = open("./graph/date_client1_ram.txt", "r") 
    date_file = file.readlines() 
    file.close()
    date_ram_client1 = [] 
    for z in range(len(date_file)):
        date_ram_client1.append(str(date_file[z].rstrip("\n")))
    return date_ram_client1

#####Graph client 1 swap-date
def data_points_client1_swap(): 

    f = open("./graph/swap_client1.txt", "r") 
    ram_file = f.readlines() 
    f.close() 
    swap_client1 = []

    for i in range(len(ram_file)): 
        swap_client1.append(int(ram_file[i].rstrip("\n")))
    return swap_client1

def data_points_client1_swap_date():
    file = open("./graph/date_client1_swap.txt", "r") 
    date_file = file.readlines() 
    file.close()
    date_swap_client1 = [] 
    for z in range(len(date_file)):
        date_swap_client1.append(str(date_file[z].rstrip("\n")))
    return date_swap_client1
##############################CLIENT 1 graph##############################

##############################CLIENT 2 graph##############################
#####Graph client 2 ram-date
def data_points_client2_ram(): 

    f = open("./graph/ram_client2.txt", "r") 
    ram_file = f.readlines() 
    f.close() 
    client2_ram = []

    for i in range(len(ram_file)): 
        client2_ram.append(int(ram_file[i].rstrip("\n")))
    return client2_ram

def data_points_client2_date_ram():
    file = open("./graph/date_client2_ram.txt", "r") 
    date_file = file.readlines() 
    file.close()
    date_ram_client2 = [] 
    for z in range(len(date_file)):
        date_ram_client2.append(str(date_file[z].rstrip("\n")))
    return date_ram_client2

#####Graph client 2 swap-date
def data_points_client2_swap(): 

    f = open("./graph/swap_client2.txt", "r") 
    ram_file = f.readlines() 
    f.close() 
    swap_client2 = []

    for i in range(len(ram_file)): 
        swap_client2.append(int(ram_file[i].rstrip("\n")))
    return swap_client2

def data_points_client2_swap_date():
    file = open("./graph/date_client2_swap.txt", "r") 
    date_file = file.readlines() 
    file.close()
    date_swap_client2 = [] 
    for z in range(len(date_file)):
        date_swap_client2.append(str(date_file[z].rstrip("\n")))
    return date_swap_client2

##############################CLIENT 2 graph##############################
"""
def data_points_client1_ram_y():
    tab_client1_UsedRam=create_table_client1_ram()
    countlxml_RamUsed_client1=count_client1_ram()
    y=create_table_client1_ram()
    tab_client1_UsedRam2=tab_client1_UsedRam[1:countlxml_RamUsed_client1]
    date_x = [el[1] for el in tab_client1_UsedRam2]
    return date_x

def data_points_client1_date_x():
    tab_client1_UsedRam=create_table_client1_ram()
    countlxml_RamUsed_client1=count_client1_ram()
    y=create_table_client1_ram()
    ram_y=[]
    ram_y2=[]
    tab_client1_UsedRam2=tab_client1_UsedRam[1:countlxml_RamUsed_client1]
    print(tab_client1_UsedRam2)
    for z in range(tab_client1_UsedRam2):
        ram_y2 = [el[2] for el in tab_client1_UsedRam2]
        ram_y.append(int(ram_y2[z].rstrip("\n")))
    return ram_y
""" 


def app(): 
    # initialise a window. 
    root = Tk() 
    root.config(background='white') 
    root.geometry("1300x550") 
     
    lab = Label(root, text="Live Plotting", bg = 'white').pack() 
     
    fig = Figure() 
     
    ax = fig.add_subplot(111) 
    ax.set_xlabel("date") 
    ax.set_ylabel("Ram utilisé") 
    ax.grid() 
    graph = FigureCanvasTkAgg(fig, master=root) 
    graph.get_tk_widget().pack(side="top",fill='both',expand=True) 
 
    def plotter(): 
        while continuePlotting: 
            ax.cla() 
            ax.grid() 
            X = data_points_client1_date_ram()
            Y = data_points_client1_ram()
            #ax.set_xticks(data_points_client1_date_x) # Tickmark + label at every plotted point
            #ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax.plot(X, Y, marker='o', color='orange') 
            ax.tick_params(axis='x', labelsize=8)
            plt.plot(range(0, 500))
            ax.set_xlabel("date") 
            ax.set_ylabel("RAM utilisé")
            graph.draw() 
            time.sleep(1) 
 
    def gui_handler(): 
        change_state() 
        threading.Thread(target=plotter).start() 

    def stop_thread():
        change_state()
        root.destroy()

    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    c = Button(root, text="Close", command=stop_thread, bg="red", fg="white")
    b.pack()
    c.pack()
     
    root.mainloop() 

def app2(): 
    # initialise a window.
    root = Tk() 
    root.config(background='white') 
    root.geometry("1300x550") 
     
    lab = Label(root, text="Live Plotting", bg = 'white').pack() 
     
    fig = Figure() 
     
    ax2 = fig.add_subplot(111) 
    ax2.set_xlabel("date") 
    ax2.set_ylabel("swap utilisé") 
    ax2.grid() 
    graph = FigureCanvasTkAgg(fig, master=root) 
    graph.get_tk_widget().pack(side="top",fill='both',expand=True) 
 
    def plotter(): 
        while continuePlotting: 
            ax2.cla() 
            ax2.grid() 
            X = data_points_client1_swap_date()
            Y = data_points_client1_swap()
            #ax.set_xticks(data_points_client1_date_x) # Tickmark + label at every plotted point
            #ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax2.plot(X, Y, marker='o', color='orange')
            ax2.tick_params(axis='x', labelsize=8)
            ax2.set_xlabel("date") 
            ax2.set_ylabel("swap utilisé")
            graph.draw() 
            time.sleep(1) 
 
    def gui_handler(): 
        change_state()
        threading.Thread(target=plotter).start()

    def stop_thread():
        change_state()
        root.destroy()
 
    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    c = Button(root, text="Close", command=stop_thread, bg="red", fg="white")
    b.pack()
    c.pack()  
     
    root.mainloop()

def app3(): 
    # initialise a window.
    root = Tk() 
    root.config(background='white') 
    root.geometry("1300x550") 
     
    lab = Label(root, text="Live Plotting", bg = 'white').pack() 
     
    fig = Figure() 
     
    ax3 = fig.add_subplot(111) 
    ax3.set_xlabel("date") 
    ax3.set_ylabel("swap utilisé") 
    ax3.grid() 
    graph = FigureCanvasTkAgg(fig, master=root) 
    graph.get_tk_widget().pack(side="top",fill='both',expand=True) 
 
    def plotter(): 
        while continuePlotting: 
            ax3.cla() 
            ax3.grid() 
            X = data_points_client2_date_ram()
            Y = data_points_client2_ram()
            #ax.set_xticks(data_points_client1_date_x) # Tickmark + label at every plotted point
            #ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax3.plot(X, Y, marker='o', color='orange')
            ax3.tick_params(axis='x', labelsize=8) 
            ax3.set_xlabel("date") 
            ax3.set_ylabel("ram utilisé")
            graph.draw() 
            time.sleep(1) 
 
    def gui_handler(): 
        change_state()
        threading.Thread(target=plotter).start()

    def stop_thread():
        change_state()
        root.destroy()
 
    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    c = Button(root, text="Close", command=stop_thread, bg="red", fg="white")
    b.pack()
    c.pack()  
     
    root.mainloop()

def app4(): 
    # initialise a window.
    root = Tk() 
    root.config(background='white') 
    root.geometry("1300x550") 
     
    lab = Label(root, text="Live Plotting", bg = 'white').pack() 
     
    fig = Figure() 
     
    ax4 = fig.add_subplot(111) 
    ax4.set_xlabel("date") 
    ax4.set_ylabel("swap utilisé") 
    ax4.grid() 
    graph = FigureCanvasTkAgg(fig, master=root) 
    graph.get_tk_widget().pack(side="top",fill='both',expand=True) 
 
    def plotter(): 
        while continuePlotting: 
            ax4.cla() 
            ax4.grid() 
            X = data_points_client2_swap_date()
            Y = data_points_client2_swap()
            #ax.set_xticks(data_points_client1_date_x) # Tickmark + label at every plotted point
            #ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax4.plot(X, Y, marker='o', color='orange')
            ax4.tick_params(axis='x', labelsize=8)
            ax4.set_xlabel("date") 
            ax4.set_ylabel("swap utilisé")
            graph.draw() 
            time.sleep(1) 
 
    def gui_handler(): 
        change_state()
        threading.Thread(target=plotter).start()

    def stop_thread():
        change_state()
        root.destroy()
 
    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    c = Button(root, text="Close", command=stop_thread, bg="red", fg="white")
    b.pack()
    c.pack()  
     
    root.mainloop()