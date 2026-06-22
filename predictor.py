import joblib

model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

email = input("Enter Email Content:\n")

data = vectorizer.transform([email])

prediction = model.predict(data)

if prediction[0] == 1:
    print("⚠ Phishing Email Detected")
else:
    print("✅ Safe Email")
