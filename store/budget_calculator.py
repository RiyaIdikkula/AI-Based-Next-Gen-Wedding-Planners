# budget_calculator.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the data
weddings_df = pd.read_csv('weddings.csv')
packages_df = pd.read_csv('packages.csv')

# Merge the DataFrames on Package_ID
merged_df = pd.merge(weddings_df, packages_df, on='Package_ID')

# Features and target variable
X = merged_df[['Guest_Count', 'Package_Cost']]
y = merged_df['Total_Budget']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'wedding_budget_model.pkl')
