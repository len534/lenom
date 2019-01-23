#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd


def to_df(excel):
    df = pd.read_excel(excel,index_col=None,names =['No','date','start_time','end_time','type','podgr','lesson','stud_count','auditory','kurs','group','speciality','Prepod'])
    df = df.drop(columns=['No','podgr']) #удаляет колонки:№,номер подгр.,т.к. не несут информации.
    wrong = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'Дата']
    for item in wrong:
             df = df[df.date != item]
    return df

def get_lesson(lesson):
    keys = ['start_time','end_time','type','lesson','stud_count','auditory','kurs','group','speciality']
    lesson_dict = dict()
    for item in keys:
        lesson_dict[item] = lesson[1][item].values[0]
    return lesson_dict

def get_date(date_element):
    date_day = dict(date = date_element[0])
    lessons = list()
    for lesson in date_element[1].groupby(['start_time']):
        lessons.append(get_lesson(lesson))
    date_day['lessons'] = lessons
    return date_day

def get_professor(prof_element):
    professor = dict(professor_name = prof_element[0])
    dates = list()
    for date_element in prof_element[1].groupby(['date']):
        dates.append(get_date(date_element))
    professor['dates'] = dates
    return professor

def frame_to_dict(dataframe):
    data = []
    for prof_element in dataframe.groupby(['Prepod']):
        data.append(get_professor(prof_element))
        
    return data

def excel_to_json():
    path =os.getcwd()+'\\data\\'
    fpath = path+'test.xlsx'
    df = to_df(fpath)
    with open('data_from_excel.json', 'w', encoding='utf-8') as file:
        file.write(str(frame_to_dict(df)).replace('nan',"'nan'"))

def excel_to_json_str(fpath):
    df = to_df(fpath)
    return str(frame_to_dict(df)).replace('nan',"'nan'")
        
if __name__ == "__main__":
    excel_to_json()
