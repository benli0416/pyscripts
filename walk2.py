#coding=utf-8
import os
import os.path
import datetime,time,sys
rootdir = "e:\picture"                            


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
				
				print filename+sep+filesizeM+sep+filesuffix+sep+lastModified+sep+lastAccessed+sep+created+sep+str(filestats)
			except:
				info=sys.exc_info()
				continue
				#print info[0],":",info[1]			
		
		