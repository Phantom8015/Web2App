const { app, BrowserWindow } = require('electron');
const p = require('./package.json');

function createWindow() {
    const win = new BrowserWindow({
        width: 1920,
        height: 1080,
        webPreferences: {
            nodeIntegration: true
        },
        icon: __dirname + './icon.png',
        title: "Loading..."
    });
    win.setMenuBarVisibility(false);
    win.webContents.on('before-input-event', (event, input) => {
        if (input.control && input.shift && input.key.toLowerCase() === 'arrowleft') {
            win.webContents.goBack();
        } else if (input.control && input.shift && input.key.toLowerCase() === 'arrowright') {
            win.webContents.goForward();
        }
    });
    win.webContents.on('new-window', (event, url) => {
        event.preventDefault();
        win.loadURL(url);
    });

    win.loadURL(p.url);
}

app.whenReady().then(createWindow);
