from customtkinter import *
import os
import shutil
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image

image_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")

def on_drop(event):
    # event.data is a raw Tcl list; use splitlist to handle multiple/spaced paths, see note above
    folders = window.tk.splitlist(event.data)
    # link_box.delete(0, "end")
    for folder in folders:
        link_box.insert("end", folder + "\n")

def move_img(line,image_name,folder_name):
    # ساخت مسیر پوشه جدید با اسم "1" داخل destination_folder
    new_folder = os.path.join(line, str(folder_name))

    # ساخت پوشه (اگه از قبل وجود نداشته باشه)
    os.makedirs(new_folder, exist_ok=True)

    # مسیر کامل مبدا و مقصد
    source_path = os.path.join(line, image_name)
    destination_path = os.path.join(new_folder, image_name)

    # انتقال فایل
    shutil.move(source_path, destination_path)

window = CTk()                                             
window.geometry("620x600")                                 
window.title("Image Width Sorter")                               

window.grid_rowconfigure([0,1,2,3,4], weight=0)
window.grid_columnconfigure([0], weight=1)

# Inject DnD into CustomTkinter's root
TkinterDnD.require(window)

drag_drop_input = CTkEntry(window,                          
                      placeholder_text="⬇️ Drag files here...",height=70)  
drag_drop_input.grid(row = 0,pady=10,sticky='nsew')

link_box = CTkTextbox(window,)   
link_box.grid(row = 1,pady=10,sticky='nsew')

drag_drop_input.drop_target_register(DND_FILES)
drag_drop_input.dnd_bind("<<Drop>>", on_drop)

def start_project_func():
    window.configure(state="disabled")
    for widget in result_frame.winfo_children():
        widget.destroy()
    text_content = link_box.get("0.0", "end")
    lines = text_content.split("\n")

    for line in lines:
        img_2page = 0
        img_1page = 0
        line = line.strip()
        if line != "":
            try:
                image_files = [f for f in os.listdir(line) if f.lower().endswith(image_extensions)]
                for image_name in image_files:
                    with Image.open(os.path.join(line, image_name)) as img:
                        width, height = img.size

                    if width < height:
                        move_img(line, image_name, 1)
                        img_1page += 1
                    else:
                        move_img(line, image_name, 2)
                        img_2page +=1
                if image_files != []:
                    if img_1page > 0 and img_2page > 0:
                        text_lbl = "[  ✅ Successful ] "+line + f" [(1) page:{img_1page} , (2) page:{img_2page}]"
                    elif img_1page > 0:
                        text_lbl = "[  ✅ Successful ] "+line + f" [(1) page:{img_1page}]"
                    else:
                        text_lbl = "[  ✅ Successful ] "+line + f" [(2) page:{img_2page}]"
                    
                    lbl = CTkLabel(result_frame,
                    text=text_lbl,
                    anchor="w",)
                    lbl.grid(pady = 1,sticky='w')
                else:
                    text_lbl = "[🔍 img not found] "+line
                    lbl = CTkLabel(result_frame,
                    text=text_lbl,
                    anchor="w",)
                    lbl.grid(pady = 1,sticky='w')
            except:
                text_lbl = "[❌ Unsuccessful ] "+line
                lbl = CTkLabel(result_frame,
                text=text_lbl,
                anchor="w",)
                lbl.grid(pady = 1,sticky='w')
    link_box.delete(0.0,END)
    window.configure(state="normal")
                

button = CTkButton(window,text="start",
                corner_radius=10,
                height=50,
                command=start_project_func
                )
button.grid(row = 2,pady=10,sticky='nsew')

result_frame = CTkScrollableFrame(window,)
result_frame.grid(row = 3,pady=10,sticky='nsew')

window.mainloop()