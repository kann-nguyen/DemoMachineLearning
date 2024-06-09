import os
import streamlit as st
import numpy as np
import pickle
import tensorflow as tf
from text_preprocessing import perform_preprocessing

# Disable oneDNN custom operations warning if desired
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load the TF-IDF vectorizer
with open(r'C:\Users\admin\Downloads\tfidf_vect.pkl', 'rb') as f:
    tfidf_vect = pickle.load(f)

with open(r'C:\Users\admin\Downloads\nb_tfidf_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Class dictionary
class_dict = {'0': 'World', '1': 'Sports', '2': 'Business', '3': 'Sci/Tech'}

def convert_to_string_or_list(input_text):
    if isinstance(input_text, str):
        return [input_text]
    elif isinstance(input_text, list):
        return input_text
    else:
        return [str(input_text)]


# Streamlit app
st.title('Text Classification Demo')

# Text input
user_input = st.text_area("Enter text for classification:", "")

if st.button('Classify'):
    if user_input:
        user_input_processed = convert_to_string_or_list(user_input)
        preprocessed_input = [perform_preprocessing(text) for text in user_input_processed]
        
        # Transform the preprocessed input using the TF-IDF vectorizer
        input_tfidf = tfidf_vect.transform(preprocessed_input)
        
        # Predict
        predicted_label = loaded_model.predict(input_tfidf)
        
        # Display the result
        st.write("Predicted label:", class_dict.get(str(predicted_label[0]), "Unknown"))
    else:
        st.write("Please enter some text for classification.")
