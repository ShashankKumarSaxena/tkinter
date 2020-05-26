import time
from tkinter import *
from tkinter import ttk
import random, sqlite3
import tkinter.messagebox
from tkinter import messagebox
import time
from PIL import ImageTk

flag = 0
counter = 1
conn = sqlite3.connect('database.db')
c = conn.cursor()


def admin_login():
    root.withdraw()
    admin1 = Toplevel() #toplevel creates a new window while frame creates window in the same window
    admin1.title("ADMIN LOGIN PAGE")
    admin1.geometry("600x600+500+0")
    admin1.config(background="white")
    admin1.logo_icon = PhotoImage(file="final.png")
    admin1.bg_icon = ImageTk.PhotoImage(file="ibg.jpg")

    bg_lbl = Label(admin1, image=admin1.bg_icon).pack()

    lf = Frame(admin1, width=400, height=340, relief="ridge", background="white", bd=5)
    lf.place(x=130, y=100)




    logolbl = Label(lf, image=admin1.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
    l1 = Label(lf, font=("Helvetica", 16, "bold"), bg="white", fg="black", text="Username").grid(row=1,column=0,padx=20,pady=10)

    l2 = Label(lf, font=("Helvetica", 16, "bold"), bg="white", fg="black", text="Password").grid(row=2,column=0,padx=20,pady=10)

    admin_entry = StringVar()
    p = StringVar()
    admin_entry.set("")
    p.set("")
    e1 = Entry(lf, width=12, font=("Helvetica", 16, "bold"), bd=5,relief=GROOVE, textvariable=admin_entry).grid(row=1, column=1,padx=20)
    e2 = Entry(lf, width=12, font=("Helvetica", 16, "bold"), bd=5,relief=GROOVE, show="*", textvariable=p).grid(row=2, column=1, padx=20)


    def admin_User():
        print("hello " + str(admin_entry.get()))
        if admin_entry.get() == "devansh" and p.get() == "123456":
            admin1.withdraw()
            admin()
        else:
            messagebox.showinfo("Error!!", "Invalid Password or Username")

    def Home():
        admin1.withdraw()
        root.deiconify()

    b1 = Button(lf, font=("georgia", 15), width=8, relief=GROOVE, text="Login", background="blue",fg="white",
                command=admin_User).grid(row=3,column=1,pady=10)

    b2 = Button(lf, font=("georgia", 15), width=8, relief=GROOVE, text="Home", background="blue", fg="white", command=Home).grid(row=3,column=0,pady=10)



def bills():
    root.withdraw()
    billing = Toplevel()
    billing.title("PROJECT BY DEVANSH")
    billing.bg_icon = ImageTk.PhotoImage(file="ibg.jpg")
    billing.geometry("1350x750+0+0")
    bg_lbl = Label(billing, image=billing.bg_icon).pack()
    tf = Frame(billing, width=900, height=100, padx=5, pady=5, background="powder blue", relief='ridge', bd=10)
    tf.place(x=0, y=0)
    lf = Frame(billing, width=900, pady=10, height=650, relief="ridge", background="powder blue", bd=10)
    lf.place(x=0, y=100)
    lf1a = Frame(lf, width=450, height=500, relief="ridge", background="powder blue", bd=10)
    lf1a.place(x=0, y=10)
    lf1b = Frame(lf, width=430, height=500, relief="ridge", background="powder blue", bd=10)
    lf1b.place(x=450, y=10)
    lf2 = Frame(lf, width=880, height=125, relief="ridge", background="powder blue", bd=10)
    lf2.place(x=0, y=475)
    rf = Frame(billing, width=450, height=750, padx=10, pady=30, relief="ridge", background="powder blue", bd=10)
    rf.place(x=900, y=0)
    rf1 = Frame(rf, width=200, height=100, relief="ridge", background="powder blue", bd=10)
    rf1.place(x=0, y=0)
    rf2 = Frame(rf, width=400, height=500, padx=10, pady=10, relief="ridge", background="white", bd=10)
    rf2.place(x=0, y=50)
    rf3 = Frame(rf, width=400, padx=10, pady=10, height=150, relief="ridge", background="powder blue", bd=10)
    rf3.place(x=0, y=520)
    title = Label(tf, font=("Helvetica", 30, "bold"), fg="black", background="powder blue",
                  text="                      SumitBaba IceCream Waale                           ")
    title.pack(side=LEFT)
    title1 = Label(rf1, font=("Helvetica", 18, "bold"), fg="blue", background="powder blue", text="RECEIPT")
    title1.pack(side=LEFT)
    # =================================================Declaration===========================================================#

    var = IntVar()
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set('0')
    var14.set("0")
    var15.set("0")
    var16.set("0")

    s = IntVar()
    s1 = IntVar()
    s2 = IntVar()
    s3 = IntVar()
    s4 = IntVar()
    s5 = IntVar()
    s6 = IntVar()
    s7 = IntVar()
    s8 = IntVar()
    s9 = IntVar()
    s10 = IntVar()
    s11 = IntVar()
    s12 = IntVar()
    s13 = IntVar()
    s.set("30")
    s1.set("25")
    s2.set("10")
    s3.set("15")
    s4.set("17")
    s5.set("19")
    s6.set("30")
    s7.set("29")
    s8.set("25")
    s9.set("0")
    s10.set("22")
    s11.set("18")
    s12.set("30")
    s13.set('9')

    # =================================================function============================================================#
    def create_table():
        c.execute(
            "CREATE TABLE IF NOT EXISTS data(bill_no text,bacon Integer,pista integer,chocolate integer,mango integer,strawberry integer,vanilla integer,blue_moon integer,magnum integer,cornetto integer,kulfi integer,milk_shake integer,choco_top integer,affogato integer,brownie integer,sub_total integer,gst integer,total_cost integer)")
        conn.commit()

    def insert(r, v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16):
        c.execute(
            "INSERT INTO data(bill_no,bacon,pista,chocolate,mango,strawberry,vanilla,blue_moon,magnum,cornetto,kulfi,milk_shake,choco_top,affogato,brownie,sub_total,gst,total_cost) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (r, v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16))
        conn.commit()

    def exit():
        Exit = tkinter.messagebox.askyesno("Ice Cream Billing System", "Are you sure want to exit the System..?")
        if Exit > 0:
            billing.destroy()

    def home():
        root.deiconify()
        billing.withdraw()

    def reset():
        var.set("0")
        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        var13.set('0')
        var14.set("0")
        var15.set("0")
        var16.set("0")
        txt.configure(state="normal")
        txt.delete('1.0', END)
        txt.configure(state="disabled")

    def ran():
        b = random.randint(1000000, 9999999)
        return b

    def receipt():
        global counter
        r = ran()
        v = var.get()
        v1 = var1.get()
        v2 = var2.get()
        v3 = var3.get()
        v4 = var4.get()
        v5 = var5.get()
        v6 = var6.get()
        v7 = var7.get()
        v8 = var8.get()
        v9 = var9.get()
        v10 = var10.get()
        v11 = var11.get()
        v12 = var12.get()
        v13 = var13.get()
        v14 = var14.get()
        v15 = var15.get()
        v16 = var16.get()

        e14.configure(state="normal")
        PriceOfItem = (
                    var.get() * 30 + var1.get() * 35 + var2.get() * 20 + var3.get() * 10 + var4.get() * 30 + var5.get() * 35 + var6.get() * 40 + var7.get() * 80 + var8.get() * 50 + var9.get() * 45 + var10.get() * 50 + var11.get() * 70 + var12.get() * 60 + var13.get() * 90)
        price = PriceOfItem
        a = var14.set(price)
        e14.configure(state=DISABLED)
        e15.configure(state=NORMAL)
        GSTOfItem = round(
            var.get() * 30 * 0.06 + var1.get() * 35 * 0.06 + var2.get() * 20 * 0.06 + var3.get() * 10 * 0.06 + var4.get() * 30 * 0.06 + var5.get() * 35 * 0.06 + var6.get() * 40 * 0.06 + var7.get() * 80 * 0.06 + var8.get() * 50 * 0.06 + var9.get() * 45 * 0.06 + var10.get() * 50 * 0.06 + var11.get() * 70 * 0.06 + var12.get() * 60 * 0.06 + var13.get() * 90 * 0.06)
        gst = GSTOfItem
        b = var15.set(gst)
        e15.configure(state=DISABLED)
        e16.configure(state="normal")
        TotalCostOfItem = PriceOfItem + GSTOfItem
        total = TotalCostOfItem
        c = var16.set(total)
        e16.configure(state="disabled")
        if ((
                var.get() or var1.get() or var2.get() or var3.get() or var4.get() or var5.get() or var6.get() or var7.get() or var8.get() or var9.get() or var10.get() or var11.get() or var12.get() or var13.get()) == 0):
            txt.configure(state="disabled")
            messagebox.showinfo("Waring", "Please Entry First")
        else:
            txt.configure(state="normal")
            txt.insert("1.0", "\t      SumitBaba IceCream waale\t\t\n")
            txt.insert(END, "-------------------------------------------------------------\n")
            txt.insert(END, "Bill No.\t\t" + str(r) + "\n")
            txt.insert(END, "-------------------------------------------------------------\n")
            txt.insert(END, "Item \t \tQty\t     Rate\n")
            txt.insert(END, "-------------------------------------------------------------\n")
            if var.get() != 0:
                txt.insert(END, "Bacon \t \t" + str(var.get()) + "\t   ₹" + str(var.get() * 30) + "/-\n \n")
            if var1.get() != 0:
                txt.insert(END, "Pista \t \t" + str(var1.get()) + "\t  ₹" + str(var1.get() * 35) + "/- \n  \n")
            if var2.get() != 0:
                txt.insert(END, "Chocolate \t \t" + str(var2.get()) + "\t  ₹" + str(var2.get() * 20) + "/- \n \n")
            if var3.get() != 0:
                txt.insert(END, "Mango\t \t" + str(var3.get()) + "\t   ₹" + str(var3.get() * 10) + "/-\n \n")
            if var4.get() != 0:
                txt.insert(END, "Strawberry\t \t" + str(var4.get()) + "\t   ₹" + str(var4.get() * 30) + "/-\n \n")
            if var5.get() != 0:
                txt.insert(END, "Vanilla \t \t" + str(var5.get()) + "\t   ₹" + str(var5.get() * 35) + "/-\n \n")
            if var6.get() != 0:
                txt.insert(END, "Blue Moon \t \t" + str(var6.get()) + "\t   ₹" + str(var6.get() * 40) + "/-\n \n")
            if var7.get() != 0:
                txt.insert(END, "Magnum \t \t" + str(var7.get()) + "\t   ₹" + str(var7.get() * 80) + "/-\n \n")
            if var8.get() != 0:
                txt.insert(END, "Cornetto \t \t" + str(var8.get()) + "\t   ₹" + str(var8.get() * 50) + "/-\n \n")
            if var9.get() != 0:
                txt.insert(END, "Kulfi \t \t" + str(var9.get()) + "\t  ₹" + str(var9.get() * 45) + "/-\n \n")
            if var10.get() != 0:
                txt.insert(END, "Milk Shake \t \t" + str(var10.get()) + "\t   ₹" + str(var10.get() * 50) + "/-\n \n")
            if var11.get() != 0:
                txt.insert(END, "Choc Top \t \t" + str(var11.get()) + "\t   ₹" + str(var11.get() * 70) + "/-\n \n")
            if var12.get() != 0:
                txt.insert(END, "Affogato \t \t" + str(var12.get()) + "\t   ₹" + str(var12.get() * 60) + "/-\n \n")
            if var13.get() != 0:
                txt.insert(END, "Brownie \t \t" + str(var13.get()) + "\t   ₹" + str(var13.get() * 90) + "/-\n \n")
            txt.insert(END, "------------------------------------------------------------\n ")
            txt.insert(END, "Sub total \t \t ₹" + str(var14.get()) + "/-\n ")
            txt.insert(END, "GST \t \t ₹" + str(var15.get()) + "/-\n ")
            txt.insert(END, "Total cost \t \t ₹" + str(var16.get()) + "/-\n ")
            txt.configure(state='disabled')
            y = messagebox.askyesno("Ice-Cream Billing System", "Want to save?")
            if y > 0:
                create_table()
                v = var.get()
                v1 = var1.get()
                v2 = var2.get()
                v3 = var3.get()
                v4 = var4.get()
                v5 = var5.get()
                v6 = var6.get()
                v7 = var7.get()
                v8 = var8.get()
                v9 = var9.get()
                v10 = var10.get()
                v11 = var11.get()
                v12 = var12.get()
                v13 = var13.get()
                v14 = var14.get()
                v15 = var15.get()
                v16 = var16.get()
                insert(r, v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16)
                messagebox.showinfo("Success", "Saved Sucessfully!")

        if Stock(v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16):
            billing.withdraw()

        reset()

    def CostOfItem():
        e14.configure(state="normal")
        PriceOfItem = (
                    var.get() * 30 + var1.get() * 35 + var2.get() * 20 + var3.get() * 10 + var4.get() * 30 + var5.get() * 35 + var6.get() * 40 + var7.get() * 80 + var8.get() * 50 + var9.get() * 45 + var10.get() * 50 + var11.get() * 70 + var12.get() * 60 + var13.get() * 90)
        price = PriceOfItem
        a = var14.set(price)
        e14.configure(state=DISABLED)
        e15.configure(state=NORMAL)
        GSTOfItem = round(
            var.get() * 30 * 0.06 + var1.get() * 35 * 0.06 + var2.get() * 20 * 0.06 + var3.get() * 10 * 0.06 + var4.get() * 30 * 0.06 + var5.get() * 35 * 0.06 + var6.get() * 40 * 0.06 + var7.get() * 80 * 0.06 + var8.get() * 50 * 0.06 + var9.get() * 45 * 0.06 + var10.get() * 50 * 0.06 + var11.get() * 70 * 0.06 + var12.get() * 60 * 0.06 + var13.get() * 90 * 0.06)
        gst = GSTOfItem
        b = var15.set(gst)
        e15.configure(state=DISABLED)
        e16.configure(state="normal")
        TotalCostOfItem = PriceOfItem + GSTOfItem
        total = TotalCostOfItem
        c = var16.set(total)
        e16.configure(state="disabled")
        info(a, b, c)

    def info(a, b, c):
        if var14.get() == var15.get() == var16.get() == 0:
            messagebox.showinfo("Ice-Cream Billing System", "Please,Do Entry first... ")

    # =============================Label============================================

    t1 = Label(lf1a, font=("Helvetica", 20), padx=10, pady=10, fg='blue', background='powder blue', text='Type')
    t1.place(x=00, y=20)
    Qty = Label(lf1a, font=("Helvetica", 18,), padx=10, pady=10, background='powder blue', fg='blue', text='Qty')
    Qty.place(x=170, y=20)
    stock = Label(lf1a, font=("Helvetica", 20), padx=10, pady=10, fg='blue', background='powder blue', text='Stock')
    stock.place(x=240, y=20)
    Price = Label(lf1a, font=("Helvetica", 18,), padx=10, pady=10, background='powder blue', fg='blue', text='Price')
    Price.place(x=345, y=20)

    l0 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Bacon')
    l0.place(x=0, y=100)

    l0 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹30/-')
    l0.place(x=345, y=100)

    l1 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Pista')
    l1.place(x=0, y=150)

    l1 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹35/-')
    l1.place(x=345, y=150)

    l2 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Chocolate')
    l2.place(x=0, y=200)

    l2 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹20/-')
    l2.place(x=345, y=200)

    l3 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Mango')
    l3.place(x=0, y=250)

    l3 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹10/-')
    l3.place(x=345, y=250)

    l4 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Strawberry')
    l4.place(x=0, y=300)

    l4 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹30/-')
    l4.place(x=345, y=300)

    l5 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Vanilla')
    l5.place(x=0, y=350)

    l5 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹35/-')
    l5.place(x=345, y=350)

    l6 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Blue Moon')
    l6.place(x=0, y=400)

    l6 = Label(lf1a, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹40/-')
    l6.place(x=345, y=400)

    t2 = Label(lf1b, font=("Helvetica", 20), padx=10, pady=10, fg='blue', background='powder blue', text='Type')
    t2.place(x=0, y=20)
    Qty = Label(lf1b, font=("Helvetica", 20), padx=10, pady=10, fg='blue', background='powder blue', text='Qty')
    Qty.place(x=150, y=20)
    stock = Label(lf1b, font=("Helvetica", 20), padx=10, pady=10, fg='blue', background='powder blue', text='Stock')
    stock.place(x=240, y=20)
    Price = Label(lf1b, font=("Helvetica", 19), padx=10, pady=10, fg='blue', background='powder blue', text='Price')
    Price.place(x=330, y=20)

    l7 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Magnum')
    l7.place(x=00, y=100)

    l7 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹80/-')
    l7.place(x=330, y=100)

    l8 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Cornetto')
    l8.place(x=00, y=150)

    l8 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹50/-')
    l8.place(x=330, y=150)

    l9 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Kulfi')
    l9.place(x=00, y=200)

    l9 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹45/-')
    l9.place(x=330, y=200)

    l10 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Milk Shake')
    l10.place(x=00, y=250)

    l10 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹50/-')
    l10.place(x=330, y=250)

    l11 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Choc Top')
    l11.place(x=0, y=300)

    l11 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹70/-')
    l11.place(x=330, y=300)

    l12 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Affogato')
    l12.place(x=00, y=350)

    l12 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹60/-')
    l12.place(x=330, y=350)

    l13 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Brownie')
    l13.place(x=00, y=400)

    l13 = Label(lf1b, font=("Helvetica", 19, 'bold'), padx=10, pady=10, background='powder blue', text='₹90/-')
    l13.place(x=330, y=400)

    l14 = Label(lf2, font=("Helvetica", 20, "bold"), text="Sub Total", fg="blue", bg="powder blue")
    l14.place(x=130, y=10)

    l15 = Label(lf2, font=("Helvetica", 20, "bold"), text="GST", fg="blue", bg="powder blue")
    l15.place(x=500, y=10)

    l15 = Label(lf2, font=("Helvetica", 20, "bold"), text="Total Cost", fg="blue", bg="powder blue")
    l15.place(x=300, y=60)

    # ==================In stock===

    y0 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s)
    y0.place(x=250, y=110)
    y1 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s1)
    y1.place(x=250, y=160)
    y2 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s2)
    y2.place(x=250, y=210)
    y3 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s3)
    y3.place(x=250, y=260)
    y4 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s4)
    y4.place(x=250, y=310)
    y5 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s5)
    y5.place(x=250, y=360)
    y6 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=s6)
    y6.place(x=250, y=410)
    y7 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s7)
    y7.place(x=250, y=110)
    y8 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s8)
    y8.place(x=250, y=160)
    y9 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s9)
    y9.place(x=250, y=210)
    y10 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s10)
    y10.place(x=250, y=260)
    y11 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s11)
    y11.place(x=250, y=310)
    y12 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s12)
    y12.place(x=250, y=360)
    y13 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=s13)
    y13.place(x=250, y=410)
    y0.configure(state=DISABLED)
    y1.configure(state=DISABLED)
    y2.configure(state=DISABLED)
    y3.configure(state=DISABLED)
    y4.configure(state=DISABLED)
    y5.configure(state=DISABLED)
    y6.configure(state=DISABLED)
    y7.configure(state=DISABLED)
    y8.configure(state=DISABLED)
    y9.configure(state=DISABLED)
    y10.configure(state=DISABLED)
    y11.configure(state=DISABLED)
    y12.configure(state=DISABLED)
    y13.configure(state=DISABLED)
    global flag
    if flag == 1:
        c.execute("SELECT * FROM stock")
        t = c.fetchall()
        b = len(t)
        if b > 0:
            for i in t:
                p0 = str(i[0])
                p1 = i[1]
                p2 = i[2]
                p3 = i[3]
                p4 = i[4]
                p5 = i[5]
                p6 = i[6]
                p7 = i[7]
                p8 = i[8]
                p9 = i[9]
                p10 = i[10]
                p11 = i[11]
                p12 = i[12]
                p13 = i[13]

            y0.configure(state=NORMAL)
            y1.configure(state=NORMAL)
            y2.configure(state=NORMAL)
            y3.configure(state=NORMAL)
            y4.configure(state=NORMAL)
            y5.configure(state=NORMAL)
            y6.configure(state=NORMAL)
            y7.configure(state=NORMAL)
            y8.configure(state=NORMAL)
            y9.configure(state=NORMAL)
            y10.configure(state=NORMAL)
            y11.configure(state=NORMAL)
            y12.configure(state=NORMAL)
            y13.configure(state=NORMAL)

            s.set(p0)
            s1.set(p1)
            s2.set(p2)
            s3.set(p3)
            s4.set(p4)
            s5.set(p5)
            s6.set(p6)
            s7.set(p7)
            s8.set(p8)
            s9.set(p9)
            s10.set(p10)
            s11.set(p11)
            s12.set(p12)
            s13.set(p13)

            y0.configure(state=DISABLED)
            y1.configure(state=DISABLED)
            y2.configure(state=DISABLED)
            y3.configure(state=DISABLED)
            y4.configure(state=DISABLED)
            y5.configure(state=DISABLED)
            y6.configure(state=DISABLED)
            y7.configure(state=DISABLED)
            y8.configure(state=DISABLED)
            y9.configure(state=DISABLED)
            y10.configure(state=DISABLED)
            y11.configure(state=DISABLED)
            y12.configure(state=DISABLED)
            y13.configure(state=DISABLED)
            flag = 0
    # ==================================Entries
    e0 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var)
    e0.place(x=170, y=110)
    e1 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var1)
    e1.place(x=170, y=160)
    e2 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var2)
    e2.place(x=170, y=210)
    e3 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var3)
    e3.place(x=170, y=260)
    e4 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var4)
    e4.place(x=170, y=310)
    e5 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var5)
    e5.place(x=170, y=360)
    e6 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=var6)
    e6.place(x=170, y=410)
    e7 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var7)
    e7.place(x=170, y=110)
    e8 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var8)
    e8.place(x=170, y=160)
    e9 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var9)
    e9.place(x=170, y=210)
    e10 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var10)
    e10.place(x=170, y=260)
    e11 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var11)
    e11.place(x=170, y=310)
    e12 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var12)
    e12.place(x=170, y=360)
    e13 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=var13)
    e13.place(x=170, y=410)
    e14 = Entry(lf2, font=('Helvetica', 18, 'bold'), width=7, textvariable=var14)
    e14.place(x=270, y=10)
    e15 = Entry(lf2, font=('Helvetica', 18, 'bold'), width=7, textvariable=var15)
    e15.place(x=580, y=10)
    e16 = Entry(lf2, font=('Helvetica', 18, 'bold'), width=7, textvariable=var16)
    e16.place(x=450, y=60)

    e14.configure(state="disabled")

    e15.configure(state="disabled")

    e16.configure(state="disabled")

    # ===============================Receipt TextBox=======================================================================

    txt = Text(rf2, font=("Helvetica", 12, "bold"), fg="purple", width=34)
    txt.grid(row=0, column=0)
    s = Scrollbar(rf2)
    s.grid(row=0, column=1, ipady=10)
    s.config(command=txt.yview)
    txt.configure(state='disabled')
    # =============================Receipt Button====================================#
    btnReset = Button(rf3, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=6, width=6, height=1, bg='gold',
                      text='Reset', command=reset).place(x=0, y=0)
    btnTotal = Button(rf3, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=6, width=6, height=1, bg='gold',
                      text='Total', command=CostOfItem).place(x=130, y=0)
    btnQuit = Button(rf3, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=6, width=6, height=1, bg='gold',
                     text='Quit', command=exit).place(x=80, y=60)
    btnReceipt = Button(rf3, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=6, width=6, height=1, bg='gold',
                        text='Receipt', command=receipt).place(x=260, y=0)
    btnHome = Button(rf3, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=6, width=6, height=1, bg='gold',
                     text='Home', command=home).place(x=200, y=60)


