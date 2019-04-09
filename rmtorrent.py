import os


class DelugeControl:
    def __init__(self):
        pass

    def readInfo(self):
        '''
        Parse Info to dictionart
        '''
        os.system("deluge-console info > info.txt")

    def rmCompleteTorrent(self):
        pass


if __name__ == '__main__':
    print("test")

    dc = DelugeControl()
    dc.readInfo()

    print("done")
