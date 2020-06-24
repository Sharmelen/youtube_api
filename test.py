import pymysql
import numpy as np
from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


connection = pymysql.connect(host='37.59.55.185', user='4Kdgz5M8bA', port=3306, password='s09exGmH7V',
                                 db='4Kdgz5M8bA',
                                 cursorclass=pymysql.cursors.DictCursor)

def language_category():
    try:
        with connection.cursor() as cursor:

            sqlQuery_1 = "SELECT COUNT(video_id), language FROM videos_week GROUP BY language ;"

            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()
            s = []
            v = []

            for row in rows:
                language = row

                video_numbers = language['COUNT(video_id)']
                lang_category = language['language']

                s.append(video_numbers)
                v.append(lang_category)

            language_barchart(s,v)

        connection.commit()

    except pymysql.err.InternalError as e:
        print('{}'.format(e))
    print()

def view_evolution_category():
    try:
        with connection.cursor() as cursor:
            sqlQuery = 'SELECT * FROM videos_week'

            cursor.execute(sqlQuery)

            rows = cursor.fetchall()
            url_id = []
            case_1 = []
            case_2 = []
            case_3 = []
            case_4 = []
            case_5 = []
            case_6 = []

            for row in rows:
                url_id_1 = row['video_id']
                initial_view = row['20_4_2020'] - row['13_4_2020']
                middle_view = row['27_4_2020'] - row['20_4_2020']
                final_view = row['2_5_2020'] - row['27_4_2020']

                if final_view > middle_view > initial_view:
                    #print('GOING UP')
                    case_1.append(row)

                elif initial_view > middle_view > final_view:
                    #print('GOING DOWN')
                    case_2.append(row)

                elif initial_view == middle_view == final_view:
                    #print('NO CHANGE')
                    case_3.append(row)
                elif initial_view < middle_view > final_view:
                    #print('GO UP THEN GO DOWN')
                    case_4.append(row)

                elif initial_view > middle_view < final_view:
                    #print('GO DOWN THEN GO UP')
                    case_5.append

                else:
                    #print('New Graph')
                    case_6.append

            view_pattern_pie_chart(case_1,case_2,case_3,case_4,case_5,case_6)
            view_going_up(case_1)

    except pymysql.err.InternalError as e:
        print('{}'.format(e))

def famous_channel_category():
    try:
        with connection.cursor() as cursor:
            sqlQuery = 'SELECT COUNT(video_id) ,channel_title FROM videos WHERE channel_title = "ChuChu TV Nursery Rhymes & Kids Songs" OR channel_title = "Bounce Patrol - Kids Songs" OR channel_title = "Cocomelon - Nursery Rhymes" OR channel_title = "Little Baby Bum - Nursery Rhymes & Kids Songs" OR channel_title = "CVS 3D Rhymes & Kids Songs" GROUP BY channel_title'
            cursor.execute(sqlQuery)

            rows = cursor.fetchall()
            s = []
            v = []
            for x in range (len(rows)):
                count = rows[x]['COUNT(video_id)']
                channel_name = rows[x]['channel_title']
                s.append(count)
                v.append(channel_name)

            famous_channel_piechart(s,v)
    except pymysql.err.InternalError as e:
        print('{}'.format(e))


def language_barchart(s,v):

    height = s
    bars = v
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))

    # use the plt.xticks function to custom labels
    plt.xticks(y_pos, bars, color='orange', rotation=45, fontweight='bold', fontsize='13', horizontalalignment='center')

    # remove labels
    plt.title('Language Category')
    plt.tick_params(labelbottom='off')

    plt.show()




def view_pattern_pie_chart(case_1,case_2,case_3,case_4,case_5,case_6):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'GOING UP', 'GOING DOWN', 'NO CHANGE', 'GO UP THEN GO DOWN', 'GO DOWN THEN GO UP', 'NEW PATTERN'
    sizes = [len(case_1), len(case_2), len(case_3), len(case_4), len(case_5),len(case_6)]
    explode = (0, 0, 0, 0, 0.3, 0.2)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def view_going_up(case_6):
    en = []
    fr = []
    ko = []
    ar = []
    ru = []
    es = []
    it = []
    hi = []
    tr = []
    pl = []
    id = []
    ja = []
    vi = []
    sw = []
    de = []
    pt = []

    for x in range (len(case_6)):
        language = case_6[x]['language']
        print(language)
        if language == 'en':
            en.append(language)
        if language == 'fr':
            fr.append(language)
        if language == 'ko':
            ko.append(language)
        if language == 'ar':
            ar.append(language)
        if language == 'ru':
            ru.append(language)
        if language == 'es':
            es.append(language)
        if language == 'it':
            it.append(language)
        if language == 'hi':
            hi.append(language)
        if language == 'tr':
            tr.append(language)
        if language == 'pl':
            pl.append(language)
        if language == 'id':
            id.append(language)
        if language == 'ja':
            ja.append(language)
        if language == 'vi':
            vi.append(language)
        if language == 'sw':
            sw.append(language)
        if language == 'de':
            de.append(language)
        if language == 'pt':
            pt.append(language)

    bars = 'en', 'fr', 'ko', 'ar', 'ru', 'es', 'it', 'hi', 'tr', 'pl', 'id', 'ja','vi','sw','de','pt'
    height = [len(en), len(fr), len(ko), len(ar), len(ru),len(es),len(it),len(hi),len(tr),len(pl),len(id),len(ja),len(vi),len(sw),len(de),len(pt)]

    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))

    # use the plt.xticks function to custom labels
    plt.xticks(y_pos, bars, color='orange', rotation=45, fontweight='bold', fontsize='17', horizontalalignment='right')

    # remove labels
    plt.tick_params(labelbottom='off')
    plt.title('Language Category')
    plt.xlabel('Language')
    plt.ylabel('Video Count')
    plt.show()

