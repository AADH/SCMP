#Gonna add some TF2 item examples(?)
import urllib.request
page = urllib.request.urlopen("http://steamcommunity.com/market/search?q=&category_440_Type%5B%5D=any&appid=440")
text = page.read().decode("utf8")
print(text)
