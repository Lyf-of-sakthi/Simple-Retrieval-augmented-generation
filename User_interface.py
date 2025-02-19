from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw()
def get_file():
    file = askopenfilename(title = "Select any document", filetypes = [("Text files",".txt")])
    if file:
        print("selected file: ", file)
    else:
        print("no file selected")
    if file:
        return file
    else:
        print("No file selected")
        return None
