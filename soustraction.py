from astropy.io import fits
img = fits.getdata('C:/Users/kuume/OneDrive/Bureau/python/img/a.fits', ext=0) 
dark = fits.getdata('C:/Users/kuume/OneDrive/Bureau/python/img/b.fits') 
darksub = img - dark
fits.writeto('s15_sub.fits', darksub) # save output