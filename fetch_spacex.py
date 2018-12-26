import requests


def download_image(url, filename):
    response = requests.get(url)
    with open(f"./images/{filename}", "wb") as f:
        f.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    spacex_response = requests.get(url)
    spacex_json = spacex_response.json()
    spacex_image_links = spacex_json["links"]["flickr_images"]
    for picture_number, link in enumerate(spacex_image_links):
        spacex_picture_filename = f"spacex{picture_number + 1}.jpg"
        download_image(link, spacex_picture_filename)
