
from tkinter import *
accounts = {}


class Transaction:
    def insert_data():
        global accounts
        print(accounts, end='\n\n')        

    def main_page():
        global accounts

        main_window=Toplevel(root)
        main_window.geometry('400x400')
        main_window.title("Main Window")
        main_window.resizable(False,False)

        create_Account=Button(main_window,text="Create Account",command=Transaction.creating_account)
        Withdraw_Amount=Button(main_window,text="Withdraw Amount",command=Transaction.withdrawl)
        Deposit_Amount=Button(main_window,text="Deposit Amount",command=Transaction.deposit)
        Transfer_Amount=Button(main_window,text="Transfer Amount",command=Transaction.transfer)
        Account_Details=Button(main_window,text="Account Details",command=Transaction.details)

        create_Account.grid(row=0,column=0,pady=50,padx=70)
        Withdraw_Amount.grid(row=0,column=1,pady=50)
        Transfer_Amount.grid(row=1,column=0,pady=50,padx=70)
        Deposit_Amount.grid(row=1,column=1)
        Account_Details.grid(row=2,column=0,pady=40)


    def creating_account():
        global accounts

        creating_account_window=Toplevel(root)
        creating_account_window.geometry('400x400')
        creating_account_window.title("Create Account")
        creating_account_window.resizable(False,False)

        name=Label(creating_account_window,text="Customer Name:")
        id=Label(creating_account_window,text="Customer ID:")
        mno=Label(creating_account_window,text="Customer Mobile No:")
        acc_no=Label(creating_account_window,text="Account No:")

        name_entry=Entry(creating_account_window)
        accounts['name_entry'] = name_entry.get()
        id_entry=Entry(creating_account_window)
        accounts['id_entry'] = id_entry.get()
        mobileno_entry=Entry(creating_account_window)
        accounts['mobileno_entry'] = mobileno_entry.get()
        acc_no_entry=Entry(creating_account_window)
        accounts['acc_no_entry'] = acc_no_entry.get()

        name_entry.grid(row=0,column=1,padx=10,pady=10)
        id_entry.grid(row=1,column=1,padx=10,pady=10)
        mobileno_entry.grid(row=2,column=1,padx=10,pady=10)
        acc_no_entry.grid(row=3,column=1,padx=10,pady=10)
        name.grid(row=0,column=0,padx=50,pady=10)
        id.grid(row=1,column=0,padx=50,pady=10)
        mno.grid(row=2,column=0,padx=50,pady=10)
        acc_no.grid(row=3,column=0,padx=50,pady=10)

        submit=Button(creating_account_window,text="Submit",command=Transaction.insert_data)
        submit.grid(row=4,column=1,padx=10,pady=10)
        acc_no=acc_no_entry.get()
        

    def withdrawl():
        global accounts

        creating_withdrawl_window=Toplevel(root)
        creating_withdrawl_window.geometry('400x400')
        creating_withdrawl_window.title("Create Withdrawl")
        creating_withdrawl_window.resizable(False,False)

        acc_no_label=Label(creating_withdrawl_window,text="Enter Your Account No:")
        amount_label=Label(creating_withdrawl_window,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)

        acc_no_entry=Entry(creating_withdrawl_window)
        accounts['acc_no_entry'] = acc_no_entry.get()
        amount_entry=Entry(creating_withdrawl_window)
        accounts['amount_entry'] = amount_entry.get()

        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)

        submit=Button(creating_withdrawl_window,text="Submit",command=Transaction.insert_data)
        submit.grid(row=3,column=1,padx=10,pady=10)


    def deposit():
        global accounts

        creating_deposited_window=Toplevel(root)
        creating_deposited_window.geometry('400x400')
        creating_deposited_window.title("Create deposited")
        creating_deposited_window.resizable(False,False)

        acc_no_label=Label(creating_deposited_window,text="Enter Your Account No:")
        amount_label=Label(creating_deposited_window,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)

        acc_no_entry=Entry(creating_deposited_window)
        accounts['acc_no_entry'] = acc_no_entry.get()
        amount_entry=Entry(creating_deposited_window)
        accounts['amount_entry'] = amount_entry.get()

        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)

        submit=Button(creating_deposited_window,text="Submit",command=Transaction.insert_data)
        submit.grid(row=3,column=1,padx=10,pady=10)


    def transfer():
        global accounts

        creating_transfer_window=Toplevel(root)
        creating_transfer_window.geometry('400x400')
        creating_transfer_window.title("create transfer")
        creating_transfer_window.resizable(False,False)

        sender_acc_label=Label(creating_transfer_window,text="Enter Sender Account No:")
        rece_acc_label=Label(creating_transfer_window,text="Enter Receiver Account No:")
        money_label=Label(creating_transfer_window,text="Enter Amount:")
        sender_acc_label.grid(row=0,column=0,padx=50,pady=10)
        rece_acc_label.grid(row=1,column=0,padx=50,pady=10)
        money_label.grid(row=2,column=0,padx=50,pady=10)

        sender_acc_entry=Entry(creating_transfer_window)
        accounts['sender_acc_entry'] = sender_acc_entry.get()
        rece_acc_entry=Entry(creating_transfer_window)
        accounts['rece_acc_entry'] = rece_acc_entry.get()
        money_entry=Entry(creating_transfer_window)
        accounts['money_entry'] = money_entry.get()


        sender_acc_entry.grid(row=0,column=1,padx=10,pady=10)
        rece_acc_entry.grid(row=1,column=1,padx=10,pady=10)
        money_entry.grid(row=2,column=1,padx=10,pady=10)

        submit=Button(creating_transfer_window,text="Submit",command=Transaction.insert_data)
        submit.grid(row=3,column=1,padx=10,pady=10)


    def details():
        global accounts

        creating_details_window=Toplevel(root)
        creating_details_window.geometry('400x400')
        creating_details_window.title("Create details")
        creating_details_window.resizable(False,False)

        name=Label(creating_details_window,text="Customer Name:")
        id=Label(creating_details_window,text="Customer ID:")
        mno=Label(creating_details_window,text="Customer Mobile No:")
        acc_type=Label(creating_details_window,text="Account Type:")
        balance=Label(creating_details_window,text="Customer Account Balance:")

        name.grid(row=0,column=0,padx=50,pady=10)
        id.grid(row=1,column=0,padx=50,pady=10)
        mno.grid(row=2,column=0,padx=50,pady=10)
        acc_type.grid(row=3,column=0,padx=50,pady=10)      


root=Tk()
root.title("Banking Management System")
root.geometry('400x400')
name=Label(text="Customer Name")

user_name=Entry(root)
accounts['user_name'] = user_name.get()
password=Label(text="Password")
user_password=Entry(root)
# accounts['user_password'] = user_password.get()

name.grid(row=0,column=0,padx=20,pady=10)
password.grid(row=1,column=0,padx=20,pady=10)
user_name.grid(row=0,column=1,padx=20,pady=10)
user_password.grid(row=1,column=1,padx=20,pady=10)

submit=Button(root,text="Submit",command=Transaction.main_page)
submit.grid(row=2,column=4)
root.mainloop()
