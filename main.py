"""
Supermarket Billing System
This Python-based application provides a simple and efficient way to manage billing operations in a supermarket setting.

jeninsutradhar@gmail.com
"""
import os
import random
import sys
# Tkinter for Graphical User-Interface
from tkinter import *
from tkinter import messagebox


class Bill_App:

    def _insert_products(self, widget, product_name, price):
        """
        This function is used to insert the product information into the text area.
        It checks if the quantity of the product is not zero. If it's not zero, it
        inserts the product name, quantity, and price into the text area.
        
        Args:
            widget (Tkinter variable): The Tkinter variable representing the quantity of the product.
            product_name (str): The name of the product.
            price (str): The price of the product.
            
        Returns:
            None
        """
        if widget.get() != 0:
            self.txtarea.insert(END, f"{product_name}\t\t {widget.get()}\t{price}\n")

    def _insert_tax(self, widget, tax_name):
        """
        This function is used to insert the tax information into the text area.
        It checks if the tax amount is not "0.0 Rs". If it's not "0.0 Rs", it
        inserts the tax name and amount into the text area.
        
        Args:
            widget (Tkinter variable): The Tkinter variable representing the tax amount.
            tax_name (str): The name of the tax.
            
        Returns:
            None
        """
        if widget.get() != "0.0 Rs":
            self.txtarea.insert(END, f"{tax_name} : {widget.get()}\n")

    def __init__(self, root):
        self.root = root
        self.root.geometry("1340x750+0+0")  # UI Dimensions
        self.root.configure(bg="#f0f0f0")  # Light Grey background
        self.root.title("Billing Software")  # Title

        # =========================== Main UI ===========================
        # Title Heading
        title = Label(
            self.root,
            text="SuperMarket Billing System",
            bd=12,
            relief=FLAT,
            font=("Poppin", 20, "bold"),
            bg="#9e9e9e",
            fg="black",
        ).pack(fill=X)

        # =========================== Variables =========================
        # snacks
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()
        self.pasta = IntVar()

        # Grocery
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.atta = IntVar()

        # Beauty & Hygine
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()

        # Total
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()

        # store the total cost of products
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()  # Customer name
        self.bill_no = StringVar()  # Bill no.

        # Other
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()  # Customer Phone Number

        # =========================== Customer Details Label Frame =========================
        details = LabelFrame(
            self.root,
            text="Customer Details :",
            font=("Arial", 14, "bold"),
            bg="#f7f7f7",
            fg="black",
            relief=FLAT,
            bd=10,
        )
        details.place(x=0, y=80, relwidth=1)
        # Customer Name
        cust_name = Label(
            details, text="Customer Name:", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=0, padx=15)
        cust_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.c_name
        ).grid(row=0, column=1, padx=8)
        # Customer's Contact Number
        contact_name = Label(
            details, text="Contact No.", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=2, padx=10)
        contact_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.phone
        ).grid(row=0, column=3, padx=8)
        # Bill number
        bill_name = Label(
            details, text="Bill.No.", font=("Arial", 13), bg="#f7f7f7", fg="black"
        ).grid(row=0, column=4, padx=10)
        bill_entry = Entry(
            details, borderwidth=2, width=30, textvariable=self.bill_no
        ).grid(row=0, column=5, padx=8)

        # =========================== Snacks Label Frame ===================================
        snacks = LabelFrame(
            self.root,
            text="Snacks",
            font=("Arial", 12, "bold"),
            bg="#f7f7f7",
            fg="black",
            relief=FLAT,
            bd=10,
        )
        snacks.place(x=5, y=180, height=400, width=325)
        # Neutella
        item1 = Label(
            snacks,
            text="Nutella Choco Spread",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=0, column=0, pady=11)
        item1_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.nutella
        ).grid(row=0, column=1, padx=10)
        # Noodles
        item2 = Label(
            snacks,
            text="Noodles(1 Pack)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=1, column=0, pady=11)
        item2_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.noodles
        ).grid(row=1, column=1, padx=10)
        # Lays
        item3 = Label(
            snacks,
            text="Lays(10Rs)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=2, column=0, pady=11)
        item3_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.lays
        ).grid(row=2, column=1, padx=10)
        # Oreo
        item4 = Label(
            snacks,
            text="Oreo(20Rs)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=3, column=0, pady=11)
        item4_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.oreo
        ).grid(row=3, column=1, padx=10)
        # Muffin
        item5 = Label(
            snacks,
            text="Chocolate Muffin",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=4, column=0, pady=11)
        item5_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.muffin
        ).grid(row=4, column=1, padx=10)
        # Silk
        item6 = Label(
            snacks,
            text="Cadbury Silk",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=5, column=0, pady=11)
        item6_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.silk
        ).grid(row=5, column=1, padx=10)
        # Namkeen
        item7 = Label(
            snacks,
            text="Namkeen (400g)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=6, column=0, pady=11)
        item7_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.namkeen
        ).grid(row=6, column=1, padx=10)
        # Pasta
        item8 = Label(
            snacks,
            text="Maggi Pasta",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=7, column=0, pady=11)
        item8_entry = Entry(
            snacks, borderwidth=2, width=15, textvariable=self.pasta
        ).grid(row=7, column=1, padx=10)

        # =========================== Grocery Label Frame ===================================
        grocery = LabelFrame(
            self.root,
            text="Grocery",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        grocery.place(x=340, y=180, height=400, width=325)
        # Atta
        item9 = Label(
            grocery,
            text="Aashirvaad Atta(1kg)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=0, column=0, pady=11)
        item9_entry = Entry(
            grocery, borderwidth=2, width=15, textvariable=self.atta
        ).grid(row=0, column=1, padx=10)
        # Rice
        item10 = Label(
            grocery,
            text="Basmathi Rice(1kg)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=2, column=0, pady=11)
        item10_entry = Entry(
            grocery, borderwidth=2, width=15, textvariable=self.rice
        ).grid(row=2, column=1, padx=10)
        # Sugar
        item12 = Label(
            grocery,
            text="Refined Sugar(1kg)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=4, column=0, pady=11)
        item12_entry = Entry(
            grocery, borderwidth=2, width=15, textvariable=self.sugar
        ).grid(row=4, column=1, padx=10)
        # Dal
        item13 = Label(
            grocery,
            text="Daal(1kg)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=5, column=0, pady=11)
        item13_entry = Entry(
            grocery, borderwidth=2, width=15, textvariable=self.dal
        ).grid(row=5, column=1, padx=10)
        # Tea
        item14 = Label(
            grocery,
            text="Tea Powder(1kg)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=6, column=0, pady=11)
        item14_entry = Entry(
            grocery, borderwidth=2, width=15, textvariable=self.tea
        ).grid(row=6, column=1, padx=10)

        # =========================== Beauty and Hygine Label Frame ===================================
        hygine = LabelFrame(
            self.root,
            text="Beauty & Hygine",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        hygine.place(x=677, y=180, height=400, width=325)
        # Soap
        item15 = Label(
            hygine,
            text="Bathing Soap",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=0, column=0, pady=11)
        item15_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.soap
        ).grid(row=0, column=1, padx=10)
        # Shampoo
        item16 = Label(
            hygine,
            text="Shampoo(1ltr)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=1, column=0, pady=11)
        item16_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.shampoo
        ).grid(row=1, column=1, padx=10)
        # Lotion
        item17 = Label(
            hygine,
            text="Body Lotion(1ltr)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=2, column=0, pady=11)
        item17_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.lotion
        ).grid(row=2, column=1, padx=10)
        # Cream
        item18 = Label(
            hygine,
            text="Face Cream",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=3, column=0, pady=11)
        item18_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.cream
        ).grid(row=3, column=1, padx=10)
        # Foam
        item19 = Label(
            hygine,
            text="Shaving Foam",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=4, column=0, pady=11)
        item19_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.foam
        ).grid(row=4, column=1, padx=10)
        # Mask
        item20 = Label(
            hygine,
            text="Face Mask(1piece)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=5, column=0, pady=11)
        item20_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.mask
        ).grid(row=5, column=1, padx=10)
        # Sanitizer
        item21 = Label(
            hygine,
            text="Hand Sanitizer(50ml)",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="#6C3483",
        ).grid(row=6, column=0, pady=11)
        item21_entry = Entry(
            hygine, borderwidth=2, width=15, textvariable=self.sanitizer
        ).grid(row=6, column=1, padx=10)

        # ================================ BILLAREA ===================================
        billarea = Frame(self.root, bd=10, relief=FLAT, bg="#f7f7f7")
        billarea.place(x=1010, y=180, width=330, height=400)

        bill_title = Label(
            billarea,
            text="Bill Area",
            font=("Arial", 17, "bold"),
            bd=7,
            relief=FLAT,
            bg="#f7f7f7",
            fg="black",
        ).pack(fill=X)

        # Create a vertical scrollbar widget
        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        # Create a text widget for displaying the bill, linking it with the scrollbar
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        # Pack the scrollbar widget to the right side of its container, filling the Y-axis
        scrol_y.pack(side=RIGHT, fill=Y)
        # Configure the scrollbar to scroll the text widget's view
        scrol_y.config(command=self.txtarea.yview)
        # Pack the text widget to fill the available space and allow expansion
        self.txtarea.pack(fill=BOTH, expand=1)

        # =================================================billing menu=========================================================================================
        billing_menu = LabelFrame(
            self.root,
            text="Billing Summary",
            font=("Arial", 12, "bold"),
            relief=FLAT,
            bd=10,
            bg="#f7f7f7",
            fg="black",
        )
        billing_menu.place(x=0, y=600, relwidth=1, height=150)

        # ==== TOTAL ====
        # Total Snacks Price
        total_snacks = Label(
            billing_menu,
            text="Total Snacks Price",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=0, column=0)
        total_snacks_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.total_sna
        ).grid(row=0, column=1, padx=10, pady=7)
        # Total Grocery Price
        total_grocery = Label(
            billing_menu,
            text="Total Grocery Price",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=1, column=0)
        total_grocery_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.total_gro
        ).grid(row=1, column=1, padx=10, pady=7)
        # Total Hygine Price
        total_hygine = Label(
            billing_menu,
            text="Total Beauty & Hygine Price",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=2, column=0)
        total_hygine_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.total_hyg
        ).grid(row=2, column=1, padx=10, pady=7)

        # ==== TAX ====
        # Snacks Tax
        tax_snacks = Label(
            billing_menu,
            text="Snacks Tax",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=0, column=2)
        tax_snacks_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.a
        ).grid(row=0, column=3, padx=10, pady=7)
        # Grocery Tax
        tax_grocery = Label(
            billing_menu,
            text="Grocery Tax",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=1, column=2)
        tax_grocery_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.b
        ).grid(row=1, column=3, padx=10, pady=7)
        # Hygine Tax
        tax_hygine = Label(
            billing_menu,
            text="Beauty & Hygine Tax",
            font=("Arial Black", 11),
            bg="#ffffff",
            fg="black",
        ).grid(row=2, column=2)
        tax_hygine_entry = Entry(
            billing_menu, width=30, borderwidth=1, textvariable=self.c
        ).grid(row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=4, relief=GROOVE, bg="white")
        button_frame.place(x=900, width=400, height=95)

        button_total = Button(
            button_frame,
            text="Total Bill",
            font=("Arial Black", 15),
            pady=10,
            bg="white",
            fg="#6C3483",
            relief=FLAT,
            command=lambda: total(self),
        ).grid(row=0, column=0, padx=12, pady=6)
        button_clear = Button(
            button_frame,
            text="Clear Field",
            font=("Arial Black", 15),
            pady=10,
            bg="white",
            fg="#6C3483",
            relief=FLAT,
            command=lambda: clear(self),
        ).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(
            button_frame,
            text="Exit",
            font=("Arial Black", 15),
            pady=10,
            bg="white",
            fg="#6C3483",
            width=5,
            relief=FLAT,
            command=lambda: exitbtn(self),
        ).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


