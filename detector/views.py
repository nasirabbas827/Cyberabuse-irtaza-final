from django.shortcuts import render
import pandas as pd
import re
import joblib
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')

tfidf = joblib.load(os.path.join(MODELS_DIR, 'tfidf_vectorizer.pkl'))
nb_model = joblib.load(os.path.join(MODELS_DIR, 'nb_model.pkl'))
svm_model = joblib.load(os.path.join(MODELS_DIR, 'svm_model.pkl'))
rf_model = joblib.load(os.path.join(MODELS_DIR, 'rf_model.pkl'))

roman_urdu_stopwords = [
    'hai', 'aur', 'ke', 'ka', 'ki', 'ko', 'mein', 'se', 'par', 'bhi',
    'ye', 'wo', 'ek', 'nahi', 'to', 'hi', 'tak', 'kar', 'raha', 'tha',
    'hain', 'ho', 'ne', 'ba', 'si', 'ji', 'han', 'kya', 'ab', 'lekin'
]

positive_keywords = [
    'acha', 'behtareen', 'mehnati', 'intelligent', 'pyara',
    'sharif', 'student', 'pasand', 'honest', 'best', 'sincere'
]

def preprocess_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join(word for word in text.split() if word not in roman_urdu_stopwords)
    return text

def predict(request):
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        if comment:
            cleaned = preprocess_text(comment)
            features = tfidf.transform([cleaned]).toarray()

            nb_prediction = nb_model.predict(features)[0]
            svm_prediction = svm_model.predict(features)[0]
            rf_prediction = rf_model.predict(features)[0]

            if any(word in cleaned for word in positive_keywords):
                final_prediction = 'non-abusive'
                nb_prediction = svm_prediction = rf_prediction = 'non-abusive'
            else:
                if svm_prediction == rf_prediction and nb_prediction != svm_prediction:
                    nb_prediction = svm_prediction

                all_preds = [nb_prediction, svm_prediction, rf_prediction]
                final_prediction = Counter(all_preds).most_common(1)[0][0]

            return render(request, 'index.html', {
                'cleaned_comment': cleaned,
                'nb_prediction': nb_prediction,
                'svm_prediction': svm_prediction,
                'rf_prediction': rf_prediction,
                'final_prediction': final_prediction
            })

    return render(request, 'index.html')
