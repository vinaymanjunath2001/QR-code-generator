
import tkinter as tk
import qrcode
from PIL import ImageTk, Image

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200), Image.ANTIALIAS)
    qr_image = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image
    
    output_label.config(text="QR CODE Generation Successful")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# URL entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=5)

# QR code display
qr_label = tk.Label(root)
qr_label.pack(pady=5)

output_label = tk.Label(root)
output_label.pack(pady=5)

root.mainloop()

