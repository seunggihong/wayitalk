import pandas as pd
from dotenv import load_dotenv
import re
from datetime import datetime
import os

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH')
USER_NAME = os.environ.get('USER_NAME')

path = DATA_PATH
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.txt')]

data = {'날짜': [], '시간': [], '발언자': [], '내용': []}

for file_name in file_list_py:
    with open(path + file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines[1:]:
        match = re.match(r'(\d{4}\.\s\d{2}\.\s\d{2}\.\s\d{2}:\d{2}),\s(.+?)\s:\s(.+)', line)
        if match:
            date_time_str, speaker, content = match.groups()
            date_time = datetime.strptime(date_time_str, '%Y. %m. %d. %H:%M')
            data['날짜'].append(date_time.date())
            data['시간'].append(date_time.time())
            data['발언자'].append(speaker)
            data['내용'].append(content)

df = pd.DataFrame(data)

df.to_csv(DATA_PATH + 'talk.csv')
