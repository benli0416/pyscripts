#coding=utf-8
import os,os.path,datetime,time,sys,Image

#rootdir = r"V:\factory\372502167961401"                            
rootdir = r"U:\pyscripts\imtest"
 
def resize(infile,outfile):
	im = Image.open(infile)
	#print infile,im.format, im.size, im.mode
	#im.show()
	(x,y) = im.size #read image size
	x_s = 1440 #define standard width
	y_s = y * x_s / x #calc height based on standard width
	#print x_s,y_s
	out = im.resize((x_s,y_s),Image.ANTIALIAS)
	out.save(outfile)
	print infile,filesizeM,im.format, im.size, im.mode,(x_s,y_s)

for parent,dirnames,filenames in os.walk(rootdir):
	for i in filenames:
			try:
			        sep = "~~~"
				filename = os.path.join(parent,i)
				filestats = os.stat(filename)
				filesizeM = str(os.path.getsize(filename)/1024.00/1024.00)
				filesuffix = os.path.splitext(filename)[1]
				lastModified = datetime.datetime.fromtimestamp( filestats.st_mtime ).strftime('%Y%m%d%H%M%S')
				lastAccessed = datetime.datetime.fromtimestamp( filestats.st_atime ).strftime('%Y%m%d%H%M%S')
				created = datetime.datetime.fromtimestamp(filestats.st_ctime ).strftime('%Y%m%d%H%M%S') 
				
				#print filename+sep+filesizeM+sep+filesuffix+sep+lastModified+sep+lastAccessed+sep+created+sep+str(filestats)
				
				if os.path.getsize(filename)/1024.00/1024.00 > 8.00:  
					resize(filename,filename)
					
				
			except:
				info=sys.exc_info()
				print info[0],":",info[1]
				continue
							
		
		