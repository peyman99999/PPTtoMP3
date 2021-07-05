import os
import re
import sys
import pathlib
import time
from pprint import pprint

# Getting the files path and validating it
def inpPath():
	inp = input("*** Enter files' location: ")
	return inp


# files = os.scandir('/media/peyman/EA6CFFC16CFF869B/University/ترم 4/Immunology/sound')
'''try:
    files = os.scandir(inp)
except FileNotFoundError as err:
	print('\n', 'Error finding the directory:', err)
	sys.exit()
except:
	sys.exit()'''


format_tuple = (
	'.3gp',	'.8svx', '.aa', '.aac', '.aax',	'.act', '.aiff', '.alac', '.amr', '.ape', '.au', 
	'.awb', '.cda', '.dct', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', 
	'.m4p', '.mmf', '.mogg', '.mp3', '.mpc', '.msv', '.nmf', '.opus', '.org', '.org', '.raw', 
	'.rf64', '.rm', '.sln', '.tta', '.voc', '.vox', '.wav', '.webm', '.wma', '.wv'
)


# Body of program
def body(filesLocation):
    inpPath = pathlib.Path(filesLocation)
    if not inpPath.exists():
    	print('!!! Invalid path, try again next time. !!!')
    	raise Exception('!!! Invalid path, try agian next time. !!!')

    # Printing beginnig files
    files = os.scandir(inpPath)
    # print(files)
    files_list = list(files)
    
    if __name__ == '__main__':
    	print('\n', 'Files currently in the directory:(sorted) ')
    	pprint(sorted([e.name for e in files_list]))


    # Checking the name and changing it
    for f in files_list:
    	# print(f.name, end='\n')
    	# print(len(f.name))
    	if sys.platform.startswith('linux'): 
    	    path_name = re.search(r'(.+/)([^\d]+)(\d+)(\..+)', f.path).groups()
    	    # print(path_name, 'regex')
    	    # print(path_name[2], 'regex')
    	elif sys.platform.startswith('win32'):
    	    path_name = re.search(r'(.+\\)([^\d]+)(\d+)(\..+)', f.path).groups()
    
    	if path_name[3].lower() in format_tuple:
    		if int(path_name[2]) < 10 and len(path_name[2]) < 2:
    		    # print(path_name[2], '***')
    		    new_name = path_name[1] + '0' + path_name[2]
    		    # print(new_name)
    		    os.rename(f.path, path_name[0] + new_name + path_name[3])

    # Printing final results
    files2 = os.scandir(filesLocation)
    if __name__ == '__main__':
    	print('\n', 'New files:(sorted)')
    	pprint(sorted([e.name for e in list(files2)]))
    
    print('** Renaming Completed **')
    time.sleep(1)

# pprint(files_list)
# print(type(next(files)))
# print(next(files).name)
# print(next(files).path)
# help('posix.DirEntry')

if __name__ == '__main__':
	Location = inpPath()
	body(Location)