from logging import root
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageEnhance

FILE = None
FILE_POINTER = 0
FILE_LEN = 0
IMAGE = None

def changeImage(im):
    global imageContainer
    width, height = im.size
    img = ImageTk.PhotoImage(
        im.resize((int(550 * (width / height)), 550), Image.ANTIALIAS)
    )
    imageContainer.config(image=img)
    imageContainer.image = img

def loadImage():
    global IMAGE
    IMAGE = getImages()


def getFile():
    global FILE,IMAGE
    filetypes = (
        ('JPG', '*.jpg'),
        ('JPEG', '*.jpeg'),
        ('All files', '*.*')
    )
    FILE = fd.askopenfilenames(
        title='Open files',
        initialdir='./',
        filetypes=filetypes
    )
    # print(len(FILE))
    loadImage()
    changeImage(IMAGE)

def SliderChanges(event):
    global w,IMAGE
    # Enhance Contrast
    curr_con = ImageEnhance.Contrast(IMAGE)
    new_con = 0.3
    
    # Contrast enhanced by a factor of 0.3
    new_im = curr_con.enhance(new_con)
    changeImage(new_im.point( lambda p: 255 if p > w.get() else 0 ))
    # print(w.get())

def on_closing():
    global master
    master.destroy()

def getImages():
    global FILE
    return Image.open(FILE[FILE_POINTER]).convert('LA')
    

master = Tk()
master.title("Dataset Generator")
# set window size
master.geometry("1080x667")
# set window color
master["background"] = "#fcfcfc"
o = Button(master,text="Open",command=getFile)
o.pack()
imageContainer = Label(master)
imageContainer.pack()
imageContainer.focus_set()
w = Scale(master, from_=0, to=255, orient=HORIZONTAL)
w.bind("<ButtonRelease-1>", SliderChanges)
w.pack()
s = Button(master,text="Save",command=getFile)
s.pack()

master.protocol("WM_DELETE_WINDOW", on_closing)
mainloop()