# 🚖 Predicting Taxi Fares Using Machine Learning
**A Regression Analysis**

This project aims to build a robust predictive model that estimates taxi fares based on features like trip distance, duration, and traffic-related information. The primary goal is to create an accurate fare estimation model that can help customers and service providers understand fare breakdowns in advance.

**Project Overview**
Problem Statement: Predict the fare amount for taxi rides using various trip and location-based features.

Target Variable: Trip_Price

Tools & Libraries: Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

**🧹 Data Preprocessing**
Null Value Handling: Dropped rows where the target variable Trip_Price was missing, as these entries cannot be used for supervised learning.

Data Matching: Ensured consistency between the Trip_Price and other associated columns like trip_distance, trip_duration, and geolocation variables to avoid misaligned or noisy training data.

**📊 Modeling Techniques**
1. Linear Regression

2. Polynomial Regression

3. XGBoost Regressor

Among these, Polynomial Regression yielded the best results with:

R² Score: 0.937

Mean Squared Error (MSE): 34.59

**📈 Key Insights**
Trip_Distance_km, Per_Km_Rate, Per_Minute_Rate, Trip_Duration_Minutes, Traffic_Conditions_Low were among the most influential features.

Fare estimation accuracy increased significantly after applying polynomial features.
