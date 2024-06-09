Text Classification Demo
Introduction
This repository contains a Streamlit app that demonstrates text classification using a pre-trained Naive Bayes classifier with TF-IDF vectorization.

Setup
Clone the Repository: Clone this repository to your local machine.

Install Dependencies: Make sure you have the necessary dependencies installed. You can install them using the following command:

Sao chép mã
pip install -r requirements.txt
Run the App: Run the Streamlit app using the following command:

arduino
Sao chép mã
streamlit run text_classification.py
Usage
Text Input: Enter the text you want to classify into the provided text area.

Classification: Click the "Classify" button to classify the input text.

Result: The predicted label for the input text will be displayed below the input area.

File Description
text_classification.py: This Python script contains the code for the Streamlit app.
text_preprocessing.py: This Python script contains functions for preprocessing text data.
tfidf_vect.pkl: This pickle file contains the TF-IDF vectorizer trained on the dataset.
nb_tfidf_model.pkl: This pickle file contains the pre-trained Naive Bayes classifier.
Notes
Make sure to replace the file paths in the code with the appropriate paths to the pickle files on your system.
Acknowledgments
The code for this project is inspired by various tutorials and examples available online. Special thanks to the authors of those resources for sharing their knowledge and code.

License
This project is licensed under the MIT License - see the LICENSE file for details.
