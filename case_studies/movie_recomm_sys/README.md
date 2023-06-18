# Movie Recommendation System
A case study of **Recommendation System** course.


## <u>**Description:**</u>
In this case study, the aim is to apply different techniques to build recommendation systems such as `Rank-based` & `Collaborative Filtering-based` recommendation systems to recommend Movies to users.


## <u>**Data Dictionary:**</u>
The ratings dataset contains the following attributes:
* **`userId`**: the ID of user
* **`movieId`**: the ID of movie
* **`rating`**: score given by users
* **`timestamp`**: recording time


## <u>**Questions:**</u>

1. **Explore the Dataset**\
**Q 1.1** Print the top 5 rows of the dataset and describe the dataset.\
**Q 1.2** Describe the distribution of ratings.\
**Q 1.3** What are the total number of unique users and unique movies?\
**Q 1.4** Is there a movie in which the same user interacted with it more than once?\
**Q 1.5** Which is the most interacted movie in the dataset?\
**Q 1.6** Which user interacted the most with any movie in the dataset?\
**Q 1.7** What is the distribution of the user-movie interactions in this dataset?

2. **Create Rank Based Recommendation System**

3. **Build a User based Collaborative Filtering Recommendation System**\
**Q 3.1** What is the RMSE for the baseline user-based collaborative filtering recommendation system?\
**Q 3.2** What is the Predicted rating for a user with userId =4 and for movieId= 10 and movieId=3?\
**Q 3.3** Perform hyperparameter tuning for the baseline user-based collaborative filtering recommendation system and find the RMSE for tuned user-based collaborative filtering recommendation system?\
**Q 3.4** What is the Predicted rating for a user with userId =4 and for movieId= 10 and movieId=3 using tuned user-based collaborative filtering?\
**Q 3.5** Predict the top 5 movies for userId=4 with a similarity-based recommendation system?

4. **Build a Item based Collaborative Filtering Recommendation System**\
**Q 4.1** What is the RMSE for the baseline item-based collaborative filtering recommendation system?\
**Q 4.2** What is the Predicted rating for a user with userId =4 and for movieId= 10 and movieId=3?\
**Q 4.3** Perform hyperparameter tuning for the baseline item-based collaborative filtering recommendation system and find the RMSE for tuned item-based collaborative filtering recommendation system?\
**Q 4.4** What is the Predicted rating for an item with userId =4 and for movieId= 10 and movieId=3 using tuned item-based collaborative filtering?\
**Q 4.5** Predict the top 5 movies for userId=4 with a similarity-based recommendation system?

5. **Build a matrix factorization recommendation system**\
**Q 5.1** What is the RMSE for baseline SVD based collaborative filtering recommendation system?\
**Q 5.2** What is the Predicted rating for a user with userId =4 and for movieId= 10 and movieId=3?\
**Q 5.3** Perform hyperparameter tuning for the baseline SVD based collaborative filtering recommendation system and find the RMSE for tuned SVD based collaborative filtering recommendation system?\
**Q 5.4** What is the Predicted rating for a user with userId =4 and for movieId= 10 and movieId=3 using SVD based collaborative filtering?\
**Q 5.5** Predict the top 5 movies for userId=4 with SVD based recommendation system?

6. **Compute the precision and recall, for each of the 6 models, at k = 5 and 10.**

7. **Compare the results and provide insights**\
**Q 7.1** Compare the results from the baseline user-user and item-item-based models.\
**Q 7.2** How do these baseline models compare to each other with respect to the tuned user-user and item-item models?\
**Q 7.3** The matrix factorization model is different from the collaborative filtering models. Briefly describe this difference. Also, compare the RMSE and precision-recall for the models.\
**Q 7.4** Does it improve? Can you offer any reasoning as to why that might be?