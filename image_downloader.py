import requests

class Images_Downloader:

    def __init__(self, url):
        self.file_name = 'download.png'
        self.url = url
        print(self.file_name)

    def download_image(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.file_name, "wb") as f: 
                f.write(response.content)

        else:
            print(response.status_code)