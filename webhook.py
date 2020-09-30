import requests #dependency
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('DISCORD_WEBHOOK_URL')

data = {}
#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data["content"] = "message content"
data["username"] = "custom username"

#leave this out if you dont want an embed
data["embeds"] = []
embed = {}
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
embed["description"] = "text in embed"
embed["title"] = "embed title"
data["embeds"].append(embed)

result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))