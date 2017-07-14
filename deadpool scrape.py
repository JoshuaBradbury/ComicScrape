from bs4 import BeautifulSoup
import requests

comics = {}

pageCount = 42

count = 0

for i in range(1, pageCount + 1):
    r = requests.get("http://marvel.wikia.com/wiki/Category:Wade_Wilson_(Earth-616)/Appearances?page=" + str(i))
    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for div in soup.find_all("div", { "class" : "category-gallery-item" }):
        titleDiv = div.find_all("div", { "class" : "title" })[0]
        if "Vol" in titleDiv.text:
            title, vol = titleDiv.text.split("Vol")
            title = title.strip()
            vol = vol.strip()
            if not title in comics:
                comics[title] = {}
            values = vol.strip().split(" ")
            major, minor = values[0], values[1]
            if not major in comics[title]:
                comics[title][major] = {}
            if not minor in comics[title][major]:
                comics[title][major][minor] = "http://marvel.wikia.com/wiki/" + title + "_Vol_" + vol.replace(" ", "_")
            count += 1

print(count)

title = "Deadpool"
volume = 1
issues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for issue in issues:
    print(comics[title][str(volume)][str(issue)])
