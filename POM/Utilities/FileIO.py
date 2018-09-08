import random
import string
import pathlib
import os
from Utilities.DateTime import DateTime


class FileIO:
    @staticmethod
    def CreateFile(FilePath, FileNameLength=None, FileSize=1024, NumberOfFiles=1, FileExtension=".txt",AddTimeStamp=False):
        pathlib.Path(FilePath).mkdir(parents=True, exist_ok=True)
        if (AddTimeStamp):TimeStamp = "-" + DateTime.GetTimeStamp();
        else: TimeStamp = ""
        if (FileNameLength is not None):
            FileName = ''.join(random.choice(string.ascii_letters) for _ in range(FileNameLength))
            FileName = "Auto-" + FileName
        else:
            FileName = "Auto-"
        FileLocationList = list();
        for Counter in range(NumberOfFiles):
            FileLocation = FilePath + "\\" + FileName + "_" + str(Counter) + TimeStamp + FileExtension;
            FileLocationList.append(FileLocation);
            with open(FileLocation, 'wb') as FileWrite:
                Data = os.urandom(FileSize)
                Data = ''.join(random.choice(string.ascii_letters) for _ in range(FileSize))
                FileWrite.write(Data.encode('utf-8'))
                # fout.write(Data)
        return FileLocationList;