def retrival():
    root.withdraw()
    retrival = Toplevel()
    retrival.title("PROJECT BY DEVANSH")
    retrival.geometry("1350x750+0+0")
    retrival.config(background="powder blue")
    lf = Frame(retrival, width=925, background="powder blue", height=100, bd=10, padx=10, pady=10, relief=RIDGE)
    lf.place(x=0, y=0)
    lfd = Frame(retrival, width=925, background="powder blue", height=550, bd=10, pady=10, padx=10, relief="ridge")
    lfd.place(x=0, y=100)
    rf = Frame(retrival, width=425, height=650, background="powder blue", bd=10, relief="ridge", padx=10, pady=10)
    rf.place(x=925, y=0)
    rf1 = Frame(rf, width=125, height=50, background="medium spring green", bd=6, relief="ridge", padx=5, pady=5)
    rf1.place(x=5, y=5)
    title = Label(lf, font=("Helvetica", 30, "bold"), fg="black", background="powder blue",
                  text="                      SumitBaba IceCream Waale                           ")
    title.pack(side=LEFT)

    txt1 = Text(rf, width=37, font=("Helvetica", 12, "bold"), fg='purple', bd=10, relief="ridge", height=28)
    s = Scrollbar(rf, relief="ridge", bd=7)
    s.place(x=330, y=290)
    s.config(command=txt1.yview)
    txt1.configure(state='disabled')
    txt1.place(x=0, y=57)

    m = IntVar()
    m.set("0")

    # ========================================
    def clear():
        m.set("0")
        txt1.configure(state=NORMAL)
        txt1.delete("1.0", END)
        txt1.configure(state=DISABLED)

    def back():
        retrival.withdraw()
        root.deiconify()

    def bye():
        y = messagebox.askyesno("Ice-Cream Billing System", "Are you sure want to exit?")
        if y > 0:
            retrival.destroy()
            root.destroy()

    def search():
        s = m.get()
        if s == 0:
            messagebox.showinfo("Warning", "Please Input Bill no")
        txt1.configure(state="normal")
        txt1.delete("1.0", END)
        c.execute("SELECT * FROM data WHERE bill_no=" + str(s))
        d = c.fetchall()
        for i in d:
            txt1.insert("1.0", "\t      SumitBaba IceCream Waale\t\n")
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Bill No.\t\t" + str(i[0]) + "\n")
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Item \t \tQty\t     Rate\n")
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Bacon \t \t" + str(i[1]) + "\t   ₹" + str(i[1] * 30) + "/-\n \n")
            txt1.insert(END, "Pista \t \t" + str(i[2]) + "\t  ₹" + str(i[2] * 35) + "/- \n  \n")
            txt1.insert(END, "Chocolate \t \t" + str(i[3]) + "\t  ₹" + str(i[3] * 20) + "/- \n \n")
            txt1.insert(END, "Mango\t \t" + str(i[4]) + "\t   ₹" + str(i[4] * 10) + "/-\n \n")
            txt1.insert(END, "Strawberry\t \t" + str(i[5]) + "\t   ₹" + str(i[5] * 30) + "/-\n \n")
            txt1.insert(END, "Vanilla \t \t" + str(i[6]) + "\t   ₹" + str(i[6] * 35) + "/-\n \n")
            txt1.insert(END, "Blue Moon \t \t" + str(i[7]) + "\t   ₹" + str(i[7] * 40) + "/-\n \n")
            txt1.insert(END, "Magnum \t \t" + str(i[8]) + "\t   ₹" + str(i[8] * 80) + "/-\n \n")
            txt1.insert(END, "Cornetto \t \t" + str(i[9]) + "\t   ₹" + str(i[9] * 50) + "/-\n \n")
            txt1.insert(END, "Kulfi \t \t" + str(i[10]) + "\t  ₹" + str(i[10] * 45) + "/-\n \n")
            txt1.insert(END, "Milk Shake \t \t" + str(i[11]) + "\t   ₹" + str(i[11] * 50) + "/-\n \n")
            txt1.insert(END, "Choc Top \t \t" + str(i[12]) + "\t   ₹" + str(i[12] * 70) + "/-\n \n")
            txt1.insert(END, "Affogato \t \t" + str(i[13]) + "\t   ₹" + str(i[13] * 60) + "/-\n \n")
            txt1.insert(END, "Brownie \t \t" + str(i[14]) + "\t   ₹" + str(i[14] * 90) + "/-\n \n")
            txt1.insert(END, "------------------------------------------------------------\n ")
            txt1.insert(END, "Sub total \t \t ₹" + str(i[15]) + "/-\n ")
            txt1.insert(END, "GST \t \t ₹" + str(i[16]) + "/-\n ")
            txt1.insert(END, "TOTAL \t \t ₹" + str(i[17]))

        txt1.configure(state="disabled")

    def history():
        txt1.configure(state="normal")
        txt1.delete("1.0", END)
        c.execute("SELECT * FROM data")
        d = c.fetchall()
        l = len(d)
        if l == 0:
            messagebox.showinfo("Warning", "No History Found!!!!")

        txt1.insert("1.0", "\t      SumitBaba IceCream Waale\t\n")
        for i in d:
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Bill No.\t\t" + str(i[0]) + "\n")
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Item \t \tQty\t     Rate\n")
            txt1.insert(END, "-------------------------------------------------------------\n")
            txt1.insert(END, "Bacon \t \t" + str(i[1]) + "\t   ₹" + str(i[1] * 30) + "/-\n \n")
            txt1.insert(END, "Pista \t \t" + str(i[2]) + "\t  ₹" + str(i[2] * 35) + "/- \n  \n")
            txt1.insert(END, "Chocolate \t \t" + str(i[3]) + "\t  ₹" + str(i[3] * 20) + "/- \n \n")
            txt1.insert(END, "Mango\t \t" + str(i[4]) + "\t   ₹" + str(i[4] * 10) + "/-\n \n")
            txt1.insert(END, "Strawberry\t \t" + str(i[5]) + "\t   ₹" + str(i[5] * 30) + "/-\n \n")
            txt1.insert(END, "Vanilla \t \t" + str(i[6]) + "\t   ₹" + str(i[6] * 35) + "/-\n \n")
            txt1.insert(END, "Blue Moon \t \t" + str(i[7]) + "\t   ₹" + str(i[7] * 40) + "/-\n \n")
            txt1.insert(END, "Magnum \t \t" + str(i[8]) + "\t   ₹" + str(i[8] * 80) + "/-\n \n")
            txt1.insert(END, "Cornetto \t \t" + str(i[9]) + "\t   ₹" + str(i[9] * 50) + "/-\n \n")
            txt1.insert(END, "Kulfi \t \t" + str(i[10]) + "\t  ₹" + str(i[10] * 45) + "/-\n \n")
            txt1.insert(END, "Milk Shake \t \t" + str(i[11]) + "\t   ₹" + str(i[11] * 50) + "/-\n \n")
            txt1.insert(END, "Choc Top \t \t" + str(i[12]) + "\t   ₹" + str(i[12] * 70) + "/-\n \n")
            txt1.insert(END, "Affogato \t \t" + str(i[13]) + "\t   ₹" + str(i[13] * 60) + "/-\n \n")
            txt1.insert(END, "Brownie \t \t" + str(i[14]) + "\t   ₹" + str(i[14] * 90) + "/-\n \n")
            txt1.insert(END, "------------------------------------------------------------\n ")
            txt1.insert(END, "Sub total \t \t ₹" + str(i[15]) + "/-\n ")
            txt1.insert(END, "GST \t \t ₹" + str(i[16]) + "/-\n ")
            txt1.insert(END, "Total cost \t \t ₹" + str(
                i[17]) + "/-\n\n\n\n                      SumitBaba IceCream Waale\n")
        txt1.configure(state="disabled")

    # =====================================Button=================================================

    sbtn = Button(rf, width=6, cursor='hand2', height=2, bd=4, bg='cyan', text='Search', command=search)
    sbtn.place(x=297, y=5)
    hBtn = Button(lfd, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=15, height=7, bg='cyan',
                  text='Home', command=back).place(x=30, y=30)
    histBtn = Button(lfd, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=15, height=7, bg='cyan',
                     text='History', command=history).place(x=350, y=30)
    rBtn = Button(lfd, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=15, height=7, bg='cyan',
                  text='Reset', command=clear).place(x=650, y=30)
    qBtn = Button(lfd, padx=5, pady=5, fg="black", cursor='hand2', font=("arial", 14, 'bold'), bd=10, width=15,
                  height=7, bg='cyan', text='Quit', command=bye).place(x=350, y=300)

    # =====================================Label==================================================
    rf1L = Label(rf1, text="Bill No", font=("Helvetica", 20, "bold"), background="medium spring green")
    rf1L.place(x=0, y=0)

    # =====================================Entries=================================================
    r1 = Entry(rf, width=10, font=("Helvetica", 20, "bold"), bd=8, relief="ridge", textvariable=m)
    r1.place(x=130, y=5)


