import requests
from  bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("a",class_ ="mt_a")

def country_list():
    cont_list =[]
    for i in range(len(data)):
        cont_list.append(data[i].get_text())
    return cont_list    
value = country_list()
print(" country :        rank: \n ..................................")
for index,i in enumerate(value):
    space = (20 - len(i))
    print(f"   {i}{' '*space}{index}")
