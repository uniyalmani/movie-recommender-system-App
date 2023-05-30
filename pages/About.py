import streamlit as st

st.title("About")

content = """
    Movie Recommender System Using TMDB Dataset and Machine Learning

    The Movie Recommender System, is a personal project that showcases a movie recommendation system built using the TMDB (The Movie Database) dataset and machine learning techniques. This project aims to demonstrate the capabilities of a movie recommender system and provide users with personalized movie recommendations based on their preferences.

    The TMDB dataset serves as the primary source of movie information for this project. It contains a vast collection of movie details such as titles, overviews, cast members, crew information, and movie posters. This dataset provides a comprehensive and rich set of features for analyzing movies and identifying similarities between them.

    The Movie Recommender System utilizes machine learning algorithms to generate accurate movie recommendations. The project repository, available at https://github.com/uniyalmani/movie-recommender-system, contains the model and code implementation used for building the recommendation system.

    The project employs various machine learning techniques, such as collaborative filtering, content-based filtering, or a hybrid approach, to provide personalized movie recommendations. Collaborative filtering analyzes user behavior and preferences to identify similar users and recommend movies that have been popular among those users but have not been seen by the target user. Content-based filtering focuses on movie characteristics, such as genres, cast members, directors, and plot summaries, to recommend movies with similar attributes to those enjoyed by the user. The hybrid approach combines the strengths of both collaborative and content-based filtering to improve recommendation accuracy.

    This Movie Recommender System website showcases the functionality of the recommendation system. It provides a user-friendly interface where users can input their preferences and receive personalized movie recommendations. The website allows users to explore movie titles, read overviews, view cast members, and browse movie posters. Based on the user's preferences, the system processes the input and generates tailored recommendations using the implemented machine learning model.

    It's important to note that this project is primarily a showcase and demonstration of a movie recommender system. It serves as an example of how machine learning techniques can be applied to provide personalized recommendations based on user preferences. The project repository contains the code and model implementation for reference and further exploration.

    Overall, This Movie Recommender System demonstrates the potential of using the TMDB dataset and machine learning algorithms to build an effective movie recommendation system. By leveraging user preferences and movie attributes, the system aims to enhance the movie-watching experience by suggesting movies that align with users' tastes and interests.
"""

st.write(content)
st.write("email - Ashutoshuniyal21@gmail.com")
