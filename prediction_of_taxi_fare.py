# -*- coding: utf-8 -*-
"""Prediction_of_Taxi_Fare.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WiNeR6MnpyYJpskM7Sd5dr5Ef3iPh29x
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv(r'/content/taxi_trip_pricing.csv')
df.head()

df.info()

df.describe()

df.select_dtypes(exclude=np.number)

df.columns.nunique()

df.isnull().sum()

# Percentage of missing values for each column
missing_percentage = df.isnull().mean() * 100

# Display columns with at least some missing values
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)

# Show the result
print(missing_percentage)

df_num=df.select_dtypes(include=np.number)
df_cat=df.select_dtypes(exclude=np.number)

df_cleaned = df.dropna(subset=['Trip_Price'])
print(df_cleaned.isnull().sum())

df_num=df_cleaned.select_dtypes(include=np.number)
df_num.shape

df_cat=df_cleaned.select_dtypes(exclude=np.number)
df_cat.shape

df_num.shape

df_num.isnull().sum()

df_cat.isnull().sum()

# Percentage of missing values for each column
missing_percentage = df_num.isnull().mean() * 100

# Display columns with at least some missing values
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)

# Show the result
print(missing_percentage)



df_cat[['Time_of_Day','Day_of_Week','Traffic_Conditions','Weather']].nunique()

df_cat['Time_of_Day'].unique()

df['Day_of_Week'].unique()

df['Traffic_Conditions'].unique()

df['Weather'].unique()

"""## Univariate Analysis"""

for i in df_num:
    plt.figure(figsize=(8, 6))
    sns.histplot(df_num[i], bins=30, kde=True)  # kde=True adds a kernel density estimate
    plt.title(f'Distribution of {i}')
    plt.xlabel(i)
    plt.ylabel('Frequency')
    plt.show()

# Barplots for categorical features
for i in df_cat:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df_cat[i])
    plt.title(f'Frequency distribution of {i}')
    plt.xlabel(i)
    plt.ylabel('Count')
    plt.show()

for i in df_cat:
    print(f"Frequency counts for {i}:")
    print(df_cat[i].value_counts())

sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

df.groupby('Weather')['Trip_Price'].mean()

"""###### In the Rain Seanson Taxi Price was High Comparing other parameters.

#### Checking The Correlation between the Numeric Variable.
"""

sns.heatmap(df_num.corr(),annot=True,cmap='coolwarm')
plt.show()

"""#### If the distance of trip become more means 'Trip Price' will be 'High'.  """

order=df.groupby('Traffic_Conditions')['Trip_Price'].mean().sort_values()
order

sns.barplot(df,x="Traffic_Conditions",y='Trip_Price')
plt.show()

"""###### When the Traffic is high,Price of Taxi is also High."""

df.groupby('Day_of_Week')['Trip_Price'].mean()

"""##### Taxi Price In the Weekday was collected more compare to Weekends."""

df.groupby('Time_of_Day')['Trip_Price'].mean()

# In The Afternoon time price of the taxi littel bit high compared the other 3.

"""## Bivariate Analysis"""

# Numerical Columns Analysis with Trip_Price
for i in df_num:
    plt.figure(figsize=(8, 4))
    sns.scatterplot(x=df_num[i], y=df['Trip_Price'])
    plt.title(f'{i} vs Trip_Price')
    plt.show()

for i in df_cat:
  plt.figure(figsize=(8,4))
  sns.boxplot(x=i,y='Trip_Price',data=df,)
  plt.title(f'{i} vs Trip_Price')
  plt.xticks(rotation=90)
  plt.show()

"""## Missing Value Treatment"""

df_num.isnull().sum()

sns.boxplot(df_num)

"""##### For Numerical Variables"""

df_num['Trip_Distance_km'].fillna(df_num['Trip_Distance_km'].median(), inplace=True)
df_num['Passenger_Count'].fillna(df_num['Passenger_Count'].mean(), inplace=True)
df_num['Base_Fare'].fillna(df_num['Base_Fare'].mean(), inplace=True)
df_num['Per_Km_Rate'].fillna(df_num['Per_Km_Rate'].mean(), inplace=True)
df_num['Per_Minute_Rate'].fillna(df_num['Per_Minute_Rate'].mean(), inplace=True)
df_num['Trip_Duration_Minutes'].fillna(df_num['Trip_Duration_Minutes'].mean(), inplace=True)

df_num.isnull().sum()

"""###### For Categorical Variables"""

df_cat = df_cat.apply(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else x, axis=0)

df_cat.isnull().sum()

