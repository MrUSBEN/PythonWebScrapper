import webbrowser
import requests,bs4
#from bs4 import BeautifulSoup
import os
#--------use to define working directory----
os.chdir("D:\\KEK\\webExp\\")
#-------------------------------------------
#getting raw site data to mine
res = requests.get("http://www.google.com")
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))    
fo=open("data.txt","wb+")
for chunk in res.iter_content(100000):
	fo.write(chunk)
fo.close()
print("Web page raw data saved.")
print("------------------------")
parser = bs4.BeautifulSoup(res.text,"html.parser")
#print(type(parser))
print("Searching for all links...")
print("------------------------")
#Displaying then writing extracted data to file 
fo1=open("linkData.txt","a")
for link in parser.find_all('a'):
    linkData = link.get('href')
    fo1.write(linkData+'\n')
    print(linkData)
fo1.close()



