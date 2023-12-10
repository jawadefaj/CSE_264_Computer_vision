
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
img_cv2 = cv2.resize(cv2.imread(IMG_FILENAME), (800, 600), interpolation = cv2.INTER_AREA)
IMG = ImageTk.PhotoImage(Image.open(IMG_FILENAME).resize((800, 600), resample = 0))
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
        x = TOP_LEFT[0]
        y = TOP_LEFT[1]
        canvas.create_oval(y-5,x-5,y+5,x+5,width=2,outline='red')
        print("TOP_LEFT ", TOP_LEFT)

    else:
        BOTTOM_RIGHT = event.y, event.x
        x = BOTTOM_RIGHT[0]
        y = BOTTOM_RIGHT[1]
        print("BOTTOM_RIGHT", BOTTOM_RIGHT)
        canvas.create_oval(y-5,x-5,y+5,x+5,width=2,outline='red')
        try:
            SUM_B, SUM_G, SUM_R = ( 0, 0, 0)
            for i in range(0, 20, 1):
                NewY = TOP_LEFT[0] + i
                NewX = TOP_LEFT[1] + i
                REC_H = BOTTOM_RIGHT[0] - NewY
                REC_W = BOTTOM_RIGHT[1] - NewX
                crop_img = img_cv2[NewY:NewY + REC_H, NewX:NewX + REC_W]
                # cv2.imshow("OUT", crop_img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                AVG_B, AVG_G, AVG_R = avarage_BGR.find_avarage(crop_img)
                SUM_B, SUM_G, SUM_R = SUM_B + AVG_B, SUM_G + AVG_G, SUM_R + AVG_R 
            print("Average value ", round(SUM_R/20, 3), round(SUM_G/20, 3), round(SUM_B/20, 3))

        except:
            BOTTOM_RIGHT = None
            traceback.print_exc()



canvas.bind('<Button-1>', on_click)

canvas.create_image((0,0), anchor=tkinter.NW, image=IMG)
master.mainloop()