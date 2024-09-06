import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

with open("miracle_in_the_andes.txt", 'r', encoding="utf-8") as file:
    book = file.read()

# Count How many chapters are there using regex

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern,book)

# Counting the occurrence of each word

pattern1 = re.compile("[a-zA-Z]+")
findings1 = re.findall(pattern1,book)

d= {}

for word in findings1:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value,key) for (key,value) in d.items()]
sorted(d_list,reverse=True)

# print(d_list)

# extract all non english words

english_words = stopwords.words("english")
filtered_words = []
for word in english_words:
    filtered_words.append(word)
print(filtered_words)



# List of each paragraph

pattern2 = re.compile("Chapter [0-9]+")
chapters = re.split(pattern2,book)

neg = []
pos = []
chapter_number = []
analyzer = SentimentIntensityAnalyzer()
for i,chapter in enumerate(chapters) :
    score = analyzer.polarity_scores(chapter)
    chapter_number.append(i+1)
    print(score)
    neg.append(score['neg'])
    pos.append(score['pos'])


print(chapter_number)

# plot negative and positive data of each paragraph

st.title("Positivity")
pos_figure = px.line(x=chapter_number,y=pos,labels={"x":"chapter","y":"positivity"})
st.plotly_chart(pos_figure)

st.title("Negativity")
neg_figure = px.line(x=chapter_number,y=neg,labels={"x":"chapter","y":"negativity"})
st.plotly_chart(neg_figure)






