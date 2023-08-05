#A simple URL shortening API wrapper Python library.
#https://pypi.org/project/pyshorteners/

import pyshorteners

#url_mapping = {} Dictionary
url_mapping = {}

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url

print("\n ==== Welcome to Link Shortener ==== ")
while True:
    long_url = input("\nEnter Your URL----: ")
    short_url = shorten_url(long_url)
    print(f"\nYour Shortened URL: {short_url}")

    next = input("\nDo you want to shorten more URLs? (yes/no): ")
    if next == "no":
        break

