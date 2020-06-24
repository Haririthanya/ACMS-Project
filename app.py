from flask import Flask, render_template,request
import os
import random
from pathlib import Path
import pandas as pd
import numpy as np 
import math
import sys
from queue import PriorityQueue 



app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
links = ["/newspaper","/book","/magazine"]
userid = ''
df = pd.read_csv('users.csv')

def getUserPreference(userid):
    userlist = df[df['userid']==userid].to_dict('records')[0]
    userlist.pop('userid')
    keymaxval = max(userlist,key=userlist.get)
    userpreference = {keymaxval:userlist[keymaxval]}
    return userpreference

def closestValue(arr,product,image_links,value,submag):
    pq = PriorityQueue()
    for j in range(1):
        pq.put((-abs(arr[j]-value),j))
    for j in range(1,len(arr)):
        diff = abs(arr[j]-value) 
        p,pi = pq.get() 
        curr = -p 
        if diff>curr: 
            pq.put((-curr,pi)) 
            continue
        else: 
            pq.put((-diff,j)) 
    while(not pq.empty()):        
        p,q = pq.get()
    closestValue = arr[q]
    if product=='Magazine':
        image_links.append(submag.iloc[q]['Url'])
    elif product=='Book':   
        dict1 = {'url':'','author':'','book':''}
        dict1['url'] = submag.iloc[q]['url']
        dict1['author'] = submag.iloc[q]['bookauthor']
        dict1['book'] = submag.iloc[q]['bookname']
        image_links.append(dict1)


@app.route("/",methods=['GET','POST'])
def index():
    target = os.path.join(APP_ROOT, 'images/')
    path = 'static/images'
    files=os.listdir(path)
    print("path:",files)
    for f in files:
        if f=='Photography':
            path = path+'/Photography'
    pictures = os.listdir(path)
    if '.DS_Store' in pictures:
        pictures.remove('.DS_Store')
    image_sources = []        
    for p in pictures:
        image_sources.append(path+'/'+p)
    print(image_sources)
    d=random.choice(pictures) 
    while d == '.DS_Store':
        d=random.choice(pictures)
    path = path +'/'+d
    print(path)
    print(d)
    links = ['Books','Newspaper','Magazine']
    return render_template('in.html',imgsrc = image_sources,link=links,len=len(image_sources),links=links)


@app.route("/newspaper",methods=['GET','POST'])
def newspaper():
    userid = request.args.get('name')
    userpreference = getUserPreference(userid)
    keymaxval = list(userpreference.keys())[0]
    value = userpreference[keymaxval]
    df = pd.read_csv('magazine.csv')
    image_links = []
    arr = list(df[keymaxval])
    closestValue(arr,'Magazine',image_links,value,df)
    print(image_links)
    return render_template('newspaper.html',imgsrc=image_links)

@app.route("/ebook",methods=['GET','POST'])
def ebook():
    userid = request.args.get('name')
    userpreference = getUserPreference(userid)
    keymaxval = list(userpreference.keys())[0]
    value = userpreference[keymaxval]
    df = pd.read_csv('book.csv')
    noofmag = df['bookid'].unique()
    image_links = []
    for i in noofmag:
        submag = df[df['bookid']==i]
        print(submag)
        arr = list(submag[keymaxval])
        print(arr,"arr")
        closestValue(arr,'Book',image_links,value,submag)
    randomlist = []
    for i in range(0,len(noofmag)):
        n = random.randint(100,1000)
        randomlist.append(n)
    print(image_links)
    return render_template('ebook.html',imgsrc = image_links,amount = randomlist)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8001,debug=True)