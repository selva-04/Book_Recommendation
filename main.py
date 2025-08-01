'''
final rating  -  rating table
book pivot -rating matrix
boook names - book name
'''
import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Colloborative FIltering and KNN')
st.text(" ")
st.text(" ")
model = pickle.load(open('loaded_files/model.pkl','rb'))
book_names = pickle.load(open('loaded_files/book_name.pkl','rb'))
rating_matrix = pickle.load(open('loaded_files/rating_matrix.pkl','rb'))






def recommend_book(book_name):
    books_list = []
    book_id = np.where(rating_matrix.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(rating_matrix.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    
    
    for i in range(len(suggestion)):
            books = rating_matrix.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list      



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

st.text(" ")

if st.button('Show Recommendation'):
    recommended_books = recommend_book(selected_books)
    

    for i in range(1, 6):
        st.text(recommended_books[i])
