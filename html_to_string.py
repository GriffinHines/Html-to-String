from pathlib import Path
import os

#replace input.html with the path to your html file
data=Path('input.html').read_text().replace('\"','\\"').replace('\n','\\n\"+\n\"')

#create file
file_object = open('output.txt', 'a')
file_object.write('\"'+data)
file_object.close()
#remove closing +"
file_object = open('output.txt', 'rb+')
file_object.seek(-3, os.SEEK_END)
file_object.truncate()
file_object.close()
