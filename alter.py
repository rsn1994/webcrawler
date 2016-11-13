import csv
import os
import requests
from bs4 import BeautifulSoup

colHeader = ['imageurl']
colField = {'imageurl':'IMAGE URL'}

page = requests.get('http://www.pondiuni.edu.in')
print(page.status_code)
soup = BeautifulSoup(page.content)
tags = soup.find_all('img')
# print " ".join(set(tag['alt'] for tag in tags)) 

 
def Filewriter(imgul):
    fileName = "out" + ".csv"
    if os.access(fileName, os.F_OK):
        fileMode = 'a+'
    else:
        fileMode = 'w'

    csvWriter = csv.DictWriter(open(fileName, fileMode), fieldnames=colHeader)

    if fileMode == 'w':
        csvWriter.writerow(colField)  # Writing Column Header

    if not(imgul):
        imgul = "Alt text not defined"

    # writing each row with data
    csvWriter.writerow({'imageurl':imgul})
    return  

for i in tags:
    Filewriter(i.get('alt'))

