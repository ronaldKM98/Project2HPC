# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
#from tabulate import tabulate
import glob

fields = ['id', 'title', 'content']

stop_words = set(stopwords.words('english'))

quotation = [".", "?", "!", ",", ";", ":", "-", "_", "[", "]", "{", "}", "(", ")", "...", "\'", "\"", '“', '’', '”', "$", "%", "^", "&", "*", "-", "\\", "/", "@", "!", "—"]
for i in quotation: stop_words.add(i)

#Clean the content field
def clean_data(s):
    word_tokens = word_tokenize(s)
    filtered_str = []
    for word in word_tokens:
        word = word.lower()
        if word not in stop_words:
            filtered_str.append(word)
    
    return ' '.join(filtered_str)


# Read data from file                                                          
path = "/opt/datasets"
allFiles = glob.glob(path + "/*.csv")
i = 0
for fileName in allFiles:
    print(fileName)
    data_frame = pd.read_csv(fileName, skipinitialspace=True, usecols=fields)
    data_frame['content'].dropna(inplace=True)
    data_frame['content'] = data_frame['content'].apply(clean_data)
    i+=1
    data_frame.to_csv(str(i) + ".csv", sep='\t')
