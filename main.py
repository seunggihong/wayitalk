import konlpy
from utils.LoadData import slice_data, load_data
from dotenv import load_dotenv
import os

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH')
USER_NAME = os.environ.get('USER_NAME')

df = load_data(DATA_PATH)
df = slice_data(df, USER_NAME)

print(df.head())