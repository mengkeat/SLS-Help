from PIL import Image
import zipfile as zf
import os

OUT_PDF_NAME = "output.pdf"

def save_to_pdf(image_list, pdf_fname = OUT_PDF_NAME):
    """
    Given image_list of image files
    - Extract the base dir path from the first in image_list
    - Collates all images to a single pdf
    - Write to the OUT_PDF_NAME in the same directory
    """
    if len(image_list)==0: return
    imgs = [Image.open(iname) for iname in image_list]

    bname = os.path.dirname(image_list[0])
    pdf_filename = os.path.join(bname, pdf_fname)
    print(f"Generating pdf: {pdf_filename}")
    imgs[0].save(pdf_filename, save_all=True, append_images=imgs[1:])


def zip_img_to_pdf(zfile, out_pdf = OUT_PDF_NAME):
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

    save_to_pdf(ifiles)