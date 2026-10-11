import tkinter as tk 
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import sqlite3
from datetime import datetime

# Database Setup
def setup_database():
    conn = sqlite3.connect("hotel_reservation.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        room_number TEXT UNIQUE NOT NULL,
                        category TEXT NOT NULL,
                        price REAL NOT NULL,
                        description TEXT NOT NULL,
                        is_available BOOLEAN DEFAULT 1
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT,
                        room_number TEXT NOT NULL,
                        check_in DATE NOT NULL,
                        check_out DATE NOT NULL,
                        feedback TEXT,
                        rating INTEGER,
                        FOREIGN KEY (room_number) REFERENCES rooms(room_number)
                    )''')

    conn.commit()
    conn.close()


# Main GUI Application
class HotelReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Grey Horn Luxury Reservation System")
        self.root.geometry("1400x900")  # Larger window size
        
        # Set a theme for an elegant appearance
        self.root.set_theme("arc")
        
        # Background image (ensure to have an actual image or a placeholder)
        try:
            self.background_img = Image.open("hotel_background.jpg")
        except FileNotFoundError:
            self.background_img = Image.new('RGB', (1400, 900), color='lightblue')  # Placeholder
        self.background_img = ImageTk.PhotoImage(self.background_img)
        self.background_label = tk.Label(self.root, image=self.background_img)
        self.background_label.place(relwidth=1, relheight=1)

        # Main title with a luxurious font and background
        title_label = tk.Label(self.root, text="Hotel Grey Horn Luxury", font=("Helvetica", 36, "bold"), bg="#2f4f4f", fg="white")
        title_label.pack(pady=40, fill=tk.X)

        # Creating a frame to hold menu buttons with stylish designs
        menu_frame = tk.Frame(self.root, bg="#f5f5f5")
        menu_frame.pack(pady=40)

        self.create_menu_buttons(menu_frame)

    def create_menu_buttons(self, menu_frame):
        """Creates stylish menu buttons with larger sizes and enhanced design."""
        button_style = {
            'width': 40,  # Make the buttons wider
            'height': 4,  # Make the buttons taller
            'font': ('Helvetica', 18, 'bold'),  # Increase font size and make it bold
            'bg': "#6fa3ef",  # Light blue background for buttons
            'fg': "white",  # White text color
            'activebackground': "#3a75c3",  # Darker blue on hover
            'bd': 0,  # Remove border for a cleaner look
            'relief': "raised",  # Raised effect for elegance
            'padx': 20,  # Horizontal padding inside the button
            'pady': 20   # Vertical padding inside the button
        }

        button_texts = [
            ("View Available Rooms", self.view_rooms),
            ("Book a Room", self.book_room),
            ("Manage Bookings", self.manage_bookings),
            ("View Reservation", self.view_reservation),
            ("About Us", self.about_us),
            ("Help/Functions Overview", self.help_overview),
            ("Feedback", self.submit_feedback),
            ("Cancel Reservation", self.cancel_reservation),
        ]

        row, col = 0, 0
        for text, command in button_texts:
            button = ttk.Button(menu_frame, text=text, command=command)
            button.grid(row=row, column=col, padx=30, pady=15, sticky="ew", ipadx=40, ipady=20)
            col += 1
            if col == 2:  # Limit to two buttons per row for a larger layout
                col = 0
                row += 1

    def view_rooms(self):
        """Display available rooms in a new window with larger fonts and spaces."""
        view_window = tk.Toplevel(self.root)
        view_window.title("Available Rooms")
        view_window.geometry("1000x700")
        view_window.configure(bg="#f0f0f0")

        conn = sqlite3.connect("hotel_reservation.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rooms WHERE is_available = 1")
        rooms = cursor.fetchall()
        conn.close()

        tk.Label(view_window, text="Available Rooms", font=("Helvetica", 24, "bold"), bg="#0288d1", fg="white").pack(pady=20)

        room_table = ttk.Treeview(view_window, columns=("Room Number", "Category", "Price", "Description"), show="headings")
        room_table.heading("Room Number", text="Room Number")
        room_table.heading("Category", text="Category")
        room_table.heading("Price", text="Price")
        room_table.heading("Description", text="Description")

        for room in rooms:
            room_table.insert("", tk.END, values=(room[1], room[2], f"${room[3]:.2f}", room[4]))

        room_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

    def book_room(self):
        """Room booking form with smaller font size for better fitting of Submit button."""
        book_window = tk.Toplevel(self.root)
        book_window.title("Book a Room")
        book_window.geometry("900x700")
        book_window.configure(bg="#f5f5f5")

        # Label and Entry for Name
        tk.Label(book_window, text="Full Name:", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        name_entry = ttk.Entry(book_window, font=("Helvetica", 14))
        name_entry.pack(pady=10)

        # Label and Entry for Phone Number
        tk.Label(book_window, text="Phone Number:", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        def validate_phone_input(P):
            if P == "" or P.isdigit():  # Allow empty input and only numeric input
                if len(P) <= 10:  # Limit to 10 characters
                    return True
                else:
                    return False
            return False

        phone_validation = book_window.register(validate_phone_input)
        phone_entry = ttk.Entry(book_window, font=("Helvetica", 14), validate="key", validatecommand=(phone_validation, "%P"))
        phone_entry.pack(pady=10)

        # Label and Entry for Email
        tk.Label(book_window, text="Email (optional):", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        email_entry = ttk.Entry(book_window, font=("Helvetica", 14))
        email_entry.pack(pady=10)

        # Label and Combobox for Room Type
        tk.Label(book_window, text="Room Type:", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        room_types = ["Single", "Double", "Suite", "Penthouse"]
        room_combobox = ttk.Combobox(book_window, values=room_types, font=("Helvetica", 14), state="readonly")
        room_combobox.pack(pady=10)

        # Label and Entry for Check-in Date
        tk.Label(book_window, text="Check-in Date (YYYY-MM-DD):", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        check_in_entry = ttk.Entry(book_window, font=("Helvetica", 14))
        check_in_entry.pack(pady=10)

        # Label and Entry for Check-out Date
        tk.Label(book_window, text="Check-out Date (YYYY-MM-DD):", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        check_out_entry = ttk.Entry(book_window, font=("Helvetica", 14))
        check_out_entry.pack(pady=10)

        # Submit button with slightly bigger size
        submit_button = ttk.Button(book_window, text="Submit Booking", command=lambda: self.submit_booking(
            name_entry.get(), phone_entry.get(), email_entry.get(), room_combobox.get(), check_in_entry.get(), check_out_entry.get()), width=20, padding=10)
        submit_button.pack(pady=30)

    def submit_booking(self, name, phone, email, room_type, check_in, check_out):
        """Insert booking into the database."""
        if not name or not phone or not room_type or not check_in or not check_out:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        conn = sqlite3.connect("hotel_reservation.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bookings (name, phone, email, room_number, check_in, check_out) VALUES (?, ?, ?, ?, ?, ?) ",
                       (name, phone, email, room_type, check_in, check_out))
        conn.commit()
        conn.close()

        messagebox.showinfo("Booking Successful", "Your room has been successfully booked!")

    def cancel_reservation(self):
        """Cancel reservation logic."""
        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Cancel Reservation")
        cancel_window.geometry("600x400")

        tk.Label(cancel_window, text="Enter Reservation ID to Cancel:", font=("Helvetica", 14)).pack(pady=20)
        reservation_id_entry = ttk.Entry(cancel_window, font=("Helvetica", 14))
        reservation_id_entry.pack(pady=10)

        def cancel_booking():
            reservation_id = reservation_id_entry.get()
            if not reservation_id:
                messagebox.showerror("Error", "Please enter a reservation ID.")
                return

            conn = sqlite3.connect("hotel_reservation.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bookings WHERE id = ?", (reservation_id,))
            reservation = cursor.fetchone()

            if reservation:
                cursor.execute("DELETE FROM bookings WHERE id = ?", (reservation_id,))
                conn.commit()
                messagebox.showinfo("Success", f"Reservation {reservation_id} has been cancelled.")
            else:
                messagebox.showerror("Error", "Reservation ID not found.")

            conn.close()

        cancel_button = ttk.Button(cancel_window, text="Cancel Reservation", command=cancel_booking)
        cancel_button.pack(pady=20)

    def manage_bookings(self):
        """Manage bookings logic."""
        manage_window = tk.Toplevel(self.root)
        manage_window.title("Manage Bookings")
        manage_window.geometry("1000x700")
        manage_window.configure(bg="#f5f5f5")

        conn = sqlite3.connect("hotel_reservation.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, room_number, check_in, check_out FROM bookings")
        bookings = cursor.fetchall()
        conn.close()

        tk.Label(manage_window, text="Manage Bookings", font=("Helvetica", 24, "bold"), bg="#0288d1", fg="white").pack(pady=20)

        booking_table = ttk.Treeview(manage_window, columns=("ID", "Name", "Room Number", "Check-in", "Check-out"), show="headings")
        booking_table.heading("ID", text="ID")
        booking_table.heading("Name", text="Name")
        booking_table.heading("Room Number", text="Room Number")
        booking_table.heading("Check-in", text="Check-in")
        booking_table.heading("Check-out", text="Check-out")

        for booking in bookings:
            booking_table.insert("", tk.END, values=booking)

        booking_table.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

    def view_reservation(self):
        """View a specific reservation based on user input."""
        view_reservation_window = tk.Toplevel(self.root)
        view_reservation_window.title("View Reservation")
        view_reservation_window.geometry("1000x700")
        view_reservation_window.configure(bg="#f5f5f5")

        tk.Label(view_reservation_window, text="Enter Reservation ID:", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=10)
        reservation_id_entry = ttk.Entry(view_reservation_window, font=("Helvetica", 14))
        reservation_id_entry.pack(pady=10)

        def search_reservation():
            reservation_id = reservation_id_entry.get()
            if not reservation_id:
                messagebox.showerror("Error", "Please enter a reservation ID.")
                return

            conn = sqlite3.connect("hotel_reservation.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM bookings WHERE id = ?", (reservation_id,))
            reservation = cursor.fetchone()
            conn.close()

            if reservation:
                messagebox.showinfo("Reservation Details", f"Name: {reservation[1]}\nPhone: {reservation[2]}\nEmail: {reservation[3]}\nRoom: {reservation[4]}\nCheck-in: {reservation[5]}\nCheck-out: {reservation[6]}")
            else:
                messagebox.showerror("Error", "Reservation not found.")

        search_button = ttk.Button(view_reservation_window, text="Search", command=search_reservation)
        search_button.pack(pady=20)

    def exit_application(self):
        """Exit the application."""
        self.root.quit()

    def about_us(self):
        """About Us window with hotel details and staff information."""
        about_window = tk.Toplevel(self.root)
        about_window.title("About Us")
        about_window.geometry("1000x700")
        about_window.configure(bg="#f5f5f5")

        about_text = """
        Welcome to Hotel Grey Horn Luxury, where elegance meets comfort.

        Our hotel offers top-tier amenities:
        - Free Wi-Fi in all rooms
        - Complimentary breakfast
        - Spa and wellness center
        - Fitness center
        - 24/7 concierge service
        - Fine dining restaurant
        - Swimming pool
        - Arcade & games

        Our rooms range from deluxe to penthouse suites. Enjoy an unforgettable stay with us!

        **Our Staff**
        - The cleaning staff is sole reason for spotless surrounding
        - 24/7 reception to assist you and even guide to local tourist part
        - Your stay is comfortable and luxurious all thanks to our service staffs
        

        **Meet Our Main Staff & Owner:**
        - John Grey, Owner
        - Sarah Horn, General Manager
        - Jane Smith, Front Desk Manager
        - Bob Johnson, Head Chef
        """
        tk.Label(about_window, text=about_text, font=("Helvetica", 14), bg="#f5f5f5", justify=tk.LEFT).pack(padx=20, pady=20)
    
    def help_overview(self):
        """Help overview for all features."""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help Overview")
        help_window.geometry("800x600")
        help_window.configure(bg="#f5f5f5")

        help_text = """
        1. View Available Rooms: Displays available rooms and their details.

        2. Book a Room: Allows you to book a room by providing necessary details.

        3. Manage Bookings: View and manage all your existing bookings.

        4. View Reservation: Search for a specific reservation by ID.

        5. About Us: Learn more about the hotel and its amenities.

        6. Feedback: Submit your feedback about your stay.

        7. Cancel Reservation: Cancel a booking by providing the reservation ID.
        """
        tk.Label(help_window, text=help_text, font=("Helvetica", 14), bg="#f5f5f5", justify=tk.LEFT).pack(padx=20, pady=20)

    def submit_feedback(self):
        """Submit feedback from the user."""
        feedback_window = tk.Toplevel(self.root)
        feedback_window.title("Submit Feedback")
        feedback_window.geometry("900x700")
        feedback_window.configure(bg="#f5f5f5")

        tk.Label(feedback_window, text="Your Feedback:", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=20)
        feedback_text = ttk.Entry(feedback_window, font=("Helvetica", 14), width=60)
        feedback_text.pack(pady=10)

        tk.Label(feedback_window, text="Rate Your Experience (1-5):", font=("Helvetica", 14), bg="#f5f5f5").pack(pady=20)
        rating = ttk.Combobox(feedback_window, values=[1, 2, 3, 4, 5], font=("Helvetica", 14), state="readonly")
        rating.pack(pady=10)

        def submit_feedback_info():
            feedback = feedback_text.get()
            rating_value = rating.get()

            if not feedback or not rating_value:
                messagebox.showerror("Error", "Please fill in both fields.")
                return

            conn = sqlite3.connect("hotel_reservation.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bookings (feedback, rating) VALUES (?, ?)", (feedback, rating_value))
            conn.commit()
            conn.close()

            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
        
        submit_button = ttk.Button(feedback_window, text="Submit Feedback", command=submit_feedback_info)
        submit_button.pack(pady=20)

# Initialize the app
setup_database()
root = ThemedTk()
app = HotelReservationApp(root)
root.mainloop()

