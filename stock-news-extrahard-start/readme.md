
# Stock News Alert 📈📰

A Python automation project that tracks stock price movements using the Alpha Vantage API and sends the latest related news headlines via SMS using Twilio whenever the stock price changes significantly.

---

## Features

- Fetches daily stock data from Alpha Vantage
- Calculates percentage change between the last two trading days
- Retrieves top 3 related news articles using NewsAPI
- Sends stock alerts and news summaries directly to your phone via SMS
- Uses environment variables for API key security

---

## Tech Stack

- Python 3
- Alpha Vantage API
- NewsAPI
- Twilio SMS API
- Requests
- python-dotenv

---

## Project Structure

```bash
.
├── main.py
├── twillo.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stock-news-alert.git
cd stock-news-alert
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:

```bash
pip install requests python-dotenv twilio
```

---

## API Setup

### Alpha Vantage API

Get your free API key from:

https://www.alphavantage.co/support/#api-key

### NewsAPI

Get your API key from:

https://newsapi.org/

### Twilio

Create a Twilio account and get:

- Account SID
- Auth Token
- Twilio phone number

https://www.twilio.com/

---

## Environment Variables

Create a `.env` file in the root directory:

```env
STK_PRICE_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_newsapi_key

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
TARGET_PHONE_NUMBER=your_personal_number
```

---

## How It Works

1. Fetches stock closing prices for the last two trading days
2. Calculates percentage difference
3. If stock changes more than ±5%:
   - Fetches latest news articles related to the company
   - Sends SMS updates to your phone

---

## Example SMS Output

```text
TSLA: 🔺5.2%

Headline: Tesla shares surge after earnings report
Brief: Tesla stock jumped after reporting stronger-than-expected quarterly revenue.

Headline: Elon Musk announces new AI plans
Brief: Tesla's CEO shared updates about the company's future AI roadmap.

Headline: EV market sees strong growth
Brief: Electric vehicle adoption continues to rise globally.
```

---

## Running the Project

```bash
python main.py
```

---

## Example Stock Configuration

```python
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

You can also track Indian stocks:

```python
STOCK = "TMPV.BSE"
COMPANY_NAME = "Tata Motors Passenger Vehicles"
```

---

## Notes

- Alpha Vantage free tier has request limits.
- NewsAPI free plan may have limited article access.
- Stock markets are closed on weekends and holidays, which may affect date calculations.

---

## Future Improvements

- Add support for multiple stocks
- Store historical alerts in a database
- Schedule automatic execution using cron jobs
- Add email notifications
- Deploy on cloud platforms like AWS or Render

---

## License

This project is licensed under the MIT License.

---

## Author

Made with ❤️ using Python
