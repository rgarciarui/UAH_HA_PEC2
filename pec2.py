# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from stackapi import StackAPI

SITE = StackAPI('stackoverflow')

SITE.page_size = 100
SITE.max_pages = 100

questions = SITE.fetch('questions', min=20, tagged='python', sort='votes')
questions

'''
for key in questions:
  print( key, ":", questions[key])
'''
qlist = questions['items']  

'''
qlist[0]


qlist[0]['owner']['user_id']
qlist[0]['question_id']
qlist[0]['title']
qlist[0]['is_answered']
qlist[0]['view_count']
qlist[0]['creation_date']
qlist[0]['owner']['reputation']
qlist[0]['owner']['user_type']
qlist[0]['answer_count']

for i in range(len(qlist)):
    print(qlist[i]['owner'].get('user_id'))
    #print(qlist[i]['owner']['user_id'])

questions.keys()

type(questions['items'])
'''

import pandas as pd
df = pd.DataFrame(qlist)
'''
for i in range(len(qlist)):
    
    qlist[0]['question_id']
    qlist[0]['title']
    qlist[0]['is_answered']
    qlist[0]['view_count']
    qlist[0]['creation_date']
    qlist[0]['owner'].get('reputation')
    qlist[0]['owner'].get('user_type')
    qlist[0]['answer_count']
    
'''    
df.columns.values

'''qlist2 = df['owner'].values.tolist()'''

owner = pd.DataFrame(df['owner'].values.tolist())
    
owner = owner.drop(['accept_rate', 'display_name', 'link', 'profile_image'], axis=1)
owner.head()
    
df = df.drop(['accepted_answer_id', 'closed_date', 'closed_reason', 'community_owned_date', 
       'last_activity_date', 'last_edit_date', 'link', 'locked_date', 'migrated_from', 
         'owner', 'protected_date', 'score', 'tags'], axis=1)
    
dfPython = pd.concat([df, owner], axis=1, join_axes=[df.index])

dfPython.columns.values

sequence = ['user_id', 'question_id', 'title', 'is_answered',
            'view_count', 'creation_date', 'reputation',
            'user_type', 'answer_count']

dfPython = dfPython.reindex(columns=sequence)

sequence = {'user_id': 'IDUser', 
            'question_id': 'IDQuestion', 
            'title': 'Title', 
            'is_answered': 'IsAnswered',
            'view_count': 'ViewCount', 
            'creation_date': 'CreationDate', 
            'reputation': 'Reputation',
            'user_type': 'UserType', 
            'answer_count': 'AnswerCount'}

dfPython = dfPython.rename(columns = sequence) 


dfPython.loc[dfPython['IsAnswered'] == 'True']









