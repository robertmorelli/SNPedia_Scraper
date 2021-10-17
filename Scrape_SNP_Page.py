import requests
from bs4 import BeautifulSoup


#a search by keyword for the tables on page for RS numbers
def findInTables(string,tables):
  for x in tables:
    tbody=x.find("tbody")
    if(tbody):
      tr=tbody.find("tr")
      if(tr):
        td=tr.findAll("td")
        if(td):
          if(td[0].text==string):
            return "".join([x.text for x in td[1:]])
  print(string+" not found")
  return None




#soup up and roll out!
def SoupUp(rs):
  url = 'https://www.snpedia.com/index.php/'+rs
  response = requests.get(url)
  while(response.status_code!=200):
    response = requests.get(url)
  html = str(response.content)
  soup=BeautifulSoup(html)
  return soup


#big ol controller boy
def Scrape_SNP_Page(rs):
  stuff=[]

  soup=SoupUp(rs)




  bigRectangleThing=soup.find("div", {"class": "aside-right col-sm-4"})


  #finds gene table because it cannot be found by keyword search function
  tables=bigRectangleThing.findAll("table")
  sortable=soup.find("table",{"class":"sortable smwtable"})
  if(not sortable):
    print(rs+"!!!!!!!!")
    return[]
  sortbody=sortable.find("tbody")
  Gtable=sortbody.findAll("tr")[1:]

  toa=[[y.text[:-2] for y in x.findAll("td")] for x in Gtable]


  #adding everything that can be found using keyword search
  stuff.append(rs)
  stuff.append(findInTables("Orientation",tables))
  stuff.append(findInTables("Stabilized",tables))
  stuff.append(findInTables("Reference",tables))
  stuff.append(findInTables("Chromosome",tables))
  stuff.append(findInTables("Position",tables))
  #has to be in try except because im clipping the \n that exists when there is text. if there is no text it will crash
  try:
    stuff.append(findInTables("Gene",tables)[:-2])
  except:
    stuff.append(None)
  #makes a list for every column in the gene table. this is for easy db entry


  return [[*stuff,*x] for x in toa]

