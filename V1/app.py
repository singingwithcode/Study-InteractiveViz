import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('Spotify Most Streamed Songs.csv')

df_cleaned = df.dropna()
df_cleaned = df.dropna(axis=1)

st.title("Spotify Most Streamed Songs")
st.caption("https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs/data")

st.header("danceability vs streams")
st.caption("description of view")
st.scatter_chart(df_cleaned,  x='streams', y='danceability_%', color='artist_count')

st.header("danceability vs energy")
st.scatter_chart(df_cleaned,  x='energy_%', y='danceability_%', color='released_year')

st.header("Trends in Song Releases Over the Years")
st.balloons()
col1, col2, col3 = st.columns(3)
col1.checkbox("country")
col2.checkbox("rock")
col3.checkbox("folk")
st.slider("genre")
release_trends = df_cleaned['released_year'].value_counts().sort_index().reset_index()
release_trends.columns = ['released_year', 'song_count']
st.line_chart(release_trends,  x='released_year', y='song_count')

fig2 = px.scatter(df_cleaned, 
                  x='danceability_%', 
                  y='streams', 
                  color='artist_count',
                  hover_data=['track_name', 'artist(s)_name'],
                  title='Danceability vs Streams',
                  color_continuous_scale='Plasma')
st.plotly_chart(fig2)

fig3 = px.histogram(df_cleaned, 
                    x='bpm', 
                    title='Distribution of BPM',
                    color='released_year',
                    color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig3)

fig = px.scatter_matrix(df_cleaned,
                          dimensions=['danceability_%', 'energy_%', 'valence_%', 'acousticness_%', 'bpm'],
                          title='Pair Plot of Selected Features',
                          color='released_year',
                            color_continuous_scale='Plasma')
st.plotly_chart(fig)