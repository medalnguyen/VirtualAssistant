from googlesearch import search
import requests

url = search("Câu nói theo xu hướng của giới trẻ", lang="vi")

text = requests.get(url[0])

print(text)