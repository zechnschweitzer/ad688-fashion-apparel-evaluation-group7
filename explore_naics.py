import pandas as pd
import glob
import os

files = glob.glob("data/raw/*.parquet")
df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

known_apparel_companies = [
    "adidas", "vuoriinc", "tjx", "jobs.tjx.com", "careers.michaels.com",
    "ralph lauren", "macy's", "macys", "nordstrom", "kohl's", "kohls",
    "jcpenney", "foot locker", "dsw", "ross stores", "burlington",
    "victoria's secret", "victorias secret", "under armour", "lululemon",
    "columbia sportswear", "vf corporation", "pvh corp", "kontoor brands",
    "urban outfitters", "anthropologie", "american eagle outfitters",
    "abercrombie & fitch", "hollister co", "forever 21", "old navy",
    "banana republic", "gap inc", "the gap", "chico's fas"
]

df["COMPANY_CLEAN"] = df["COMPANY_NAME"].astype(str).str.strip().str.lower()
company_match = df["COMPANY_CLEAN"].isin(known_apparel_companies)
naics_match = df["NAICS_2022_3"] == "458"
industry_match = naics_match | company_match

role_terms = [
    "business analyst", "data analyst", "business intelligence",
    "analytics", "insights analyst", "merchandising analyst",
    "reporting analyst", "operations analyst"
]
role_pattern = "|".join(role_terms)
role_match = df["TITLE_CLEAN"].str.contains(role_pattern, case=False, na=False)

filtered = df[industry_match & role_match].copy()

print("Rows matching BOTH (widened roles):", len(filtered))

os.makedirs("data/interim", exist_ok=True)
filtered.to_csv("data/interim/apparel_analyst_filtered.csv", index=False)
print("Saved to data/interim/apparel_analyst_filtered.csv")

print("\nAll matched titles and companies:")
print(filtered[["TITLE_CLEAN", "COMPANY_NAME", "STATE_NAME"]].to_string())
