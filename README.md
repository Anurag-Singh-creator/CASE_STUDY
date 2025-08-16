# Pricing Treatment Analysis
| File/Folder                    | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`EDA.ipynb`**                | **Exploratory Data Analysis.**  Loads `pricing_treatment.csv`, cleans column names, and provides summary statistics and visualizations for price, bookings and revenue by trade\_code, time period and treatment status.  Helps you understand the distribution of the data and check assumptions before modelling.                                                                                                                                          |
| **`price_ananlysis.ipynb`**    | **Price implementation check.**  Verifies how the intervention affected prices. Produces bar charts summarising the price change by cluster and treatment status.                                        |
| **`ate_bookings.ipynb`**       | **Average Treatment Effect on Bookings.**  Implements Difference‑in‑Differences and TWFE models to estimate how the price intervention impacted bookings.  Computes raw average treatment effects (ATE) and regression‑adjusted estimates for each cluster.  Includes a bar plot showing the negative ATE on bookings across clusters and a table with coefficients and p‑values.                                                                            |
| **`ate_grossprofits.ipynb`**   | **ATE on Gross Profit under Margin Assumptions.**  Extends the DiD framework to bookings * (revenue - cost).  Because the dataset lacks a cost column, the notebook assumes a range of uniform margins (10–50%) and calculates cost as `price × (1 − margin)`.  It then computes the DiD on gross profit per cluster and reports whether the effect is statistically significant.  Results show that only one cluster exhibits a significant and large decline in gross profit. |
| **`heterogenity.ipynb`**       | **Heterogeneity of Treatment Effects.**  Uses the helper module to cluster trade codes into n groups based on mean and standard deviation of prices and bookings.  Then re‑estimates treatment effects separately within each cluster, comparing outcomes across clusters and interpreting how the intervention’s impact varies by trade characteristics. It tuns out to be that the optimum value of n = 3. And we have 3 clusters-  cluster 0, cluster 1, cluster 2. This is an important step because there is presence of Latent heterogenity which needs to be discovered and the ATE has to be seen in the backdrop of that latent heterogenity for better understanging of treatment effects.                                                                                            |
                                                                                          |
| **`heterogenity_clusters.py`** | **Clustering helper module.**  Defines `get_trade_code_clusters(df, n_clusters=3, random_state=42)` which aggregates each `trade_code`’s mean and standard deviation of price and bookings, scales the features and applies K‑means to assign each trade to a cluster.  Returns a dictionary mapping each `trade_code` to its cluster ID.  This module is imported in several notebooks to ensure consistent clustering.                                     |
| **`pricing_treatment.csv`**    | **Dataset.**  A CSV file containing the daily panel used for the case study.  Columns include `date` (timestamp), `trade_code` (route identifier), `treatment` (indicator for the new pricing algorithm vs. control), `price`, `bookings`, and `revenue`.  In some analyses you’ll also find derived variables such as `cost` (based on assumed margin) and cluster assignments.                                                                             |
| **`requirements.txt`**         | Lists the Python dependencies (`pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels`, `linearmodels`, `scikit‑learn`) needed to run the notebooks.                                                                                                                                                                                                                                                                                                       |
| **`.gitignore`**               | Standard Git ignore rules, e.g. to exclude notebook checkpoints and Python cache files.                                                                                                                                                                                                                                                                                                                                                                      |
| **`__pycache__/`**             | Automatically generated cache for compiled Python modules (not needed for analysis).                                                                                                                                                                                                                                                                                                                                                                         |

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



