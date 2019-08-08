import tkinter as tk
from ManagerFrame import ManagerFrame

class LoginFrame(tk.Frame):
    def __init__(self, lokr_object):
        self.lokr = lokr_object
        tk.Frame.__init__(self, self.lokr)
        self.ex = tk.Button(self, text = 'Exit', command=quit)
        self.logolbl = tk.Label(self, text= '\n', image=self.lokr.logo, pady = 50)
        self.title = tk.Label(self, text="Lokr",  font =('Lucida Console', 40))
        self.logtitle = tk.Label(self, text="\nVersion: " + str(self.lokr.ver) + "\n\nPlease Login:")
        self.usr = tk.Entry(self)
        self.pas = tk.Entry(self, show='*')
        self.usrl = tk.Label(self, text='Username:')
        self.pasl = tk.Label(self, text='Password:')
        self.login = tk.Button(self, text='Launch', command=self.checkUser)
        self.newusr = tk.Button(self, text = 'Register', command=self.newUserPrompt)
        self.clear = tk.Button(self, text = 'Clear', command=self.clearFields)
        self.confirm = tk.Label(self)
        # TODO: split this into another method
        self.logolbl.pack()
        self.title.pack()
        self.logtitle.pack()
        self.usrl.pack()
        self.usr.pack()
        self.pasl.pack()
        self.pas.pack()
        self.login.pack()
        self.newusr.pack()
        self.clear.pack()
        self.confirm.pack()
        self.bind("<Return>", self.checkUser) 
        self.pack()
        
    def checkUser(self, event=None):
        if (self.usr.get() in self.lokr.readUsersFile()) == True and self.lokr.authenticate(self.usr.get(), self.pas.get()) == True:
            # usrname = str(usr.get())
            self.confirm.config(text='You have successfully logged on!' )
            self.lokr.setUserLokrFile(self.usr.get())
            self.usr.delete(0, tk.END)
            self.pas.delete(0, tk.END)
            self.logolbl.pack_forget()
            self.title.pack_forget()
            self.logtitle.pack_forget()
            self.usrl.pack_forget()
            self.usr.pack_forget()
            self.pasl.pack_forget()
            self.pas.pack_forget()
            self.login.pack_forget()
            self.newusr.pack_forget()
            self.clear.pack_forget()
            self.confirm.pack_forget()
            self.unbind("<Return>")
            self.lokr.title('LOKR MANAGER')
            self.pack_forget()
            ManagerFrame(self.lokr)
        else:
            self.confirm.config(text='Your username and/or password is incorrect.' )
            self.usr.delete(0, tk.END)
            self.pas.delete(0, tk.END)

    def clearFields(self):
        self.usr.delete(0, tk.END)
        self.pas.delete(0, tk.END)
        self.confirm.config(text=' ' )

    def newUserPrompt(self):
        #shows prompts to create new user and create new SL locker
        self.newusrl = tk.Label(self, text='Create a username:')
        self.newusrl.pack()
        self.newusr = tk.Entry(self)
        self.newusr.pack()
        self.newpasl = tk.Label(self, text='Create a password:')
        self.newpasl.pack()
        self.newpas = tk.Entry(self, show='*')
        self.newpas.pack()
        self.newconl = tk.Label(self, text='Confirm password:')
        self.newconl.pack()
        self.newcon = tk.Entry(self, show='*')
        self.newcon.pack()
        self.unbind("<Return>")
        self.register_button = tk.Button(self, text="Register!", command=self.register)
        self.register_button.pack(expand = True)
    
    def register(self):
        #makes sure no two usr names are same, creates locker and displays success lbl
        if (self.newusr.get() in self.lokr.readUsersFile()) == False and self.newpas.get() == self.newcon.get():
            self.lokr.saveUser(self.newusr.get(), self.newpas.get())
            self.lokr.createLokr(self.newusr.get())
            self.confirm.config(text='You have successfully registered!\n A new Lokr has been created for you.')
            self.newusrl.pack_forget()
            self.newusr.pack_forget()
            self.newpasl.pack_forget()
            self.newpas.pack_forget()
            self.newconl.pack_forget()
            self.newcon.pack_forget()
            self.register_button.pack_forget()
            self.bind("<Return>")
        else:
            self.confirm.config(text='Username already exists or passwords do not match. Please retry.')
            self.bind("<Return>", self.checkUser)