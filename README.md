#  Italian Cafe Billing System

The **Italian Billing System** is a Python-based desktop GUI application developed using **Tkinter**. It is designed for small Italian cafés or restaurants to simplify the billing process. The software allows item selection, calculates the total cost (including GST), generates a bill, and even sends it to the customer's email directly.

## 🧾 Features
- GUI-based intuitive billing system
- Categorized Italian menu: Pasta, Veg Pizza, Non-Veg Pizza, Beverages
- Quantity-based price calculation
- Tax and total bill calculation
- Save and retrieve bills by Bill Number
- Print bill functionality
- Send generated bill via email to the customer
- Entry validation and error handling
- Item cap (up to 20 items)

## 🛠 Tools & Technologies Used
- **Language:** Python
- **GUI Framework:** Tkinter
- **Email Sending:** `smtplib`
- **Date & Time:** `datetime`
- **Utilities:** `os`, `tempfile`, `random`
- **IDE:** VS Code 

## 📦 Project Structure
```plaintext
ItalianBillingSystem/
│
├── bills/                     # Saved bill text files
├── icons/                     # Icons
├── italian_billing_system.py  # Main source code
└── README.md                  # Project documentation
