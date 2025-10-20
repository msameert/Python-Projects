import requests
from datetime import datetime

#token = "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"
username = "MSAMEERT"
#repos = ["Python-Projects","AIS_project","streamlit_grayfilter-app","GPA-Calculator.app"]
repos = ["mini-projects"]

headers = {"Authorization" : f"Bearer {token}"}
total_commit = 0

start_date = input("Enter your starting date (YYYY-MM-DD) : ")+"T00:00:00Z"
end_date = input("Enter the end date (YYYY-MM-DD) : ")+"T23:59:59Z"

start = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
end = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%SZ")
days = (end - start).days

for repo in repos:
 response = requests.get(f"https://api.github.com/repos/{username}/{repo}/commits?=author={username}&since={start_date}&until={end_date}per_page=100", headers=headers)
 data = response.json()

 if isinstance(data,list):          
  count = len(data)
  total_commit += count

print(f"Your total commits from {start_date} to {end_date} are {total_commit}")

if total_commit == days:
  print("Your commit strength level is Good")
elif total_commit > days:
  print("Your commit strength level is Excellent!")
elif total_commit < days:
  print("Your commit strength level is Average : Work Hard")



