# Importing libraries
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, UnidentifiedImageError

# Image uploader

def upload():
    try:
        path = askopenfilename()
        image = Image.open(path)
        image = resize_image(image)
        messagebox.showwarning(title='Warning!',message='Image uploaded is too large, it will be resized')
        img = ImageTk.PhotoImage(image)
        canvas.img = img
        canvas.create_image(canvas_width/2,canvas_height/2,image=img)

    except UnidentifiedImageError:
        messagebox.showwarning(title="Upload Error",
                               message="Image could not be read. Please try again.")
        
    get_explanation_map()
    get_explanation_text()

def get_explanation_map():
    # Get Image from XAI
    try:
        img = Image.open(f'../DeepfakeBench/figures/{'archi.png'}')
        img = resize_image(img)
        img = ImageTk.PhotoImage(img)
        canvas_xai.img = img
        canvas_xai.create_image(canvas_width/2,canvas_height/2,image=img,anchor='center')
    except UnidentifiedImageError:
        messagebox.showwarning(title="XAI Error",
                               message="Image could not be read. Please try uploading again.")

def get_explanation_text():
    canvas_text.create_text(canvas_width/2, canvas_height/2, fill="darkblue",font="Times 12",
                        text="Click the bubbles that are multiples of two.",anchor="center")

def resize_image(image):
    img_w, img_h = image.size
    if img_w > canvas_width or img_h > canvas_height:
        while img_w > canvas_width or img_h > canvas_height:
            img_w *= .99
            img_h *= .99
        image = image.resize((int(img_w),int(img_h)))
    return image

# Main

if __name__ == '__main__':
    
    window = tk.Tk()

    W, H = window.winfo_screenwidth(), window.winfo_screenheight()
    canvas_width, canvas_height = int(W/3), int(H/3)

    window.title('Explaining Deepfake')
    window.geometry(f'{int(W)}x{int(H)}')

    canvas = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='white')
    canvas.pack()

    upload_button = Button(window,text='Upload',command=lambda:upload(),padding=10)
    upload_button.config(width=float(W/3))
    upload_button.pack(side='top')

    canvas_xai = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='white',bd=0, highlightthickness=10, relief='ridge')
    canvas_xai.pack(side='left',fill="both", expand=True)

    canvas_text = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='white')
    canvas_text.pack(side='right',fill="both", expand=True)

    window.mainloop()
