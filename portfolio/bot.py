import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWdDd0J2EmmVshFolKTYOxGTffWQEQjDb5xQ&s"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  response = requests.get(url)



