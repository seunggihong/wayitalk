import pandas as pd
import re
from datetime import datetime
import os
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

def load_data(data_path, file_format='.txt'):
    file_list = os.listdir(data_path)
    file_name_list = [file for file in file_list if file.endswith(file_format)]
    data = {'datetime': [], 'time': [], 'user': [], 'message': []}

    for file_name in file_name_list:
        with open(data_path + file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines[1:]:
            match = re.match(r'(\d{4}\.\s\d{2}\.\s\d{2}\.\s\d{2}:\d{2}),\s(.+?)\s:\s(.+)', line)
            if match:
                date_time_str, speaker, content = match.groups()
                date_time = datetime.strptime(date_time_str, '%Y. %m. %d. %H:%M')
                data['datetime'].append(date_time.date())
                data['time'].append(date_time.time())
                data['user'].append(speaker)
                data['message'].append(content)

    return pd.DataFrame(data)

def slice_data(data_frame, user_name):
    data = {'data':[], 'target':[]}
    cnt = 0
    while True:
        if cnt == (len(data_frame) -1) :
            break
        user = data_frame['user'][cnt]
        message = ''
        for i in range(cnt, len(data_frame)-1):
            if user == data_frame['user'][i]:
                message += (data_frame['message'][i] + " ")
                cnt += 1
            else:
                break

        if user == user_name:
            data['target'].append(message)
        else :
            data['data'].append(message)
    
    return pd.DataFrame(data)


def tokenizer_to_pad(data_frame, max_len=20) :
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data_frame)
    encoded = tokenizer.texts_to_sequences(data_frame)
    seq = sequence.pad_sequences(encoded, maxlen=max_len)
    return seq