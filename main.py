from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
from android.permissions import Permission, request_permissions, check_permission
from kivymd.uix.label import MDLabel
from kivy.logger import Logger
from kivymd.app import MDApp
import os

def log(msg):
	Logger.info(msg)

def check_permissions(perms):
	for perm in perms:
		if check_permission(perm) != True:
			return False
	return True

def writer():
	
	testfile = 'Testing'                 # file with a string
	
	perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
	
	if  check_permissions(perms)!= True:
		request_permissions(perms)    # get android permissions     
		exit()                        # app has to be restarted; permissions will work on 2nd start
		
	try:
		Logger.info('Got requested permissions')    
		ffolder = os.path.join(primary_external_storage_path(),'KT') #folder name
		fname = os.path.join(ffolder,'testfile.txt')                 #file name
		log(f'writing to: {fname}')
		try:
			os.makedirs(ffolder)
			with open(fname, 'w') as f:        # write testfile
				f.write(testfile)
			return fname
		except Exception as e:
			pass
	
	except:
		log('could not write to external storage ... missing permissions ?')    

class MyApp(MDApp):

	def build(self):
		writer()              # <---- calling testwrite() here
		ffolder = os.path.join(primary_external_storage_path(),'KT')
		fname = os.path.join(ffolder,'testfile.txt')
		text = open(fname,'r').read()                          #reading the written txt
		return MDLabel(text = text, halign="center")           # displaying
	
MyApp().run()
