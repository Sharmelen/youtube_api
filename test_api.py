from youtube_api import YouTubeDataAPI
import pafy
from bs4 import BeautifulSoup
import requests
import pymysql
import os
import re

#video_id, channel_title, channel_id, publish_date, video_title, video_description, video_category, collection_date, video_url, \
#video_rating, video_length, video_likes, video_dislikes, view_count

url = 'https://www.youtube.com/watch?v=hp1TOvFKlgE&t=824s'
#AIzaSyASfy22lmaxSt2-MbAk9nMZql3wTtLFSZ0
#AIzaSyAEvNFEm7GFThoESLqU1ZQkikUR484beEI
def youtube_data_collector(url):
    api_key = 'AIzaSyAEvNFEm7GFThoESLqU1ZQkikUR484beEI'
    yt = YouTubeDataAPI(api_key)

    searches = yt.search(q=url, max_results=2)

    data = searches[0]
    print("video_id: ", data['video_id'])
    video_id = data['video_id']
    print("channel title: ", data['channel_title'])
    channel_title = data['channel_title']
    print("channel id : ", data['channel_id'])
    channel_id = data['channel_id']
    print("Publish Date : ", data['video_publish_date'])
    publish_date = data['video_publish_date']
    print("Video Title : ", data['video_title'])
    video_title = data['video_title']
    print("Video Description : ", data['video_description'])
    video_description = data['video_description']
    print("Video Category : ", data['video_category'])
    video_category = data['video_category']
    print("Video Thumbnail : ", data['video_thumbnail'])
    print("Date Collected : ", data['collection_date'])
    collection_date = data['collection_date']


    video = pafy.new('https://www.youtube.com/watch?v={}'.format(video_id))

    print('video url : https://www.youtube.com/watch?v={}'.format(video_id))
    video_url = 'video url : https://www.youtube.com/watch?v={}'.format(video_id)
    print("video rating : ", video.rating)
    video_rating = video.rating
    print("video length : ", video.length)
    video_length = video.length
    print("video likes : ", video.likes)
    video_likes = video.likes
    print("video dislikes : ", video.dislikes)
    video_dislikes = video.dislikes
    print("video views : ", video.viewcount)
    view_count = video.viewcount


    database(channel_title, channel_id, publish_date, video_title, video_description, collection_date, video_url,
             video_rating, video_length, video_likes, video_dislikes)

def find_related_videos(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    videos = []

    view_count = soup.find_all('a', class_="content-link spf-link yt-uix-sessionlink spf-link")

    list = str(view_count).split()

    related_link = [i for i in list if i.startswith('href')]

    for x in range(len(related_link)):
        v = 'https://www.youtube.com{}'.format(related_link[x].strip('href=""'))
        print(v)

        videos.append(v)

    for y in range(len(videos)):
        url = videos[y]
        #print(url)
        youtube_data_collector(url)


def database(channel_title, channel_id, publish_date, video_title, video_description, collection_date, video_url,
             video_rating,video_length,video_likes,video_dislikes ):

    connection = pymysql.connect(host=' ', user=' ', port=3306, password=' ', db=' ',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            sqlQuery_1 = "INSERT videos (video_id,channel_title,channel_id,video_publish_date,video_title, video_description, " \
                       "collection_date) VALUES (%s,%s,%s,%s,%s,%s,%s);"
            sqlQuery_2 = "INSERT videos_view (video_id, video_rating, video_length,video_likes,video_dislikes) VALUES (%s,%s,%s,%s,%s)"

            cursor.execute(sqlQuery_1,(video_url,channel_title,channel_id,publish_date,video_title,video_description,
                                            collection_date))

            cursor.execute(sqlQuery_2,(video_url,video_rating,video_length,video_likes,video_dislikes))



            print('hello')
        connection.commit()

    except pymysql.err.InternalError as e:
        print('{}'.format(e))




find_related_videos(url)