def admin():
    root.withdraw()
    admin = Toplevel()
    admin.title("PROJECT BY DEVANSH")
    admin.geometry("900x750+150+50")
    admin.config(background="powder blue")
    tf = Frame(admin, width=900, height=100, padx=5, pady=5, background="powder blue", relief='ridge', bd=10)
    tf.place(x=0, y=0)
    lf = Frame(admin, width=900, pady=10, height=650, relief="ridge", background="powder blue", bd=10)
    lf.place(x=0, y=100)
    lf1a = Frame(lf, width=450, height=500, relief="ridge", background="powder blue", bd=10)
    lf1a.place(x=0, y=10)
    lf1b = Frame(lf, width=430, height=500, relief="ridge", background="powder blue", bd=10)
    lf1b.place(x=450, y=10)
    lf2 = Frame(lf, width=880, height=125, relief="ridge", background="powder blue", bd=10)
    lf2.place(x=0, y=475)
    t1 = Label(lf1a, font=("Helvetica", 20, 'bold'), padx=10, pady=10, fg='blue', background='powder blue', text='Type')
    t1.place(x=20, y=20)
    Qty = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', fg='blue',
                text='In Stock')
    Qty.place(x=190, y=20)
    title = Label(tf, font=("Helvetica", 30, "bold"), fg="blue", background="powder blue",
                  text="                         Admin Page                                 ")
    title.pack(side=LEFT)

    # =========================================Label

    l0 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Bacon')
    l0.place(x=20, y=100)
    l1 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Pista')
    l1.place(x=20, y=150)
    l2 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Chocolate')
    l2.place(x=20, y=200)
    l3 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Mango')
    l3.place(x=20, y=250)
    l4 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Strawberry')
    l4.place(x=20, y=300)
    l5 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Vanilla')
    l5.place(x=20, y=350)
    l6 = Label(lf1a, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Blue Moon')
    l6.place(x=20, y=400)
    t2 = Label(lf1b, font=("Helvetica", 20, 'bold'), padx=10, pady=10, fg='blue', background='powder blue', text='Type')
    t2.place(x=20, y=20)
    Qty = Label(lf1b, font=("Helvetica", 20, 'bold'), padx=10, pady=10, fg='blue', background='powder blue',
                text='In Stock')
    Qty.place(x=170, y=20)

    l7 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Magnum')
    l7.place(x=20, y=100)
    l8 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Cornetto')
    l8.place(x=20, y=150)
    l9 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Kulfi')
    l9.place(x=20, y=200)
    l10 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Milk Shake')
    l10.place(x=20, y=250)
    l11 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Choc Top')
    l11.place(x=20, y=300)
    l12 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Affogato')
    l12.place(x=20, y=350)
    l13 = Label(lf1b, font=("Helvetica", 18, 'bold'), padx=10, pady=10, background='powder blue', text='Brownie')
    l13.place(x=20, y=400)

    # ==============================================Declartion====

    u = IntVar()
    u1 = IntVar()
    u2 = IntVar()
    u3 = IntVar()
    u4 = IntVar()
    u5 = IntVar()
    u6 = IntVar()
    u7 = IntVar()
    u8 = IntVar()
    u9 = IntVar()
    u10 = IntVar()
    u11 = IntVar()
    u12 = IntVar()
    u13 = IntVar()

    u.set("30")
    u1.set("25")
    u2.set("10")
    u3.set("15")
    u4.set("17")
    u5.set("19")
    u6.set("30")
    u7.set("29")
    u8.set("25")
    u9.set("0")
    u10.set("22")
    u11.set("18")
    u12.set("30")
    u13.set('9')

    # =====================def
    def new_table():
        c.execute(
            "CREATE TABLE IF NOT EXISTS stock(bacon Integer,pista integer,chocolate integer,mango integer,strawberry integer,vanilla integer,blue_moon integer,magnum integer,cornetto integer,kulfi integer,milk_shake integer,choco_top integer,affogato integer,brownie integer)")
        conn.commit()

    def insert_in_table(x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):
        c.execute(
            "INSERT INTO stock(bacon,pista,chocolate,mango,strawberry,vanilla,blue_moon,magnum,cornetto,kulfi,milk_shake,choco_top,affogato,brownie) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13))
        conn.commit()

    def home():
        admin.withdraw()
        root.deiconify()

    def iExit():
        y = messagebox.askyesno("Ice-Cream Billing System", "Want to Exit the System?")
        if y == 1:
            admin.destroy()
            root.destroy()

    def reset():
        c.execute("DELETE FROM stock;")
        conn.commit()
        u.set("0")
        u1.set("0")
        u2.set("0")
        u3.set("0")
        u4.set("0")
        u5.set("0")
        u6.set("0")
        u7.set("0")
        u8.set("0")
        u9.set("0")
        u10.set("0")
        u11.set("0")
        u12.set("0")
        u13.set('0')
        messagebox.showinfo("SuCESS", "Reset Successfull!!!")

    def update():
        global flag

        new_table()
        x = u.get()
        x1 = u1.get()
        x2 = u2.get()
        x3 = u3.get()
        x4 = u4.get()
        x5 = u5.get()
        x6 = u6.get()
        x7 = u7.get()
        x8 = u8.get()
        x9 = u9.get()
        x10 = u10.get()
        x11 = u11.get()
        x12 = u12.get()
        x13 = u13.get()

        insert_in_table(x, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
        messagebox.showinfo('Success', 'Successfully Saved')
        flag = 1
        u.set("0")
        u1.set("0")
        u2.set("0")
        u3.set("0")
        u4.set("0")
        u5.set("0")
        u6.set("0")
        u7.set("0")
        u8.set("0")
        u9.set("0")
        u10.set("0")
        u11.set("0")
        u12.set("0")
        u13.set('0')

    # =============================================Entry
    f0 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u)
    f0.place(x=190, y=110)
    f1 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u1)
    f1.place(x=190, y=160)
    f2 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u2)
    f2.place(x=190, y=210)
    f3 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u3)
    f3.place(x=190, y=260)
    f4 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u4)
    f4.place(x=190, y=310)
    f5 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u5)
    f5.place(x=190, y=360)
    f6 = Entry(lf1a, font=('Helvetica', 18, 'bold'), width=5, textvariable=u6)
    f6.place(x=190, y=410)
    f7 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u7)
    f7.place(x=190, y=110)
    f8 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u8)
    f8.place(x=190, y=160)
    f9 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u9)
    f9.place(x=190, y=210)
    f10 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u10)
    f10.place(x=190, y=260)
    f11 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u11)
    f11.place(x=190, y=310)
    f12 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u12)
    f12.place(x=190, y=360)
    f13 = Entry(lf1b, font=('Helvetica', 18, 'bold'), width=5, textvariable=u13)
    f13.place(x=190, y=410)

    # ==============================Button
    rstBtn = Button(lf2, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=9, bg='cyan',
                    text='Reset', command=reset)
    rstBtn.place(x=50, y=20)
    updateBtn = Button(lf2, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=9, bg='cyan',
                       text='Update', command=update).place(x=250, y=20)
    homeBtn = Button(lf2, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=9, bg='cyan',
                     text='Home', command=home).place(x=450, y=20)
    quitBtn = Button(lf2, padx=5, pady=5, fg="black", font=("arial", 14, 'bold'), bd=10, width=9, bg='cyan',
                     text='Quit', command=iExit).place(x=650, y=20)


