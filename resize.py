from PIL import Image
import glob

root_dir = "C:/Users/kuume/OneDrive/Bureau/python/img"


for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    im = Image.open(filename)
    imResize = im.resize((1024,1024), Image.ANTIALIAS)
    imResize.save(filename , 'JPEG', quality=90)