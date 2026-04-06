import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI




# Load key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the real CSV properly
df = pd.read_csv("data/Transaction details.csv")

# Clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Ensure essential columns exist
required_cols = [
    "MerchantName", "City", "Purpose", "PaymentMethod",
    "DeviceType", "Gender", "Amount", "TransactionDate"
]

for col in required_cols:
    if col not in df.columns:
        print("Missing column:", col)

# Convert date column
try:
    df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
except:
    pass

# Precompute REAL dataset metrics
metrics = {
    "top_merchants": df["MerchantName"].value_counts().to_dict(),
    "merchant_amount": df.groupby("MerchantName")["Amount"].sum().to_dict(),

    "top_cities": df["City"].value_counts().to_dict(),
    "city_amount": df.groupby("City")["Amount"].sum().to_dict(),

    "top_purposes": df["Purpose"].value_counts().to_dict(),
    "purpose_amount": df.groupby("Purpose")["Amount"].sum().to_dict(),

    "top_payment_methods": df["PaymentMethod"].value_counts().to_dict(),

    "device_usage": df["DeviceType"].value_counts().to_dict(),

    "gender_distribution": df["Gender"].value_counts().to_dict(),
}
    # MERCHANT + CITY combination totals
merchant_city_amount = (
      df.groupby(["MerchantName", "City"])["Amount"].sum().reset_index()
)

metrics["merchant_city_amount"] = {
      f"{row['MerchantName']}|{row['City']}": float(row["Amount"])
        for idx, row in merchant_city_amount.iterrows()
}

# CITY + PURPOSE combination totals
city_purpose_amount = (
    df.groupby(["City", "Purpose"])["Amount"].sum().reset_index()
)

metrics["city_purpose_amount"] = {
    f"{row['City']}|{row['Purpose']}": float(row["Amount"])
    for idx, row in city_purpose_amount.iterrows()
}

# CITY + PURPOSE remaining balance
if "remainingbalance" in df.columns:
    city_purpose_balance = (
        df.groupby(["City", "Purpose"])["remainingbalance"].sum().reset_index()
    )

    metrics["city_purpose_balance"] = {
        f"{row['City']}|{row['Purpose']}": float(row["remainingbalance"])
        for idx, row in city_purpose_balance.iterrows()
    }


# Monthly amounts (handled safely)
if "TransactionDate" in df.columns:
    metrics["monthly_amount"] = (
        df.groupby(df["TransactionDate"].dt.to_period("M"))["Amount"]
        .sum()
        .astype(float)
        .to_dict()
    )
else:
    metrics["monthly_amount"] = {}







def ask_chatbot(question):
    prompt = f"""
    You are an AI UPI Transaction Analyst.

    Use ONLY the following dataset metrics:

    METRICS = {metrics}


      Key format = "City|Purpose" exactly matching dataset values.

    Example:
    "Mumbai|Shopping"

  

    RULES:
    - Use EXACT values from METRICS.
    - Do NOT guess.
    - If something is missing, say: "No data available for this city-purpose combination."
    - Provide clear insights using the real numbers.
    RULES:
    - Use EXACT values from METRICS.
    - If a value doesn't exist, respond: "This data is not available in the dataset."
    - Do NOT guess or invent numbers.
    - Provide clear, useful insights.
    - Months in metrics are in YYYY-MM format.

    - If user asks:
    "transaction for <merchant> in <city>"
    → Look inside METRICS["merchant_city_amount"] 
      using key: "MerchantName|City"

Example:
"Amazon|Mumbai"


    User asked: {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content



