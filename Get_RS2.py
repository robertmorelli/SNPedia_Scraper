import requests
from bs4 import BeautifulSoup
import os


def findRSOnPage(sop):
  listss=sop.findAll("div",{"class":"mw-category-group"})
  lis=[]
  for lists in listss:
    for li in [x.text for x in lists.findAll("li")]:
      lis.append(li)
  return lis



#finds and returns next page url if present
def nextpage(sop):
  for x in sop.findAll("a"):
    if(x.text=="next page"):
      return "https://www.snpedia.com"+x['href']
  return None


#gets all gene names
def Get_RS():
  url = 'https://snpedia.com/index.php?title=Category:Is_a_snp'
  try:
    os.remove("RSList.txt")
  except:
    pass
  files=open("RSList.txt","w+")

  #snpedia is built like a linked list so this really is the only way
  while(url):
    response = requests.get(url)
    while(response.status_code!=200):
      response = requests.get(url)
    html = str(response.content)
    soup=BeautifulSoup(html)
    page=findRSOnPage(soup)

    #id gather clean up commas later than risk entering a non gene value
    files.write(",")
    files.write(",".join(page))
    files.write(",")
    url=nextpage(soup)
  files.close()
  print("RS Saved")
Get_RS()
