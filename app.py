import streamlit as st
import pandas as pd
import pickle
import requests
import gzip

def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0ebde39143b75dfe60202557eb478a5b&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recomend(op):
    movie_index = movies2[movies2['title'] == op].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
    Rec =[]
    rec_movies_posters = []
    for i in movies_list:
        movie_id = movies2.iloc[i[0]].movie_id
        Rec.append(movies2.iloc[i[0]].title)
        rec_movies_posters.append(fetch_poster(movie_id))
    return Rec,rec_movies_posters     

with gzip.open('compressed.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

movies = pickle.load(open('movies2.pkl', 'rb'))
movies2 = pd.DataFrame(movies)
lis = movies2['title'].values



st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .reportview-container {
        background: rgb(72 173 209)
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Movie Recomender System 🎥')
option = st.selectbox(
    'select your movie',
    lis)
#recomend button

if st.button('Recomended movies!!'):
    names,posters = recomend(option)
    # for i in r:
    #    st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5,gap = "medium")   
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])