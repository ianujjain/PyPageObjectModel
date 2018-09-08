from Utilities.FileIO import  FileIO


FileLocationList = FileIO.CreateFile(FilePath="D:\\Dude\\", NumberOfFiles=7, FileNameLength=10, AddTimeStamp=True)
print(len(FileLocationList))
for Index, FileLocation in enumerate(FileLocationList):
    print(Index)