import glob
import os
from instabot import Bot
import urllib.request
import feedparser
import datetime

# CREDENTIALS(from f)





#bot = Bot()
# bot.login(username=barca.4ca, password=nmhasnobitches123) 

# <-------SCRAPING-------->
feed = feedparser.parse("https://www.news18.com/rss/tech.xml")
# PRINT NO OF ENTRIES
print('Number of RSS posts :', len(feed.entries))

while True:
  # ENTER FEED NO. (TO PREVIEW POST)
  i = int(input("Enter feed u want to see:"))
  # EXTRACTING DATA FROM FEED INDEX
  entry = feed.entries[i]
  title = entry.title
  summary = entry.summary
  tags = '#technology #tech #innovation #engineering #business #iphone #technews #science #design #apple #gadgets #electronics #android #software #programming #smartphone #bhfyp #samsung #instagood #coding #computer #pro #instatech #education #security #gadget #instagram #mobile #technologynews #art'
  cap = (title + '\n\n' + summary + '\n.\n.\n.\n' + tags)
  print(cap)
  # FOR SCRAPING IMAGE FROM RSS
  imgurl = entry.media_content[0]['url']
  # FOR DOWNLOADING THE IMAGE FROM URL
  urllib.request.urlretrieve(imgurl, "imgmain.jpg")

  # POST CONFIRMATION
  choice = input("Do you wish to post it? [Y/N]:")
  if choice == 'n' or choice == 'N':
    continue
  else:
    # <-------POSTING-------->
    # upload_photo — Uploads photo to your account.
    #bot.upload_photo("/imgmain.jpg", caption=cap)
    print("POSTED!")
    # To get time
    time = str(datetime.datetime.now())
    print(time)
    # Logging Posts
    f = open("instalog.txt", "a")
    f.write("The post titled ['" + title +
            "'] has been posted to instagram at [ " + time + " ].\n\n")
    f.close()

  # POST MORE?
  ch = input("Do you wish to enter more? [Y/N]:")
  if ch == 'n' or ch == 'N':
    break

# clear cookies to prevent errors
try:
  cookie_del = glob.glob("config/*cookie.json")
  os.remove(cookie_del[0])
except:
  pass
