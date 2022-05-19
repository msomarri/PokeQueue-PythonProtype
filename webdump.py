# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import bs4 as bs
import pandas as pd
import re
import requests
# python 3 only
import urllib.request
from urllib.error import URLError
import os


# Code that would do a batch download of pages . Aiming at downloading all the related pokemon pages
def downloadpage(arrypages, filenames):
    counter = 0
    for n in filenames:
        try:
            response = urllib.request.urlopen(arrypages[counter])
            html_content = response.read()
            s = "Pokemon Data\\" + n + ".html"
            print(s)
            print(type(s))
            with open(s, "wb") as fp:
                fp.write(html_content)
            counter = counter + 1

        except URLError as e:
            print("Unable to download page: " + str(e.reason))

# This method will grab the location information on pokemon


def grablocation(filename):
    location_info = []
    html_content = None
    try:
        html_content = requests.get(filename)
    except URLError as e:
        print("Unable to read page: " + str(e.reason))

    soup = BeautifulSoup(html_content.content, 'html.parser')
    for table in soup.find_all("tr"):
        look = table.find(class_="fooeevee")
        if look is not None:
            location_info.append(table.find(class_="fooinfo"))

    return location_info[0]


def createdatabase():
    # Open the page online
    base_web = "https://www.serebii.net/"
    html_content = None
    try:
        html_content = requests.get("https://www.serebii.net/legendsarceus/hisuipokedex.shtml")
    except URLError as e:
        print("Unable to read page: " + str(e.reason))

    soup = bs.BeautifulSoup(html_content.content, "html.parser")
    # llist will help determine all the hyperlinks so that we can store that information
    llist = []
    tableitems = []
    pic_list = []
    # Following the file format i can extract the table that im interested in using the following method
    for links in soup.find_all("td"):
        # String clean up
        s = links.get_text().strip("\n").strip("\t").strip("\n")
        # Remove any characters that are not a - z
        s = re.sub("[^a-zA-Z0-9]+", "", s)
        # Not interested  in empty spaces
        if s == " " or s == "":
            continue
        tableitems.append(s)
        llist.append(links)

        # grab information where the pictures are store
    for pic in soup.find_all(class_="pkmnblock"):
        pic_list.append(base_web + pic.img['src'])

    # By messing round with the file I can see that the list starts at 7
    # table items contain the dex number and pokemon name. we will need to seperate them out
    tableitems = tableitems[6:]
    llist = llist[6:]
    pokemon_names = []
    index = []
    counter = 1

    # Separate the data in two sections .
    # Odd would store the pokemon dex numbers
    # Even would store the pokemon name
    pokemon_link = []
    for item in tableitems:
        if counter % 2 == 0:
            pokemon_names.append(item)
        else:
            index.append(item)
            temp = llist[counter]
            pokemon_link.append(temp)
        counter = counter + 1
    # pl will contain the hyperlinks to the Pokemon information
    pl = []

    # Extract the actually links now
    for i in pokemon_link:
        pl.append(base_web + i.a['href'])

    # Information will be store into a data frame

    pfdata = pd.DataFrame()
    pfdata["dex number"] = index
    pfdata["pokemon"] = pokemon_names
    pfdata["Information links"] = pl

    # if there are no file present. This method can be used to download them
    # downloadpage(pl, pokemon_names)

    location_html = []
    location_info = []
    # Working out methods on extracting the location information
    counter = 1
    for info in pl:
        location_html.append(grablocation(info))
        print("loading current at " + str((counter / 242) * 100) + "%")
        counter = counter + 1
    for loc in location_html:
        location_info.append( loc.getText())
    pfdata["Location"] = location_info
    pfdata["picture location "] = pic_list
    pfdata["location_html"] = location_html
    # Store the links into the Excel file that we have
    pfdata.to_csv("pokemon_data.csv", index=False)
    print(html_content)




if __name__ == '__main__':
    createdatabase()


