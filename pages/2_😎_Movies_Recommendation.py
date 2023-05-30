
import streamlit as st

from Home import movies, fetch_poster, recommend



st.title("Movie Recommender System")

number_of_recommendation = st.number_input("Number of recommendations", min_value=1, max_value=30, value=5)

selected_movie_name = st.selectbox(
    'Recommendation based on...',
    movies['title'].values
)


if st.button("Recommend"):
    st.title("Recommended Movies")
    st.write("movie recommendation based on movie you selected")
    names, posters = recommend(selected_movie_name, number_of_recommendation)

    num_movies = len(names)
    num_rows = (num_movies + 4) // 5

    columns = st.columns(5)

    
    for row in range(num_rows):
        start_index = row * 5
        end_index = min((row + 1) * 5, num_movies)

        for i in range(start_index, end_index):
            with columns[i % 5]:
                st.text(names[i])
                st.image(posters[i])
