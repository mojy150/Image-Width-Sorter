from customtkinter import *
import os
import shutil
from tkinterdnd2 import TkinterDnD, DND_FILES

image_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")

def on_drop(event):
    # event.data is a raw Tcl list; use splitlist to handle multiple/spaced paths, see note above
    folders = window.tk.splitlist(event.data)
    # link_box.delete(0, "end")
    for folder in folders:
        link_box.insert("end", folder + "\n")

window = CTk()                                             
window.geometry("500x700")                                 
window.title("Image Width Sorter")                               

window.grid_rowconfigure([0,1,2,3,4], weight=0)
window.grid_columnconfigure([0], weight=1)

# Inject DnD into CustomTkinter's root
TkinterDnD.require(window)

drag_drop_input = CTkEntry(window,                          
                      placeholder_text="⬇️ Drag files here...",height=50)  
drag_drop_input.grid(row = 0,pady=10,sticky='nsew')

link_box = CTkTextbox(window,)   
link_box.grid(row = 1,pady=10,sticky='nsew')

drag_drop_input.drop_target_register(DND_FILES)
drag_drop_input.dnd_bind("<<Drop>>", on_drop)

def start_project_func():
    text_content = link_box.get("0.0", "end")  # گرفتن کل متن از ابتدا تا انتها
    lines = text_content.split("\n")

    for line in lines:
        if line.strip() != "":
            image_files = [f for f in os.listdir(line) if f.lower().endswith(image_extensions)]
            for image_name in image_files:
                
                # ساخت مسیر پوشه جدید با اسم "1" داخل destination_folder
                new_folder = os.path.join(line, "1")

                # ساخت پوشه (اگه از قبل وجود نداشته باشه)
                os.makedirs(new_folder, exist_ok=True)

                # مسیر کامل مبدا و مقصد
                source_path = os.path.join(line, image_name)
                destination_path = os.path.join(new_folder, image_name)

                # انتقال فایل
                shutil.move(source_path, destination_path)

button = CTkButton(window,text="start",
                corner_radius=10,
                height=50,
                command=start_project_func
                )
button.grid(row = 2,pady=10,sticky='nsew')

window.mainloop()