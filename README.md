🎬 CINEVERSE - Movie Ticket Booking System

A beginner-friendly Movie Ticket Booking System built using Python and Streamlit.

CINEVERSE allows users to select a movie, choose the date and show time, select a screen and ticket type, enter customer details, calculate discounts and GST, and confirm a movie ticket booking.

📌 Project Overview

This project demonstrates how Python and Streamlit can be used to build a real-world interactive movie booking application.

The application provides:

🎬 Movie selection

📅 Movie date selection

⏰ Show time selection

🖥️ Screen type selection

🎟️ Ticket category selection

👥 Number of tickets

👤 Customer details

🎁 Automatic discount calculation

🧾 GST calculation

💰 Final payment calculation

🎉 Booking confirmation

🔖 Automatic booking ID generation

🔄 Reset booking option

🛠️ Technologies Used

Technology

Purpose

Python

Application logic

Streamlit

Interactive web interface

Datetime

Booking date, time and booking ID

📁 Project Structure

Movie-Ticket-Booking/
│
├── movie_ticket_booking.py
├── requirements.txt
└── README.md

File Description

movie_ticket_booking.py
Contains the complete CINEVERSE movie ticket booking application.

requirements.txt
Contains the external Python packages required to run the application.

README.md
Contains project information, setup instructions, features and usage details.

✨ Features

1. 🎬 Movie Selection

Users can select from the available movies:

🦸 Superhero Universe

🧙 Magic Kingdom

🚀 Space Mission

❤️ Love Forever

😂 Crazy Friends

👻 Haunted House

Each movie contains information such as description, language, rating and duration.

2. 🎟️ Ticket Types

The application provides three ticket categories:

Ticket Type

Price

🎟️ Standard

₹150

💺 Premium

₹250

👑 VIP

₹400

3. ⏰ Show Times

Available show times are:

10:00 AM

1:30 PM

4:30 PM

7:30 PM

10:30 PM

4. 🖥️ Screen Types

Users can choose:

🎬 2D

✨ 3D

🔥 IMAX

5. 👥 Number of Tickets

Users can book between 1 and 10 tickets.

6. 🎁 Discount System

The application automatically applies discounts based on the number of tickets.

Tickets

Discount

1–2

0%

3–4

5%

5–10

10%

7. 🧾 GST Calculation

GST is calculated at 18% after applying the ticket discount.

8. 👤 Customer Validation

The application validates:

Full name

10-digit phone number

Email address

The booking cannot be confirmed until valid customer details are entered.

9. 🎉 Booking Confirmation

After successful validation, the application displays:

Customer information

Booking ID

Booking date

Booking time

Movie details

Show time

Screen

Ticket type

Number of tickets

Payment summary

Final amount

🧮 Billing Calculation

The application uses the following calculations.

Ticket Total

Ticket Total = Ticket Price × Number of Tickets

Discount

Discount = Ticket Total × Discount Rate

Amount After Discount

Amount After Discount = Ticket Total − Discount

GST

GST = Amount After Discount × 18%

Final Amount

Final Amount = Amount After Discount + GST

Example

For 5 Standard tickets:

Ticket Price = ₹150
Number of Tickets = 5

Ticket Total = ₹150 × 5
             = ₹750

Discount = 10% of ₹750
         = ₹75

Amount After Discount = ₹750 − ₹75
                      = ₹675

GST = 18% of ₹675
    = ₹121.50

Final Amount = ₹675 + ₹121.50
             = ₹796.50

🔄 Application Workflow

START
  ↓
Open CINEVERSE
  ↓
Enter Customer Details
  ↓
Select Movie
  ↓
Select Date
  ↓
Select Show Time
  ↓
Select Screen Type
  ↓
Select Ticket Type
  ↓
Select Number of Tickets
  ↓
Calculate Ticket Total
  ↓
Apply Discount
  ↓
Calculate GST
  ↓
Calculate Final Amount
  ↓
Validate Customer Details
  ↓
Confirm Booking
  ↓
Generate Booking ID
  ↓
Display Booking Confirmation
  ↓
END

📦 Installation

Step 1: Install Python

Check whether Python is installed:

python --version

