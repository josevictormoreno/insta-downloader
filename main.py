##Download and gui / Instagram Downloader

## Author: José Victor Moreno
## Github: https://github.com/josevictormoreno

from turtle import down
import insta_profile as instagram 
import image_downloader as image

op = input('Instagram Profile (s/n): ')

if op == 's':
    user_profile = input('Enter the instagram id: ')

    download = instagram.Profile_downloader(user_profile)
    download.downloads_profile()

else:
    image_url = input('Enter the image url: ')
    download = image.Images_Downloader(image_url)
    download.download_image()

