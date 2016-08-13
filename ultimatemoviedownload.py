import wget
import urllib2
from bs4 import BeautifulSoup
from subprocess import call
'''file_url = 'http://www.lauraveirs.com/Songs/Rapture.mp3'
file_name = wget.download(file_url)'''
idmPath = "C:\Program Files (x86)\Internet Download Manager\IDMan.exe"
site1='http://sv1.bia2dl.xyz/Movies/250%20Top%20Movies/'
site2='http://dl.farsmovie.ir/movie/'
site3='http://dl.vahidfilm.com/Movie/'
hdr = {'User-Agent': 'Mozilla/5.0'}
choice=int(raw_input("Enter 1 for Source1 (list based) or 2 for Source2(Year wise) or 3 for Source 3(Collection wise) :"))
urls=[]
url2=[]
# HTML source for homepage.
if choice==1:
	url=site1
elif choice==2:
	movie_year=raw_input("Enter the year:")	
	url=site2+movie_year+"/"
elif choice==3:
	collection_no = raw_input("Enter the colection no. , any no. from 1 to 6:")
	url=site3+collection_no+"/"
else:
	print 'Enter valid choice'
		
def parse(url):
	
    req = urllib2.Request(url,headers=hdr)
    homePage = urllib2.urlopen(req)
    homePageSoup = BeautifulSoup(homePage,'lxml')
    Results = homePageSoup.find("tbody")
    name=Results.find_all("a")
    links=Results.find_all("tr")
     
    for i, j in enumerate(name):
            print str(i)+" "+j.text.encode("utf-8")
            
    print "---------------------------------------------------"	
    	
    for k, l in enumerate(links):
            urls.append(l.a['href'])
            
def parse_site3(url):
	
    req = urllib2.Request(url,headers=hdr)
    homePage = urllib2.urlopen(req)
    homePageSoup = BeautifulSoup(homePage,'lxml')
    Results = homePageSoup.find("pre")
    name=Results.find_all("a")
    #links=Results.find_all(a['href'])
    #print name['href']
    
     
    for i, j in enumerate(name):
            print str(i)+" "+j.text.encode("utf-8")
            #url2.append(j.text.encode("utf-8"))
            if j.has_attr('href'):
				#print j['href']
				url2.append(j['href'])
	    else:
                print "url extract failed"	
            
    print "---------------------------------------------------"
    	            
def Again():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to donload any more episode? (yes or no)')
    return raw_input().lower().startswith('y')

while True:
    
	            
    movie_name=""
    if choice == 1 or choice==2:
                 
                     
        parse(url)
        index=int(raw_input("Enter index of movie:"))            
        movie_name+=urls[index]            
        file_url=url+urls[index]
        print "Downloading the movie from" + file_url
        #file_name = wget.download(file_url)
        
    elif choice==3:
            parse_site3(url)
            index1=int(raw_input("Enter the index of movie:"))
            file_url=url+url2[index1]
            file_url.replace(">", "")
            print file_url
            movie_name+=url2[index1]
            
    downloader_choice=int(raw_input("How do you want to download movie? 1: Through idm  2:Through wget"))	
            
    print "Downloading the movie..."
    if downloader_choice==1:
            call([idmPath, "/d", file_url, "/n", "/s", "/f",  movie_name + '.mp4'])
    elif downloader_choice==2:
            file_name = wget.download(file_url)
    if not Again():
		break
	
	
	    
	
	

