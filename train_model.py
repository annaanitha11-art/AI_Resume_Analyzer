import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib


# 1. Load the dataset
data = pd.read_csv("data/resume_dataset.csv")

# 2. Separate input features and target
X = data.drop("match", axis=1)
y = data["match"]

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 4. Create the Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# 5. Train the model
model.fit(X_train, y_train)

# 6. Make predictions on test data
predictions = model.predict(X_test)

# 7. Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# 8. Save the trained model
joblib.dump(model, "model/model.pkl")

print("Model saved successfully!")