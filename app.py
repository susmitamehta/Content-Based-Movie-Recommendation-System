import streamlit as st
import pickle
import requests




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names  = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(recommended_movie_names[0])
        
    with col2:
        st.subheader(recommended_movie_names[1])
         

    with col3:
        st.subheader(recommended_movie_names[2])
  
    with col4:
        st.subheader(recommended_movie_names[3])
  
    with col5:
        st.subheader(recommended_movie_names[4])
      

