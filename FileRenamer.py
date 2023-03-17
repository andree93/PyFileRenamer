import os
from pathlib import Path, PurePosixPath
import datetime


def fileRenamer(pathName, prefix):
    path = Path(pathName)
    if Path.exists(path):
        fileList = Path.iterdir(path)
        for file in fileList:
            if Path.is_file(file):
                if not prefix:
                    prefix_tmp = datetime.datetime.fromtimestamp(file.stat().st_ctime).strftime("%d%m%Y") #get file creation time, and convert to string
                nameTmp = Path(f'{prefix_tmp}-{PurePosixPath(file).name}') #build path with prefix and file name
                Path.rename(file, PurePosixPath(path).joinpath(nameTmp)) #rename file
    else:
        print("Il percorso inserito non è valido!") 

    


if __name__ == "__main__":

    prefix = input("Inserisci il prefisso da usare per i file da rinominare, altrimenti verrà usata la data di ultima modifica del file: ")
    percorso = input("Inserisci il path della cartella contenente i file da rinominare: ")
    
    fileRenamer(percorso, prefix)




