import os


class DelugeControl:
    def __init__(self):
        self.pause()
        self.torrents = self.readInfo()

    def pause(self):
        os.system('deluge-console "pause *"')

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

    def rmTorrent(self, id):
        cmd = 'deluge-console "rm {}"'.format(id)
        os.system(cmd)


if __name__ == '__main__':
    print("test")

    dc = DelugeControl()

    print(dc.torrents)

    dc.rmTorrent("cc8")

    print("done")
