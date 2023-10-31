import streamlit as st

import pickle

import numpy as np

book_pivot = pickle.load(open("book_pivot.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))


def recommed_books(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors = 6)
    suggestions_list = []
    for index in suggestions:
        suggestions_list.append(book_pivot.index[index])
    return suggestions_list

book_title = book_pivot.index.values

st.title("Book Recommender System")

selected_movie_name = st.selectbox("Select Movie" ,book_title)

if st.button("Recommend"):
    recommended_movies = recommed_books(selected_movie_name)
    for i in recommended_movies[0][1:]:
        st.write(i)
