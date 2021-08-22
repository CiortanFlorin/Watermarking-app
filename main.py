import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image

#Default watermark
wm_path="watermark.png"
wm = Image.open(wm_path)

#Change funtion to change the used watermark with another file
def change_wm():
    global wm_path
    wm_path = askopenfilename()

#Open the image to watermark
def open_image():
    upload_text.set("Loading..")
    path = askopenfilename()
    im = Image.open(path)
    wm = Image.open(wm_path)
    #Get the name of the file
    new_name=(path.split('/')[-1]).split('.')[0]
    #Make new image
    new_im=Image.new('RGB',size=im.size)
    new_im.paste(im,(0,0))
    #Resieze watermark to match the upoaded image
    rwm=wm.resize((round(im.size[0]*0.3),round(im.size[1]*0.2)))
    #Place watermark in the right bottom corner
    new_im.paste(rwm,(im.size[0]-rwm.size[0], im.size[1]-rwm.size[1]), rwm)
    new_im.save(f"images/{new_name}_watermarked.jpg","JPEG")
    new_im.show()

#Close window
def quit():
    root.destroy()

root = tk.Tk()
root.geometry("315x150")
root.title("Watermarked")
root.config(padx=25, pady=25)

upload_text=tk.StringVar()
upload_buton =tk.Button(width=17, height=2,  textvariable=upload_text,bg='#f7f5dd', font=("Courier", 8 , "bold"), command=open_image)
upload_text.set("Upload image")
upload_buton.grid(row=0, column=0, padx=(0, 10))

watermark_buton =tk.Button(width=17, height=2, text="Change watermark",bg='#f7f5dd', font=("Courier", 8, "bold"), command=change_wm)
watermark_buton.grid(row=0, column=1)

quit_button = tk.Button(width=17, height=2, text="Quit",bg='#f7f5dd', font=("Courier", 8, "bold"), command=quit)
quit_button.grid(row=1, columnspan=2, column=0, pady=(10, 0))
root.mainloop()