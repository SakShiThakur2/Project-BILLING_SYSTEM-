#  Billing System

The **Billing System( or Italian Billing System)** is a Python-based desktop GUI application developed using **Tkinter**. It is designed for small Italian cafés or restaurants to simplify the billing process. The software allows item selection, calculates the total cost (including GST), generates a bill, and even sends it to the customer's email directly.

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

## 🖥️ Main Billing System Interface
<img width="1878" height="912" alt="Screenshot 2026-01-17 203444" src="https://github.com/user-attachments/assets/19a1922a-a58a-4722-994b-86617c0ca28d" />

<img width="1920" height="1020" alt="Screenshot 2026-01-17 203645" src="https://github.com/user-attachments/assets/02af2aaa-17fc-4a4c-9a80-826ea67480cf" />

<img width="906" height="987" alt="Screenshot 2026-01-17 203748" src="https://github.com/user-attachments/assets/99e70a45-bb91-4bfd-b800-9a709bd4cb21" />

<img width="1878" height="912" alt="Screenshot 2026-01-17 204931" src="https://github.com/user-attachments/assets/08ce0ea6-b8e3-4c20-9945-144eba130cea" />

## 📦 Project Structure
```plaintext
ItalianBillingSystem/
│
├── bills/                     # Saved bill text files
├── icons/                     # Icons
├── italian_billing_system.py  # Main source code
└── README.md                  # Project documentation


