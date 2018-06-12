from bs4 import BeautifulSoup
import bs4
import webbrowser
import requests


url = "www.daka90.co.il"
r  = requests.get("http://" +url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

list_deals = soup.find_all("a", {"class":"checkOut"})

for deal in list_deals:
    description = deal.get_text()
    description = description.replace("\n\n","")
    print(description)
    ans = input("Are you interested in this deal? Y/N")
    if ans == "Y":
        print()
        deal_url = ("http://" + url + deal['href'].encode('ascii','ignore'))
        webbrowser.open_new(deal_url)


