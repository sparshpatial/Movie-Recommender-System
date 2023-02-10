import streamlit as st
import pickle
import pandas as pd

movies_list=pickle.load(open('movie.pkl','rb'))
movies_list=movies_list['title'].values
st.title('Movie Recommender System')
option = st.selectbox(
    'Select any movie',
 movies_list   
)