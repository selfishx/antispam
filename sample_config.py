from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


if DEPLOYING_ON_HEROKU := True:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")
else:
    BOT_TOKEN = "123456:qwertyuiopasdfghjklzxcvbnm"
    SUDOERS = [1243703097]
    NSFW_LOG_CHANNEL = -1001470187101
    SPAM_LOG_CHANNEL = -1001554591017
    ARQ_API_KEY = ""  # Get it from @ARQRobot
