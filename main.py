import os
import pathlib
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_image_by_collection
from dotenv import load_dotenv
from instabot import Bot


def upload_images():
    bot = Bot()
    bot.login(username=os.getenv("login"), password=os.getenv("password"))
    all_images = os.listdir("images")
    jpg_to_upload = ["images/" + image for image in all_images if image.endswith(".jpg")]
    for image in jpg_to_upload:
        bot.upload_photo(image)


if __name__ == '__main__':
    load_dotenv()
    pathlib.Path("images").mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_hubble_image_by_collection("printshop")
    upload_images()
