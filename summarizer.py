import openai
import json
import pandas as pd


#with open('config.json') as config_file:
#    data = json.load(config_file)

#key = data['openai_key']

#openai.api_key = key


from collections import Counter
import csv  


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('comments.csv')

# Select the second column and convert it to a text Series
text_series = df.iloc[:, 1].astype(str)

# Join the text Series into a single string
text_string = ' '.join(text_series)

# split() returns list of all the words in the string
split_it = text_string.split()
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(100)
  
print(most_occur)