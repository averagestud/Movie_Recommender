# Movie Recommender
This is a movie recommendation system based on content based filtering.

# Website
[Website](https://huggingface.co/spaces/Deepaprakash04/Movie_Recommender)

We all have seen how well the Recommendation Engines of popular OTT Platforms like Netflix and Amazon Prime function.
These recommendation systems are based on what is known as hybrid filtering i.e. Content Based Filtering as well as Collaborative Filtering techniques.

Here I have implemented Content based Movie Recommendation where by giving a movie name out of the 5000 Movie_TMDB Database, we can get the top 10 most correlated movies.

The main idea is to recommend movies based on the genres, director, cast, crew of the movie. This is done by taking the cosine distance between all the different movies and only displaying the closest 10 movies.
Since this is based on content based filtering, in order to extract the required genres, directors and crew, I was also able to use some of the most popular NLP Techniques like Stemming, removing stop words and etc.

I was also able to successfully deploy the model on my local machine using streamlit and here is the screenshot of the app running.
![image](https://github.com/averagestud/Movie_Recommender/assets/128608033/f822adc7-2e0d-41ae-80e0-a6e064a866f1)

 *Note: We can see the full movie poster with the help of the zoom button that is provided by streamlit.
 
