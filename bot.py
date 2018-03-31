from aiotg import Bot, Chat
import aiohttp
import os
import re

URL_TEMPLATE = "https://docs.ansible.com/ansible/latest/modules/{}_module.html"
TITLE_REGEXP = r'<h1>(.+)<a class="headerlink"'

token = os.environ["TOKEN"]
assert token, "TOKEN env var is unset"

bot = Bot(api_token=token)

async def get_message(module):
    "Get ansible docs link and synopsis for module"
    try:
        session = aiohttp.ClientSession()
        url = URL_TEMPLATE.format(module)
        async with session.get(url, timeout=60) as response:
            if response.status == 404:
                return "No module '{}' found".format(module)
            content = await response.text()
            title = re.search(TITLE_REGEXP, content).group(1)
            return "{url}\n{title}".format(url=url, title=title)
    except Exception as e:
        return "Error occurred: {}".format(str(e))


@bot.command(r"/help (.+)")
async def echo(chat: Chat, match):
    module = match.group(1)
    message = await get_message(module)
    return chat.reply(message)

bot.run()
