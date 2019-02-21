# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from stackapi import StackAPI
from datetime import datetime
import numpy as np

SITE = StackAPI('stackoverflow')

SITE.page_size = 100
SITE.max_pages = 100

'''
from stackapi import StackAPI
APP_KEY = '5RiBAhuShT6awgMXXZpIng(('
SITE = SEAPI.SEAPI('stackoverflow', key=APP_KEY, access_token=ACCESS_TOKEN)
flag = SITE.send_data('comments/123/flags/add', option_id=option_id)
'''

questions = SITE.fetch('questions', 
                       min=20, 
                       tagged='python', 
                       sort='votes',
                       fromdate = datetime(2015, 1, 1).isoformat(' '), 
                       todate = datetime(2017, 12, 31).isoformat(' '))
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
    
df = df.drop(['accepted_answer_id', 'closed_date', 'closed_reason',  
       'last_activity_date', 'last_edit_date', 'link', 'migrated_from', 
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


dfPython.loc[dfPython['IsAnswered'] != 'False']

#Encontramos los valores con False
not_answered = dfPython[dfPython['IsAnswered'].astype(str).str.contains('False')]
not_answered.head()

not_answered.iat[0,5]

pd.to_datetime(not_answered["CreationDate"], unit='ms')

min(not_answered["CreationDate"])

for i in range(len(not_answered["CreationDate"])):
    print(not_answered.iat[i, 0],
          
          
          datetime.fromtimestamp(not_answered.iat[i, 5]).strftime("%d %B, %Y %I:%M:%S"))


not_answered[not_answered["CreationDate"] == min(not_answered["CreationDate"])]


datetime.fromtimestamp(min(not_answered["CreationDate"])).strftime("%d %B, %Y %I:%M:%S")

datetime.fromtimestamp(min(not_answered["CreationDate"])).strftime("%d-%B-%Y")


dfPython["CreationDate"]


datetime.fromtimestamp(dfPython["CreationDate"]).strftime("%d-%B-%Y")

ts = list()
for i in range(len(dfPython["CreationDate"])):
    ts.append(datetime.fromtimestamp(dfPython.iat[i, 5]).strftime("%d-%B-%Y"))
    
dfPython['Fecha'] = ts


import matplotlib.pyplot as plt
import seaborn as sns

width=8 # inch
aspect=0.8 # height/width ratio
height = width*aspect
plt.figure(figsize=(width, height ))
plt.hist(dfPython['ViewCount'], color = 'blue', edgecolor = 'black', 
         bins = int(180/5))

# Add labels
plt.title('Histograma de visitas a las preguntas', size = 20)
plt.xlabel('Contador de vistas (ViewCount)', size = 16)
plt.ylabel('Número de preguntas', size = 16)

# seaborn histogram
sns.distplot(dfPython['ViewCount'], hist=True, kde=True, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})

plt.boxplot(dfPython['ViewCount'])

dfPython['ViewCount'].describe()


dfPython['IDQuestion'][10]
str(dfPython['IDQuestion'])

answers2 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = [str(dfPython['IDQuestion'][10])],
                       tagged='python', 
                       sort='votes')

answers = SITE.fetch('answers', 
                       min=20, 
                       tagged='python', 
                       fromdate = datetime(2015, 1, 1).isoformat(' '),                        
                       sort='votes')

answers2 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][0:10].tolist()
                       )


str(dfPython['IDQuestion'][0:10].tolist())

answers11 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][0:100].tolist()
                       )
answers12 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][101:200].tolist()
                       )
answers13 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][201:300].tolist()
                       )
answers13 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][201:300].tolist()
                       )



answers_0 = SITE.fetch('/questions/{ids}/answers', 
                       min=20, 
                       ids = dfPython['IDQuestion'][0:100].tolist()
                       )

qlist_0 = answers_0['items']
df_0 = pd.DataFrame(qlist_0)

for i in range(101, len(dfPython), 100):
    end = i+99
    answers_next = SITE.fetch('/questions/{ids}/answers', 
                              min=20, 
                              ids = dfPython['IDQuestion'][i:end].tolist()
                              )
    qlist_next = answers_next['items']
    df_next = pd.DataFrame(qlist_next)
    
    frames=[df_0, df_next]
    df_0 = pd.concat(frames)

df_0.head()

owner_0 = pd.DataFrame(df_0['owner'].values.tolist())
owner_0.head()

owner_0.columns.values

owner_0 = owner_0.drop(['accept_rate', 'link', 'profile_image', 'user_type'], axis=1)
owner_0.head()


df_0.columns.values

df_0 = df_0.drop(['community_owned_date', 'is_accepted', 
                  'last_activity_date', 'last_edit_date', 'owner'], axis=1)
df_0.head()


dfAnswers = pd.concat([df_0, owner_0], axis=1, join_axes=[df_0.index])
dfAnswers.head()

dfAnswers.columns.values

sequence_0 = {'answer_id': 'IDAnswer', 
              'creation_date': 'DateAnswer', 
              'question_id': 'question_id', 
              'score': 'ScoreAnswer',
              'display_name': 'DisplayName', 
              'reputation': 'ReputationIDUserAnswer', 
              'user_id': 'IDUserAnswer'}

dfAnswers = dfAnswers.rename(columns = sequence_0)
dfAnswers.head()

listIDQuestion = dfPython['IDQuestion'].tolist()

'''
row = (dfAnswers.loc[dfAnswers['question_id'] == listIDQuestion[10]])['ScoreAnswer'].idxmax()
row = (dfAnswers.loc[dfAnswers['question_id'] == listIDQuestion[0]])['ScoreAnswer'].idxmax()

resultado = pd.DataFrame()

frames=[resultado, result]

result = dfAnswers.loc[row]
result = result.reset_index()
resultado = result
resultado.reindex_axis

resultado = pd.concat(frames)

dfAnswers.iloc[row, :]

result = result.rename(columns=[0,1])

dfAnswers.loc[dfAnswers['question_id'] == listIDQuestion[10]].idxmax()
'''
listIDQuestion = dfPython['IDQuestion'].tolist()

foo = dfAnswers.loc[ (dfAnswers['question_id']==listIDQuestion[0])]
row = foo['ScoreAnswer'].idxmax()
row

foo = foo.reset_index()
foo = foo[foo['index'] == row]

resultado = foo

emptyAnswer = foo

emptyAnswer.ix[:,:] = None

for token in listIDQuestion:
    #print("Procesando el token:", token)
    foo = dfAnswers.loc[ (dfAnswers['question_id']==token)]
    #print(foo.head())
    
    if foo.empty:
        frames = [resultado, emptyAnswer]
        emptyAnswer['question_id'] = token
    else:
        row = foo['ScoreAnswer'].idxmax()
        #print("LA fila con el valor maximo es: ", row)
        foo = foo.reset_index()
        foo = foo[foo['index'] == row]
        frames = [resultado, foo]
    
    resultado = pd.concat(frames) 

# borramos primera fila
resultado = resultado.reset_index()
resultado = resultado.drop(resultado.index[[0]])

# borramos columnas
cols = [0, 1]
resultado.drop(resultado.columns[cols],axis=1,inplace=True)

# reasignamos indices
resultado = resultado.reset_index()
cols = [0]
resultado.drop(resultado.columns[cols],axis=1,inplace=True)

resultado.head()

