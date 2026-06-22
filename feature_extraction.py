import re

email = input("Enter Email:\n")

urls = re.findall(r'https?://\S+', email)

keywords = [
    "verify",
    "password",
    "login",
    "urgent",
    "update",
    "click"
]

found = []

for word in keywords:
    if word.lower() in email.lower():
        found.append(word)

print("URLs Found:", urls)
print("Suspicious Keywords:", found)
