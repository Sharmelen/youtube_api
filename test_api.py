from youtube_api import YouTubeDataAPI
import pafy
from bs4 import BeautifulSoup
import requests
import re

api_key = 'AIzaSyASfy22lmaxSt2-MbAk9nMZql3wTtLFSZ0'
yt = YouTubeDataAPI(api_key)

keyword_description = ['pretend','nursery','play','mommy','games','ryan','toys','nursery','action','cartoon','animation','rhyme','Bottle Flip']

searches = yt.search(q='ryan', max_results=2)

data = searches[1]
print("video_id: ",data['video_id'])
video_id = data['video_id']
print("channel title: ",data['channel_title'])
print("channel id : ",data['channel_id'])
print("Publish Date : ",data['video_publish_date'])
print("Video Title : ",data['video_title'])
print("Video Description : ",data['video_description'])
print("Video Category : ",data['video_category'])
print("Video Thumbnail : ",data['video_thumbnail'])
print("Date Collected : ",data['collection_date'])

vid_descriprion = data['video_description']

cumulative = []
for x in range (len(keyword_description)):
    if keyword_description[x] in vid_descriprion :
        #print("yes")

        cumulative.append(keyword_description[x])

if len(cumulative) > 2:
    print("Video Tag : Baby Video" )


url = 'https://www.youtube.com/watch?v={}'.format(video_id)

video = pafy.new('https://www.youtube.com/watch?v={}'.format(video_id))

print('https://www.youtube.com/watch?v={}'.format(video_id))
print("video rating : ",video.rating)
print("video length : ",video.length)
print("video likes : ", video.likes)
print("video dislikes : ",video.dislikes)
print("video views : ",video.viewcount)


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

view_count = soup.find_all('a',class_="content-link spf-link yt-uix-sessionlink spf-link")

list = str(view_count).split()


related_link = [i for i in list if i.startswith('href')]

for x in range (len(related_link)):

    print('https://www.youtube.com{}'.format(related_link[x].strip('href=""')))
