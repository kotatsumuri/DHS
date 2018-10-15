from modules import video_clip
from modules import opncv
from modules import jread
from modules import mapping
from modules import csvread
from modules import opf

video=jread.read("./jsons/name.json")
csv_file=jread.read("./jsons/namecsv.json")

video_clip.vi_clp(video)
array=opncv.opncv(video)
csvread.csv_to_json(csv_file)

mapping.mapping(array,video)
opf.copy_file()
opf.make_zip()
