from builtins import Exception

from django.shortcuts import render

from user.forms import *
from user.models import *
from manager.models import *
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
import pandas as pd
# from information.models import wgt
import inflect
import re
import spacy
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize

import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from gensim import corpora, models


def index(request):
    return render(request,'index.html')

def logout(request):
    return render(request, "index.html")

def userlogin(request):
    return render(request,'user/userlogin.html')


def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})


def userlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        print(sname)
        spasswd = request.POST.get('upasswd')
        print(spasswd)
        try:
            check = userModel.objects.get(email=sname,passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'user/userpage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'user/userlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'user/userlogin.html')

def search(request):
    return render(request,'user/search.html')

def usersearchresult(request):
    filename = request.GET.get('filename')
    print("document type:",filename)
    check = uploadmodel.objects.filter(filename=filename)
    print(check)
    """for x in check:
        print(x.filename)
        print(x.filetype)
        print(x.id)"""
    object = check.filter(filename=filename)
    print("object:",object)
    return render(request, 'user/usersearchresult.html',{"object":object})

def weight(request):
    if request.method == "GET":
        file = request.GET.get('file')
        print("file:",file)
        filename1 = request.GET.get('filetype')
        print("file-name:",filename1)
        # print("file", file)
        head, fileName = os.path.split(file)
        # print(type(fileName))

        fPath = settings.MEDIA_ROOT + '\\' + 'files\pdfs' + '\\' + fileName
        print("hello:",fPath)
        texts =open(fPath).read()
        print("reading started")

        # Convert each article to all lower case
        lower_text = texts.lower()

        # replace secial characters with " "
        rem_spe = re.sub(r'[^\w\s]', '', lower_text)

        # replacing numbers with text
        p = inflect.engine()
        num_text = re.sub(r'\d+', lambda m: p.number_to_words(m.group()), rem_spe)

        num_text_processed = re.sub(r'[_,\-]', '', num_text)

        # change any whitespaces to one space
        processed = re.sub(r'[ ]+', ' ', num_text_processed)
        processed = re.sub(r'\n[\n]+', '\n', num_text_processed)

        # Remove start and end white spaces
        stripped = processed.strip()

        # Create stopwords list, convert to a set for speed
        # lemmatization of words which are not stopwords
        stopwords = set(nltk.corpus.stopwords.words('english'))
        # print("stop-wrds:",stopwords)
        lemmatizer = WordNetLemmatizer()

        articles = [
            " ".join([
                lemmatizer.lemmatize(word)
                for word in word_tokenize(s)
                if word not in stopwords
            ]) for s in stripped.split('\n')
        ]
        print(articles[:9])
        # Generate bag of words object with maximum vocab size of 1000
        counter = CountVectorizer(max_features=1000)
        # Get bag of words model as sparse matrix
        bag_of_words = counter.fit_transform(articles)

        count_matrix = pd.DataFrame(bag_of_words.todense(), columns=counter.get_feature_names())
        # print(count_matrix.head())

        # again starts code
        # Generate tf-idf object with maximum vocab size of 1000
        tf_counter = TfidfVectorizer(max_features=1000, min_df=2, max_df=1.0)
        # Get tf-idf matrix as sparse matrix
        tfidf = tf_counter.fit_transform(articles)

        # Get the words corresponding to the vocab index
        # tf_counter.get_feature_names()
        dataset = pd.DataFrame(tfidf.toarray(), columns=tf_counter.get_feature_names())
        # print(dataset.head(50))

        print(dataset.astype(bool).sum(axis=0).sort_values(ascending=False))

        # keep only the features from tfidf in articles
        processed_articles = [
            [
                x
                for x in a.split()
                if x in tf_counter.get_feature_names()
            ] for a in articles
        ]
        # print("final data:", processed_articles)
        dictionary = corpora.Dictionary(processed_articles)
        corpus = [dictionary.doc2bow(text) for text in processed_articles]
        # print(corpus)
        # passing all but one to model
        ldamodel = models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=20)
        ldamodel.get_topics()
        ldamodel.print_topics(
            # num_topics=2,
            # num_words=5
        )
        # doc to topic
        print("hello im final data")
        a = list(ldamodel.get_document_topics(corpus))
        a1 = []
        a2 = []
        for x in a:
            for y in x:
                a1.append(y)
        for i in a1:
            a2.append(i[1])

        print(sum(a2))
        s = sum(a2)
        print("sum:",s)
        if s>1000:
            rank='1'
        elif s>=200 and s<=1000:
            rank='2'
        elif s>=100 and s<200:
            rank='3'
        elif s>=50 and s<100:
            rank='4'
        else:
            rank='5'
        print("now it's about label-finding")
        if s>100:
            label=1
        else:
            label=0

        check=weightmodel(file=file,filename=filename1,weight=s,rank=rank,label=label).save()
        return render(request, "user/weight.html",{"dict":s})


def pagerank(request):
    return render(request, 'user/search.html')

def search1(request):
    return render(request,'user/search1.html')

def usersearchresult1(request):
    if request.method == 'GET':
        name=request.GET.get('filename')
        print('name:',name)
        chk=weightmodel.objects.filter(filename=name)
        print("chk:",chk)
        return render(request,'user/userdisplay.html',{"qs":chk})


