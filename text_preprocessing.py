import re
import string
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Needed only once
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

def remove_html_tags(text): #Loại bỏ các thẻ HTML khỏi văn bản đầu vào.
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text
def remove_numbers(text): #Loại bỏ tất cả các chữ số khỏi văn bản đầu vào.
    result = re.sub(r'\d+', '', text)
    return result
def remove_slash_with_space(text): #Thay thế các dấu gạch chéo ngược ('\') bằng dấu cách trong văn bản đầu vào.
    return text.replace('\\', " ")
def remove_punctuation(text): #Loại bỏ tất cả dấu câu khỏi văn bản đầu vào.
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)
def text_lowercase(text): #Chuyển tất cả các ký tự trong văn bản đầu vào thành chữ thường.
    return text.lower()
def remove_whitespace(text): #Loại bỏ khoảng trắng thừa trong văn bản đầu vào.
    return  " ".join(text.split())
def remove_stopwords(text): #Loại bỏ các từ dừng (stopwords) khỏi văn bản đầu vào.
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)
def stem_words(text): #Stemming các từ trong văn bản đầu vào (tức là chuyển các từ về gốc của chúng).
    stemmer = PorterStemmer()
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return ' '.join(stems)
def lemmatize_words(text): #Lemmatizing các từ trong văn bản đầu vào (tức là chuyển các từ về dạng cơ bản của chúng dựa trên ngữ cảnh).
    lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(text)
    # provide context i.e. part-of-speech
    lemmas = [lemmatizer.lemmatize(word, pos ='v') for word in word_tokens]
    return ' '.join(lemmas)

# Perform preprocessing
def perform_preprocessing(text):
    text = remove_html_tags(text)
    text = remove_numbers(text)
    text = text_lowercase(text)
    text = remove_slash_with_space(text)
    text = remove_punctuation(text)
    # text = stem_words(text)
    text = remove_whitespace(text)
    return text