for i in df_num:
    plt.figure(figsize=(6, 3))
    sns.boxplot(y=df_num[i])
    plt.title(f'Boxplot of {i}')
    plt.show()

# The Outlier Present in the Trip_Distance_km column.

def treat_outliers_iqr(df_num, column, method='cap'):
    Q1 = df_num[column].quantile(0.25)
    Q3 = df_num[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    if method == 'remove':
        return df_num[(df_num[column] >= lower_bound) & (df_num[column] <= upper_bound)]
    elif method == 'cap':
        df_num[column] = np.where(df_num[column] > upper_bound, upper_bound,
                       np.where(df_num[column] < lower_bound, lower_bound, df_num[column]))
        return df_num

df_num = treat_outliers_iqr(df_num, 'Trip_Distance_km', method='remove')

sns.boxplot(df['Trip_Distance_km'])
plt.title("Boxplot After Capping Outliers in Trip_Distance_km")
plt.show()

df_num = treat_outliers_iqr(df_num, 'Trip_Price', method='remove')

sns.boxplot(df_num['Trip_Price'])
plt.title("Boxplot After Capping Outliers in Trip_Price")
plt.show()

"""# Encoding"""

df_dummies=pd.get_dummies(df_cat,drop_first=True,dtype=int)

df_dummies.head()

df_dummies.isnull().sum()

"""## Scalling"""

from sklearn.preprocessing import StandardScaler
# Let’s say you dropped rows with NaNs from df_num like this:
df_num_clean = df_num.dropna()
# Then do the same for cat
df_cat_clean = df_cat.loc[df_num_clean.index]
target=df_num_clean['Trip_Price']
# Now scale and reset index
scaler = StandardScaler()
df_num_scaled = pd.DataFrame(scaler.fit_transform(df_num_clean), columns=df_num_clean.columns)
df_num_scaled.reset_index(drop=True, inplace=True)
df_cat_clean.reset_index(drop=True, inplace=True)

# Encode categorical columns
df_dummies = pd.get_dummies(df_cat_clean,drop_first=True,dtype=int)

# Concatenate
df_combi = pd.concat([df_num_scaled, df_dummies], axis=1)
print(df_combi.shape)

df_combi.shape

df_combi.isnull().sum()

"""# Model Building"""

df_combi.shape

x=df_combi.drop('Trip_Price',axis=1)

x.head()

x.shape

target.head()

target.shape

print(target.isnull().sum())

"""## Train_Test_Split"""

x_train,x_test,y_train,y_test=train_test_split(x,target,test_size=.30,random_state=20)

print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

y_test.head()

y_train.head()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

"""## Linear Regression Model"""

lr=LinearRegression()
model_lr=lr.fit(x_train,y_train)
model_lr

y_pred_lr=model_lr.predict(x_test)

LR_r2 = r2_score(y_test, y_pred_lr)
LR_mse = mean_squared_error(y_test, y_pred_lr)
## Output
print(f'R-squared of Linear_model: {LR_r2:.4f}')
print(f'Mean Squared Error of Linear_model: {LR_mse:.4f}')

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred_lr)
plt.xlabel('Actual Trip Price')
plt.ylabel('Predicted Trip Price')
plt.title('Actual vs. Predicted Trip Prices')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.show()

"""## Ploynominal Regression Model"""

poly=PolynomialFeatures(degree=2,include_bias=False)
x_train_poly=poly.fit_transform(x_train)
x_test_poly=poly.transform(x_test)

# Initialize and train the model
model = LinearRegression()
model.fit(x_train_poly, y_train)

# Predict using the trained model
y_pred = model.predict(x_test_poly)

# Create a scatter plot of actual vs. predicted values
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel('Actual Trip Price')
plt.ylabel('Predicted Trip Price')
plt.title('Actual vs. Predicted Trip Prices')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.show()

"""### Model Evaluation"""

Poly_r2 = r2_score(y_test, y_pred)
Poly_mse = mean_squared_error(y_test, y_pred)
## Output
print(f'R-squared of Polynomial Model: {Poly_r2:.4f}')
print(f'Mean Squared Error of Polynomial Model: {Poly_mse:.4f}')

"""###### Poly Model- Degree=3"""

poly=PolynomialFeatures(degree=3,include_bias=False)
x_train_poly3=poly.fit_transform(x_train)
x_test_poly3=poly.transform(x_test)

# Initialize and train the model
lr_3 = LinearRegression()
model_3=lr_3.fit(x_train_poly3, y_train)
model_3

# Predict using the trained model
y_pred_3 = model_3.predict(x_test_poly3)

