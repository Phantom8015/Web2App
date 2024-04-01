# Web2App
## Requirements
- NodeJS 21.7.1+ & NPM 10.5.0+
- Python 3.12.2+ & Pip 24+
## Description
Web2App is a tool that converts a website into a desktop application. It allows you to create standalone applications for your favorite websites, enabling easier access and a more integrated experience.

## Installation
To initialize the Web2App repository, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the initialization script:
   - For Unix/Linux/MacOS: `./init.sh`
   - For Windows: `init.bat`

## Usage
Once the repository is initialized, you can convert a website into a desktop application by following these steps:
1. Ensure that the initialization process has completed successfully.
2. Run the `main.py` script:
   ```bash
   python main.py
   ```
3. When prompted, enter the URL of the website you want to convert.
4. Follow the on-screen instructions to customize the application settings.
5. After completing the setup, the desktop application for the specified website will be generated.
6. Once generated the web app shall run. Once it is ran, follow the on-screen instructions to have it built in a valid application for your operating system.
7. To navigate between pages on your web app (Mac or Windows) press Control Shift and the Left or Right arrow key.

### Common problems
1. Error during building: [ERR_ELECTRON_BUILDER_CANNOT_EXECUTE](https://github.com/electron-userland/electron-builder/issues/5134)
2. Default electron icon after building. Caused by errors in getting your website's icon.
3. Code isn't signed. A common problem faced when distributing your app. The MacOS builder automatically skips signing as it requires the $100 Apple Developer Fee.
4. Any other problems, please create an issue in the issues tab. 
  
  
  
## License
This project is licensed under the [MIT License](LICENSE).

## Disclaimer
Web2App is provided as-is without any warranty. Use it at your own risk.
