#coding=utf-8
import os
import os.path
rootdir = "v:"                            

for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames: 
		if os.path.isfile(os.path.join(parent,filename)) == False:     
			print os.path.join(parent,filename)+"<>"
		else:
			print os.path.join(parent,filename)	 