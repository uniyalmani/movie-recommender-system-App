import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-Us"
    response = requests.get(url)
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

def recommend(movie, number_of_recommendation):
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x: x[1])[1: number_of_recommendation + 1]

  recommended_movies = []
  recommended_movies_poster = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    #fetch poster 
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_poster



"#download movie_dict.pkl, similarity.pkl from https://github.com/uniyalmani/movie-recommender-system-ml-model"
movies_dict = pickle.load(open('movie_dict.pkl', 'rb')) 
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


def display_movies_in_batches(movies_df, batch_size=10):
    total_movies = len(movies_df)
    num_batches = (total_movies + batch_size - 1) // batch_size

    st.header("Movies")

    # Store the current batch index
    batch_index = st.session_state.get("batch_index", 0)

    # Create a container to hold the buttons
    # Create two columns for the buttons
    col1, col2 = st.columns([1, 4])

    # Check if "Previous" button is clicked
    if col1.button("Previous"):
        # Move to the previous batch
        batch_index -= 1
        if batch_index < 0:
            batch_index = num_batches - 1

    # Check if "Next" button is clicked
    if col2.button("Next"):
        # Move to the next batch
        batch_index += 1
        if batch_index >= num_batches:
            batch_index = 0

    # Update the batch index in session state
    st.session_state["batch_index"] = batch_index

    # Calculate the start and end index of the current batch
    start_idx = batch_index * batch_size
    end_idx = min((batch_index + 1) * batch_size, total_movies)

    # Get the current batch of movies
    batch_movies = movies_df.iloc[start_idx:end_idx]

    num_movies_per_row = 5 if batch_size >= 5 else batch_size

    # Display movie details in rows
    rows = st.columns(num_movies_per_row)
    movie_counter = 0

    num_movies = len(batch_movies)
    num_rows = (num_movies + 4) // 5

    columns = st.columns(5)

    for i, row in batch_movies.iterrows():
        movie = row
        
        poster_image = fetch_poster(movie["movie_id"])
        with columns[i % 5]:
            st.text(movie['title'])
            st.image(poster_image)

 
    


batch_size = st.number_input("Batch Size", min_value=1, max_value=100, value=10)
display_movies_in_batches(movies, batch_size)




    

