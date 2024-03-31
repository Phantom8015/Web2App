import os
import time
import ssl
import json
import logging
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image


logging.basicConfig(level=logging.ERROR)
ssl._create_default_https_context = ssl._create_unverified_context

def main(url):
    validate = False
    url = url.strip()
    try:
        urlopen(url)
        validate = True
    except:
        validate = False
    if validate:
        with open('package.json', 'r') as file:
            data = json.load(file)

        data['url'] = url

        with open('package.json', 'w') as file:
            json.dump(data, file, indent=4)
        try:
            soup = BeautifulSoup(urlopen(url), features="html.parser")
            page = urlopen(url)
            soup = BeautifulSoup(page, features="html.parser")
            icon_link = soup.find("link", rel="shortcut icon")
            name = input("Would you like to automatically set the name of the app to the website's title? (y/n): ")
            if name.lower() == "y":
                name = soup.find("title").text
            else:
                name = input("Enter the name of the app: ")
                if name.strip() == "":
                    raise ValueError("Please enter a valid name!")
                elif name.isalpha() == False:
                    raise ValueError("Please enter a valid name!")
                elif name.isdigit() == True:
                    raise ValueError("Please enter a valid name!")
                else:
                    pass

            packagejson = "package.json"
            data = {}
            with open(packagejson, "r") as f:
                data = json.load(f)
                name = "".join(e for e in name if e.isalnum() or e.isspace()).replace(" ", "-")
                data["name"] = name
            with open(packagejson, "w") as f:
                json.dump(data, f, indent=4)

            if icon_link:
                icon_url = icon_link['href']
            else:
                icon_url = "https://static-00.iconduck.com/assets.00/electron-icon-472x512-8swdbwbh.png"
            try:
                icon = urlopen(icon_url)
                with open("icon.ico", "wb") as f:
                    f.write(icon.read())
                img = Image.open("icon.ico")
                img.save("icon.png", "PNG")
                imgu = Image.open("icon.png")
                imgu.resize((512, 512)).save("icon.png")

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
            
        print("\n\nThe desktop app for that website is about to run. Do not end the script. Test the app, then run ```npx electron-builder build``` in your terminal. \n\n")
        time.sleep(5)
        os.system("npm start")
    else:
        return "Please enter a valid URL!"

print(main(url=input("Enter a url: ")))
