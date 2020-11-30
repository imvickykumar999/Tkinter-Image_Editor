from tkinter import *
import cv2, math, os
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

ex=1
rotated = 'rotated.png'
eyexml = 'eyexml.png'
deg = 'Not yet Rotated'

while ex:
    def exitfun(root):
        global ex
        ex = 0
        return root.destroy()

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    root = Tk()
    pad=200
    root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))

    def open_img(rotated):
        try:
            img = Image.open(rotated).convert('RGB')

            if img.size[0] > 300 and img.size[1] > 400:
                img = img.resize((int(img.size[0]/2),
                    int(img.size[1]/2)), Image.ANTIALIAS)

            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.pack(side = "left",
                    fill = "both", expand = "yes")

        except Exception as e:
            mess(e)

    def openfn():
        filename = filedialog.askopenfilename(title='Choose Image')
        open_img(filename)
        return filename

    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label = 'Edit', menu=filemenu)

    filemenu.add_command(label = 'Open',
            command = lambda: osopen(eyexml))

    filemenu.add_separator()
    filemenu.add_command(label = 'Exit',
            font='Helvetica 10 bold', command=root.quit)

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

            try:
                eyes = (eye_cascade.detectMultiScale(roi_gray)).tolist()
            except Exception as e:
                mess(e)
                return

            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            cv2.imwrite(eyexml, img)
            cv2.imshow('img',img)
            cv2.waitKey(3000)
            cv2.destroyAllWindows()

            arr = []
            for k in range(len(eyes)):
                arr.append(eyes[k][1])

            size = len(arr)
            diff = max(arr) + 1

            for i in range(size-1):
                for j in range(i+1,size):
                    if abs(arr[i]-arr[j]) < diff:
                        diff = abs(arr[i] - arr[j])

            i,j = 0,1
            newi = []
            while i < size and j < size:
                if i != j and abs(arr[j]-arr[i]) == diff:

                    newi.append(eyes[min([i,j])])
                    newi.append(eyes[max([i,j])])
                    eyes = newi
                    break

                elif abs(arr[j]-arr[i]) < diff:
                    j+=1
                else:
                    i+=1

            global deg
            deg = angle(eyes)
        try:
            img = Image.open(torotate)
            try:
                img = img.rotate(deg)
            except Exception as e:
                mess(e)

            img.save(rotated)
            txt = f'Rotated angle = {deg}'
            mess(txt)
            open_img(rotated)

        except IOError:
            pass

    def osopen(rotated):
        try:
            os.startfile(rotated)
        except Exception as e:
            mess(e)

    def mess(txt):
        messagebox.showinfo("showinfo", txt)

    def angle(eyes):
        ley = eyes[0][1]
        rey = eyes[1][1]
        h = ley-rey

        lex = eyes[0][0]
        rex = eyes[1][0]
        b = lex-rex
        return (math.atan(h/b)*180)/math.pi

    Button(root, bg = "yellow", font='Helvetica 18 bold',
            text='Choose Image to Rotate',
            command = lambda: rotatefun(openfn())).pack()

    Button(root, bg = "orange", font='Helvetica 12 bold',
            text='Clean frame',
            command = root.quit).pack(side = "top")

    Button(root, bg = "red", font='Helvetica 15 bold',
            text='!!! Click here, to Exit while loop !!!',
            command = lambda: exitfun(root)).pack(side = "bottom")

    l = Label(root, text = "------------>\nROTATED Image")
    l.config(font =("Courier", 30), anchor=CENTER)
    l.pack(side = 'bottom')

    root.mainloop()
