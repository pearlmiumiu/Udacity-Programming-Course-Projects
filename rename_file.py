import os

def rename_files():
	#get file names from a foler
	file_list=os.listdir(r"C:\OOP\prank")
	#print(file_list)
	saved_path=os.getcwd()
	os.chdir(r"C:\OOP\prank")
	for file_name in file_list:
		print "old name- "+ file_name
		print "new name- " + file_name.translate("None", "1234567890")
		os.rename(file_name, file_name.translate("None", "0123456789"))
	os.chdir(saved_path)

rename_files()
