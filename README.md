# 💳 FlowIQ — UPI Transaction Intelligence Platform

> *"Ask your payments data anything."*

A modern AI-powered analytics web app that helps users analyze UPI (Unified Payments Interface) transactions through natural language queries. Built using Streamlit, OpenAI GPT, and Python — this project converts raw financial data into meaningful insights, instantly.

---

## 🌟 Features

### 🔍 AI Chatbot (OpenAI GPT-powered)
Ask natural questions like:
- *"How much did I spend at Amazon in Mumbai?"*
- *"Which city has the highest transactions?"*
- *"What is the total amount spent on Shopping in Delhi?"*
- *"What is the top merchant this month?"*

> The chatbot uses **real dataset metrics — not guesses.**

---

### 📊 Data Insights
The system precomputes analytics including:
- Merchant-wise total spending
- City-wise spending
- Purpose-wise spending
- Merchant × City combinations
- City × Purpose combinations
- Monthly transaction trends
- Device type usage & Gender distribution

---

### 🧠 Smart Metric Engine
Data is processed in Python and stored in a structured dictionary:

✔ Accurate — ✔ 100% real data — ✔ No hallucinations — ✔ No wrong interpretations

All chatbot answers come **only** from the precomputed metrics dictionary.

---

### 🖥️ Beautiful Streamlit UI
- Clean blue-and-white fintech theme
- Expandable dataset viewer
- Chat-style UI with user message bubbles
- Styled AI response boxes
- Fully responsive layout

---

## 📊 Dataset Overview

| Attribute | Details |
|---|---|
| **Total Transactions** | 20,000 |
| **Cities** | Delhi, Mumbai, Bangalore, Hyderabad |
| **Merchants** | Amazon, Swiggy, Zomato, Flipkart, IRCTC |
| **Purposes** | Food, Travel, Shopping, Bill Payment, Others |
| **Payment Methods** | Phone Number, QR Code, UPI ID |
| **Average Transaction** | ₹993 |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend logic & data preprocessing |
| **Pandas** | Data cleaning & summarization |
| **Streamlit** | Web UI framework |
| **OpenAI GPT (gpt-4o-mini)** | AI chatbot engine |
| **python-dotenv** | Secure API key storage |
| **Power BI** | Visual analytics dashboard |
| **Git & GitHub** | Version control |

---

## 📁 Project Structure

```
flowiq/
│
├── data/
│   └── Transaction details.csv    # 20,000 UPI transactions
│
├── chatbot.py                      # AI assistant — metrics + OpenAI logic
├── app.py                          # Streamlit UI
├── schema.sql                      # SQL schema for database setup
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/flowiq.git
cd flowiq
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add your OpenAI API key

Create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

---

## 💬 How It Works

```
✔ Step 1 — Load Dataset
CSV → Pandas → Clean columns → Generate metrics

✔ Step 2 — Build Metrics
Python generates summaries:
  • Merchant totals          • City totals
  • City × Purpose combos    • Merchant × City combos
  • Monthly trends

✔ Step 3 — AI Answers Queries
User question → GPT-4o-mini → Matches metrics → Returns real values
```

---

## 🗄️ SQL Schema

```sql
CREATE TABLE upi_transactions (
    TransactionID         VARCHAR(20) PRIMARY KEY,
    TransactionDate       DATE,
    TransactionTime       TIME,
    Amount                DECIMAL(10,2),
    RemainingBalance      DECIMAL(10,2),
    Currency              VARCHAR(10),
    Status                VARCHAR(10),          -- 'Success' / 'Failed'
    PaymentMethod         VARCHAR(20),          -- 'Phone Number', 'QR Code', 'UPI ID'
    PaymentMode           VARCHAR(20),
    MerchantName          VARCHAR(50),          -- Amazon, Swiggy, Zomato, Flipkart, IRCTC
    Purpose               VARCHAR(30),          -- Food, Travel, Shopping, Bill Payment, Others
    City                  VARCHAR(30),          -- Delhi, Mumbai, Bangalore, Hyderabad
    Gender                VARCHAR(10),
    CustomerAge           INT,
    AgeGroup              VARCHAR(5),
    DeviceType            VARCHAR(20),
    TransactionType       VARCHAR(20),
    BankNameSent          VARCHAR(50),
    BankNameReceived      VARCHAR(50),
    CustomerAccountNumber BIGINT,
    MerchantAccountNumber BIGINT
);
```

---

---

## 🔮 Future Enhancements

- [ ] Multi-turn conversation memory
- [ ] Anomaly detection on unusual transaction spikes
- [ ] Spend forecasting using Prophet / Linear Regression
- [ ] Dashboard auto-filter triggered by chatbot response
- [ ] User authentication & personalized history

---

## 👩‍💻 Author

**Arundhati Thakur**
Data Analytics Portfolio Project
Python • SQL • Power BI • OpenAI API • Streamlit

---

## 📄 License

MIT License — free to use and modify.
