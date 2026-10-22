import pandas as pd

data = pd.read_csv("people.csv")
names = data["name"].tolist()
emails = data["email"].tolist()

for name, email in zip(names, emails):
    message = f"Hi {name}, this is a test email for {email}."
    print(message)
