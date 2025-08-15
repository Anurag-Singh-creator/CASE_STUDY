# Pricing Treatment Analysis

## Project Overview
This project analyzes the causal impact of a pricing intervention applied to selected  trade routes.  
The goal is to:
1. Estimate the effect of the treatment on **price**, **bookings**, and **revenue**.
2. Assess heterogeneity in effects across **trade clusters**.
3. Provide actionable recommendations based on the findings.

The analysis uses **Difference-in-Differences (DiD)** and **Two-Way Fixed Effects (TWFE)** models to measure treatment effects while controlling for trade and time fixed effects.

---
### Methodology

Clustering: Trade codes are grouped into 3 clusters to assess heterogeneity in treatment effects.

Treatment Definition: Pricing intervention applied to treatment group from a defined cutoff date.

Models Used:

Difference-in-Differences (DiD) to compute Average Treatment Effect (ATE).

Two-Way Fixed Effects (TWFE) to control for trade-specific and time-specific factors.


## ⚙️ Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/Anurag-Singh-creator/CASE_STUDY.git
cd CASE_STUDY

### Create a Virtual Environment
python -m venv .venv_maersk
.venv_maersk\Scripts\Activate

### Install Dependencies
pip install -r requirements.txt



