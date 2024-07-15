# Import the necessary libraries
import tkinter as tk  # for creating graphical user interface
import qrcode  # for generating QR codes
from PIL import Image, ImageTk  # for handling images
from tkinter import messagebox  # for showing message boxes



# Define a function to generate a QR code based on user input
def generate_qr():
    # Get the user input from the entry widget
    upi_id = entry.get()
    if upi_id:
        # Construct the UPI payment URL with the provided UPI ID
        payment_url = f"upi://pay?pa={upi_id}&pn=divya_singh&am=AMOUNT&cu=CURRENCY_CODE&tn=TRANSACTION_NOTE"
        
        # Create a QRCode object with specified parameters
        qr = qrcode.QRCode(
            version=1,  # controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR code
            box_size=10,  # controls the number of pixels each box of the QR code contains
            border=4  # controls how many boxes thick the border should be
        )
        qr.add_data(payment_url)  
        qr.make(fit=True)  

        # Create an image from the QR code
        qr_img = qr.make_image(fill="black", back_color="white")

        # Convert the PIL image to a Tkinter image
        qr_img_tk = ImageTk.PhotoImage(qr_img)
        
        # Create a label to display the QR code image
        label = tk.Label(frame, image=qr_img_tk)
        label.image = qr_img_tk  # keep a reference to avoid garbage collection
        label.pack(pady=20)  # add some padding around the image
    else:
        # Show an error message if the input is empty or invalid
        messagebox.showerror("Input Error", "Please enter a valid UPI ID")

# Create the main application window
root = tk.Tk()
root.title("UPI QR Code Generator")  # set the window title
root.geometry("500x500")  # set the window size

# Create a frame to hold the input and label widgets
frame = tk.Frame(root)
frame.pack(pady=20)  # add some padding around the frame

# Create and pack a label widget for the UPI ID entry
label = tk.Label(frame, text="Enter UPI ID:")
label.pack()

# Create and pack an entry widget for user input
entry = tk.Entry(frame, width=30)
entry.pack(padx=10)  # add some padding around the entry widget

# Create and pack a button to trigger the QR code generation
button = tk.Button(root, text="Generate QR Code", command=generate_qr)
button.pack(pady=20)  # add some padding around the button

# Create and pack a label to display the QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=20)  # add some padding around the label

# Run the application main loop
root.mainloop()
