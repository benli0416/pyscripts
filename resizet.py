#coding=utf-8
import os
import os.path
import datetime,time,sys
import Image

im = Image.open("U:\pyscripts\imtest\临清税务登记证Document_0.jpg")
print im.format, im.size, im.mode
#im.show()
(x,y) = im.size #read image size
x_s = 1440 #define standard width
y_s = y * x_s / x #calc height based on standard width
print x_s,y_s
out = im.resize((x_s,y_s),Image.ANTIALIAS)
out.save("U:\pyscripts\imtest\临清税务登记证Document_0.jpg")