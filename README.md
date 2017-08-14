# Optimizely Internal App Boilerplate for Google App Engine
This repo is meant to be used as a quick-start template for internal apps at Optimizely. Google App Engine's strengths include easy to setup user authentication and company billing. If you're leaning against wanting to use GAE, the creation of boilerplates for comparable frameworks like AWS and Heroku is encouraged - please feel free to link to them here and use a similar repo name format if you take that route. Here are the technologies included in this template:

* React.js
* Node Packet Manager
* Babel 6
* Webpack
* Python

## Installing the Google Cloud SDK
1. Download the newest version for your computer at https://cloud.google.com/sdk/downloads
2. Put unzipped file in `/usr/local/`, so the path is `/usr/local/google-cloud-sdk`
3. Run `/usr/local/google-cloud-sdk/install.sh` (installs gcloud)
4. Run `/usr/local/google-cloud-sdk/bin/gcloud init` (sets up gcloud authentication and lets you pick default project)
5. Run `ln -s /usr/local/google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud` (makes a command line top-level shortcut to gcloud so you don't have to run the entire path)
6. Run `sudo gcloud components install app-engine-python`, and enter your password

## Setting up locally
1. Clone or fork this repo
2. Run `touch credentials.yaml` (this is included in the .gitignore and can be used for sensitive credentials)\*
3. Run `npm run install` to make sure your packages are up to date\*

## Running locally
1. Start the local server with `dev_appserver.py .`\*
2. In a new shell, run `npm run dev` to watch for changes or build once with `npm build`\*

NOTE: You may need to run `npm install babel-core -s` if you get a "babel-core" error\*

## Using third-party Python libraries
1. Update or add to requirements.txt
2. From the root of the repo, run `pip install -t lib -r requirements.txt`

Read more about about installing third-party python libraries [here](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27)...

\* = Run these commands from the repo's root directory.

## Config.yaml
Config.yaml is where you can add configurable settings to your app. For instance, designating which email domain is allowed to access the app once signed into Google.

## Miscellaneous
- [Really great npm, webpack, babel, react setup tutorial](https://www.codementor.io/tamizhvendan/beginner-guide-setup-reactjs-environment-npm-babel-6-webpack-du107r9zr)
