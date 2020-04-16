from tkinter import *
from PIL import Image, ImageTk
from files_utils import *
import Images2PDF as I2PDF
import sys, glob

DEFAULT_DIR = "C:\\Users\\taych_000\\Documents\\HBL"

class Interface():

    def __init__(self):
        root = Tk()
        root.title("Conversion and Aggregration program")
        root.bind('<Escape>', lambda e: root.destroy())

        self.filelist = Listbox(root, width=100, selectmode=EXTENDED)
        self.filelist.grid(row=0, sticky=W+E+N+S)
        self.filelist.bind('<Button-1>', self.filelist_clickselect)
        self.filelist.bind("<Double-Button-1>", self.show_image)
        self.filelist.bind("<B1-Motion>", self.filelist_reorder)
        self.curIndex = None

        self.cmd_area = Frame(root, bg="black")
        self.cmd_area.grid(row=1, sticky=W+E+N+S)
        self.btn_gen = Button(self.cmd_area, text="Generate", command=self.gen_pdf)
        self.btn_gen.place(relx=0.5, rely=0.5, anchor=CENTER)

        selected_image = Image.open("./Sophie1.jpeg").resize((480,640))
        self.photo = ImageTk.PhotoImage(selected_image)

        self.canvas = Canvas(root, width=480, height=640)
        self.canvas.grid(row=0, column=1, rowspan=2)
        self.canvas_img = self.canvas.create_image(240,320,image=None)

    def filelist_clickselect(self, event):
        self.curIndex = self.filelist.nearest(event.y)

    def filelist_reorder(self, event):
        """
        Support for drag and drop re-selection
        """
        fl = self.filelist
        i = fl.nearest(event.y)
        old = fl.get(i)
        if i < self.curIndex:
            fl.delete(i)
            fl.insert(i+1, old)
        elif i > self.curIndex:
            fl.delete(i)
            fl.insert(i-1, old)
        self.curIndex = i
            

    def show_image(self, event):
        """ 
        Event that loads and updates canvas from the new fileclick 
        from filelist. Only shows the first file from filelist.
        """
        lst = self.filelist.curselection()
        if len(lst)==0: return
        f = self.filelist.get(lst[0])
        print(f"Display file: {f}")
        selected_img = Image.open(f).resize((480,640))
        self.photo = ImageTk.PhotoImage(selected_img)
        self.canvas.itemconfig(self.canvas_img, image=self.photo)

    def set_files(self, file_list):
        """
        Clears lsitbox self.filelist and assigns to list of string file_list
        """
        self.filelist.delete(0, END)
        for f in file_list:
            self.filelist.insert(END, f)

    def run(self): mainloop()

    def gen_pdf(self):
        sel = [self.filelist.get(x) for x in self.filelist.curselection()]
        print(f"Generate pdf: {sel}")
        I2PDF.save_to_pdf(sel)


iface = Interface()

# temp testing code
if len(sys.argv)>1 and sys.argv[1]=="TEST":
    test_files = glob.glob("C:\\Users\\taych_000\\Downloads\\*.jpg")
    iface.set_files(test_files)
else:
    d = set_today_directory("C:\\Users\\taych_000\\Documents\\HBL")
    print(f"Directory: {d}")

    f = get_today_candidate_files("C:\\Users\\taych_000\\Downloads")
    print(f"Candidate moved files: {f}")
    move_files(f,d)
    iface.set_files(img_files_dir(d))

iface.run()