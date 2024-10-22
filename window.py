import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont

class FileSelector:
    def __init__(self, root):
        self.root = root
        self.file_path = ""

        # Set up the main window
        self.root.title("Denoiser")
        self.root.geometry("500x200")
        self.root.configure(bg="#2E4053")

        # Define custom fonts
        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=12)
        self.button_font = tkfont.Font(family="Helvetica", size=10)

        # Create and pack widgets
        self.create_widgets()

        # Run the main loop
        self.root.mainloop()

    def create_widgets(self):
        # Create a title label
        title_label = tk.Label(self.root, text="Select an Image to Denoise", font=self.title_font, fg="white", bg="#2E4053")
        title_label.pack(pady=20)

        # Create a label to display the selected file
        self.label = tk.Label(self.root, text="No file selected", font=self.label_font, fg="white", bg="#2E4053")
        self.label.pack(pady=10)

        # Create a button to open the file dialog
        button = tk.Button(self.root, text="Browse", font=self.button_font, command=self.select_file, bg="#3498DB", fg="white", padx=10, pady=5)
        button.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            print(f"Selected file: {self.file_path}")
            self.root.quit()  # Close the Tkinter window after selecting the file

if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()

    # Create an instance of the FileSelector class
    file_selector = FileSelector(root)

    # After the window is closed, you can use the 'file_path' variable
    print(f"File path stored: {file_selector.file_path}")
