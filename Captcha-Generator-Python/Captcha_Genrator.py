"""
Instructions for Running the Project
1. Install captcha: pip install captcha
2. Download fonts and update the path in code (Your System PATH)
3. run the code
"""

from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

# Generate a captcha image with a random code
captcha_image = ImageCaptcha(fonts=['PATH to ChelseaMarketsr.ttf (Located in fonts folder of the project) ' ,'PATH to DejaVuSanssr.ttf (Located in fonts folder of the project)'])
captcha_code = str(randint(100000, 999999))
image_data = captcha_image.generate(captcha_code)
assert isinstance(image_data, BytesIO)
captcha_image.write(captcha_code, 'out.png')

def validate_captcha():
    # Validate the entered captcha against the generated one
    global captcha_code
    input_value = input_text.get("0.0", END)
    if int(input_value) == int(captcha_code):
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not Verified")
        refresh_captcha()

def refresh_captcha():
    # Refresh and display a new captcha
    global captcha_code
    captcha_code = str(randint(100000, 999999))
    image_data = captcha_image.generate(captcha_code)
    assert isinstance(image_data, BytesIO)
    captcha_image.write(captcha_code, 'out.png')
    photo = PhotoImage(file="out.png")
    captcha_label.config(image=photo, height=100, width=200)
    captcha_label.update()
    UpdateLabel()

# Initialize the GUI components
root = Tk()
photo = PhotoImage(file="out.png")
captcha_label = Label(root, image=photo, height=100, width=200)
input_text = Text(root, height=5, width=50)
submit_button = Button(root, text="Submit", command=validate_captcha)
refresh_button = Button(root, text="Refresh", command=refresh_captcha)

# Layout the GUI components
captcha_label.pack()
input_text.pack()
submit_button.pack()
refresh_button.pack()

# Run the GUI event loop
root.mainloop()
