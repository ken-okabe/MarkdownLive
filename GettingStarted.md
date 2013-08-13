#MarkdownLive
###Markdown Streaming Live View for SublimeText3
---
![](https://lh5.googleusercontent.com/-ZqBkq4KHjKs/UgbOLxXUjpI/AAAAAAAAEfA/KhP7SOaTsOg/w914-h514-no/markdownSS.png)

##Requirements

- MacOSX / Linux / Windows
- Sublime Text 3
- node.js >= 0.10.0

##Getting Started

- Open Menu: **Sublime Text > Preferences > Browse Packages ...**

- Open Terminal at the directory

```
$          [~/Library/Application Support/Sublime Text 3/Packages]
```
- Git Clone

```
git clone https://github.com/kenokabe/MarkdownLive
```
- Go down to newly created directory 

```
cd MarkdownLive
$          [~/Library/Application Support/Sublime Text 3/Packages/MarkdownLive]
```
- Construct the directory for node server app dependencies with `npm` tool

```
npm install
```
- Launch or Restart SublimeText3 or
`MarkdownLive: Reload Server` from SublimeText Command

-  Open a WebBrowser=> localhost:9999
Firefox is recommended since Safari&Chrome(Webkit engine) has some rattling when HTML is rendered.

- Open a markdown file to edit


>If the node server is faled to launch, you might need to specify the direct path to the node binary; 
Open 
**.../Packages/MarkdownLive/nodePath.cfg**
>If the node path is
YourHomeDir/.nvm/v0.10.15/bin/node
Specify:
```.nvm/v0.10.15/bin/node```


