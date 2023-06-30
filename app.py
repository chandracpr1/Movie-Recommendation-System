import streamlit as st
import pickle
import requests
import pandas as pd
from PIL import Image




# new_df = pickle.load(open('movies.pkl' ,'rb'))/
new_df = pd.read_pickle(open('movies.pkl' ,'rb'))
movies_list=new_df['title'].values
similarity =pd.read_pickle(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('http://api.themoviedb.org/3/movie/{}?api_key=dbdec17250350e80933c018ea7d6eaaf&language=en-US'.format(movie_id))
    data=response.json()
    #print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    rc = []
    movie_index = new_df[new_df['title'] == movie ].index[0]
    distances=similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True , key=lambda x : x[1])[1:10]
    rc_poster= []
    for i in movie_list:
        movie_id=new_df.iloc[i[0]].movie_id
        rc.append(new_df.iloc[i[0]].title)
        # fetch posters from API
        rc_poster.append(fetch_poster(movie_id))

    return rc , rc_poster

st.title(":red[Movie Recommendation Web Interface]")
image=Image.open('image1.png')
st.sidebar.image(image)
st.sidebar.write("This web app recommends similar movies based on the selected movies")

selected_movie_name = st.selectbox(
    ':red[Select any movie to find similar movies ]',
    movies_list)

st.write('Your selection:', selected_movie_name)

if st.button('Recommend'):
    names , posters=recommend(selected_movie_name)

    col1, col2, col3   = st.columns(3)

    with col1:
        st.image(posters[0])
        st.write(names[0])

    with col2:
        st.image(posters[1])
        st.write(names[1])

    with col3:
        st.image(posters[2])
        st.write(names[2])
    
    col1, col2, col3   = st.columns(3)

    with col1:
        st.image(posters[3])
        st.write(names[3])

    with col2:
        st.image(posters[4])
        st.write(names[4])

    with col3:
        st.image(posters[5])
        st.write(names[5])
    