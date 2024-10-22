import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def run_sales_prediction(df):
    """Run Linear Regression to predict sales based on store data."""

    y = df["Store_Sales"]
    x = df.drop("Store_Sales", axis=1)

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # Bin the data for classification (low, medium, high)
    bins = np.quantile(y, [0, 0.33, 0.66, 1])
    y_test_binned = np.digitize(y_test, bins) - 1
    y_pred_binned = np.digitize(y_pred, bins) - 1

    # Calculate accuracy and recall
    accuracy = accuracy_score(y_test_binned, y_pred_binned)
    recall = recall_score(y_test_binned, y_pred_binned, average='macro')

    # Confusion Matrix
    cm = confusion_matrix(y_test_binned, y_pred_binned)

    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    print("Confusion Matrix:")
    print(cm)

    # Plot Confusion Matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

    # Visualize actual vs. predicted sales
    plt.figure(figsize=(12, 6))
    plt.plot(y_test.values, label='Actual Sales', color='#1f77b4', marker='o', linestyle='-', markersize=6)
    plt.plot(y_pred, label='Predicted Sales', color='#ff7f0e', marker='x', linestyle='--', markersize=6)
    plt.title('Actual vs. Predicted Sales')
    plt.xlabel('Samples')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot histogram of actual sales
    plt.figure(figsize=(12, 6))
    plt.hist(y_test.values, bins=30, alpha=0.7, color='#2ca02c', edgecolor='black', linewidth=1.2)
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()



