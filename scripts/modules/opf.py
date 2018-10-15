import shutil

def make_zip():
    shutil.make_archive('../pages/output','zip','./output')

def copy_file():
    shutil.copy("output.html","./output")
    shutil.copy("map.css","./output")
