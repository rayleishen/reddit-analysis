from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')


nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA


import csv

#can be changed by user
top_comments=99


sia=SIA()
results = []
comments = []
with open('test.csv', errors="ignore") as file_obj:
    reader_obj = csv.reader(file_obj)
    for line in reader_obj:
        #a=sia.polarity_scores(str(line))
        #print(a)
        pol_score=sia.polarity_scores(str(line))
        pol_score['comment']=line
        results.append(pol_score)
        
        
        
#for line in comments:        
 #   pol_score=sia.polarity_scores(line)
  #  pol_score['comment']=line
   # results.append(pol_score)
        
        
pprint(results[:top_comments], width=100)

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()

df2 = df[['comment', 'label']]
df2.to_csv('reddit_comments_labels.csv', mode='a', encoding='utf-8', index=False)


print("Positive comments:\n")
pprint(list(df[df['label'] == 1].comment)[:5], width=200)

print("\nNegative comments:\n")
pprint(list(df[df['label'] == -1].comment)[:5], width=200)

print(df.label.value_counts())

print(df.label.value_counts(normalize=True) * 100)


#BAR GRAPH

fig, ax = plt.subplots(figsize=(8, 8))

data = df.label.value_counts(normalize=True) * 100

sns.barplot(x=data.index, y=data, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()


#PIE CHART

data = df.label.value_counts(normalize=True) * 100
labels = ['Negative', 'Neutral', 'Positive']

colors = sns.color_palette('pastel')[0:5]

#create pie chart
plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.show()