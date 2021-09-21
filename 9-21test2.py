from wordcloud import WordCloud
txt = 'oh fuck shit bro'
wd = WordCloud().generate(txt)
wd.to_file('test2.jpg')



