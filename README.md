# 💳 FlowIQ — UPI Transaction Intelligence Platform

> *"Ask your payments data anything."*

An AI-powered UPI transaction analytics platform built with Python, Streamlit, and OpenAI — enabling natural language querying over 20,000 real UPI transactions across 4 Indian cities.

---

## 🚀 Live Demo

> Ask questions like:
> - *"How much was spent at Amazon in Delhi?"*
> - *"What is the total food spending in Mumbai?"*
> - *"Which city has the highest transaction volume?"*

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
| **Date Range** | 2024 |

---

## 🧠 Features

- 📈 **Power BI Dashboard** — Visual KPIs including revenue trends, merchant performance, city-wise spend, success/failure rates
- 💬 **AI Conversational Assistant** — Ask questions in plain English and get instant data-backed answers
- 🔍 **Multi-dimension Analytics** — Merchant × City, City × Purpose, Age Group, Gender, Device Type breakdowns
- ⚡ **Precomputed Metrics** — Fast responses via aggregated dataset metrics passed to LLM
- 🎨 **Custom Streamlit UI** — Clean, styled interface with expandable dataset viewer

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Data Storage** | CSV / SQL (PostgreSQL schema included) |
| **Data Processing** | Python, Pandas |
| **AI Engine** | OpenAI GPT-4o-mini |
| **Web App** | Streamlit |
| **Dashboard** | Power BI |
| **Environment** | python-dotenv |

---

## 📁 Project Structure

```
flowiq/
│
├── data/
│   └── Transaction details.csv       # 20,000 UPI transactions
│
├── chatbot.py                         # AI assistant logic (OpenAI + metrics)
├── app.py                             # Streamlit UI
├── schema.sql                         # SQL schema for database setup
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variable template
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/flowiq.git
cd flowiq
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Add your OpenAI API key inside .env
```

`.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
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
    Status                VARCHAR(10),
    PaymentMethod         VARCHAR(20),
    PaymentMode           VARCHAR(20),
    MerchantName          VARCHAR(50),
    Purpose               VARCHAR(30),
    City                  VARCHAR(30),
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

## 💡 How the AI Assistant Works

```
User Question
     ↓
Precomputed Metrics (Pandas aggregations)
     ↓
Prompt Engineering (metrics + question → GPT-4o-mini)
     ↓
Natural Language Answer
```

The assistant has access to:
- Top merchants by transaction count & total amount
- City-wise spend breakdown
- Merchant × City combination totals
- City × Purpose combination totals
- Monthly transaction trends
- Payment method, device type & gender distribution

---

## 📸 Screenshots

> *(Add Power BI dashboard screenshot here)*
> *(Add Streamlit chatbot UI screenshot here)*

---

## 📝 Sample Questions to Ask

```
"How much was spent at Zomato in Bangalore?"
"Which city has the most transactions?"
"What is the total travel spending in Delhi?"
"Which merchant has the highest revenue?"
"Show me monthly transaction trends"
"What is the most used payment method?"
```

---

## 🔮 Future Enhancements

- [ ] Multi-turn conversation memory
- [ ] Anomaly detection (unusual transaction spikes)
- [ ] Spend forecasting using Prophet / Linear Regression
- [ ] Dashboard auto-filter based on chatbot response
- [ ] User authentication & personalized history

---

## 👩‍💻 Author

**Arundhati Thakur**
- Built as part of a Data Analytics portfolio project
- Tools: Python • SQL • Power BI • OpenAI API • Streamlit

---

## 📄 License

MIT License — free to use and modify.
