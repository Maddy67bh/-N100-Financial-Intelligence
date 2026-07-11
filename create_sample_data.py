import pandas as pd
from pathlib import Path

folder = Path("data/raw")
folder.mkdir(parents=True, exist_ok=True)

# Companies
companies = pd.DataFrame({
    "company_id":[1,2,3,4,5],
    "ticker":["RELIANCE","TCS","INFY","HDFCBANK","ICICIBANK"],
    "company_name":[
        "Reliance Industries",
        "TCS",
        "Infosys",
        "HDFC Bank",
        "ICICI Bank"
    ],
    "sector":[
        "Energy",
        "IT",
        "IT",
        "Banking",
        "Banking"
    ]
})

companies.to_excel(folder/"companies.xlsx", index=False)


# Profit and Loss
profit_loss = pd.DataFrame({
    "company_id":[1,1,2,2,3,3],
    "year":[2024,2025,2024,2025,2024,2025],
    "sales":[10000,12000,8000,9000,7000,8500],
    "profit":[2000,2500,1800,2200,1500,1900]
})

profit_loss.to_excel(
    folder/"profitandloss.xlsx",
    index=False
)


# Balance Sheet
balance = pd.DataFrame({
    "company_id":[1,2,3],
    "year":[2025,2025,2025],
    "assets":[50000,40000,30000],
    "liabilities":[25000,20000,15000]
})

balance.to_excel(
    folder/"balancesheet.xlsx",
    index=False
)


# Cash Flow
cashflow = pd.DataFrame({
    "company_id":[1,2,3],
    "year":[2025,2025,2025],
    "operating_cashflow":[3000,2500,2000]
})

cashflow.to_excel(
    folder/"cashflow.xlsx",
    index=False
)


# Stock Prices
prices = pd.DataFrame({
    "company_id":[1,2,3],
    "date":["2025-01-01","2025-01-01","2025-01-01"],
    "close_price":[2500,3800,1600]
})

prices.to_excel(
    folder/"stock_prices.xlsx",
    index=False
)


print("All Excel files created successfully")