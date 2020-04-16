import datetime as DT
import os, glob, shutil

IMG_EXT = ["*.jpeg", "*.jpg", "*.png"]

def month_day():
    now = DT.date.today()
    return now.strftime("%b %d")

def set_today_directory(ROOT):
    """
    Given today's date, create appropriate directory in ROOT/{Mth}{Day}
    Returns the full path to directory
    """
    now = month_day()
    dir_name = now.replace(' ','')
    dest_dir = os.path.join(ROOT, dir_name)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    return dest_dir

def get_file_month_day(fpath):
    """ Returns the 'mth day' string belonging to a file """
    t = os.path.getctime(fpath)
    return DT.date.fromtimestamp(t).strftime("%b %d")

def get_today_candidate_files(path):
    """
    Goes to today's candidate directory "path" and obtains list
    of files created with today's date and returns list
    """
    files = []
    for ext in IMG_EXT:
        files.extend(glob.glob(os.path.join(path, ext)))
    today = month_day()
    return [f for f in files if get_file_month_day(f)==today]

def move_files(filelist, dest_dir):
    for f in filelist:
        print(f"Moving {f} to {dest_dir}")
        shutil.move(f, dest_dir)

if __name__=="__main__":   
    d = set_today_directory("C:\\Users\\taych_000\\Documents\\HBL")
    print(f"Directory: {d}")

    f = get_today_candidate_files("C:\\Users\\taych_000\\Downloads")
    print(f"Files: {f}")

    print(f"Moving files to {d}")
    move_files(f, d)