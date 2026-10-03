import pandas as pd
import glob
import os

files = glob.glob("data/raw/*.parquet")
df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

print("=== Filter Funnel ===")
print(f"Stage 0, raw source (all parts): {len(df)}")

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

print(f"Stage 1a, NAICS 458 only: {naics_match.sum()}")
print(f"Stage 1b, known apparel/fashion employer only: {company_match.sum()}")
print(f"Stage 1, NAICS 458 OR known employer (industry_match): {industry_match.sum()}")

role_terms = [
    "business analyst", "data analyst", "business intelligence",
    "analytics", "insights analyst", "merchandising analyst",
    "reporting analyst", "operations analyst"
]
role_pattern = "|".join(role_terms)
role_match = df["TITLE_CLEAN"].str.contains(role_pattern, case=False, na=False)

print(f"Stage 2, role-title keyword match only (any industry): {role_match.sum()}")

filtered = df[industry_match & role_match].copy()

print(f"Stage 3, industry_match AND role_match (final filtered set): {len(filtered)}")

# Duplicate check on the final set, mirrors what other groups log
dup_count = filtered.duplicated(subset=["ID"]).sum() if "ID" in filtered.columns else "ID column not found, skipped"
print(f"Duplicate IDs in final set: {dup_count}")

os.makedirs("data/interim", exist_ok=True)
filtered.to_csv("data/interim/apparel_analyst_filtered.csv", index=False)
print("\nSaved to data/interim/apparel_analyst_filtered.csv")

os.makedirs("outputs", exist_ok=True)
with open("outputs/filter_funnel.md", "w") as f:
    f.write("# Filter Funnel\n\n")
    f.write("| Stage | Count |\n")
    f.write("|---|---|\n")
    f.write(f"| Raw source (21 parquet parts) | {len(df)} |\n")
    f.write(f"| NAICS 458 only | {naics_match.sum()} |\n")
    f.write(f"| Known apparel/fashion employer only | {company_match.sum()} |\n")
    f.write(f"| NAICS 458 OR known employer | {industry_match.sum()} |\n")
    f.write(f"| Role-title keyword match (any industry) | {role_match.sum()} |\n")
    f.write(f"| Final filtered set (industry AND role) | {len(filtered)} |\n")
print("Saved funnel table to outputs/filter_funnel.md")

print("\nAll matched titles and companies:")
print(filtered[["TITLE_CLEAN", "COMPANY_NAME", "STATE_NAME"]].to_string())
