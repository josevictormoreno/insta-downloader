##Download and gui / Instagram Downloader

## Author: José Victor Moreno
## Github: https://github.com/josevictormoreno

import instaloader 

instagram = instaloader.Instaloader()
user_profile = input('Enter the instagram id: ')

instagram.download_profile(user_profile, profile_pic_only=True)