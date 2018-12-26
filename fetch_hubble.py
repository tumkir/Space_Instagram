import requests


def download_image(url, filename):
    response = requests.get(url)
    with open(f"./images/{filename}", "wb") as f:
        f.write(response.content)


def get_file_extension(link):
    file_extension = link.split(".")[-1]
    return file_extension


def fetch_hubble_image_by_id(id):
    hubble_api_link = "http://hubblesite.org/api/v3/image/"
    hubble_response = requests.get(f"{hubble_api_link}{id}")
    hubble_json = hubble_response.json()
    hubble_image_link = hubble_json["image_files"][-1]["file_url"]
    download_image(hubble_image_link, f"{id}.{get_file_extension(hubble_image_link)}")


def fetch_hubble_image_by_collection(collection_name):
    hubble_api_link = "http://hubblesite.org/api/v3/images/"
    hubble_response = requests.get(f"{hubble_api_link}{collection_name}")
    hubble_json = hubble_response.json()
    for image_info in hubble_json:
        fetch_hubble_image_by_id(image_info["id"])
