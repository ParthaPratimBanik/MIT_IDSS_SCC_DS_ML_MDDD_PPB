# Pima Diabetes Analysis
A case study of Foundations of Data Science course.


## <u>**Description:**</u>
In this case study, the aim is to analyze diabetes data and address some important insights.
This case study is mainly focused on Exploratory Data Analysis (EDA).


## <u>**Problem Statement:**</u>
Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.

A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. Here, different aspects of Diabetes are analyzed by doing EDA.

## <u>**Data Dictionary:**</u>
Below is the attribute information:

**`Pregnancies`**: Number of times pregnant\
**`Glucose`**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test\
**`Blood pressure`**: Diastolic blood pressure (mm Hg)\
**`SkinThickness`**: Triceps skinfold thickness (mm)\
**`Insulin`**: 2-Hour serum insulin (mu U/ml) test\
**`BMI`**: Body mass index (weight in kg/(height in m)^2)\
**`DiabetesPedigreeFunction`**: A function that scores the likelihood of diabetes based on family history\
**`Age`**: Age in years\
**`Outcome`**: Class variable (0: the person is not diabetic or 1: the person is diabetic)


## <u>**Questions:**</u>

Q 1. Import the necessary libraries and briefly explain the use of each library\
Q 2. Read the given dataset\
Q3. Show the last 10 records of the dataset. How many columns are there?\
Q4. Show the first 10 records of the dataset\
Q5. What do you understand by the dimension of the dataset? Find the dimension of the `pima` dataframe.\
Q6. What do you understand by the size of the dataset? Find the size of the `pima` dataframe.\
Q7. What are the data types of all the variables in the data set?\
Q8. What do you mean by missing values? Are there any missing values in the `pima` dataframe?\
Q9. What does summary statistics of data represents? Find the summary statistics for all variables except 'Outcome' in the `pima` data? Take one column/variable from the output table and explain all the statistical measures.\
Q 10. Plot the distribution plot for the variable 'BloodPressure'. Write detailed observations from the plot.\
Q 11. What is the 'BMI' for the person having the highest 'Glucose'?\
Q 12. \
Q 12.1 What is the mean of the variable 'BMI'?\
Q 12.2 What is the median of the variable 'BMI'?\
Q 12.3 What is the mode of the variable 'BMI'?\
Q 12.4 Are the three measures of central tendency equal?\
Q 13. How many women's 'Glucose' level is above the mean level of 'Glucose'?\
Q 14. How many entries (women) have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the median of 'BMI'?\
Q 15. Below is the pairplot of variables 'Glucose', 'SkinThickness' and 'DiabetesPedigreeFunction'. Write you observations from the plot.\
Q 16. Plot the scatterplot between 'Glucose' and 'Insulin'. Write your observations from the plot.\
Q 17. Plot the boxplot for the 'Age' variable. Are there outliers?\
Q 18. Plot histograms for variable Age to understand the number of women in different Age groups given that they have diabetes or not. Explain both histograms and compare them.\
Q 19. What is Inter Quartile Range of all the variables? Why is it used? Which plot visualizes the same?\
Q 20. Find and visualize the the correlation matrix. Write your observations from the plot.