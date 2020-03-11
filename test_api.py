from youtube_api import YouTubeDataAPI
import pafy

api_key = 'USE YOUR OWN API KEY'
yt = YouTubeDataAPI(api_key)

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

video = pafy.new('https://www.youtube.com/watch?v={}'.format(video_id))

print('https://www.youtube.com/watch?v={}'.format(video_id))
print("video rating : ",video.rating)
print("video length : ",video.length)
print("video likes : ", video.likes)
print("video dislikes : ",video.dislikes)
print("video views : ",video.viewcount)
