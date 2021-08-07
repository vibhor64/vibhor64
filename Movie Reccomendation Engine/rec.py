import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)
movie_titles = pd.read_csv("Movie_Id_Titles")
df = pd.merge(df,movie_titles,on='item_id')

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
moviemat = df.pivot_table(index='user_id',columns='title',values='rating')

def query(movie): 
    user_ratings = moviemat[f'{movie}']
    similar = moviemat.corrwith(user_ratings)
    corr_q = pd.DataFrame(similar,columns=['Correlation'])
    corr_q.dropna(inplace=True)
    corr_q = corr_q.join(ratings['num of ratings'])
    corr_q[corr_q['num of ratings']>100].sort_values('Correlation',ascending=False).head()

a = input("What movie? ")
query(a)