from PIL import Image
import os.path as path
from os import walk
from sys import argv

if __name__ == '__main__':
    dir_name = argv[1]
    
    if path.exists(dir_name) and path.isdir(dir_name):

        listOfFiles = list()
        for (dirpath, dirnames, filenames) in walk(dir_name):
            listOfFiles += [
                path.join(dirpath, file) for file 
                in filenames 
                if '.git' not in dirpath and path.splitext(path.join(dirpath, file))[1].lower() == '.tif' 
                or '.git' not in dirpath and path.splitext(path.join(dirpath, file))[1].lower() == '.tiff'
            ]

        i = 0

        for image_tiff in listOfFiles:
            f, e = path.splitext(image_tiff)
            outfile = f + ".png"
            if image_tiff != outfile:
                try:
                    with Image.open(image_tiff) as im:
                        if (not path.exists(outfile)):
                            im.save(outfile)
                except OSError:
                    print("cannot convert", image_tiff)

            i = i + 1
            archive_max_count = len(listOfFiles)
            percent = 100 * ( i / archive_max_count )
            percent = int(percent)
            complete_text = '\rCompletado ' + str(percent) + '%'
            print(complete_text, end='', flush=True)

