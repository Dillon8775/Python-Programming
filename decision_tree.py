import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

data = {
    "heart_rate": [72, 85, 60, 95, 70, 88, 65],
    "steps": [8000, 3000, 12000, 2000, 9000, 4000, 11000],
    "sleep_hours": [7, 5, 8, 4, 7.5, 5.5, 8],
    "spo2": [98, 95, 99, 93, 97, 94, 99],
    "health_status": [2, 1, 2, 0, 2, 1, 2]  # Target
}

df = pd.DataFrame(data)

X = df.drop("health_status", axis=1)
y = df["health_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))