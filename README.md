# 🤖 AI News Bot

A Python automation that scrapes Hacker News every morning, filters articles by topic, summarizes them using NLP, and delivers a clean briefing to Discord — automatically, every day at 6AM.

Built as my first AI automation project. No CS degree. Started from zero.

-----

## 📸 Demo

<img src="blob:chrome-untrusted://media-app/23c1bdfa-b812-4535-8aba-965cc58e91f7" alt="Screenshot 2026-03-27 6.45.12 PM.png"/><img width="1366" height="647" alt="image" src="https://github.com/user-attachments/assets/5c3a283a-34fc-4fb0-96e8-c03eaeafbdbb" />




-----

## 🧠 What It Does

1. **Scrapes** Hacker News for the latest headlines using BeautifulSoup
1. **Filters** articles by keywords relevant to AI, automation, and Python
1. **Summarizes** each article using NLP (LSA algorithm via Sumy)
1. **Delivers** the top 3 matches to a Discord channel via webhook
1. **Runs automatically** every morning at 6AM using a cron job — no manual input needed

-----

## ⚙️ How It Works

```
Hacker News → Python Scraper → Keyword Filter → NLP Summarizer → Discord
```

The script is scheduled with `cron` to run daily. Once set up, it runs completely hands-free.

-----

## 🛠️ Built With

|Tool           |Purpose          |
|---------------|-----------------|
|Python         |Core language    |
|BeautifulSoup  |HTML scraping    |
|Requests       |HTTP calls       |
|Sumy (LSA)     |NLP summarization|
|Discord Webhook|Delivery         |
|Cron           |Scheduling       |




