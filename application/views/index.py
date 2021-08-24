from django.views import View
from django.shortcuts import render
from bs4 import BeautifulSoup
from ..models import User
import requests
import pandas as pd
import re

class IndexView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        keyword = user.key1
        if(user.key2 != None):
            keyword += " " + user.key2
        if(user.key3 != None):
            keyword += " " + user.key3
        if(user.key4 != None):
            keyword += " " + user.key4
        if(user.key5 != None):
            keyword += " " + user.key5
        print(keyword)
        
        number = 10
        search_results_df = get_search_results_df(keyword,number)
        
        context = {
            'search_results' : search_results_df.to_html(),
        }
        
        return render(request, 'registration/index.html', context)


def get_search_results_df(keyword,number):
    columns = ["rank", "title", "writer", "year", "citations", "url"]
    df = pd.DataFrame(columns=columns) #表の作成
    html_doc = requests.get("https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num=" + str(number) + "&q=" + keyword).text
    soup = BeautifulSoup(html_doc, "html.parser") # BeautifulSoupの初期化
    tags1 = soup.find_all("h3", {"class": "gs_rt"})  # title&url
    tags2 = soup.find_all("div", {"class": "gs_a"})  # writer&year
    tags3 = soup.find_all(text=re.compile("引用元"))  # citation

    rank = 1
    for tag1, tag2, tag3 in zip(tags1, tags2, tags3):
        title = tag1.text.replace("[HTML]","")
        url = tag1.select("a")[0].get("href")
        writer = tag2.text
        writer = re.sub(r'\d', '', writer)
        year = tag2.text
        year = re.sub(r'\D', '', year)
        citations = tag3.replace("引用元","")
        se = pd.Series([rank, title, writer, year, citations, url], columns)
        df = df.append(se, columns)
        rank += 1
    return df