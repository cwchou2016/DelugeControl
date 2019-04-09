import os


class DelugeControl:
    def __init__(self):
        self.torrents = self.readInfo()

    def readInfo(self):
        '''
        Parse Info to dictionary
        '''

        os.system("deluge-console info > info.txt")

        dict_content = {}
        torrent_list = []
        with open("info.txt") as f:
            f.readline()
            for line in f:
                line = line.strip(" ")
                if line == '\n':
                    torrent_list.append(dict_content)
                    dict_content = {}
                    continue

                sline = line.split(":")
                dict_content[sline[0]] = sline[1].strip(' ').strip('\n')

        os.system("rm info.txt")
        return torrent_list

    def rmCompleteTorrent(self):
        pass


if __name__ == '__main__':
    print("test")

    dc = DelugeControl()

    print(dc.torrents)

    print("done")
