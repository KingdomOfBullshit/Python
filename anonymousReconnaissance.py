import mechanize
import subprocess

def viewPage(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	source_code = page.read()
	
	# Clear the screen
	subprocess.call("clear", shell = True)
	print ("-")*60
	print("Here is the source code: ")
	print ("-")*60
	print(source_code)
	
viewPage("https://www.foursquarecms.com")
hideMeProxy = ("http://87.255.70.183:8080")
testProxy = (viewPage, hideMeProxy)
