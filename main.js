const electron = require('electron');
const url = require('url');
const path = require('path');

const{app, BrowserWindow, Menu} = electron; 
let mainWindow; 

app.on('ready', function() {
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol:'file',
        slashes: true
    }));

    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    Menu.setApplicationMenu(mainMenu);
    
});

function createNewArticleWindow() {
    newsarticleWindow = new BrowserWindow({
        width: 400,
        height: 200,
        title: 'News Article Analyzer'
    });
    newsarticleWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'newsarticle.html'),
        protocol:'file',
        slashes: true
    }));
}

const mainMenuTemplate = [
    {
        label:'News Articles',
        click(){
            createNewArticleWindow(); 
        }
    }, {
        label:'Articles'
    }, {
        label:'Tweets'
    },  {
        label:'Chats'
    },  {
        label:'Email'
    },  {
        label:'Help'
    }
];