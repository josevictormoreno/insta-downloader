import requests

class Images_Downloader:

    def __init__(self, url, file_name):
        self.file_name = file_name
        self.url = url

    def download_image(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.file_name, "wb") as f: 
                f.write(response.content)

        else:
            print(response.status_code)