import requests
import json
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import os

# Discord webhook URL
webhook_url = os.getenv("WEBHOOK_URL")

# Get URLs and price thresholds from environment variable
urls_json = os.getenv("URLS_JSON")
urls_data = json.loads(urls_json)

for url_data in urls_data:
    url = url_data["url"]
    price_threshold = url_data["price_threshold"]

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the price value
    price = float(soup.select_one("div.price__current  span.money").text.replace("£", ""))  # Remove currency symbol and convert to float

    # Check if the price is less than threshold
    if price <= price_threshold:
        # Create a message with the price and the URL
        message = f"Price: {price}\nURL: {url}"

        # Create a Discord webhook object
        webhook = DiscordWebhook(url=webhook_url, content=message)

        # Send the message to the Discord webhook
        webhook.execute()
