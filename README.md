# Automate Lead Categorization and Slack Alerts using Make.com

This workflow automatically analyzes email replies using GPT-4 and sends categorized alerts to Slack.  
I built this as a fresher to learn how Make.com connects multiple tools without writing full custom code.

---

## What this workflow does

1. **Listens for email replies** – When a new reply arrives, Make.com receives it automatically.  
2. **Asks GPT-4 to read it** – The AI decides whether it’s *Positive*, *Not Interested*, or an *Unsubscribe* request.  
3. **Extracts just the category** – Converts the AI output into clean JSON data.  
4. **Notifies Slack instantly** – Posts a short message in the sales channel with lead info and classification.  

---

## Why I built this

- I wanted to understand how automation platforms like Make.com save manual work.  
- As a beginner, connecting GPT-4 + Slack taught me real-world use cases without needing advanced programming.  
- This project shows I can combine no-code automation with some coding logic when needed.  

---

## Tools used

- **Make.com** — automation workflow builder  
- **OpenAI GPT-4** — AI model for classifying replies  
- **Slack API** — sends instant team alerts  

---

## Real-world example

If you send 200 cold emails a day, it’s tough to check each reply manually.  
This workflow instantly tells your team which replies are positive leads,  
so they can follow up faster.

---

## Files included

- `Slack-Alerts-using-Make.com.json` – cleaned Make.com workflow export  
- `helper.py` – simple Python script to test email categorization logic locally  
- `Slack-Alerts-using-Make.com.png` – screenshot showing Slack alert example  

---

## How to use

1. Import `lead_categorization_slack.json` into Make.com.  
2. Replace connections (`areeshausmani93_connection`) with your own Slack and OpenAI credentials.  
3. Run the scenario — every new email reply will be analyzed and sent to Slack automatically.  