# Function to calculate the total bill
def total(self):
    # Check if customer details are filled
    if self.c_name.get() == "" or self.phone.get() == "":
        messagebox.showerror("Error", "Fill the complete Customer Details!!")

    # Calculate the total price of snacks
    # Each snack is priced at Rs. 120
    self.nu = self.nutella.get() * 120
    self.no = self.noodles.get() * 40
    self.la = self.lays.get() * 10
    self.ore = self.oreo.get() * 20
    self.mu = self.muffin.get() * 30
    self.si = self.silk.get() * 60
    self.na = self.namkeen.get() * 15
    total_snacks_price = (
        self.nu + self.no + self.la + self.ore + self.mu + self.si + self.na
    )

    # Set the total snacks price in the UI
    self.total_sna.set(str(total_snacks_price) + " Rs")

    # Calculate the tax on snacks
    self.a.set(str(round(total_snacks_price * 0.05, 3)) + " Rs")

    # Calculate the total price of grocery
    # Each product is priced at a different rate
    self.at = self.atta.get() * 42
    self.pa = self.pasta.get() * 120
    self.oi = self.oil.get() * 113
    self.ri = self.rice.get() * 160
    self.su = self.sugar.get() * 55
    self.te = self.tea.get() * 480
    self.da = self.dal.get() * 76
    total_grocery_price = (
        self.at + self.pa + self.oi + self.ri + self.su + self.te + self.da
    )

    # Set the total grocery price in the UI
    self.total_gro.set(str(total_grocery_price) + " Rs")

    # Calculate the tax on grocery
    self.b.set(str(round(total_grocery_price * 0.01, 3)) + " Rs")

    # Calculate the total price of beauty and hygiene
    # Each product is priced at a different rate
    self.so = self.soap.get() * 30
    self.sh = self.shampoo.get() * 180
    self.cr = self.cream.get() * 130
    self.lo = self.lotion.get() * 500
    self.fo = self.foam.get() * 85
    self.ma = self.mask.get() * 100
    self.sa = self.sanitizer.get() * 20
    total_hygine_price = (
        self.so + self.sh + self.cr + self.lo + self.fo + self.ma + self.sa
    )

    # Set the total hygiene price in the UI
    self.total_hyg.set(str(total_hygine_price) + " Rs")

    # Calculate the tax on hygiene
    self.c.set(str(round(total_hygine_price * 0.10, 3)) + " Rs")

    # Calculate the total bill
    self.total_all_bill = (
        total_snacks_price
        + total_grocery_price
        + total_hygine_price
        + (round(total_grocery_price * 0.01, 3))
        + (round(total_hygine_price * 0.10, 3))
        + (round(total_snacks_price * 0.05, 3))
    )

    # Set the total bill in the UI
    self.total_all_bil = str(self.total_all_bill) + " Rs"

    # Print the billing details
    billarea(self)


