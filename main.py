# Download and gui / Instagram Downloader

# Author: José Victor Moreno
# Github: https://github.com/josevictormoreno
import insta_profile as instagram
import image_downloader as image
import PySimpleGUI as sg
import os

sg.theme('Material1')
layout = [[sg.Text('Paste image link or username here...')],
          [sg.Text('URL/user: '), sg.InputText()],
          [sg.Checkbox('Profile Image', default=False, key='is_profile')],
          [sg.Button('Download', key='download'), sg.Button('Cancel')],
          [sg.Output(size=(40, 2))]]

window = sg.Window('Image downloader', layout)

while True:
    event, values = window.read()
    image_link = values[0]
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    is_profile = values['is_profile']
    if is_profile == True:
        download = instagram.Profile_downloader(image_link)
        download.downloads_profile()
    else:
        download = image.Images_Downloader(image_link)
        download.download_image()
    print('Download Complete!')

window.close()
