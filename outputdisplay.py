import tkinter as tk
from PIL import Image, ImageTk

class ImageDisplay:
    def __init__(self, root, image):
        self.root = root
        self.root.title("Image Display")
        self.root.geometry("800x600")
        self.root.configure(bg="#2E4053")

        # Convert the provided image to a format compatible with Tkinter
        self.photo = ImageTk.PhotoImage(image)

        # Create and pack the widgets
        self.create_widgets()

        # Run the main loop
        self.root.mainloop()

    def create_widgets(self):
        # Create a label to display the image
        image_label = tk.Label(self.root, image=self.photo, bg="#2E4053")
        image_label.pack(pady=20)

        # Create a close button
        close_button = tk.Button(self.root, text="Close", command=self.close_window, bg="#E74C3C", fg="white", padx=10, pady=5)
        close_button.pack(pady=10)

    def close_window(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    # Example: Create a root window
    root = tk.Tk()

    # Assume 'image_variable' is the PIL.Image object stored in another program
    # Example: Create an example image (replace this with your actual image variable)
    image_variable = Image.new("RGB", (300, 200), color=(255, 0, 0))  # A red image

    # Create an instance of the ImageDisplay class, passing the image object
    image_display = ImageDisplay(root, image_variable)
