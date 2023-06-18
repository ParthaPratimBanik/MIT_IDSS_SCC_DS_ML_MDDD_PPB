# Hotel Booking Cancellation Prediction
A case study of **Classification and Hypothesis Testing** course.


## <u>**Description:**</u>
This case study is on **`Classification and Hypothesis Testing`**. The aim is to apply different classification techniques to solve the problem of predicting Hotel Booking Cancellations.


## <u>**Problem Statement:**</u>
A significant number of hotel bookings are called off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with. Such losses are particularly high on last-minute cancellations.

The new technologies involving online booking channels have dramatically changed customers’ booking possibilities and behavior. This adds a further dimension to the challenge of how hotels handle cancellations, which are no longer limited to traditional booking and guest characteristics.

The cancellation of bookings impacts a hotel on various fronts:
1. Loss of resources (revenue) when the hotel cannot resell the room.
2. Additional costs of distribution channels by increasing commissions or paying for publicity to help sell these rooms.
3. Lowering prices last minute, so the hotel can resell a room, reducing the profit margin.
4. Human resources to make arrangements for the guests.

## <u>**Objective:**</u>
INN Hotels Group has a chain of hotels in Portugal, they are facing problems with the high number of booking cancellations. They hope that the increasing number of cancellations calls for a Machine Learning based solution that can help predict which booking is likely to be canceled. Therefore, they have reached out to a firm for data-driven solutions where **Data Scientists**:
* Have to analyze the data provided to find which factors have a high influence on booking cancellations and
* Build a predictive model that can predict which booking is going to be canceled in advance, and
* Help in formulating profitable policies for cancellations and refunds.

## <u>**Data Dictionary:**</u>
The data contains the different attributes of customers' booking details. The detailed data dictionary is given below.

* **`Booking_ID`**: the unique identifier of each booking
* **`no_of_adults`**: Number of adults
* **`no_of_children`**: Number of Children
* **`no_of_weekend_nights`**: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
* **`no_of_week_nights`**: Number of weeknights (Monday to Friday) the guest stayed or booked to stay at the hotel
* **`type_of_meal_plan`**: Type of meal plan booked by the customer:
    * Not Selected – No meal plan selected
    * Meal Plan 1 – Breakfast
    * Meal Plan 2 – Half board (breakfast and one other meal)
    * Meal Plan 3 – Full board (breakfast, lunch, and dinner)
* **`required_car_parking_space:`** Does the customer require a car parking space? (0 - No, 1- Yes)
* **`room_type_reserved:`** Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels Group
* **`lead_time:`** Number of days between the date of booking and the arrival date
* **`arrival_year:`** Year of arrival date
* **`arrival_month:`** Month of arrival date
* **`arrival_date:`** Date of the month
* **`market_segment_type:`** Market segment designation.
* **`repeated_guest:`** Is the customer a repeated guest? (0 - No, 1- Yes)
* **`no_of_previous_cancellations:`** Number of previous bookings that were canceled by the customer prior to the current booking
* **`no_of_previous_bookings_not_canceled:`** Number of previous bookings not canceled by the customer prior to the current booking
* **`avg_price_per_room:`** Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
* **`no_of_special_requests:`** Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
* **`booking_status:`** Flag indicating if the booking was canceled or not.

## <u>**Questions:**</u>

<i>Question 1</i>: Check the summary statistics of the dataset and write your observations\
<i>Question 2</i>: Univariate Analysis\
<i>Question 2.1</i>: Plot the histogram and box plot for the variable Lead Time using the hist_box function provided and write your insights.\
<i>Question 2.2</i>: Plot the histogram and box plot for the variable Average Price per Room using the hist_box function provided and write your insights.\
<i>Question 3</i>: Bivariate Analysis\
<i>Question 3.1</i>: Find and visualize the correlation matrix using a heatmap and write your observations from the plot.\
<i>Question 3.2</i>: Plot the stacked barplot for the variable Market Segment Type against the target variable Booking Status using the stacked_barplot function provided and write your insights.\
<i>Question 3.3</i>: Plot the stacked barplot for the variable Repeated Guest against the target variable Booking Status using the stacked_barplot function provided and write your insights.\
<i>Question 4</i>: Logistic Regression\
<i>Question 4.1</i>: Build a Logistic Regression model (Use the sklearn library)\
<i>Question 4.2</i>: Check the performance of the model on train and test data\
<i>Question 4.3</i>: Find the optimal threshold for the model using the Precision-Recall Curve.\
<i>Question 4.4</i>: Check the performance of the model on train and test data using the optimal threshold.\
<i>Question 5</i>: Support Vector Machines\
<i>Question 5.1</i>: Build a Support Vector Machine model using a linear kernel-Comment on model performance\
<i>Question 5.2</i>: Check the performance of the model on train and test data\
<i>Question 5.3</i>: Find the optimal threshold for the model using the Precision-Recall Curve.\
<i>Question 5.4</i>: Check the performance of the model on train and test data using the optimal threshold.\
<i>Question 5.5</i>: Build a Support Vector Machines model using RBF kernel\
<i>Question 5.6</i>: Check the performance of the model on train and test data\
<i>Question 5.7</i>: Check the performance of the model on train and test data using the optimal threshold.\
<i>Question 6</i>: Decision Trees\
<i>Question 6.1</i>: Build a Decision Tree Model\
<i>Question 6.2</i>: Check the performance of the model on train and test data\
<i>Question 6.3</i>: Perform hyperparameter tuning for the decision tree model using GridSearchCV\
<i>Question 6.4</i>: Check the performance of the model on the train and test data using the tuned model\
<i>Question 6.5</i>: What are some important features based on the tuned decision tree?\
<i>Question 7</i>: Random Forest\
<i>Question 7.1</i>: Build a Random Forest Model\
<i>Question 7.2</i>: Check the performance of the model on the train and test data\
<i>Question 7.3</i>: What are some important features based on the Random Forest?\
<i>Question 8</i>: Conclude ANY FOUR key takeaways for business recommendations