# Functions to print the bill
def intro(self):
    """
    This function is responsible for clearing the text area and inserting the
    necessary information to display the billing details.

    It deletes the contents of the text area from index 0.1 to the end.
    Then, it inserts the store details and the customer details.
    Afterwards, it inserts the heading for the product information.

    The inserted information is formatted in a specific way to make it visually
    appealing when displayed in the UI.
    """

    # Clear the text area from index 0.1 to the end
    self.txtarea.delete(0.1, END)

    # Insert the store details
    self.txtarea.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")

    # Insert the bill number and customer details
    self.txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")

    # Insert the heading for the product information
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    """
    This function is responsible for printing the billing details.
    It inserts the product information, taxes, and the total bill amount
    into the text area.
    """

    # Insert the product information
    self._insert_products(self.nutella, "Nutella", self.nu)
    self._insert_products(self.noodles, "Noodles", self.no)
    self._insert_products(self.lays, "Lays", self.la)
    self._insert_products(self.oreo, "Oreo", self.ore)
    self._insert_products(self.muffin, "Muffins", self.mu)
    self._insert_products(self.silk, "Silk", self.si)
    self._insert_products(self.namkeen, "Namkeen", self.na)
    self._insert_products(self.atta, "Atta", self.at)
    self._insert_products(self.pasta, "Pasta", self.pa)
    self._insert_products(self.rice, "Rice", self.ri)
    self._insert_products(self.oil, "Oil", self.oi)
    self._insert_products(self.sugar, "Sugar", self.su)
    self._insert_products(self.dal, "Daal", self.da)
    self._insert_products(self.tea, "Tea", self.te)
    self._insert_products(self.soap, "Soap", self.so)
    self._insert_products(self.shampoo, "Shampoo", self.sh)
    self._insert_products(self.lotion, "Lotion", self.lo)
    self._insert_products(self.cream, "Cream", self.cr)
    self._insert_products(self.foam, "Foam", self.fo)
    self._insert_products(self.mask, "Mask", self.ma)
    self._insert_products(self.sanitizer, "Sanitizer", self.sa)

    # Insert the taxes
    self._insert_tax(self.a, "Total Snacks Tax")
    self._insert_tax(self.b, "Total Grocery Tax")
    self._insert_tax(self.c, "Total Beauty & Hygiene Tax")

    # Insert the total bill amount
    self.txtarea.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    for widget in [
        self.nutella,
        self.noodles,
        self.lays,
        self.oreo,
        self.muffin,
        self.silk,
        self.namkeen,
        self.atta,
        self.pasta,
        self.rice,
        self.oil,
        self.sugar,
        self.dal,
        self.tea,
        self.soap,
        self.shampoo,
        self.lotion,
        self.cream,
        self.foam,
        self.mask,
        self.sanitizer,
        self.total_sna,
        self.total_gro,
        self.total_hyg,
        self.a,
        self.b,
        self.c,
        self.c_name,
        self.bill_no,
        self.phone,
    ]:
        widget.set(0)


def exitbtn(self):
    """
    This function is a method of the Bill_App class. It is used to exit the
    application. When the exit button is clicked, it calls the `destroy`
    method of the root (main) Tkinter window. This method closes the window and
    ends the application.

    Args:
        self: The instance of the class.

    Returns:
        None
    """
    # Call the `destroy` method of the root window to close the application.
    self.root.destroy()


# Create a Tkinter root window
root = Tk()

# Create an instance of the Bill_App class and pass the root window as an argument
obj = Bill_App(root)

# Start the Tkinter main event loop, which will run the application
# and allow the user to interact with it
root.mainloop()

