
# Author: José Victor Moreno
# Github: https://github.com/josevictormoreno

import instaloader 

class Profile_downloader:
    
    def __init__(self, profile):
        self.profile = profile 

    def downloads_profile(self):
        instagram = instaloader.Instaloader()
        instagram.download_profile(self.profile, profile_pic_only=True)