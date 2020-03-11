from youtube_api import YouTubeDataAPI

api_key = 'GET_YOUR_API_KEY'
yt = YouTubeDataAPI(api_key)

searches = yt.search(q='ryan',
                     max_results=1)
print(searches[0])

data = searches[0]

print(data['channel_title'])
