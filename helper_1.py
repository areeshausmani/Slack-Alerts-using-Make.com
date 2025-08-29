# helper.py
# Author: areeshausmani93@gmail.com
# This is a small helper script to test email categorization locally

import json

def categorize_email(reply_text):
    # very simple logic to simulate GPT-4 classification
    reply_lower = reply_text.lower()
    if "stop" in reply_lower or "unsubscribe" in reply_lower:
        return "Unsubscribe"
    elif "not interested" in reply_lower or "no thanks" in reply_lower:
        return "Not Interested"
    else:
        return "Positive"

# test data
sample_replies = [
    "Hey, this looks great!",
    "No thanks, not interested.",
    "Please stop emailing me."
]

for reply in sample_replies:
    print(json.dumps({"reply": reply, "category": categorize_email(reply)}, indent=2))
