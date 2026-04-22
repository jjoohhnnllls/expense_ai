import re
from datetime import datetime


##parse text input by user
def parse_expense(text):
    text = text.lower()

    # Extract amount (number)
    amount_match = re.search(r'\d+(\.\d+)?', text)
    amount = float(amount_match.group()) if amount_match else None

    # Simple category detection
    categories = ["food", "transport", "shopping", "entertainment", "other"]

    category = "other"
    for cat in categories:
        if cat in text:
            category = cat
            break

    # Default date = today
    date = datetime.today().strftime('%Y-%m-%d')

    return {
        "amount": amount,
        "category": category,
        "date": date,
        "note": text
    }

#################################################################################
# explanation

# INPUT
#"Spent 15 on food"

# OUTPUT
#{
#  amount: 15,
#  category: "food",
#  date: "2026-04-22",
#  note: "spent 15 on food"
#}
#################################################################################