def famous_channel_piechart(s,v):
    labels = v[0],v[1],v[2],v[3],v[4]
    sizes = [s[0], s[1], s[2], s[3], s[4]]
    explode = (0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
    print()



def single_channel_progress():
    try:
        with connection.cursor() as cursor:
            # https://www.youtube.com/watch?v=up0K2x2FC8Y channel = Amelia, Avelina & Akim                 type : latest
            # https://www.youtube.com/watch?v=cReKsCZdxoc channel = RubyandBonnie                          type : latest
            # https://www.youtube.com/watch?v=0QgjdRqr3Ik channel = MickTheMage                            type : oldest
            # https://www.youtube.com/watch?v=n0INguuO9WM channel = Comptines et chansons                  type : oldest
            # https://www.youtube.com/watch?v=kHSFpGBFGHY channel = ChuChu TV Nursery Rhymes & Kids Songs  type : most viewed
            # https://www.youtube.com/watch?v=j8z7UjET1Is channel = Bounce Patrol - Kids Songs             type : most viewed
            # https://www.youtube.com/watch?v=nbqHTdvUYTg channel = AWESOME SOLITUDE TV                    type : less viewed
            # https://www.youtube.com/watch?v=yc-wq2hnvzE channel = THE FILIPINO MOUSA                     type : less viewed

            sqlQuery_1 = "SELECT * FROM videos_week WHERE video_id = 'https://www.youtube.com/watch?v=0QgjdRqr3Ik' ;"

            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()

            week_1 = rows[0]['13_4_2020']
            week_2 = rows[0]['20_4_2020'] - rows[0]['13_4_2020']
            week_3 = rows[0]['27_4_2020'] - rows[0]['20_4_2020']
            week_4 = rows[0]['2_5_2020'] - rows[0]['27_4_2020']
            week_5 = rows[0]['9_5_2020'] - rows[0]['2_5_2020']
            week_6 = rows[0]['16_5_2020'] - rows[0]['9_5_2020']
            week_7 = rows[0]['24_5_2020'] - rows[0]['16_5_2020']
            week_8 = rows[0]['31_5_2020'] - rows[0]['24_5_2020']
            week_9 = rows[0]['7_6_2020'] - rows[0]['31_5_2020']

            x = ['13/4','20/4','27/4','2/5','9/5','16/5','24/5','31/5','7/6']
            y = [0,int(week_2),int(week_3),int(week_4),int(week_5),int(week_6),int(week_7),int(week_8),int(week_9)]
            print('initial view :' ,week_1)
            plt.plot(x, y)
            plt.xlabel('Date')
            plt.ylabel('View Count')
            plt.title('View Evolution')
            plt.show()

        connection.commit()




    except pymysql.err.InternalError as e:
        print('{}'.format(e))


def view_classifier():

    try:
        with connection.cursor() as cursor:
            # https://www.youtube.com/watch?v=up0K2x2FC8Y channel = Amelia, Avelina & Akim                 type : latest
            # https://www.youtube.com/watch?v=cReKsCZdxoc channel = RubyandBonnie                          type : latest
            # https://www.youtube.com/watch?v=0QgjdRqr3Ik channel = MickTheMage                            type : oldest
            # https://www.youtube.com/watch?v=n0INguuO9WM channel = Comptines et chansons                  type : oldest
            # https://www.youtube.com/watch?v=kHSFpGBFGHY channel = ChuChu TV Nursery Rhymes & Kids Songs  type : most viewed
            # https://www.youtube.com/watch?v=j8z7UjET1Is channel = Bounce Patrol - Kids Songs             type : most viewed
            # https://www.youtube.com/watch?v=nbqHTdvUYTg channel = AWESOME SOLITUDE TV                    type : less viewed
            # https://www.youtube.com/watch?v=yc-wq2hnvzE channel = THE FILIPINO MOUSA                     type : less viewed

            sqlQuery_1 = "SELECT * FROM `videos_week`;"

            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()

            below_100000 = []
            below_500000 = []
            below_1mil   = []
            below_10mil  = []
            below_20mil  = []
            for x in range (len(rows)):
                value = rows[x]['13_4_2020']
                if value < 100001:
                    below_100000.append(value)
                elif value > 100001 and value < 500001 :
                    below_500000.append(value)
                elif value > 500000 and value < 1000001:
                    below_1mil.append(value)
                elif value > 1000000 and value < 5000001:
                    below_10mil.append(value)
                else:
                    below_20mil.append(value)

            all_colors = [k for k, v in pltc.cnames.items()]

            view_score = [len(below_100000),len(below_500000),len(below_1mil),len(below_10mil),len(below_20mil)]
            view_label = ['x < 100001', '100000 < x < 500001', '500000 < x < 1000001', '1000000 < x < 5000001', 'x > 5000000']
            fracs = np.array(view_score)
            labels = view_label

            explode = ((fracs == max(fracs)).astype(int) / 20).tolist()

            for val in range(1):
                colors = sample(all_colors, len(fracs))
                plt.figure(figsize=(8, 8))
                plt.pie(fracs, autopct='%1.1f%%',
                        shadow=True, explode=explode, colors=colors)
                plt.title('View Amount Classification')
                plt.legend(labels, loc=(1.00, 0.7), shadow=True, title = 'View Value Range')
                plt.show()
        connection.commit()

    except pymysql.err.InternalError as e:
        print('{}'.format(e))

def view_predict():

    try:
        with connection.cursor() as cursor:


            sqlQuery_1 = "SELECT * FROM videos_week WHERE video_id = 'https://www.youtube.com/watch?v=j8z7UjET1Is' ;"

            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()


            week_1 = rows[0]['13_4_2020']
            week_2 = rows[0]['20_4_2020'] - rows[0]['13_4_2020']
            week_3 = rows[0]['27_4_2020'] - rows[0]['20_4_2020']
            week_4 = rows[0]['2_5_2020'] - rows[0]['27_4_2020']
            week_5 = rows[0]['9_5_2020'] - rows[0]['2_5_2020']
            week_6 = rows[0]['16_5_2020'] - rows[0]['9_5_2020']
            week_7 = rows[0]['24_5_2020'] - rows[0]['16_5_2020']
            week_8 = rows[0]['31_5_2020'] - rows[0]['24_5_2020']

            x = np.arange(7).reshape(-1, 1)
            y = [week_1, int(week_2), int(week_3), int(week_4), int(week_5),
                 int(week_6), int(week_7), int(week_8)]
            #print(x)
            print(y)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=0)

            simplelinearRegression = LinearRegression()
            simplelinearRegression.fit(x_train, y_train)

            fv = []
            for x in range (5):

                y_predict = simplelinearRegression.predict([[x+7]])
                fv.append(rows[0]['31_5_2020']+int(y_predict))

            x = ['7/6','14/6','21/6','28/6','5/7']
            future = fv
            print(future)

            plt.plot(x, future)
            plt.xlabel('Date')
            plt.ylabel('View Count')
            plt.title('Future Cumulative View Evolution')
            plt.show()



        connection.commit()




    except pymysql.err.InternalError as e:
        print('{}'.format(e))

