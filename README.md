# Python Strenghshop Discord Notifier

With the help of Youtube and ChatGPT I put together a discord bot that would notify me if the price of an item I am looking at changes below a certain value.

## Usage

1. get url of Strenghshop item you want to look at
2. get your discord webhook url
3. update the .env.example and rename to .env
4. run `docker compose up -d`

```
# Replace the urls in the URLS_JSON with the url you want to look for and the value in the thresholds to what price you want to be notified when it goes below.

```

## Development

```
python3 -m venv ~/.python-strenghshop-discord-notifyer
source ~/.python-strenghshop-discord-notifyer/bin/activate
pip install --upgrade pip && pip install -r requirements.txt

export WEBHOOK_URL=your-discord-webhook-here
export URLS_JSON='[{"url": "https://www.example.com/product1", "price_threshold": 100.00}, {"url": "https://www.example.com/product2", "price_threshold": 150.00}, {"url": "https://www.example.com/product3", "price_threshold": 200.00}]'


# Deactiveage and Clean up venv

deactivate

rm -r ~/.python-strenghshop-discord-notifyer

```
