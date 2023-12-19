import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH')
USER_NAME = os.environ.get('USER_NAME')

df = pd.read_csv(DATA_PATH)

my_df = df.loc[df['User'] == USER_NAME]

print(my_df)