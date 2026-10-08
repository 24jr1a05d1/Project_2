import streamlit as st
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CINEVERSE - Movie Booking",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# IMPORTANT:
# This CSS is only for styling.
# All visible content below is created using Streamlit widgets.
# ============================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap'
    );

    /* Main application background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                #ede9fe 0%,
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 20%,
                #fce7f3 0%,
                transparent 25%
            ),
            linear-gradient(
                135deg,
                #faf5ff,
                #ffffff,
                #fdf2f8
            );
    }

    /* Main container */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    h1 {
        font-family: 'Fredoka', sans-serif !important;
        font-size: 55px !important;
        font-weight: 700 !important;
        text-align: center;
        color: #7c3aed !important;
        letter-spacing: 2px;
    }

    /* Headings */
    h2, h3 {
        font-family: 'Fredoka', sans-serif !important;
        color: #4c1d95 !important;
    }

    /* Normal text */
    p, label, span {
        font-family: 'Poppins', sans-serif;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        min-height: 45px;
        border: none;
        border-radius: 14px;
        background: linear-gradient(
            135deg,
            #7c3aed,
            #db2777
        );
        color: white !important;
        font-family: 'Fredoka', sans-serif;
        font-size: 16px;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow:
            0 8px 20px rgba(124, 58, 237, 0.30);
    }

    /* Input text */
    input {
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        font-family: 'Poppins', sans-serif !important;
    }

    /* Select box */
    [data-baseweb="select"] {
        color: #111827 !important;
    }

    [data-baseweb="select"] * {
        color: #111827 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #312e81,
            #6d28d9,
            #be185d
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background: white;
        border-radius: 18px;
        padding: 15px;
        border: 2px solid #ddd6fe;
        box-shadow:
            0 6px 18px rgba(0, 0, 0, 0.07);
    }

    /* Expander */
    .streamlit-expanderHeader {
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MOVIE DATA
# ============================================================

MOVIES = {

    "🦸 Superhero Universe": {
        "description": "Action-packed superhero adventure",
        "language": "English",
        "rating": "⭐ 4.8/5",
        "duration": "2h 35m"
    },

    "🧙 Magic Kingdom": {
        "description": "Fantasy adventure filled with magic",
        "language": "English",
        "rating": "⭐ 4.6/5",
        "duration": "2h 20m"
    },

    "🚀 Space Mission": {
        "description": "Thrilling journey beyond the stars",
        "language": "English",
        "rating": "⭐ 4.7/5",
        "duration": "2h 15m"
    },

    "❤️ Love Forever": {
        "description": "A beautiful romantic story",
        "language": "Telugu",
        "rating": "⭐ 4.5/5",
        "duration": "2h 25m"
    },

    "😂 Crazy Friends": {
        "description": "Comedy, friendship and fun",
        "language": "Telugu",
        "rating": "⭐ 4.4/5",
        "duration": "2h 10m"
    },

    "👻 Haunted House": {
        "description": "A mysterious horror experience",
        "language": "Telugu",
        "rating": "⭐ 4.3/5",
        "duration": "2h 05m"
    }
}


# ============================================================
# TICKET PRICES
# ============================================================

TICKET_PRICES = {
    "🎟️ Standard": 150,
    "💺 Premium": 250,
    "👑 VIP": 400
}


# ============================================================
# SCREEN / SHOW DETAILS
# ============================================================

SHOW_TIMES = [
    "10:00 AM",
    "1:30 PM",
    "4:30 PM",
    "7:30 PM",
    "10:30 PM"
]


SCREEN_TYPES = [
    "🎬 2D",
    "✨ 3D",
    "🔥 IMAX"
]


# ============================================================
# SESSION STATE
# ============================================================

if "booking_confirmed" not in st.session_state:
    st.session_state.booking_confirmed = False


# ============================================================
# MAIN TITLE
# ============================================================

st.title("🎬 CINEVERSE")

st.markdown(
    "### 🍿 Your Movie • Your Seat • Your Experience ❤️",
    unsafe_allow_html=False
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

st.success(
    "✨ Welcome to CINEVERSE! "
    "Book your favorite movie and enjoy the show! 🍿🎬"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("👤 Customer Details")

    customer_name = st.text_input(
        "Full Name",
        placeholder="Enter your name"
    )

    customer_phone = st.text_input(
        "Phone Number",
        placeholder="10-digit mobile number",
        max_chars=10
    )

    customer_email = st.text_input(
        "Email",
        placeholder="example@gmail.com"
    )

    st.divider()

    st.header("🎟️ Booking Offers")

    st.write("🥉 1–2 Tickets → No Discount")
    st.write("🥈 3–4 Tickets → 5% OFF")
    st.write("🥇 5+ Tickets → 10% OFF")

    st.divider()

    if st.button("🔄 Reset Booking"):

        st.session_state.booking_confirmed = False

        st.rerun()


# ============================================================
# MAIN LAYOUT
# ============================================================

selection_column, summary_column = st.columns(
    [1.35, 1]
)


# ============================================================
# MOVIE SELECTION
# ============================================================

with selection_column:

    st.header("🎬 Select Your Movie")

    selected_movie = st.selectbox(
        "Choose a Movie",
        list(MOVIES.keys())
    )

    movie_info = MOVIES[selected_movie]


    # --------------------------------------------------------
    # MOVIE INFORMATION
    # --------------------------------------------------------

    st.subheader(selected_movie)

    st.write(
        f"📝 **Description:** "
        f"{movie_info['description']}"
    )

    st.write(
        f"🌐 **Language:** "
        f"{movie_info['language']}"
    )

    st.write(
        f"⭐ **Rating:** "
        f"{movie_info['rating']}"
    )

    st.write(
        f"⏱️ **Duration:** "
        f"{movie_info['duration']}"
    )


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    st.subheader("📅 Select Date")

    selected_date = st.date_input(
        "Movie Date"
    )


    # --------------------------------------------------------
    # SHOW TIME
    # --------------------------------------------------------

    st.subheader("⏰ Select Show Time")

    selected_time = st.selectbox(
        "Available Shows",
        SHOW_TIMES
    )


    # --------------------------------------------------------
    # SCREEN TYPE
    # --------------------------------------------------------

    st.subheader("🖥️ Select Screen")

    screen_type = st.selectbox(
        "Screen Type",
        SCREEN_TYPES
    )


    # --------------------------------------------------------
    # TICKET TYPE
    # --------------------------------------------------------

    st.subheader("🎟️ Select Ticket Type")

    ticket_type = st.selectbox(
        "Ticket Category",
        list(TICKET_PRICES.keys())
    )

    ticket_price = TICKET_PRICES[ticket_type]


    # --------------------------------------------------------
    # NUMBER OF TICKETS
    # --------------------------------------------------------

    st.subheader("👥 Number of Tickets")

    number_of_tickets = st.number_input(
        "Tickets",
        min_value=1,
        max_value=10,
        value=1,
        step=1
    )


# ============================================================
# BOOKING SUMMARY
# ============================================================

with summary_column:

    st.header("🧾 Booking Summary")


    # --------------------------------------------------------
    # PRICE CALCULATION
    # --------------------------------------------------------

    ticket_total = (
        ticket_price *
        number_of_tickets
    )


    # --------------------------------------------------------
    # DISCOUNT
    # --------------------------------------------------------

    if number_of_tickets >= 5:

        discount_rate = 0.10

    elif number_of_tickets >= 3:

        discount_rate = 0.05

    else:

        discount_rate = 0


    discount = (
        ticket_total *
        discount_rate
    )


    # --------------------------------------------------------
    # TAX
    # --------------------------------------------------------

    amount_after_discount = (
        ticket_total - discount
    )

    gst = (
        amount_after_discount * 0.18
    )


    # --------------------------------------------------------
    # FINAL TOTAL
    # --------------------------------------------------------

    final_total = (
        amount_after_discount +
        gst
    )


    # --------------------------------------------------------
    # SUMMARY DETAILS
    # --------------------------------------------------------

    with st.container(border=True):

        st.subheader(
            f"🎬 {selected_movie}"
        )

        st.write(
            f"📅 **Date:** "
            f"{selected_date.strftime('%d-%m-%Y')}"
        )

        st.write(
            f"⏰ **Show:** "
            f"{selected_time}"
        )

        st.write(
            f"🖥️ **Screen:** "
            f"{screen_type}"
        )

        st.write(
            f"🎟️ **Ticket Type:** "
            f"{ticket_type}"
        )

        st.write(
            f"👥 **Number of Tickets:** "
            f"{number_of_tickets}"
        )

        st.divider()

        st.write(
            f"🎫 Ticket Price: "
            f"₹{ticket_price:.2f}"
        )

        st.write(
            f"💰 Ticket Total: "
            f"₹{ticket_total:.2f}"
        )

        st.write(
            f"🎁 Discount: "
            f"-₹{discount:.2f}"
        )

        st.write(
            f"🧾 GST (18%): "
            f"₹{gst:.2f}"
        )

        st.divider()

        st.metric(
            "💰 TOTAL AMOUNT",
            f"₹{final_total:.2f}"
        )


# ============================================================
# CUSTOMER VALIDATION + BOOKING
# ============================================================

st.divider()

st.header("🎟️ Confirm Your Booking")


confirm_booking = st.button(
    "🎬 BOOK TICKETS NOW"
)


if confirm_booking:

    # --------------------------------------------------------
    # NAME VALIDATION
    # --------------------------------------------------------

    if not customer_name.strip():

        st.warning(
            "⚠️ Please enter your full name."
        )

    # --------------------------------------------------------
    # PHONE VALIDATION
    # --------------------------------------------------------

    elif not customer_phone.strip():

        st.warning(
            "⚠️ Please enter your phone number."
        )

    elif (
        not customer_phone.isdigit()
        or len(customer_phone) != 10
    ):

        st.warning(
            "⚠️ Please enter a valid "
            "10-digit phone number."
        )

    # --------------------------------------------------------
    # EMAIL VALIDATION
    # --------------------------------------------------------

    elif (
        not customer_email.strip()
        or "@" not in customer_email
        or "." not in customer_email
    ):

        st.warning(
            "⚠️ Please enter a valid email address."
        )

    # --------------------------------------------------------
    # BOOKING SUCCESS
    # --------------------------------------------------------

    else:

        st.session_state.booking_confirmed = True

        st.balloons()


# ============================================================
# FINAL BOOKING CONFIRMATION
# ============================================================

if st.session_state.booking_confirmed:

    st.divider()

    st.header(
        "🎉 BOOKING CONFIRMED!"
    )

    st.success(
        f"Congratulations {customer_name}! "
        f"Your movie tickets have been booked successfully. 🍿"
    )


    # ========================================================
    # BOOKING ID
    # ========================================================

    booking_time = datetime.now()

    booking_id = booking_time.strftime(
        "%Y%m%d%H%M%S"
    )


    # ========================================================
    # CUSTOMER INFORMATION
    # ========================================================

    st.subheader(
        "👤 Customer Information"
    )

    customer_col1, customer_col2 = st.columns(2)

    with customer_col1:

        st.write(
            f"**Name:** {customer_name}"
        )

        st.write(
            f"**Phone:** {customer_phone}"
        )

        st.write(
            f"**Email:** {customer_email}"
        )

    with customer_col2:

        st.write(
            f"**Booking ID:** #{booking_id}"
        )

        st.write(
            f"**Booking Date:** "
            f"{booking_time.strftime('%d-%m-%Y')}"
        )

        st.write(
            f"**Booking Time:** "
            f"{booking_time.strftime('%I:%M %p')}"
        )


    # ========================================================
    # MOVIE DETAILS
    # ========================================================

    st.subheader(
        "🎬 Movie Details"
    )

    booking_col1, booking_col2 = st.columns(2)

    with booking_col1:

        st.write(
            f"**Movie:** {selected_movie}"
        )

        st.write(
            f"**Date:** "
            f"{selected_date.strftime('%d-%m-%Y')}"
        )

        st.write(
            f"**Show Time:** {selected_time}"
        )

    with booking_col2:

        st.write(
            f"**Screen:** {screen_type}"
        )

        st.write(
            f"**Ticket Type:** {ticket_type}"
        )

        st.write(
            f"**Tickets:** {number_of_tickets}"
        )


    # ========================================================
    # PAYMENT SUMMARY
    # ========================================================

    st.subheader(
        "💰 Payment Summary"
    )

    payment_col1, payment_col2, payment_col3, payment_col4 = (
        st.columns(4)
    )

    with payment_col1:

        st.metric(
            "Ticket Total",
            f"₹{ticket_total:.2f}"
        )

    with payment_col2:

        st.metric(
            "Discount",
            f"₹{discount:.2f}"
        )

    with payment_col3:

        st.metric(
            "GST",
            f"₹{gst:.2f}"
        )

    with payment_col4:

        st.metric(
            "Final Amount",
            f"₹{final_total:.2f}"
        )


    # ========================================================
    # FINAL MESSAGE
    # ========================================================

    st.success(
        f"🍿 Enjoy **{selected_movie}**! "
        f"Your total payment is "
        f"**₹{final_total:.2f}**. "
        f"Have a wonderful movie experience! 🎬❤️"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎬 CINEVERSE • Movie Ticket Booking System • "
    "Built with Python + Streamlit"
)