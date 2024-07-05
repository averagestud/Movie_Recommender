import streamlit as st
import pickle
import pandas as pd
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f19da43b6e95d951f63c85c751fee805&&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:10]
    
    recommended_movies=[]
    recommended_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        #Fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_posters

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
local_css("styles.css")

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie did you watch recently?',
    (movies['title'].values))

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    # Create a container for the movies
    st.markdown('<div class="movie-container">', unsafe_allow_html=True)
    
    for i in range(len(names)):
        
        movie_search_url = f"https://www.google.com/search?q={names[i]}"
        movie_html = f'''
            <div class="movie">
                <a href="{movie_search_url}" target="_blank">
                    <p>{names[i]}</p>
                    <img src="{posters[i]}" class="movie-poster" />
                </a>
            </div>
        '''
        st.markdown(movie_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
