import csv 
from pathlib import Path

logopath = Path("./logos/")
table = [["team_abbr", "logo_url"]]

for logo in logopath.iterdir():
    team_abbr = logo.stem
    logo_url = f"https://raw.githubusercontent.com/shoenot/NFL-Team-Logos-Transparent-Squared/refs/heads/main/logos/{team_abbr}.png"
    table.append([team_abbr, logo_url])

with open("logo_urls.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerows(table)
