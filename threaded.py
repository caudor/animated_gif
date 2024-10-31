import threading
from datetime import time
from tkinter import Image, Label, PhotoImage

from PIL import ImageTk

from app import root

i = 0
ph = ImageTk.PhotoImage(Image.fromarray(i[i]))
imglabel = Label(f2, image=ph)
imglabel.grid(row=0, column=0)


def runthegif(root, i):
    while True:
        i = i + 7
        i = i % 150

        ph = ImageTk.PhotoImage(PhotoImage(file='chris.gif', format='gif -index %i' % i))
        imagelabel = Label(f2, image=ph)
        imagelabel.grid(row=0, column=0)
        time.sleep(0.1)


t1 = threading.Thread(target=runthegif, args=(root, i))
t1.start()

root.mainloop()