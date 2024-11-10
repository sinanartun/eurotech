import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score
import h2o

# Initialize H2O
h2o.init()

# Load the test data
test_data_path = r"data\bank_transactions_data_2_test.csv"
test_df = pd.read_csv(test_data_path)

# Preprocess the test data
selected_columns = ["TransactionAmount", "CustomerAge", "TransactionDuration", "LoginAttempts", "AccountBalance"]
X_test = test_df[selected_columns]
y_test = (test_df["TransactionAmount"] > 1000).astype(int)
y_test.name = "HighTransaction"  # Rename the target column

# Load the model
model_path = r"models\model_weight_5.00.pkl\DRF_1_AutoML_10_20241109_195239"  # Adjust the path as needed
model = h2o.load_model(model_path)

# Convert test data to H2OFrame
test_data = h2o.H2OFrame(pd.concat([X_test, y_test], axis=1))
test_data['HighTransaction'] = test_data['HighTransaction'].asfactor()

# Make predictions
predictions = model.predict(test_data).as_data_frame()
y_pred = predictions['predict'].astype(int)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
print("Accuracy Score:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

# Visualize the results
class_labels = ['0', '1']
f1_scores = [report[label]['f1-score'] for label in class_labels]
plt.figure(figsize=(10, 6))
plt.bar(class_labels, f1_scores)
plt.xlabel('Class')
plt.ylabel('F1-Score')
plt.title('F1-Score for Each Class')
plt.show()
