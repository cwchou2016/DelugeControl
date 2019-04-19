#!/usr/bin/python3

import os


class DelugeControl:
    def __init__(self):
        self.pause()
        self.torrents = []
        self.readInfo()

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
        torrent_list.append(dict_content)
        self.torrents = torrent_list

    def rmCompletedTorrents(self):
        for item in self.torrents:
            if item.get("Progress") is not None:
                continue
            self.rmTorrent(item.get("ID"))

    def rmTorrent(self, id):
        cmd = 'deluge-console "rm {}"'.format(id)
        os.system(cmd)


if __name__ == '__main__':
    print("processing rmCompleteTorrent")

    dc = DelugeControl()
    dc.rmCompletedTorrents()
    print(dc.torrents)

    print("done")
