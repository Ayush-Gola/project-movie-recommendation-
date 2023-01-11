import pickle
import pandas as pd
import requests
import streamlit as st

def recommend(movie):
    movie_index = movies[movies['title_x'] == movie].index[0]
    ditances = similarity[movie_index]
    movies_list = sorted(list(enumerate(ditances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    recommend_movies_link = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title_x)
        recommend_movies_posters.append(movies.iloc[i[0]].poster_path)
        recommend_movies_link.append(movies.iloc[i[0]].wiki_link)
    return recommend_movies,recommend_movies_posters,recommend_movies_link

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load((open('similarity.pkl','rb')))

st. set_page_config(layout="wide",)
st.title("WELCOME")
selected = st.selectbox(
'Which movie would you like to watch?',movies['title_x'].values)

if st.button('Recommend Movies'):
    names,posters,link = recommend(selected)
    st.header('We recommend you these movies on basis of your choice:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(names[0])
        st.image(posters[0])
        st.write("[Details]({0})".format(link[0]))
    with col2:
        st.subheader(names[1])
        st.image(posters[1])
        st.write("[Details]({0})".format(link[1]))
    with col3:
        st.subheader(names[2])
        st.image(posters[2])
        st.write("[Details]({0})".format(link[2]))
    with col4:
        st.subheader(names[3])
        st.image(posters[3])
        st.write("[Details]({0})".format(link[3]))
    with col5:
        st.subheader(names[4])
        st.image(posters[4])
        st.write("[Details]({0})".format(link[4]))