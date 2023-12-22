import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH')
USER_NAME = os.environ.get('USER_NAME')

df = pd.read_csv(DATA_PATH)

count = 0
messages = []
target = []

while True:
    print(count)
    if count == len(df):
        break
    else:
        user = df['User'][count]
        mss = ''
        for i in range(count, len(df)):
            if user == df['User'][i]:
                mss += (df['Message'][i] + "\n")
                count += 1
            else:
                messages.append(mss)
                target.append(user)
                break

print(target)