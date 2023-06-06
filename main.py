import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook#
import os

# URL to scrape
url = os.getenv("URL")

# Discord webhook URL
webhook_url = os.getenv("WEBHOOK_URL")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the price value
price = float(soup.select_one("div.price__current  span.money").text.replace("£", ""))  # Remove currency symbol and convert to float

# Check if the price is less than 218.00
if price < 218.00:
    # Create a message with the price and the URL
    message = f"Price: {price}\nURL: {url}"

    # Create a Discord webhook object
    webhook = DiscordWebhook(url=webhook_url, content=message)

    # Send the message to the Discord webhook
    webhook.execute()
