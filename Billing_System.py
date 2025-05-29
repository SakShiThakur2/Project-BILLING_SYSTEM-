# cosmaticFrame -> PASTA FRAME
# BATH SOAP -> Pesto
# FACE CREAM -> Papalina
# FACE WASH -> Spaghetti
# HAIR COLOR -> Marinara
# Shampoo -> Balognese
# BODY LOTION->  Carbonara

# grossFrame -> VEG PIZZA FRAME
# RICE -> Margherita
# OIL -> Neapolitan 
# DALL -> Lucas
# WHEAT ->  Alla Marinara
# SUGAR ->  Caprese
# TEA -> Ortolana

# drinkFrame -> Non-Veg Pizza
# COCA COLA -> Pepperoni
# MAZA -> Diavola
# PEPSI -> Chicken Tikka
# SPRITE -> Pollo Pesto
# DEW ->Pollo BBQ
# FROOTI -> Bolognese



from tkinter import*
from datetime import datetime
from tkinter import messagebox
import random,os,tempfile,smtplib

def clear():

    bathSoap_Entry.delete(0,END)
    faceCream_Entry.delete(0,END)
    faceWash_Entry.delete(0,END)
    hairSpray_Entry.delete(0,END)
    hairWash_Entry.delete(0,END)
    bodyLotion_Entry.delete(0,END)

    Rice_Entry.delete(0,END)
    oil_Entry.delete(0,END)
    dall_Entry.delete(0,END)
    wheat_Entry.delete(0,END)
    sugar_Entry.delete(0,END)
    Tea_Entry.delete(0,END)

    Cola_Entry.delete(0,END)
    maza_Entry.delete(0,END)
    Pepsi_Entry.delete(0,END)
    Sprite_Entry.delete(0,END)
    Dew_Entry.delete(0,END)
    Frooti_Entry.delete(0,END)

    Conclave_Entry.delete(0,END)
    Bingo_Entry.delete(0,END)
    BlueSparkel_Entry.delete(0,END)
    Orzata_Entry.delete(0,END)
    Chinotto_Entry.delete(0,END)
    Cedrata_Entry.delete(0,END)

    cosPrice_Entry.delete(0,END)
    grossPrice_Entry.delete(0,END)
    coldDrink_Entry.delete(0,END)

    PhoneEntry.delete(0,END)
    Bill_noEntry.delete(0,END)


    textArea.config(state=NORMAL)  # <--- Add this line first
    textArea.delete(1.0, END) 
    
    bathSoap_Entry.insert(0,0)
    faceCream_Entry.insert(0,0)
    faceWash_Entry.insert(0,0)
    hairSpray_Entry.insert(0,0)
    hairWash_Entry.insert(0,0)
    bodyLotion_Entry.insert(0,0)

    Rice_Entry.insert(0,0)
    oil_Entry.insert(0,0)
    dall_Entry.insert(0,0)
    wheat_Entry.insert(0,0)
    sugar_Entry.insert(0,0)
    Tea_Entry.insert(0,0)

    Cola_Entry.insert(0,0)
    maza_Entry.insert(0,0)
    Pepsi_Entry.insert(0,0)
    Sprite_Entry.insert(0,0)
    Dew_Entry.insert(0,0)
    Frooti_Entry.insert(0,0)

    Conclave_Entry.insert(0,0)
    Bingo_Entry.insert(0,0)
    BlueSparkel_Entry.insert(0,0)
    Orzata_Entry.insert(0,0)
    Chinotto_Entry.insert(0,0)
    Cedrata_Entry.insert(0,0)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_Textarea.get(1.0,END)
            reciver_address=recieverEntry.get()
            ob.sendmail(senderEntry.get(),reciver_address,message)
            ob.quit()
            messagebox.showinfo('Confirm',"Successfully send ",parent=root1)
            root1.destroy()
        
        except:
            messagebox.showerror('Error','Something went wrong',parent=root1)



    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('ERROR','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gold')
        root1.maxsize()
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=("arial",16,'bold'),bg='goldenrod',fg='midnight blue')
        senderFrame.grid(row=0,column=0,padx=40,pady=25)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='goldenrod',fg='midnight blue')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=40,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bd=6,bg='goldenrod',fg='midnight blue')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=40,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=("arial",16,'bold'),bd=6,bg='goldenrod',fg='midnight blue')
        recipientFrame.grid(row=1,column=0,padx=10,pady=20)

        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bd=6,bg='goldenrod',fg='midnight blue')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=40,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bd=6,bg='goldenrod',fg='midnight blue')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_Textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=3,relief=SUNKEN,width=57,height=15)
        email_Textarea.grid(row=2,column=0,columnspan=2)
        email_Textarea.delete(1.0,END)
        email_Textarea.insert(END,textArea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t        '))

        sendButton=Button(root1,text="SEND",font=('arial',16,'bold'),width=10,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=10)


        root1.mainloop()

def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==Bill_noEntry.get():
            f = open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        try:
            bill_content = textArea.get(1.0, END)
            # Use 'utf-8' encoding to handle special characters like ₹
            with open(f'bills/{billnumber}.txt', 'w', encoding='utf-8') as file:
                file.write(bill_content)
            
            messagebox.showinfo('Success', f'Bill {billnumber} is saved successfully')
            billnumber = random.randint(0, 1000000)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save the bill: {e}')


billnumber=random.randint(0,1000000)

def bill_area():
    mobile_number = PhoneEntry.get()

    if not mobile_number.isdigit() or len(mobile_number) != 10:
        messagebox.showerror("Error", "Customer Mobile No. must be exactly 10 digits!")
        return
    
    elif cosPrice_Entry.get()=='' or grossPrice_Entry.get()=='' or coldDrink_Entry.get()=='':
        messagebox.showerror("Error","No Products Are Selected !")

    elif cosPrice_Entry.get()=='0 Rs' and grossPrice_Entry.get()=='0 Rs' and coldDrink_Entry.get()=='0 Rs':
        messagebox.showerror("Error","No Products Are Selected !")
    
    else:
        # Insert bill details automatically
        textArea.config(state=NORMAL)  # Enable text area for system updates

        textArea.delete(1.0, END)  # Clear previous content (if needed)

        textArea.insert(END, "\t\t\tWELCOME CUSTOMER\n")
        textArea.insert(END, "\t\t\t  Little Italy\n")
        textArea.insert(END, f'\n--------------------------------------------------')
        textArea.insert(END, f'\nBill Number : {billnumber}')
        textArea.insert(END, f'\nCustomer Phone No. : {PhoneEntry.get()}')
        textArea.insert(END, f'\n===================================================')
        textArea.insert(END, '\nItem \t\tQuantity \t\tPrice \t\tAmount')
        textArea.insert(END, f'\n===================================================')

        if bathSoap_Entry.get() != '0':
            textArea.insert(END, f"\nPesto \t\t {bathSoap_Entry.get()} \t\t 280 \t\t{bathSoap} Rs")
        if faceCream_Entry.get() != '0':
            textArea.insert(END, f"\nPapalina \t\t {faceCream_Entry.get()} \t\t 260 \t\t{faceCream} Rs")
        if faceWash_Entry.get() != '0':
            textArea.insert(END, f"\nSpaghetti \t\t {faceWash_Entry.get()} \t\t 250 \t\t{faceWash} Rs")
        if hairSpray_Entry.get() != '0':
            textArea.insert(END, f"\nMarinara \t\t {hairSpray_Entry.get()} \t\t 270 \t\t{hairSpray} Rs")
        if hairWash_Entry.get() != '0':
            textArea.insert(END, f"\nBalognese \t\t {hairWash_Entry.get()} \t\t 300 \t\t{hairWash} Rs")
        if bodyLotion_Entry.get() != '0':
            textArea.insert(END, f"\nCarbonara \t\t {bodyLotion_Entry.get()} \t\t 310 \t\t{bodyLotion} Rs")

        if Rice_Entry.get() != '0':
            textArea.insert(END, f"\nMargherita \t\t {Rice_Entry.get()}  \t\t 320 \t\t{Rice} Rs")
        if oil_Entry.get() != '0':
            textArea.insert(END, f"\nNeapolitan\t\t {oil_Entry.get()} \t\t 350 \t\t{oil} Rs")
        if dall_Entry.get() != '0':
            textArea.insert(END, f"\nLucas\t\t {dall_Entry.get()} \t\t 360 \t\t{dall} Rs")
        if wheat_Entry.get() != '0':
            textArea.insert(END, f"\nAlla-Marinara\t\t {wheat_Entry.get()} \t\t 340 \t\t{wheat} Rs")
        if sugar_Entry.get() != '0':
            textArea.insert(END, f"\nCaprese\t\t {sugar_Entry.get()} \t\t 370 \t\t{sugar} Rs")
        if Tea_Entry.get() != '0':
            textArea.insert(END, f"\nOrtolana\t\t {Tea_Entry.get()} \t\t 380 \t\t{Tea} Rs")

        if Cola_Entry.get() != '0':
            textArea.insert(END, f"\nPepperoni \t\t {Cola_Entry.get()} \t\t 380 \t\t{cola} Rs")
        if maza_Entry.get() != '0':
            textArea.insert(END, f"\nDiavola \t\t {maza_Entry.get()} \t\t 390 \t\t{maza} Rs")
        if Pepsi_Entry.get() != '0':
            textArea.insert(END, f"\nChicken-Tikka \t\t {Pepsi_Entry.get()} \t\t 370 \t\t{Pepsi} Rs")
        if Sprite_Entry.get() != '0':
            textArea.insert(END, f"\nPollo-Pesto \t\t {Sprite_Entry.get()} \t\t 380 \t\t{Sprite} Rs")
        if Dew_Entry.get() != '0':
            textArea.insert(END, f"\nPollo-BBq \t\t {Dew_Entry.get()} \t\t 390 \t\t{Dew} Rs")
        if Frooti_Entry.get() != '0':
            textArea.insert(END, f"\nBolognese \t\t {Frooti_Entry.get()} \t\t 400 \t\t{Frooti} Rs")

        if Conclave_Entry.get() != '0':
            textArea.insert(END ,f"\nConclave \t\t {Conclave_Entry.get()} \t\t 140 \t\t{Conclave} RS")
        if Bingo_Entry.get() != '0':
            textArea.insert(END ,f"\nBingo \t\t {Bingo_Entry.get()} \t\t 130 \t\t{Bingo} RS")
        if BlueSparkel_Entry.get() != '0':
            textArea.insert(END ,f"\nBlue-Sparkel \t\t {BlueSparkel_Entry.get()} \t\t 150 \t\t{BlueSparkel} RS")
        if Orzata_Entry.get() != '0':
            textArea.insert(END ,f"\nOrzata \t\t {Orzata_Entry.get()} \t\t 160 \t\t{Orzata} RS")
        if Chinotto_Entry.get() != '0':
            textArea.insert(END ,f"\nChinotto \t\t {Chinotto_Entry.get()} \t\t 170 \t\t{Chinotto} RS")
        if Cedrata_Entry.get() != '0':
            textArea.insert(END ,f"\nCedrata \t\t {Cedrata_Entry.get()} \t\t 170 \t\t{Cendrata} RS")
        
        textArea.insert(END, f'\n-----------------------------------------------------')
        textArea.insert(END, f'\n\nTotal Bill \t\t\t{total_bill}')
        textArea.insert(END, f'\n-----------------------------------------------------')
        textArea.insert(END, f'\n\nPrice above are final \n(include of 5% GST,tax and Services Charges)')
        textArea.insert(END, f'\n\n\tThanks for visit, plz come again')

        save_bill()  # Save the bill automatically

        textArea.config(state=DISABLED)  # Disable manual editing after bill is inserted


def set_date():
    current_date_time = datetime.now().strftime("%d-%m-%Y , %H:%M:%S ")  # Format the date and time
    dateEntry.delete(0, END)  # Clear any existing text in the entry
    dateEntry.insert(0, current_date_time)  # Insert the current date and time

def total():
    global bathSoap,faceCream,faceWash,hairSpray,hairWash,bodyLotion
    global Rice,oil,dall,wheat,sugar,Tea
    global cola,maza,Pepsi,Sprite,Dew,Frooti
    global Conclave,Bingo,BlueSparkel,Orzata,Chinotto,Cendrata
    global cosPrice_Entry,grossPrice_Entry,coldDrink_Entry
    global total_bill


    # Get quantities from all entry fields
    try:
        bathSoap_qty = int(bathSoap_Entry.get())
        faceCream_qty = int(faceCream_Entry.get())
        faceWash_qty = int(faceWash_Entry.get())
        hairSpray_qty = int(hairSpray_Entry.get())
        hairWash_qty = int(hairWash_Entry.get())
        bodyLotion_qty = int(bodyLotion_Entry.get())

        Rice_qty = int(Rice_Entry.get())
        oil_qty = int(oil_Entry.get())
        dall_qty = int(dall_Entry.get())
        wheat_qty = int(wheat_Entry.get())
        sugar_qty = int(sugar_Entry.get())
        Tea_qty = int(Tea_Entry.get())

        cola_qty = int(Cola_Entry.get())
        maza_qty = int(maza_Entry.get())
        Pepsi_qty = int(Pepsi_Entry.get())
        Sprite_qty = int(Sprite_Entry.get())
        Dew_qty = int(Dew_Entry.get())
        Frooti_qty = int(Frooti_Entry.get())

        Conclave_qty = int(Conclave_Entry.get())
        Bingo_qty = int(Bingo_Entry.get())
        BlueSparkel_qty = int(BlueSparkel_Entry.get())
        Orzata_qty = int(Orzata_Entry.get())
        Chinotto_qty = int(Chinotto_Entry.get())
        Cendrata_qty = int(Cedrata_Entry.get())

        # Total items quantity
        total_items = (
            bathSoap_qty + faceCream_qty + faceWash_qty + hairSpray_qty + hairWash_qty + bodyLotion_qty +
            Rice_qty + oil_qty + dall_qty + wheat_qty + sugar_qty + Tea_qty +
            cola_qty + maza_qty + Pepsi_qty + Sprite_qty + Dew_qty + Frooti_qty +
            Conclave_qty + Bingo_qty + BlueSparkel_qty + Orzata_qty + Chinotto_qty + Cendrata_qty
        )

        if total_items > 20:
            messagebox.showerror("Limit Exceeded", "Only 20 items can be billed at a time.")
        else:
            # Cosmetics
            bathSoap = bathSoap_qty * 280
            faceCream = faceCream_qty * 260
            faceWash = faceWash_qty * 250
            hairSpray = hairSpray_qty * 270
            hairWash = hairWash_qty * 300
            bodyLotion = bodyLotion_qty * 310

            total_cos_price = bathSoap + faceCream + faceWash + hairSpray + hairWash + bodyLotion
            cosPrice_Entry.delete(0, END)
            cosPrice_Entry.insert(0, f'{total_cos_price} Rs')

            # Groceries
            Rice = Rice_qty * 320
            oil = oil_qty * 350
            dall = dall_qty * 360
            wheat = wheat_qty * 340
            sugar = sugar_qty * 370
            Tea = Tea_qty * 380

            cola = cola_qty * 380
            maza = maza_qty * 390
            Pepsi = Pepsi_qty * 370
            Sprite = Sprite_qty * 380
            Dew = Dew_qty * 390
            Frooti = Frooti_qty * 400

            total_gross_price = Rice + oil + dall + wheat + sugar + Tea + cola + maza + Pepsi + Sprite + Dew + Frooti
            grossPrice_Entry.delete(0, END)
            grossPrice_Entry.insert(0, f'{total_gross_price} Rs')

            # Drinks
            Conclave = Conclave_qty * 140
            Bingo = Bingo_qty * 130
            BlueSparkel = BlueSparkel_qty * 150
            Orzata = Orzata_qty * 160
            Chinotto = Chinotto_qty * 170
            Cendrata = Cendrata_qty * 170

            total_drink_price = Conclave + Bingo + BlueSparkel + Orzata + Chinotto + Cendrata
            coldDrink_Entry.delete(0, END)
            coldDrink_Entry.insert(0, f'{total_drink_price} Rs')

            # Total bill
            total_bill = total_cos_price + total_gross_price + total_drink_price
            

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric quantities.")

root =Tk()
root.title('billing System')   #title of the window
root.maxsize()
root.configure(bg='light pink')
root.iconbitmap('BILLING_SYATEM/pay_cash_payment_money_dollar_bill_icon_143267.ico') 
#by default the icon is leaf so we change the icon using method iconbitmap
root.resizable(0,0)



#-------------          HEADING LABEL(BILL EASE)        ------------------------------------------
#add font ,background color,font color for text, than add border (bd)to label in x-direction
headingLabel=Label(root,text='Italian Cafe Billing System',
                   font=('times new roman',26,'bold'),bg='steel blue2',fg='midnight blue',bd=5,relief=GROOVE)
headingLabel.pack(fill=X,pady=0)       
#position of label, so it simply add label in top fill=X is for completely fill label on x-axis


#----------------------------------                 CUSTOMER DETAILS LABEL FRAME         -----------------------------:
customer_detail_frame=LabelFrame(root,text='Customer Details',
                                 font=('times new roman',14,'bold'),fg='light sky blue',bd=5,relief=GROOVE,bg='orchid4')
customer_detail_frame.pack(fill=X,pady=0)

#<----------|     DATE TIME        |--------->
dateLabel=Label(customer_detail_frame,text='Date and Time',font=('times new roman',15,'bold'),bg='orchid4',fg='white')
dateLabel.grid(row=0,column=0,padx=30)

#<----------|      DATE TIME       |---------->
dateEntry=Entry(customer_detail_frame,font=('arial',12),bd=1,width=20)
dateEntry.grid(row=0,column=1,padx=30)

set_date()
#<----------|     PHONE       |---------->
PhoneLabel=Label(customer_detail_frame,text='Phone No.',font=('times new roman',15,'bold'),bg='orchid4',fg='white')
PhoneLabel.grid(row=0,column=2,padx=30,pady=2)

#<----------|     PHONE ENTRY     |---------->
PhoneEntry=Entry(customer_detail_frame,font=('arial',16),bd=1,width=20)
PhoneEntry.grid(row=0,column=3,padx=30)

#<----------|     BILL_NO     |---------->
Bill_noLabel=Label(customer_detail_frame,text='Bill No.',font=('times new roman',15,'bold'),bg='orchid4',fg='white')
Bill_noLabel.grid(row=0,column=4,padx=30,pady=2)

#<----------|     BILL_NO ENTRY       |---------->
Bill_noEntry=Entry(customer_detail_frame,font=('arial',12),bd=1,width=20)
Bill_noEntry.grid(row=0,column=5,padx=30)

#<----------|     SEARCH BUTTON       |---------->
searchButton=Button(customer_detail_frame,text='SEARCH',font=('arial',11,'bold'),bd=5,width=15,command=search_bill)
searchButton.grid(row=0,column=10,padx=30,pady=10)


#----------------------------------             PASTA LABEL FRAME         ------------------------------:
productFrame=Frame(root,bg='plum1')
productFrame.pack(pady=0)

# PASTA FRAME -> cosmaticFrame
cosmaticFrame=LabelFrame(productFrame,text='Pasta',
                                 font=('times new roman',20,'bold'),fg='dark blue',bd=5,relief=GROOVE,bg='light pink3')
cosmaticFrame.grid(row=0,column=0)
#   BATH SOAP -> Pesto    .................... 
bathSoapLabel=Label(cosmaticFrame,text='Pesto',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
bathSoapLabel.grid(row=0,column=0,pady=10,padx=10,sticky='w')

bathSoap_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
bathSoap_Entry.grid(row=0,column=1,pady=10,padx=10,sticky='w')
bathSoap_Entry.insert(0,0)

#    FACE CREAM -> Papalina   ......
faceCreamLabel=Label(cosmaticFrame,text='Papalina',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
faceCreamLabel.grid(row=1,column=0,pady=10,padx=10,sticky='w')

faceCream_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
faceCream_Entry.grid(row=1,column=1,pady=10,padx=10,sticky='w')
faceCream_Entry.insert(0,0)
#   FACE WASH -> Spaghetti  ...........
faceWashLabel=Label(cosmaticFrame,text='Spaghetti',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
faceWashLabel.grid(row=2,column=0,pady=10,padx=10,sticky='w')

faceWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
faceWash_Entry.grid(row=2,column=1,pady=10,padx=10,sticky='w')
faceWash_Entry.insert(0,0)
#   HAIR COLOR -> Marinara  ..............
hairSprayLabel=Label(cosmaticFrame,text='Marinara',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
hairSprayLabel.grid(row=3,column=0,pady=10,padx=10,sticky='w')

hairSpray_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
hairSpray_Entry.grid(row=3,column=1,pady=10,padx=10,sticky='w')
hairSpray_Entry.insert(0,0)
#   Shampoo -> Balognese  ..........
hairWashLabel=Label(cosmaticFrame,text='Balognese',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
hairWashLabel.grid(row=4,column=0,pady=10,padx=10,sticky='w')

hairWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
hairWash_Entry.grid(row=4,column=1,pady=10,padx=10,sticky='w')
hairWash_Entry.insert(0,0)
#   BODY LOTION->  Carbonara .........
bodyLotionLabel=Label(cosmaticFrame,text='Carbonara',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
bodyLotionLabel.grid(row=5,column=0,pady=10,padx=10,sticky='w')

bodyLotion_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=8,bd=2)
bodyLotion_Entry.grid(row=5,column=1,pady=10,padx=10,sticky='w')
bodyLotion_Entry.insert(0,0)



# -----------        VEG PIZZA     -------------------     
# grossFrame -> VEG PIZZA FRAME
grossFrame=LabelFrame(productFrame,text='Veg Pizza',
                                 font=('times new roman',20,'bold'),fg='dark blue',bd=5,relief=GROOVE,bg='light pink3')
grossFrame.grid(row=0,column=1)
#    RICE -> Margherita  ... 
RiceLabel=Label(grossFrame,text='Margherita',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
RiceLabel.grid(row=0,column=0,pady=10,padx=10,sticky='w')

Rice_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Rice_Entry.grid(row=0,column=1,pady=10,padx=10,sticky='w')
Rice_Entry.insert(0,0)

#  OIL -> Neapolitan ............
oilLabel=Label(grossFrame,text='Neapolitan',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
oilLabel.grid(row=1,column=0,pady=10,padx=10,sticky='w')

oil_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
oil_Entry.grid(row=1,column=1,pady=10,padx=10,sticky='w')
oil_Entry.insert(0,0)

# DALL -> Lucas ..........
dallLabel=Label(grossFrame,text='Lucas',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
dallLabel.grid(row=2,column=0,pady=10,padx=10,sticky='w')

dall_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
dall_Entry.grid(row=2,column=1,pady=10,padx=10,sticky='w')
dall_Entry.insert(0,0)

#  WHEAT ->  Alla Marinara...........
wheatLabel=Label(grossFrame,text='Alla Marinara',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
wheatLabel.grid(row=3,column=0,pady=10,padx=10,sticky='w')

wheat_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
wheat_Entry.grid(row=3,column=1,pady=10,padx=10,sticky='w')
wheat_Entry.insert(0,0)
#    SUGAR ->  Caprese............
sugarLabel=Label(grossFrame,text='Caprese',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
sugarLabel.grid(row=4,column=0,pady=10,padx=10,sticky='w')

sugar_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
sugar_Entry.grid(row=4,column=1,pady=10,padx=10,sticky='w')
sugar_Entry.insert(0,0)
#     TEA -> Ortolana...............
TeaLabel=Label(grossFrame,text='Ortolana',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
TeaLabel.grid(row=5,column=0,pady=10,padx=10,sticky='w')

Tea_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Tea_Entry.grid(row=5,column=1,pady=10,padx=10,sticky='w')
Tea_Entry.insert(0,0)




# ---------- NON VEG PIZZA   --------------------
# drinkFrame -> Non-Veg Pizza
drinkFrame=LabelFrame(productFrame,text='Non-Veg Pizza',
                                 font=('times new roman',20,'bold'),fg='dark blue',bd=5,relief=GROOVE,bg='light pink3')
drinkFrame.grid(row=0,column=2)
#    COCA COLA -> Pepperoni   .............. 
ColaLabel=Label(drinkFrame,text='Pepperoni',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
ColaLabel.grid(row=0,column=0,pady=10,padx=10,sticky='w')

Cola_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Cola_Entry.grid(row=0,column=1,pady=10,padx=10,sticky='w')
Cola_Entry.insert(0,0)
#    MAZA -> Diavola   ............................................................ 
mazaLabel=Label(drinkFrame,text='Diavola',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
mazaLabel.grid(row=1,column=0,pady=10,padx=10,sticky='w')

maza_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
maza_Entry.grid(row=1,column=1,pady=10,padx=10,sticky='w')
maza_Entry.insert(0,0)
#    PEPSI -> Chicken Tikka   ............................................................ 
PepsiLabel=Label(drinkFrame,text='Chicken Tikka',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
PepsiLabel.grid(row=2,column=0,pady=10,padx=10,sticky='w')
Pepsi_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Pepsi_Entry.grid(row=2,column=1,pady=10,padx=10,sticky='w')
Pepsi_Entry.insert(0,0)

#    SPRITE -> Pollo Pesto  ............................................................ 
SpriteLabel=Label(drinkFrame,text='Pollo Pesto',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
SpriteLabel.grid(row=3,column=0,pady=10,padx=10,sticky='w')

Sprite_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Sprite_Entry.grid(row=3,column=1,pady=10,padx=10,sticky='w')
Sprite_Entry.insert(0,0)
#    DEW ->Pollo BBQ   ............................................................ 
DewLabel=Label(drinkFrame,text='Pollo BBQ',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
DewLabel.grid(row=4,column=0,pady=10,padx=10,sticky='w')

Dew_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Dew_Entry.grid(row=4,column=1,pady=10,padx=10,sticky='w')
Dew_Entry.insert(0,0)
#    FROOTI -> Bolognese    ................. 
FrootiLabel=Label(drinkFrame,text='Bolognese',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
FrootiLabel.grid(row=5,column=0,pady=10,padx=10,sticky='w')

Frooti_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Frooti_Entry.grid(row=5,column=1,pady=10,padx=10,sticky='w')
Frooti_Entry.insert(0,0)



# --------         DRINK (Beverages)  -----------------------------

BeveragesFrame=LabelFrame(productFrame,text='Beverages',
                                 font=('times new roman',20,'bold'),fg='dark blue',bd=5,relief=GROOVE,bg='light pink3')
BeveragesFrame.grid(row=0,column=3)

#    Conclave  ................... 
ConclaveLabel=Label(BeveragesFrame,text='Conclave',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
ConclaveLabel.grid(row=0,column=0,pady=10,padx=10,sticky='w')

Conclave_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Conclave_Entry.grid(row=0,column=1,pady=10,padx=10,sticky='w')
Conclave_Entry.insert(0,0)
#   Bingo   ....................... 
BingoLabel=Label(BeveragesFrame,text='Bingo',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
BingoLabel.grid(row=1,column=0,pady=10,padx=10,sticky='w')

Bingo_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Bingo_Entry.grid(row=1,column=1,pady=10,padx=10,sticky='w')
Bingo_Entry.insert(0,0)
# Blue Sparkel ................. 
BlueSparkelLabel=Label(BeveragesFrame,text='Blue Sparkel',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
BlueSparkelLabel.grid(row=2,column=0,pady=10,padx=10,sticky='w')

BlueSparkel_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
BlueSparkel_Entry.grid(row=2,column=1,pady=10,padx=10,sticky='w')
BlueSparkel_Entry.insert(0,0)

# Orzata .............. 
OrzataLabel=Label(BeveragesFrame,text='Orzata',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
OrzataLabel.grid(row=3,column=0,pady=10,padx=10,sticky='w')

Orzata_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Orzata_Entry.grid(row=3,column=1,pady=10,padx=10,sticky='w')
Orzata_Entry.insert(0,0)
#    Chinotto   ..................... 
ChinottoLabel=Label(BeveragesFrame,text='Chinotto',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
ChinottoLabel.grid(row=4,column=0,pady=10,padx=10,sticky='w')

Chinotto_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Chinotto_Entry.grid(row=4,column=1,pady=10,padx=10,sticky='w')
Chinotto_Entry.insert(0,0)
# Cedrata   .......................... 
CedrataLabel=Label(BeveragesFrame,text='Cedrata',
                                 font=('times new roman',15,'bold'),fg='purple4',bd=0,relief=GROOVE,bg='light pink3')
CedrataLabel.grid(row=5,column=0,pady=10,padx=10,sticky='w')

Cedrata_Entry=Entry(BeveragesFrame,font=('times new roman',13,'bold'),width=8,bd=2)
Cedrata_Entry.grid(row=5,column=1,pady=10,padx=10,sticky='w')
Cedrata_Entry.insert(0,0)


# ******************************************        BILL FRAME          *********************************************************

billFrame=Frame(productFrame,bd=5,bg='light goldenrod',relief=GROOVE)
billFrame.grid(row=0,column=4,padx=15)

billareaLabel=Label(billFrame,text="Bill Area",font=('times new roman',15,'bold'),bd=8,relief=GROOVE)
billareaLabel.pack(fill=X)


scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)


textArea=Text(billFrame,height=20,width=60,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)

# ------------------------------------------------------------------------------------
BillMenueFrame=LabelFrame(root,text='Bill Menu',
                                 font=('times new roman',16,'bold'),fg='blue',bd=5,relief=GROOVE,bg='plum3')
BillMenueFrame.pack(fill=X)
# PASTA TOTAL PRICE 
cosPriceLabel=Label(BillMenueFrame,text='Pasta',
                                 font=('times new roman',15,'bold'),fg='purple',bd=0,relief=GROOVE,bg='plum3')
cosPriceLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')
cosPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
cosPrice_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
# PIZZA TOTAL PRICE (VEG + NON VEG)
grossPriceLabel=Label(BillMenueFrame,text='Pizza',
                                 font=('times new roman',15,'bold'),fg='purple',bd=0,relief=GROOVE,bg='plum3')
grossPriceLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')
grossPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
grossPrice_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
# BEVERAGES TOTAL PRICE 
coldDrinkLabel=Label(BillMenueFrame,text='Beverages',
                                 font=('times new roman',15,'bold'),fg='purple',bd=0,relief=GROOVE,bg='plum3')
coldDrinkLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')
coldDrink_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
coldDrink_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')

buttonFrame=Frame(BillMenueFrame,bd=3,relief=GROOVE,bg='plum1')
buttonFrame.grid(row=0,column=5,rowspan=3)

totalButton = Button(buttonFrame,text="Total",font=('arial',18,'bold'),bg='purple',fg='white',bd=3,width=10,pady=6,command=total)
totalButton.grid(row=0,column=0,pady=15,padx=15)

billButton = Button(buttonFrame,text="Bill",font=('arial',18,'bold'),bg='purple',fg='white',bd=3,width=10,pady=6,command=bill_area)
billButton.grid(row=0,column=1,pady=15,padx=15)

emailButton = Button(buttonFrame,text="Email",font=('arial',18,'bold'),bg='purple',fg='white',bd=3,width=10,pady=6,command=send_email)
emailButton.grid(row=0,column=2,pady=15,padx=15)

printButton = Button(buttonFrame,text="Print",font=('arial',18,'bold'),bg='purple',fg='white',bd=3,width=10,pady=6,command=print_bill)
printButton.grid(row=0,column=3,pady=15,padx=15)

clearButton = Button(buttonFrame,text="Clear",font=('arial',18,'bold'),bg='purple',fg='white',bd=3,width=10,pady=6,command=clear)
clearButton.grid(row=0,column=4,pady=15,padx=15)

root.mainloop()   # it move vry fast so it help to viewing our window

