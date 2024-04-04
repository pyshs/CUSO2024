# to run it : streamlit run app.py

import streamlit as st

def filter_word_n(text, n):
    """
    Filtrer les mots de plus de n caractères
    """
    words = text.split()
    filtered_words = [word for word in words if len(word) > n]
    return filtered_words

st.title("Compteur de mots")
user_text = st.text_area("Entrez votre texte ici:")
n = st.slider("Sélectionnez le nombre minimal de caractères:", 1, 30, 1)
if st.button("Valider"):
    result = filter_word_n(user_text, n)
    st.write(f"Mots avec plus de {n} caractères:")
    st.write(result)