r2 = r2_score(y_test, y_pred_3)
mse = mean_squared_error(y_test, y_pred_3)
## Output
print(f'R-squared of Poly, Degree=3: {r2:.4f}')
print(f'Mean Squared Error Poly, Degree=3: {mse:.4f}')

feature_names = poly.get_feature_names_out(x_train.columns)
feature_names

feature_names = poly.get_feature_names_out(input_features=x_train.columns)

# Display the feature names
for name in feature_names:
    print(name)

# Create a scatter plot of actual vs. predicted values
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred_3)
plt.xlabel('Actual Trip Price')
plt.ylabel('Predicted Trip Price')
plt.title('Actual vs. Predicted Trip Prices')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Diagonal line
plt.show()

"""# XG-Boost Model"""

from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV

param_dist = {
    'n_estimators': [50, 100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1, 0.3],
    'max_depth': [3, 4, 5, 6, 7, 8],
}
Xgb=XGBRegressor(random_state=25)
random_search = RandomizedSearchCV(estimator=Xgb, param_distributions=param_dist,
                                  n_iter=50, cv=5, scoring='neg_mean_squared_error',
                                   verbose=1, n_jobs=-1, random_state=25)
random_search.fit(x_train, y_train)
print("Best Parameters:", random_search.best_params_)
print("Best MSE:", -random_search.best_score_)

Xgb_model=XGBRegressor(**random_search.best_params_,random_state=25)
Xgb_model.fit(x_train,y_train)

y_pred_xgb=Xgb_model.predict(x_test)

r2 = r2_score(y_test, y_pred_xgb)
mse = mean_squared_error(y_test, y_pred_xgb)
## Output
print(f'R-squared of XgBoost : {r2:.4f}')
print(f'Mean Squared Error XgBoost : {mse:.4f}')

"""#### Grid Search CV"""

param_dist = {
    'n_estimators': [50, 100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1, 0.3],
    'max_depth': [3, 4, 5, 6, 7, 8],
}
Xgb_grid=XGBRegressor(random_state=25)
grid_search = GridSearchCV(estimator=Xgb_grid, param_grid=param_dist,
                                  cv=5, scoring='neg_mean_squared_error',
                                   verbose=1, n_jobs=-1)
grid_search.fit(x_train, y_train)
print("Best Parameters:", grid_search.best_params_)
print("Best MSE:", -grid_search.best_score_)

from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Use best params
xgb_best_model = XGBRegressor(
    learning_rate=0.1,
    max_depth=3,
    n_estimators=200,
    random_state=42
)

# Fit the model on training data
xgb_best_model.fit(x_train, y_train)

# Predict on test data
y_pred = xgb_best_model.predict(x_test)

# Evaluate
XGB_mse = mean_squared_error(y_test, y_pred)
XGB_r2 = r2_score(y_test, y_pred)

print("Final Model MSE:", mse)
print("R-squared:", r2)

# Assuming you have a DataFrame with feature names
# If X_train is a DataFrame:
feature_importances = pd.Series(xgb_best_model.feature_importances_, index=x_train.columns)

# Sort and display
feature_importances = feature_importances.sort_values(ascending=False)
print("Top Features:\n", feature_importances)

# Plot
plt.figure(figsize=(10, 6))
feature_importances.plot(kind='bar')
plt.title("Feature Importance - XGBoost")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.show()

xgb = XGBRegressor(random_state=42)

# Define parameter grid
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.8, 1.0],
    'colsample_bytree': [0.8, 1.0]
}

# GridSearchCV setup (scoring is negative MSE because sklearn minimizes loss)
grid_search = GridSearchCV(
    estimator=xgb,
    param_grid=param_grid,
    cv=3,
    scoring='neg_mean_squared_error',
    verbose=1,
    n_jobs=-1
)

# Fit on training data
grid_search.fit(x_train, y_train)

# Best parameters
print("Best Parameters:", grid_search.best_params_)

# Best model evaluation
best_model = grid_search.best_estimator_
y_pred_xgb2 = best_model.predict(x_test)

# MSE & RMSE
mse = mean_squared_error(y_test, y_pred_xgb)
# Output
print("Best Model MSE:", mse)

results = {
    "Model": ["Linear Regression", 'Polynomial_Regression', "XGBoost"],
    "MSE": [LR_mse, Poly_mse,XGB_mse],
    "R2 Score": [LR_r2,Poly_r2,XGB_r2]
}

import pandas as pd
results_df = pd.DataFrame(results)
results_df.sort_values(by="MSE")