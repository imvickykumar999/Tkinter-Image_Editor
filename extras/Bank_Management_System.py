
from tkinter import *
from tkinter import messagebox

class Transaction:
    global acc_no_entry
    global name_entry
    global id_entry
    global balance_entry
    global mobileno_entry

    def __init__(self,master):
        self.accounts={}
        self.master=master
        self.current_balance=0
        self.master.title("Banking Management System")
        self.master.geometry('500x500')

        self.master['background'] = '#58F'
        self.master.attributes('-fullscreen', True)
        self.master.bind("<Escape>",lambda even:self.master.destroy())
        
    def login(self):
        name=Label(text="Customer Name")
        user_name=Entry(self.master)
        password=Label(text="Password")
        user_password=Entry(self.master,show="*")

        name.grid(row=0,column=0,padx=20,pady=10)
        password.grid(row=1,column=0,padx=20,pady=10)
        user_name.grid(row=0,column=1,padx=20,pady=10)
        user_password.grid(row=1,column=1,padx=20,pady=10)

        submit=Button(self.master,text="Submit",bg = "yellow",command=self.main_page)
        submit.grid(row=2,column=4) 
        self.master.mainloop() 
            
    def main_page(self):
        self.master1=Toplevel(self.master)
        self.master1.geometry('500x500')
        self.master1['background'] = '#58F'

        self.master1.title("Main Window")
        self.master1.resizable(False,False)
        self.master1.attributes('-fullscreen', True)
        self.master1.bind("<Escape>",lambda even:self.master.destroy())

        create_Account=Button(self.master1,text="Create Account",bg = "yellow",command=self.creating_account)
        Withdraw_Amount=Button(self.master1,text="Withdraw Amount",bg = "yellow",command=self.withdrawl)
        Deposit_Amount=Button(self.master1,text="Deposit Amount",bg = "yellow",command=self.deposit)
        Transfer_Amount=Button(self.master1,text="Transfer Amount",bg = "yellow",command=self.transfer)
        Account_Details=Button(self.master1,text="Account Details",bg = "yellow",command=self.details)
        
        create_Account.grid(row=0,column=0,pady=50,padx=70)
        Withdraw_Amount.grid(row=0,column=1,pady=50)
        Transfer_Amount.grid(row=1,column=0,pady=50,padx=70)
        Deposit_Amount.grid(row=1,column=1)
        Account_Details.grid(row=2,column=0,pady=40)
        self.master1.mainloop()

    def creating_account(self):
        self.v = StringVar()
        self.master2=Toplevel(self.master)
        self.master2.geometry('500x500')
        self.master2['background'] = '#58F'

        self.master2.title("Create Account")
        self.master2.resizable(False,False)
        self.master2.attributes('-fullscreen', True)
        self.master2.bind("<Escape>",lambda even:self.master.destroy())
        
        self.name=Label(self.master2,text="Customer Name:")
        self.id=Label(self.master2,text="Customer ID:")
        self.mno=Label(self.master2,text="Customer Mobile No:")
        self.acc_no=Label(self.master2,text="Account No:")
        self.balance=Label(self.master2,text="Balance:")

        self.name_entry=Entry(self.master2,textvariable=self.v)
        self.id_entry=Entry(self.master2)
        self.mobileno_entry=Entry(self.master2)
        self.acc_no_entry=Entry(self.master2)
        self.balance_entry=Entry(self.master2)

        self.name_entry.grid(row=0,column=1,padx=10,pady=5)
        self.id_entry.grid(row=1,column=1,padx=10,pady=5)
        self.mobileno_entry.grid(row=2,column=1,padx=10,pady=5)
        self.acc_no_entry.grid(row=3,column=1,padx=10,pady=5)
        self.balance_entry.grid(row=4,column=1,padx=10,pady=5)
        self.name.grid(row=0,column=0,padx=10,pady=5)
        self.id.grid(row=1,column=0,padx=10,pady=5)
        self.mno.grid(row=2,column=0,padx=10,pady=5)
        self.acc_no.grid(row=3,column=0,padx=10,pady=5)
        self.balance.grid(row=4,column=0,padx=10,pady=5)

        submit=Button(self.master2,text="Submit",bg = "yellow",command=lambda:messagebox.showinfo("information","Account Created Successfully"))
        submit.grid(row=5,column=1,padx=10,pady=10)
        self.master2.mainloop()
        
    def calculate_withdrawl(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry

        if float(self.accounts['amount_entry']) > self.current_balance:
            print("Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")
    
    def withdrawl(self):
        self.master3=Toplevel(self.master)
        self.master3.geometry('500x500')
        self.master3['background'] = '#58F'

        self.master3.title("Create Withdrawl")
        self.master3.resizable(False,False)
        self.master3.attributes('-fullscreen', True)
        self.master3.bind("<Escape>",lambda even:self.master.destroy())     

        acc_no_label=Label(self.master3,text="Enter Your Account No:")
        amount_label=Label(self.master3,text="Enter Your Amount:")

        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)

        acc_no_entry=Entry(self.master3)
        amount_entry=Entry(self.master3)

        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)

        # submit=Button(self.master3,text="Submit",command=lambda:messagebox.showinfo("information","Amount Withdrawl Successfully"))
        submit=Button(self.master3,text="Submit",bg = "yellow",command=lambda: self.calculate_withdrawl(acc_no_entry, amount_entry))
        submit.grid(row=2,column=1,padx=10,pady=10)
        self.master3.mainloop() 
    
    def calculate_deposit(self, acc_no_entry, amount_entry):
        # get the data from the Entry widget
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        
        # add the data to the set
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry

        self.current_balance += float(self.accounts['amount_entry'])
        print(f"{float(self.accounts['amount_entry'])} deposited into account {float(self.accounts['acc_no_entry'])}. New balance: {self.current_balance}")


    def deposit(self):
        self.master4=Toplevel(self.master)
        self.master4.geometry('500x500')
        self.master4['background'] = '#58F'

        self.master4.title("Create deposited")
        self.master4.resizable(False,False)
        self.master4.attributes('-fullscreen', True)
        self.master4.bind("<Escape>",lambda even:self.master.destroy())

        acc_no_label=Label(self.master4,text="Enter Your Account No:")
        amount_label=Label(self.master4,text="Enter Your Amount:")

        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)

        acc_no_entry=Entry(self.master4)
        amount_entry=Entry(self.master4)

        acc_no_entry.grid(row=0,column=1,padx=50,pady=10)
        amount_entry.grid(row=1,column=1,padx=50,pady=10)

        # submit=Button(self.master4,text="Submit",command=lambda:messagebox.showinfo("information","Amount deposited Successfully"))
        submit=Button(self.master4,text="Submit",bg = "yellow",command=lambda: self.calculate_deposit(acc_no_entry, amount_entry))
        submit.grid(row=2,column=1,padx=10,pady=10)        
        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)
        self.master4.mainloop()

    def calculate_transfer(self, acc_no_entry, amount_entry):
        acc_no_entry = acc_no_entry.get()
        amount_entry = amount_entry.get()
        
        self.accounts['acc_no_entry'] = acc_no_entry
        self.accounts['amount_entry'] = amount_entry

        if float(self.accounts['amount_entry']) > self.current_balance:
            print("Insufficient balance!")
        else:
            self.current_balance -= float(self.accounts['amount_entry'])
            print(f"{float(self.accounts['amount_entry'])} withdrawn from account {self.accounts['acc_no_entry']}. New balance: {self.current_balance}")

    def transfer(self):
        self.master5=Toplevel(self.master)
        self.master5.geometry('500x500')
        self.master5['background'] = '#58F'

        self.master5.title("create transfer")
        self.master5.resizable(False,False)
        self.master5.attributes('-fullscreen', True)
        self.master5.bind("<Escape>",lambda even:self.master.destroy())

        sender_acc_label=Label(self.master5,text="Enter Sender Account No:")
        rece_acc_label=Label(self.master5,text="Enter Receiver Account No:")
        money_label=Label(self.master5,text="Enter Amount:")

        sender_acc_label.grid(row=0,column=0,padx=50,pady=10)
        rece_acc_label.grid(row=1,column=0,padx=50,pady=10)
        money_label.grid(row=2,column=0,padx=50,pady=10)

        sender_acc_entry=Entry(self.master5)
        rece_acc_entry=Entry(self.master5)
        money_entry=Entry(self.master5)

        sender_acc_entry.grid(row=0,column=1,padx=10,pady=10)
        rece_acc_entry.grid(row=1,column=1,padx=10,pady=10)
        money_entry.grid(row=2,column=1,padx=10,pady=10)

        submit=Button(self.master5,text="Submit",bg = "yellow",command=lambda: self.calculate_transfer(sender_acc_entry, money_entry))
        submit.grid(row=3,column=1,padx=10,pady=10)
        self.master5.mainloop()

    def details(self):
        self.master6=Toplevel(self.master)
        self.master6.geometry('500x500')
        self.master6['background'] = '#58F'

        self.master6.title("Create details")
        self.master6.resizable(False,False)
        self.master6.attributes('-fullscreen', True)
        self.master6.bind("<Escape>",lambda even:self.master.destroy())
        
        detail=Button(self.master6, text= "Details",width= 20,bg = "yellow",command=self.display_text)
        detail.pack()

    def display_text(self):
        self.master7=Toplevel(self.master)
        self.master7.geometry('500x500')
        self.master7['background'] = '#58F'

        self.master7.title("details")
        self.master7.resizable(False,False)
        self.master7.attributes('-fullscreen', True)
        self.master7.bind("<Escape>",lambda even:self.master.destroy())

        label1=Label(self.master7, text="", font=("Courier 22 bold"))
        label1.grid(row=0,column=1,padx=10,pady=10)
        label2=Label(self.master7, text="", font=("Courier 22 bold"))
        label2.grid(row=1,column=1,padx=10,pady=10)
        label3=Label(self.master7, text="", font=("Courier 22 bold"))
        label3.grid(row=2,column=1,padx=10,pady=10)
        label4=Label(self.master7, text="", font=("Courier 22 bold"))
        label4.grid(row=3,column=1,padx=10,pady=10)
        label5=Label(self.master7, text="", font=("Courier 22 bold"))
        label5.grid(row=4,column=1,padx=10,pady=10)

        Label(self.master7, text="Account Number=", font=("Courier 22 bold")).grid(row=0,column=0,padx=10,pady=10)
        Label(self.master7, text="Customer Name=", font=("Courier 22 bold")).grid(row=1,column=0,padx=10,pady=10)
        Label(self.master7, text="Customer ID=", font=("Courier 22 bold")).grid(row=2,column=0,padx=10,pady=10)
        Label(self.master7, text="Customer Mobile No=", font=("Courier 22 bold")).grid(row=3,column=0,padx=10,pady=10)
        Label(self.master7, text="Balance=", font=("Courier 22 bold")).grid(row=4,column=0,padx=10,pady=10)
        
        acc=self.acc_no_entry.get()
        name=self.name_entry.get()
        id=self.id_entry.get()
        mno=self.mobileno_entry.get()

        label1.configure(text=acc)
        label2.configure(text=name)
        label3.configure(text=id)
        label4.configure(text=mno)
        label5.configure(text=self.current_balance)

        self.master7.mainloop()
        

def main():
    root=Tk()
    app=Transaction(root)
    root.title("phoneBook")

    window_height = 500
    window_width = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    root.resizable(False,False)
    app.login()
    root.mainloop()
       
if __name__=='__main__':
    main()