def kgraph():
    try:
        with connection.cursor() as cursor:


            sqlQuery_1 = "SELECT * FROM videos_week;"

            cursor.execute(sqlQuery_1)

            rows = cursor.fetchall()

            for x in range (len(rows)):
                val_1 = rows[x]['13_4_2020'] - rows[x]['20_4_2020']
                val_2 = rows[x]['20_4_2020'] - rows[x]['27_4_2020']
                val_3 = rows[x]['2_5_2020'] - rows[x]['9_5_2020']
                val_4 = rows[x]['9_5_2020'] - rows[x]['16_5_2020']
                val_5 = rows[x]['16_5_2020'] - rows[x]['24_5_2020']
                val_6 = rows[x]['31_5_2020'] - rows[x]['7_6_2020']

                labels = ['20/4', '27/4', '9/5', '16/5', '24/5', '7/6']


                try:
                    val_1 = 1/val_1
                except:
                    val_1 = val_1

                try:
                    val_2 = 1/val_2
                except:
                    val_2 = val_2

                try:
                    val_3 = 1/val_3
                except:
                    val_3 = val_3

                try:
                    val_4 = 1/val_4
                except:
                    val_4 = val_4

                try:
                    val_5 = 1/val_5
                except:
                    val_5 = val_5

                try:
                    val_6 = 1/val_6
                except:
                    val_6 = val_6

                view = [val_1,val_2,val_3,val_4,val_5,val_6]


                plt.plot(labels, view)
                plt.xlabel('Date')
                plt.ylabel('View Count')
                plt.title('Future Cumulative View Evolution')

                plt.savefig('graphs\\fig_name'+str(x), bbox_inches='tight')


                plt.close()





    except pymysql.err.InternalError as e:
        print('{}'.format(e))

#language_category()
#view_evolution_category()
#famous_channel_category()

single_channel_progress()
#view_classifier()
#view_predict()
#kgraph()