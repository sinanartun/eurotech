import boto3
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Boto3 S3 client
s3_client = boto3.client('s3')
bucket = '/my-aws-bucket'          # Replace with your actual bucket name
file_name = 'Mall_Customers.csv'   # Replace with your actual file name

# Read the data from S3
obj = s3_client.get_object(Bucket=bucket, Key=file_name)
data = pd.read_csv(obj['Body'])

# Data preprocessing
# Convert 'Genre' column into dummy variables
data = pd.get_dummies(data, columns=['Genre'], drop_first=True)

# Optional: Rename columns for clarity (if needed)
data.rename(columns={'Annual_Income_(k$)': 'Annual_Income'}, inplace=True)

data.dropna(inplace=True)  # This will drop rows with any missing values


scaler = StandardScaler()
data[['Age', 'Annual_Income', 'Spending_Score']] = scaler.fit_transform(data[['Age', 'Annual_Income', 'Spending_Score']])

X = data.drop('CustomerID', axis=1)  # Features
y = data['Spending_Score']           # Target variable (example)

# Assuming 'data' is your DataFrame after preprocessing

# Create a binary target variable using the median as the threshold
threshold = data['Spending_Score'].median()
data['High_Spender'] = (data['Spending_Score'] >= threshold).astype(int)

# Define features and target variable
X = data[['Age', 'Genre_Male']]
y = data['High_Spender']

# Split the data using stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'logistic_regression_model.pkl')

# Load the model from the file
loaded_model = joblib.load('logistic_regression_model.pkl')

# Evaluate the loaded model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Make predictions on the test set using the loaded model
y_pred = loaded_model.predict(X_test)

# Evaluate the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nConfusion Matrix:\n', confusion_matrix(y_test, y_pred))
print('\nClassification Report:\n', classification_report(y_test, y_pred))


# Upload the model to S3
s3_client = boto3.client('s3')
s3_client.upload_file('logistic_regression_model.pkl', 'customerdata33', 'models/logistic_regression_model.pkl')

