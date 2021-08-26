from django.views import View
from django.shortcuts import render
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from ..models import User, Room
import requests
import pandas as pd
import re
import time
import json


class IndexView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        
        # ランキング用
        ranking = User.objects.order_by('score').reverse().all()
        
        # ブックマーク表示用
        bookmark = user.book.all()
        
        context = {
            'ranking' : ranking,
            'bookmark' : bookmark,
        }
        
        if (user.paper_set.all().count() == 0):  # 参加した輪講が0の場合、キーワードでレコメンド
            keyword = []
            keyword.append(user.keyword1)
            if(user.keyword2 != None):
                keyword.append(user.keyword2)
            else:
                keyword.append("")
            if(user.keyword3 != None):
                keyword.append(user.keyword3)
            else:
                keyword.append("")
            if(user.keyword4 != None):
                keyword.append(user.keyword4)
            else:
                keyword.append("")
            if(user.keyword5 != None):
                keyword.append(user.keyword5)
            else:
                keyword.append("")
            
            # keyword = user.keyword1
            # if(user.keyword2 != None):
            #     keyword += "%20" + user.keyword2
            # if(user.keyword3 != None):
            #     keyword += "%20" + user.keyword3
            # if(user.keyword4 != None):
            #     keyword += "%20" + user.keyword4
            # if(user.keyword5 != None):
            #     keyword += "%20" + user.keyword5
            print(keyword)
            
            number = 10
            search_results_df = get_search_results_df(keyword,number)
            
            json_records = search_results_df.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
            
            context |= {'search_results' : data}
        
        else:  # 過去に輪講に参加したことがある場合
            my_papers = user.paper_set.all()
            recommend_papers_names = []
            
            for my_paper in my_papers:
                part_users = my_paper.user.all()
                
                for part_user in part_users:
                    recommend_papers = part_user.paper_set.all()
                    
                    for recommend_paper in recommend_papers:
                        recommend_papers_names.append(recommend_paper.name)
                    
            df = pd.read_csv('./paper.csv')
            search_results_df = df[df['title'].str.contains("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")]
            
            for recommend_papers_name in recommend_papers_names:
                search_result = df[df['title'].str.contains(recommend_papers_name)]
                if(len(search_result) == 0):
                    continue
                else:
                    search_results_df = pd.concat([search_results_df, search_result])
                    
            json_records = search_results_df.reset_index().to_json(orient ='records')
            data = []
            data = json.loads(json_records)
                
            context |= {'search_results' : data}
                    
        
        # 輪講希望を出している部屋に輪講希望者が2人以上いれば、通知を表示
        jourclub_rooms = user.jourclub.all()
        for jourclub_room in jourclub_rooms:
            if(jourclub_room.jourclub.count() >= 2):
                context |= {'chance_flag': True }
                break
                
        return render(request, 'registration/index.html', context)
    
    def post(self, request, *args, **kwargs):
        room_list = Room.objects.filter(name__icontains=request.POST['keyword'])
        
        context = {
            'room_list' : room_list,
        }
        return render(request, 'chat/room_list.html', context)


def get_search_results_df(keyword,number):
    # ua = UserAgent()
    # user_agent = ua.random
    # header = {"User-Agent":user_agent}
    #time.sleep(5)
    df = pd.read_csv('./paper.csv')
    searched_df = df[df['title'].str.contains(keyword[0]) & df['title'].str.contains(keyword[1]) & df['title'].str.contains(keyword[2]) & df['title'].str.contains(keyword[3]) & df['title'].str.contains(keyword[4])]
    
    return searched_df[:number]
    
    # columns = ["rank", "title", "writer", "year", "citations", "url"]
    # df = pd.DataFrame(columns=columns) #表の作成
    # html_doc = requests.get("https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num=" + str(number) + "&q=" + keyword, headers=header).text
    # soup = BeautifulSoup(html_doc, "html.parser") # BeautifulSoupの初期化
    # tags1 = soup.find_all("h3", {"class": "gs_rt"})  # title&url
    # tags2 = soup.find_all("div", {"class": "gs_a"})  # writer&year
    # tags3 = soup.find_all(text=re.compile("引用元"))  # citation

    # rank = 1
    # for tag1, tag2, tag3 in zip(tags1, tags2, tags3):
    #     title = tag1.text.replace("[HTML]","")
    #     url = tag1.select("a")[0].get("href")
    #     writer = tag2.text
    #     writer = re.sub(r'\d', '', writer)
    #     year = tag2.text
    #     year = re.sub(r'\D', '', year)
    #     citations = tag3.replace("引用元","")
    #     se = pd.Series([rank, title, writer, year, citations, url], columns)
    #     df = df.append(se, columns)
    #     rank += 1
    # return df