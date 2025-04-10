'''
final rating  -  rating table
book pivot -rating matrix
boook names - book name
'''
import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Machine Learning')
model = pickle.load(open('loaded_files/model.pkl','rb'))
book_names = pickle.load(open('loaded_files/book_name.pkl','rb'))
#rating_table = pickle.load(open('loaded_files/rating_table.pkl','rb'))
rating_matrix = pickle.load(open('loaded_files/rating_matrix.pkl','rb'))


# def fetch_poster(suggestion):
#     book_name = []
#     ids_index = []

#     for book_id in suggestion:
#         book_name.append(rating_matrix.index[book_id])

#     for name in book_name[0]: 
#         ids = np.where(rating_table['title'] == name)[0][0]
#         ids_index.append(ids)

#     for idx in ids_index:
#         url = rating_table.iloc[idx]['image_url']

#     return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(rating_matrix.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(rating_matrix.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    # poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = rating_matrix.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list      



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books = recommend_book(selected_books)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(recommended_books[1])
    #     # st.image(poster_url[1])
    # with col2:
    #     st.text(recommended_books[2])
    #     # st.image(poster_url[2])

    # with col3:
    #     st.text(recommended_books[3])
    #     # st.image(poster_url[3])
    # with col4:
    #     st.text(recommended_books[4])
    #     # st.image(poster_url[4])
    # with col5:
    #     st.text(recommended_books[5])
    #     # st.image(poster_url[5])


    for i in range(1, 6):
        st.text(recommended_books[i])
    # st.image(poster_url[i])
