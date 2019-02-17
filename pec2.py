# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from stackapi import StackAPI

SITE = StackAPI('stackoverflow')

SITE.page_size = 100
SITE.max_pages = 20

questions = SITE.fetch('questions', min=20, tagged='python', sort='votes')
questions


for key in questions:
  print( key, ":", questions[key])
  
qlist = questions['items']  
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


import pandas as pd
df = pd.DataFrame(qlist)

for i in range(len(qlist)):
    
    qlist[0]['question_id']
    qlist[0]['title']
    qlist[0]['is_answered']
    qlist[0]['view_count']
    qlist[0]['creation_date']
    qlist[0]['owner'].get('reputation')
    qlist[0]['owner'].get('user_type')
    qlist[0]['answer_count']