# -Collaborative-Filtering-Book-Recommendation-System
This collaborative filtering book recommendation system leverages user ratings and book data to provide personalized book recommendations.


Summary:

This collaborative filtering book recommendation system leverages user ratings and book data to provide personalized book recommendations. The key steps involved in building this system include:

* Data Preprocessing: The system filters out books with fewer than 50 ratings to ensure reliability. It also focuses on users who have rated at least 200 books, identifying them as knowledgeable users.

• Data Transformation: Duplicate ratings by the same user for the same book are removed, resulting in a cleaner dataset. This processed data is then used to create a pivot table, which represents user ratings for books.

• Model Building: The system employs the k-nearest neighbors (KNN) algorithm to identify books that are similar to the one selected by the user. This is achieved by computing distances and finding the nearest neighbors based on user ratings.

• User Interaction: The system is implemented using Streamlit, a web-based framework for creating user-friendly applications. Users can select a book from the available options, and upon clicking the "Recommend" button, the system provides a list of book recommendations.

By applying these steps, the recommendation system offers users a personalised book list, enhancing their reading experience based on their preferences and the preferences of similar, knowledgeable users.S
