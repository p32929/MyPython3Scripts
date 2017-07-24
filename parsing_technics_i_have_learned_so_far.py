# Made by p32929
# My facebook ID: https://www.facebook.com/p32929

import urllib.request
def parse_formatted(url):
    request = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    HTTP_response = urllib.request.urlopen(request)
    HTML_string = HTTP_response.read().decode('utf-8')
    return HTML_string


import requests
def parse_unformatted(url):
    response = requests.get(url, headers={'User-Agent': 'Chrome'})
    HTML_string = response.content
    return HTML_string


# It also uses urllib.request
def parse_formatted_0(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    strHTML = html.decode()
    return strHTML


# Now use print to see the outputs :)
