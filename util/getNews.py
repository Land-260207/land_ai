import requests
import xml.etree.ElementTree as ET

def newsCrawler(region: str):
    URL = f"https://news.google.com/rss/search?q={region}&hl=ko&gl=KR&ceid=KR:ko"
    result = requests.get(URL)

    root = ET.fromstring(result.content)

    titles = []
    for item in root.findall(".//item"):
        title = item.find("title").text
        titles.append(title)
    print(*titles)
    return titles[:10]