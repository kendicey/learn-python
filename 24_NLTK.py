import nltk 
nltk.download('punkt')
nltk.download('stopwords')

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# separate words by a whitespace
print(word_tokenize(text))           

# separate string by sentence       
print(nltk.tokenize.sent_tokenize(text))

# stopwords are words in a stop list which are filtered out before or after processing of natural language data because they are insignificant
# 'a', 'is', 'are', 'the', 'of', 'and', 'it'
stopwords = stopwords.words('english')
new_text = []
for i in text.split():
    if i not in stopwords:
        new_text.append(i)

print(new_text)