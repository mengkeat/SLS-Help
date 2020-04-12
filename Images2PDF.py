from PIL import Image
import zipfile as zf
import os

def save_to_pdf(image_list, out_pdf):
    if len(image_list)==0: return
    imgs = [Image.open(iname) for iname in image_list]
    print(f"Generating pdf: {out_pdf}")
    imgs[0].save(out_pdf, save_all=True, append_images=imgs[1:])


def zip_img_to_pdf(zfile, out_pdf):
    with zf.ZipFile(zfile) as zipfile:
        files = [x.filename for x in zipfile.filelist]
        zipfile.extractall()
        save_to_pdf(files, out_pdf)
        for img_file in files:
            print(f"Cleaning up file: {img_file}")
            os.remove(img_file)

def process_zip(zfile):
    base = os.path.splitext(os.path.basename(zfile))[0]
    zip_img_to_pdf(zfile, f"{base}.pdf")

if __name__=="__main__":
    import tkinter, tkinter.filedialog
    root = tkinter.Tk()
    files = tkinter.filedialog.askopenfilenames(parent=root, 
                title='Choose files (jpeg, jpg, png, zip)',
                initialdir="./",
                filetypes=(("JPEG", "*.jpeg"), ("JPG","*.jpg"), ("PNG", "*.png"), ("ZIP", "*.zip")))
    files = root.tk.splitlist(files)

    zfiles = list(filter(lambda x: x[-4:]==".zip", files))
    ifiles = list(filter(lambda x: os.path.splitext(x)[1] in (".jpeg", ".jpg", ".png"), files))
    print(f"Zipfiles: {zfiles}")
    print(f"Image files: {ifiles}")

    for f in zfiles:
        print("Process zip {f}")
        process_zip(f)

    save_to_pdf(ifiles, "output.pdf")