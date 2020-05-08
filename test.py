
import sys
import tkinter
import traceback
import cv2
import avarage_BGR
from PIL import ImageTk, Image


# takes input image and ask to give 4 consicutive points and crop and calculate RGB channel

if len(sys.argv) != 2:
    print(" No input given  %s " % sys.argv[0])
    sys.exit(-1)
    
_, IMG_FILENAME = sys.argv


master = tkinter.Tk()
img_cv2 = cv2.imread(IMG_FILENAME)
IMG = ImageTk.PhotoImage(Image.open(IMG_FILENAME).resize((400, 300), resample = 0))
IMG_WIDTH, IMG_HEIGHT = IMG.width(), IMG.height()
print("Image H and W" , IMG_HEIGHT, IMG_WIDTH)

canvas = tkinter.Canvas(master, width=IMG_WIDTH, height=IMG_HEIGHT)
canvas.pack()

TOP_LEFT = None
BOTTOM_RIGHT = None


def on_click(event):

    global TOP_LEFT, BOTTOM_RIGHT
    print("Inside on_click")
    if TOP_LEFT and BOTTOM_RIGHT:
        TOP_LEFT = None
        BOTTOM_RIGHT = None
        

    elif not TOP_LEFT:
        TOP_LEFT = event.y, event.x
        print("TOP_LEFT ", TOP_LEFT)

    else:
        BOTTOM_RIGHT = event.y, event.x
        print("BOTTOM_RIGHT", BOTTOM_RIGHT)
        try:
            REC_H = BOTTOM_RIGHT[0] - TOP_LEFT[0]
            REC_W = BOTTOM_RIGHT[1] - TOP_LEFT[1]
            crop_img = img_cv2[TOP_LEFT[0]:TOP_LEFT[0] + REC_H, TOP_LEFT[1]:TOP_LEFT[1] + REC_W]
            AVG_B, AVG_G, AVG_R = avarage_BGR.find_avarage(crop_img)
            print("Average value ", AVG_R, AVG_G, AVG_B)

        except:
            BOTTOM_RIGHT = None
            traceback.print_exc()



canvas.bind('<Button-1>', on_click)

canvas.create_image((0,0), anchor=tkinter.NW, image=IMG)
master.mainloop()