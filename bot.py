from aiotg import Bot, Chat

token = os.environ["TOKEN"]
assert token, "TOKEN env var is unset"

bot = Bot(api_token=token)

@bot.command(r"/help (.+)")
def echo(chat: Chat, match):
    return chat.reply(match.group(1))

bot.run()
