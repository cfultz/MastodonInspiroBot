import json
import time
import requests
import logging
import inspirobot
from mastodon import Mastodon


# Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://cfultz.com'
)

# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

# Get Quote
logger.info("Getting Inspired")
time.sleep(3)
quote = inspirobot.generate() 
print(quote.url)

# Download Images
url = quote.url
response = requests.get(url)
if response.status_code == 200:
    with open("created_image.jpg", 'wb') as f:
        f.write(response.content)

# Toot Toot
media = mastodon.media_post("created_image.jpg")
logger.info("tooting inspiration")

mastodon.status_post("#inspirobot #AI",media_ids=media)
