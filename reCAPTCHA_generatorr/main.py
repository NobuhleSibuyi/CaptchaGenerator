import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random
import string


class CAPTCHAApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CAPTCHA Generator")
        self.master.geometry("350x250")

        # Frame for CAPTCHA and Entry
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10)

        # CAPTCHA Image Label
        self.captcha_label = tk.Label(self.frame)
        self.captcha_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Entry box for user input
        self.captcha_entry = tk.Entry(self.frame, font=("Arial", 16))
        self.captcha_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Refresh CAPTCHA Button
        self.refresh_button = tk.Button(self.frame, text="Refresh CAPTCHA", command=self.generate_captcha)
        self.refresh_button.grid(row=2, column=0, padx=10, pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.check_captcha)
        self.submit_button.grid(row=2, column=1, padx=10, pady=10)

        # Label for result message
        self.result_label = tk.Label(self.frame, text="", font=("Arial", 12), fg="green")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Okay Button that's hidden by default
        self.okay_button = tk.Button(self.frame, text="Okay", command=self.reset_result)
        self.okay_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.okay_button.grid_remove()

        # Generating first CAPTCHA
        self.correct_captcha = ""
        self.generate_captcha()

    def generate_captcha(self):
        # Generating random string
        self.correct_captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # Creating CAPTCHA image
        img = Image.new('RGB', (150, 80), color=(200, 200, 200))
        draw = ImageDraw.Draw(img)

        # Adding random lines and shapes to the background
        for _ in range(20):
            x1, y1, x2, y2 = [random.randint(0, 150) for _ in range(4)]
            draw.line((x1, y1, x2, y2), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                      width=2)

        # Using a default font
        font = ImageFont.load_default()

        # Adding text with random color and position
        for i, char in enumerate(self.correct_captcha):
            draw.text((i * 25 + 5, random.randint(0, 20)), char, font=font,
                      fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        # Saving the image
        img.save("captcha.png")

        # Displaying the image in the GUI
        captcha_image = ImageTk.PhotoImage(img)
        self.captcha_label.config(image=captcha_image)  # type: ignore
        self.captcha_label.image = captcha_image

    def check_captcha(self):
        # Check if the entered text matches the generated CAPTCHA
        user_input = self.captcha_entry.get()
        if user_input == self.correct_captcha:
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text="Incorrect! Please try again.", fg="red")

        # Show the "Okay" button
        self.okay_button.grid()
        self.captcha_entry.delete(0, tk.END)

    def reset_result(self):
        # Resetting the result label and hide the "Okay" button
        self.result_label.config(text="")
        self.okay_button.grid_remove()


# Running the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CAPTCHAApp(root)
    root.mainloop()
