# 🚖 Predicting Taxi Fares Using Machine Learning
A Regression Analysis

This project aims to build a robust predictive model that estimates taxi fares based on features like trip distance, duration, and traffic-related information. The primary goal is to create an accurate fare estimation model that can help customers and service providers understand fare breakdowns in advance.

📌 Project Overview
Problem Statement: Predict the fare amount for taxi rides using various trip and location-based features.

Target Variable: fare_amount

Tools & Libraries: Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

🧹 Data Preprocessing
Null Value Handling: Dropped rows where the target variable fare_amount was missing, as these entries cannot be used for supervised learning.

Data Matching: Ensured consistency between the fare_amount and other associated columns like trip_distance, trip_duration, and geolocation variables to avoid misaligned or noisy training data.

Feature Engineering: Created new variables such as:

Distance traveled using pickup and dropoff coordinates

Trip duration

Hour of day and day of week from timestamp data

📊 Modeling Techniques
Linear Regression

Polynomial Regression

XGBoost Regressor

Among these, Polynomial Regression yielded the best results with:

R² Score: 0.937

Mean Squared Error (MSE): 34.59

📈 Key Insights
Trip Distance, Trip Duration, and Per Km Rate were among the most influential features.

Fare estimation accuracy increased significantly after applying polynomial features.
