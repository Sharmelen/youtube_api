from youtube_api import YouTubeDataAPI
import requests
import bs4
import re
import pymysql
import pafy

connection = pymysql.connect(host='37.59.55.185', user='4Kdgz5M8bA', port=3306, password='s09exGmH7V',
                                 db='4Kdgz5M8bA',
                                 cursorclass=pymysql.cursors.DictCursor)
api_key = "AIzaSyBPZ68tFCo391ofWwOb-laiGuZM0SX7v9g"

def retrive_db():

    try:
        with connection.cursor() as cursor:

            sqlQuery_1 = "SELECT video_id FROM videos;"
            sqlQuery_2 = "INSERT videos_week (video_id, view_week_1, view_week_2, view_week_3) VALUES (%s,%s,'0','0')"
            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()
            s = []
            for row in rows:
                #print(row)
                s.append(row)


        total_vid = len(s)
        #url_append = []
        #week_1 = []
        for x in range (total_vid):

            url = (str(s[x]).split())[1].strip("',',}")
            video_id = url.strip('https://www.youtube.com/watch?v=')
            try:
                request_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
                request = requests.get(request_url)
                raw = request.text
                splits = raw.split(',')
                numbers = re.compile(r'\d+(?:\.\d+)?')

                views = splits[7]

                view_count = numbers.findall(views)
                new_view = view_count[0]

                view_updater(url,new_view)
            except:
                print('problems with video',url)



        connection.commit()

    except pymysql.err.InternalError as e:
        print('{}'.format(e))

def view_updater(url,new_view):
    try:
        with connection.cursor() as cursor:
            #INSERT videos_week (video_id, view_week_1, view_week_2, view_week_3) VALUES (%s,%s,'0','0')
            sqlQuery = "UPDATE videos_week SET view_week_3 = %s WHERE video_id = %s  "

            try:
                print(url)
                cursor.execute(sqlQuery,(new_view,url))
                print(new_view)
                print('view inserted')
            except:
                print('duplicate video')

        connection.commit()

    except pymysql.err.InternalError as e:
        print('{}'.format(e))



retrive_db()