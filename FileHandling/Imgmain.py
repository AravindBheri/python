imgfile = open('FileHandling//red-ferrari-f40-p9.jpg', 'rb')

newimgfile = open('FileHandling//f40.jpg', 'wb')
for pix in imgfile:
   newimgfile.write(pix)