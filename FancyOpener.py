import urllib.request

class Downloader(urllib.request.FancyURLopener):
	"""docstring for FancyOpener"""
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myOpener = FancyOpener()
myOpener.retrieve('http://hqultimate.com/leitor/hq/Cannibal/01/01.jpg', 'teste.jpg')