Step 2: Open the Project Folder

Open Command Prompt and navigate to the folder containing movie_ticket_booking.py.

Example:

cd "C:\Users\YourName\Desktop\Movie-Ticket-Booking"

Step 3: Install Requirements

Run:

python -m pip install -r requirements.txt

The project requires:

streamlit

The datetime module is included with Python, so it does not need to be installed separately.

▶️ How to Run

Run:

python -m streamlit run movie_ticket_booking.py

Streamlit will start the application and provide a local web address. Open that address in your browser.

🖥️ How to Use

Open the CINEVERSE application.

Enter your full name.

Enter your 10-digit phone number.

Enter your email address.

Select a movie.

Select the movie date.

Select a show time.

Select the screen type.

Select the ticket type.

Select the number of tickets.

Review the booking summary.

Click BOOK TICKETS NOW.

If the details are valid, the booking is confirmed.

View the generated booking ID and payment summary.

📚 Python Concepts Used

This project demonstrates:

Variables

Dictionaries

Lists

Functions provided by Streamlit

Conditional statements

Arithmetic operations

String methods

Date and time handling

Input validation

Session state

Form-like user interaction

🎈 Streamlit Concepts Used

The project uses Streamlit components including:

st.set_page_config()

st.title()

st.markdown()

st.success()

st.sidebar

st.header()

st.text_input()

st.selectbox()

st.date_input()

st.number_input()

st.button()

st.columns()

st.container()

st.metric()

st.warning()

st.divider()

st.caption()

st.session_state

st.rerun()

st.balloons()

🎨 User Interface

The application contains a custom CSS design with:

Movie-themed interface

Gradient background

Styled buttons

Attractive headings

Sidebar customer section

Booking summary cards

Payment metrics

Responsive Streamlit layout

The CSS is used only for styling; the visible application content is created using Streamlit components.

🧪 Testing

The application can be tested using the following cases.

Test Case 1: Empty Name

Input: Leave name empty.

Expected Result: The application displays a warning asking for the full name.

Test Case 2: Invalid Phone Number

Input: Enter fewer or more than 10 digits.

Expected Result: The application displays a warning asking for a valid 10-digit phone number.

Test Case 3: Invalid Email

Input: Enter an invalid email address.

Expected Result: The application displays a warning asking for a valid email address.

Test Case 4: Valid Booking

Input: Enter valid customer details and select all booking options.

Expected Result: Booking is confirmed and booking information is displayed.

Test Case 5: Discount

Input: Select 3–4 tickets.

Expected Result: 5% discount is applied.

Test Case 6: Higher Discount

Input: Select 5 or more tickets.

Expected Result: 10% discount is applied.

🌟 Advantages

Simple and beginner-friendly

Attractive movie booking interface

Easy ticket selection

Automatic pricing

Automatic discount calculation

Automatic GST calculation

Customer validation

Booking confirmation

Automatic booking ID

No database required

Suitable for college mini-projects

Easy to run locally

⚠️ Limitations

No database is used for permanent booking storage.

Bookings are not stored permanently.

Online payment is not actually processed.

Booking ID is generated from the current date and time.

The project is mainly intended for learning and academic purposes.

🔮 Future Enhancements

The project can be extended with:

🔐 User login and registration

🗄️ Database integration

💺 Real-time seat selection

🧾 PDF ticket generation

📧 Email ticket delivery

💳 Online payment gateway

📱 Mobile-friendly enhancements

📊 Admin dashboard

🎟️ QR code on tickets

⭐ Movie reviews and ratings

🔔 Booking notifications

📜 Booking history

🎫 Cancellation and refund system

🎓 Learning Outcomes

After completing this project, a beginner can understand how to:

Build an interactive application using Python.

Create a web interface using Streamlit.

Work with dictionaries and lists.

Accept and validate user input.

Perform pricing calculations.

Implement discount and GST logic.

Use Streamlit session state.

Generate dynamic booking information.

Organize a Python project.

Create and use a requirements.txt file.

Write project documentation using README.md.

📄 License

This project is intended for educational and learning purposes.

👨‍💻 Author

CINEVERSE – Movie Ticket Booking System

Built with Python + Streamlit.