from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import praw
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia= SIA()
results = []
df = pd.read_csv(r'C:\Users\AK\Documents\GitHub\redditAnalysis')
for line in df:
    pol_score=sia.polarity_scores(line)
    pol_score['comment']=line
    results.append(pol_score)
pprint(results[:3], width=100)