def Stock(v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16):
    c.execute("SELECT * FROM stock")
    d = c.fetchall()
    conn.commit()
    l = len(d)
    for i in d:
        a = i[0]
        a1 = i[1]
        a2 = i[2]
        a3 = i[3]

        a4 = i[4]
        a5 = i[5]

        a6 = i[6]
        a7 = i[7]
        a8 = i[8]
        a9 = i[9]
        a10 = i[10]
        a11 = i[11]
        a12 = i[12]
        a13 = i[13]

    print(a, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)
    print(type(a))
    print(v, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16)

    b = a - v
    b1 = a1 - v1
    b2 = a2 - v2
    b3 = a3 - v3
    b4 = a4 - v4
    b5 = a5 - v5
    b6 = a6 - v6
    b7 = a7 - v7
    b8 = a8 - v8
    b9 = a9 - v9
    b10 = a10 - v10

    b11 = a11 - v11
    b12 = a12 - v12
    b13 = a13 - v13

    if b >= 0 and b1 >= 0 and b2 >= 0 and b3 >= 0 and b4 >= 0 and b5 >= 0 and b6 >= 0 and b7 >= 0 and b8 >= 0 and b9 >= 0 and b10 >= 0 and b11 >= 0 and b12 >= 0 and b13 >= 0:
        c.execute(
            "INSERT INTO stock(bacon,pista,chocolate,mango,strawberry,vanilla,blue_moon,magnum,cornetto,kulfi,milk_shake,choco_top,affogato,brownie) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (b, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13))


    else:
        messagebox.showinfo("Warning", "Out of stock!!")
        return 0

    print(b, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13)
    print(type(b))


def billcolor1(event):
    billBtn["bg"] = "cyan"
    billBtn['image'] = bimg
    billBtn['width'] = 575
    billBtn['height'] = 260


def billcolor2(event):
    billBtn['bg'] = "steel blue"
    billBtn['text'] = 'Billing System'
    billBtn['image'] = ''
    billBtn['width'] = 45
    billBtn['height'] = 9


def closecolor1(event):
    ExitBtn["bg"] = "red"
    ExitBtn['image'] = cimg
    ExitBtn['width'] = 790
    ExitBtn['height'] = 190


def closecolor2(event):
    ExitBtn['bg'] = "salmon"
    ExitBtn['text'] = 'Exit System'
    ExitBtn['image'] = ''
    ExitBtn['width'] = 63
    ExitBtn['height'] = 6


def retcolor1(event):
    RetrivalBtn["bg"] = "cyan"
    RetrivalBtn['image'] = rimg
    RetrivalBtn['width'] = 575
    RetrivalBtn['height'] = 260


def retcolor2(event):
    RetrivalBtn['bg'] = "steel blue"
    RetrivalBtn['text'] = 'Retrival System'
    RetrivalBtn['image'] = ''
    RetrivalBtn['width'] = 45
    RetrivalBtn['height'] = 9





root = Tk()
bimg = PhotoImage(file="bill1.png")
cimg = PhotoImage(file="close.png")
rimg = PhotoImage(file="info1.png")

root.title("PROJECT BY DEVANSH")
root.geometry("1350x750+0+0")

root.bg_icon=ImageTk.PhotoImage(file="ibg.jpg")
bg_lbl = Label(root, image=root.bg_icon)
bg_lbl.pack()

top = Frame(root, width=1330, height=100,bg="purple", bd=10, relief="ridge", padx=0, pady=0)
top.place(x=10, y=10)
title = Label(top, font=("Helvetica", 52, "bold"), fg="darkorchid3", text="            Ice-Cream Billing System            ")
title.pack()

billBtn = Button(root, height=10, font=("georgia", 15), cursor="hand2", width=47, relief=RIDGE, pady=5, padx=5,
                 text="Billing System", background="steel blue", bd=10, command=bills)
billBtn.place(x=40, y=150)
billBtn.bind('<Enter>', billcolor1)
billBtn.bind('<Leave>', billcolor2)

RetrivalBtn = Button(root, height=10, font=("georgia", 15),cursor="hand2", width=47, relief=RIDGE, pady=5, padx=5,
                     text="Settings", background="steel blue", bd=10, command=retrival)
RetrivalBtn.place(x=700, y=150)
RetrivalBtn.bind('<Enter>', retcolor1)
RetrivalBtn.bind('<Leave>', retcolor2)


def quit():
    Quit = tkinter.messagebox.askyesno("Ice-Cream Billing System", "Are you sure want to exit the System..?")
    if Quit > 0:
        root.destroy()


ExitBtn = Button(root, height=7, font=("georgia", 15), cursor="hand2", width=65, relief=RIDGE, pady=5, padx=5,
                 text="Exit System", background="salmon", bd=10, command=quit)
ExitBtn.place(x=260, y=475)
ExitBtn.bind('<Enter>', closecolor1)
ExitBtn.bind('<Leave>', closecolor2)

adminBtn = Button(top, height=4, width=10, bd=7, relief=RIDGE, font=("georgia", 10, "bold"), text="Admin",
                  background="gold", command=admin_login)
adminBtn.place(x=0, y=3)



root.mainloop()
