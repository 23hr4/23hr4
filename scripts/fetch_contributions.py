import sys
import json
import requests
from bs4 import BeautifulSoup

USERNAME = "23hr4"

def fetch():
    url = f"https://github.com/users/{USERNAME}/contributions"
    res = requests.get(url)
    if res.status_code != 200:
        print("Veri çekilemedi!")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    days = []
    
    for cell in soup.find_all("td", class_="ContributionCalendar-day"):
        date = cell.get("data-date")
        level = cell.get("data-level", "0")
        if date:
            days.append({"date": date, "level": int(level)})

    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(days, f, indent=2)
    print("data/contributions.json güncellendi!")

if __name__ == "__main__":
    fetch()