# Data Dictionary — apparel_analyst_clean.csv

Cleaned dataset for Business/Data Analyst roles within NAICS 458
(Clothing, Clothing Accessories, Shoe, and Jewelry Retailers), filtered
using NAICS 458 + an exact-match apparel brand list + narrow analyst
title matching. 19 verified rows.

## Identification

| Field | Description |
|---|---|
| ID | Unique job posting identifier |
| TITLE_CLEAN | Standardized/cleaned job title |
| TITLE_RAW | Original job title as posted |
| COMPANY_NAME | Employer name |
| COMPANY_CLEAN | Standardized employer name |
| POSTED | Date the job was posted |

## Salary

| Field | Description |
|---|---|
| SALARY | Original salary text as posted |
| SALARY_FROM | Lower bound of posted salary range |
| SALARY_TO | Upper bound of posted salary range |
| ORIGINAL_PAY_PERIOD | Pay period as posted (e.g. hourly, annual) |

## Experience

| Field | Description |
|---|---|
| MIN_YEARS_EXPERIENCE | Minimum years of experience required |
| MAX_YEARS_EXPERIENCE | Maximum years of experience required |

## Education

| Field | Description |
|---|---|
| MIN_EDULEVELS_NAME | Minimum education level required |
| MAX_EDULEVELS_NAME | Maximum education level required |

## Skills

| Field | Description |
|---|---|
| SKILLS_NAME | General skills listed in the posting |
| SPECIALIZED_SKILLS_NAME | Specialized/technical skills listed |
| SOFTWARE_SKILLS_NAME | Software tools listed |

## Remote/Onsite

| Field | Description |
|---|---|
| REMOTE_TYPE_NAME | Work arrangement (Remote, Hybrid, On-site, Unknown) |

## Location

| Field | Description |
|---|---|
| CITY_NAME | City of the job posting |
| STATE_NAME | State of the job posting |
| COUNTY_NAME | County of the job posting |
| MSA_NAME | Metropolitan Statistical Area name |

## Industry / Occupation

| Field | Description |
|---|---|
| NAICS_2022_6 | 6-digit NAICS 2022 industry code |
| NAICS_2022_6_NAME | Industry name for the NAICS code |
| SOC_5 | 5-digit SOC occupation code |
| SOC_5_NAME | Occupation name for the SOC code |
