import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string

spam_df = pd.read_csv('spam.csv', encoding="ISO-8859-1")

# subset
spam_df = spam_df[['v1', 'v2']]
spam_df.rename(columns={'v1': 'spam', 'v2': 'text'}, inplace=True)

# convert spam col to binary
spam_df.spam = spam_df.spam.apply(lambda s: True if s=='spam' else False)

# lowercase string and remove punctuation
spam_df.text = spam_df.text.apply(lambda t: t.lower().translate(str.maketrans('', '', string.punctuation)))

# shuffle
spam_df = spam_df.sample(frac=1)

# print(spam_df)

for t in spam_df[spam_df.spam == True].iloc[:5].text:
    print(t)
    print('---------')

for t in spam_df[spam_df.spam == False].iloc[:5].text:
    print(t)
    print('---------')