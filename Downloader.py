import random
from Files import Files
from urllib import request


class Downloader(object):
    """docstring for Downloader"""

    def __init__(self, arg):
        super(Downloader, self).__init__()
        self.arg = arg

    def downloadImage(url):
        name = random.randrange(1, 99999)
        full_name = 'image_' + str(name) + ".jpg"
        request.urlretrieve(url, full_name)

    def downloadFile(url, savePath):
        response = request.urlopen(url)
        csv = response.read()
        csv = str(csv)
        file = Files
        file.writeFile(savePath, csv)

var = Downloader
var.downloadImage('http://pudim.com.br/pudim.jpg')
var.downloadFile(
    'http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv', 'csvFile.csv')
