from tkinter import *

import cv2, math, os, pyautogui

from tkinter import messagebox

from PIL import ImageTk, Image

from tkinter import filedialog

import webbrowser, urllib.request



web = "https://github.com/imvickykumar999/Tkinter-Image_Editor/raw/main/image%20editor/"

url = ['haarcascade_eye.xml', 'haarcascade_frontalface_default.xml']

web_haarcascade = ['web_haarcascade_eye.xml', 'web_haarcascade_frontalface_default.xml']



if not (os.path.exists(web_haarcascade[0]) and os.path.exists(web_haarcascade[1])):

    print('\n\tWait few seconds, xml file is missing\n and, need to download...\n\t...File is downloading')

    for i in range(2):

        web_file = urllib.request.urlopen(web + url[i])

        file = open(web_haarcascade[i],'w')



        for line in web_file:

            decoded_line = line.decode("utf-8")

            file.write(f'{decoded_line}')

        file.close()

    print('\n\tfile is downloaded...')



path = ''

rotated = os.path.join(path, 'rotated.png')

eyexml = os.path.join(path, 'eyexml.png')

sspng = os.path.join(path, 'screenshot.png')

cv = os.path.join(path, 'cv2.png')

editor = os.path.join(path, 'editorexe.py')



haarcascade_eye = os.path.join(path, 'web_haarcascade_eye.xml')

haarcascade_frontalface_default = os.path.join(path,

                    'web_haarcascade_frontalface_default.xml')



deg = 'Not yet Rotated'

url = "https://vixportfoliowithflask.herokuapp.com/skills"

ipwebcam = 'https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN&gl=US'

proj = 'https://github.com/imvickykumar999/Tkinter-Image_Editor/tree/master'

ip_url = 'http://192.168.43.1:8080/video'

ex=True



def ss() :

    myScreenshot = pyautogui.screenshot()

    myScreenshot.save(sspng)



def git_upload():

    from vixuploader import github as vix

    vix.upload()



def exitfun(root):

    global ex

    ex = False

    ss()
    return root.destroy()



def open_img(rotated):

    try:

        img = Image.open(rotated).convert('RGB')



        if img.size[0] > 600 and img.size[1] > 600:

            img = img.resize((int(img.size[0]/2),

                int(img.size[1]/2)), Image.ANTIALIAS)



        img = ImageTk.PhotoImage(img)

        panel = Label(root, image=img)

        panel.image = img

        panel.pack(side = "left",

                fill = "both", expand = "yes")



    except Exception as e:

        mess(e)



def camera(ip_url, cv):

    video = cv2.VideoCapture(ip_url)



    while True:

        check, frame = video.read()

        frame = cv2.putText(frame, 'Press SPACE to Click', (50, 50),

                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Capturing', frame)



        key = cv2.waitKey(1)

        if key == ord(' '):

            break



    video.release()

    cv2.destroyAllWindows()

    cv2.imwrite(cv, frame)

    return cv



def openfn(ip_url):

    global cv

    try:

        cv = camera(ip_url, cv)



    except Exception as e:

        mess('Download IP webcam app from Help Menu !!!\n' + str(e))



    open_img(cv)

    return cv



def openfile():

    global cv

    cv = filedialog.askopenfilename(title='Choose Image')



    open_img(cv)

    return cv



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

        mess('Opened in respected File Viewer')

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



def callback(url):

    try:

        webbrowser.open_new(url)

    except Exception as e:

        mess(e)



while ex:

    root = Tk()



    face_cascade = cv2.CascadeClassifier(haarcascade_frontalface_default)

    eye_cascade = cv2.CascadeClassifier(haarcascade_eye)



    pad=120

    root.geometry("{0}x{1}+0+0".format(

            root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))



    menu = Menu(root)

    root.config(menu=menu)



    filemenu = Menu(menu)

    menu.add_cascade(label = 'Open', menu=filemenu)



    filemenu.add_command(label = 'eye_xml.png',

            command = lambda: osopen(eyexml))



    filemenu.add_command(label = 'haarcascade_eye.xml',

            command = lambda: osopen(haarcascade_eye))



    filemenu.add_command(label = 'haarcascade_frontalface_default.xml',

            command = lambda: osopen(haarcascade_frontalface_default))



    filemenu.add_command(label = 'editorexe.py',

            command = lambda: osopen(editor))



    filemenu.add_separator()

    filemenu.add_command(label = 'Exit',

            font='Helvetica 10 bold', command = root.destroy)



    helpmenu = Menu(menu)

    menu.add_cascade(label = 'Help', menu=helpmenu)



    helpmenu.add_command(label = 'Angle Rotated',

            command = lambda: mess(deg))



    helpmenu.add_command(label = 'My Website',

            command = lambda: callback(url))



    helpmenu.add_command(label = 'IP Webcam App',

            command = lambda: callback(ipwebcam))



    helpmenu.add_command(label = 'This Project on GitHub',

            command = lambda: callback(proj))



    Button(root, bg = "yellow", font='Helvetica 15 bold',

            text='Choose Image to Rotate from Laptop Camera',

            command = lambda: rotatefun(openfn(0))).pack(side = "top")



    Button(root, bg = "pink", font='Helvetica 15 bold',

            text='Choose Image to Rotate from Mobile Camera',

            command = lambda: rotatefun(openfn(ip_url))).pack(side = "top")



    Button(root, bg = "green", font='Helvetica 15 bold',

            text='Choose Image to Rotate from Folder',

            command = lambda: rotatefun(openfile())).pack(side = "top")



    Button(root, bg = "red", font='Helvetica 12 bold',

            text='!!! Click here, to Exit while loop !!!',

            command = lambda: exitfun(root)).pack(side = "bottom")



    l = Label(root, text = "------------>\nROTATED Image")

    l.config(font =("Courier", 30), anchor=CENTER)

    l.pack(side = 'bottom')



    Button(root, bg = "orange", font='Helvetica 10 bold',

            text='Clean frame',

            command = root.quit).pack(side = "bottom")



    root.mainloop()



git_upload()

