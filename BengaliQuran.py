# Made by p32929
# My facebook ID: https://www.facebook.com/p32929

import urllib.request, re
def parse(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    strHTML = html.decode()
    return strHTML

print("List of the Suras:\n")
website = "http://www.ourholyquran.com"
string = parse(website)

naa = re.findall(r'<a href="(.*?)">(.*?)</a>', string)
for c in range(51, 165):
    print(naa[c][1])
print("\n")

key = int(input("Enter a sura number to read: "), 10)
print("\n")
final = website + naa[key + 50][0]
parsedData = parse(final)
ayats = re.findall(r'la-text\">(.*?)</', parsedData)

count = 0
for ayat in ayats:
    print(ayat)
    count += 1

print("\n\n//Total ayats = " + str(count))
