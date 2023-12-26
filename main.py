from konlpy.tag import Okt
from utils.LoadData import slice_data, load_data
from dotenv import load_dotenv
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH')
USER_NAME = os.environ.get('USER_NAME')

df = load_data(DATA_PATH)
df = slice_data(df, USER_NAME)

okt = Okt()
df['data'] = df['data'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', "", x))
df['target'] = df['target'].apply(lambda x : re.sub(r'[^ ㄱ-ㅣ가-힣]+', "", x))

df['data'] = df['data'].apply(lambda x : okt.se(x))
df['target'] = df['target'].apply(lambda x : okt.morphs(x))