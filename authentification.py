from tkinter import *
from functools import partial

def validateLogin(username, password):
        username=username.get()
        password=password.get()
        if (username == "alex" and password == "alex"):
                tkWindow.destroy()
                print("ok")
                import afficheur_root as run
                run.foo()
        else:
                tkWindow.destroy()
                print("nok")
                import afficheur_user as run2
                run2.foo()

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Authentification')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)


tkWindow.mainloop()