from tkinter import *
import cv2, math, os
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

w = Label(root, text ='Choose Image to Rotate', font = "50")
w.pack()

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

torotate = openfn()
x = torotate
img = Image.open(x)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img
panel.pack()

rotated = 'rotated.png'
deg = 'Not yet Rotated'

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label = 'Edit', menu=filemenu)

filemenu.add_command(label = 'Rotate',
        command = lambda: rotatefun(torotate))
filemenu.add_command(label = 'Open',
        command = lambda: osopen(rotated))

filemenu.add_separator()
filemenu.add_command(label = 'Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label = 'Help', menu=helpmenu)
helpmenu.add_command(label = 'Message', command = lambda: mess(deg))

def rotatefun(torotate):
    img = cv2.imread(torotate)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        global deg
        deg = angle(eyes)
    try:
        img = Image.open(torotate)
        img = img.rotate(deg)

        img.save(rotated)
    except IOError:
        pass

def osopen(rotated):
#     rotated = openfn()
    os.startfile(rotated)

def open_img():
#     x = openfn()
    x = rotated
    img = Image.open(x)
    # img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def mess(deg):
    ourMessage = f'Rotated angle = {deg}'
    messagebox.showinfo("showinfo", ourMessage)

def angle(eyes):
    ley = eyes[0][1]
    rey = eyes[1][1]
    h = ley-rey

    lex = eyes[0][0]
    rex = eyes[1][0]
    b = lex-rex

    return (math.atan(h/b)*180)/math.pi

Button(root, text = 'open rotated image',
                    command = open_img).pack()
root.mainloop()

try:
    root.destroy()
except:
    pass
