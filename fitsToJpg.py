import sys
import numpy as np
import os
try:
    from astropy.io import fits
except ImportError:
    import pyfits as fits
from PIL import Image

# Read command line arguments
path = "C:/Users/kuume/OneDrive/Bureau/python/img/"
dir_list = os.listdir(path) 

print(dir_list)
for fit in dir_list:
    try:
        fitsfilename = path + '/' + fit
        vmin, vmax = float(500), float(1000)
    except IndexError:
        sys.exit('Usage: ' + sys.argv[0] + ' FITSFILENAME VMIN VMAX')

    # Try to read data from first HDU in fits file
    data = fits.open(fitsfilename)[0].data
    # If nothing is there try the second one
    if data is None:
        data = fits.open(fitsfilename)[1].data

    # Clip data to brightness limits
    data[data > vmax] = vmax
    data[data < vmin] = vmin
    # Scale data to range [0, 1] 
    data = (data - vmin)/(vmax - vmin)
    # Convert to 8-bit integer  
    data = (255*data).astype(np.uint8)
    # Invert y axis
    data = data[::-1, :]

    # Create image from data array and save as jpg
    image = Image.fromarray(data, 'L')
    imagename = fitsfilename.replace('.fits', '.jpg')
    image.save(imagename)