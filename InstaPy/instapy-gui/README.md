<p align='center'>
	<h1 align="center">InstaPy GUI</h1>
	<p align="center">Graphical User Interface for <a href='https://github.com/timgrossmann/InstaPy'>InstaPy</a> Automation including some useful Analytics.<p>
	<p align="center">
		<a href="https://travis-ci.com/breuerfelix/instapy-gui">
		<img src="https://travis-ci.com/breuerfelix/instapy-gui.svg?branch=master">
		</a>
		<a href="https://discord.gg/FDETsht">
		<img src="https://img.shields.io/discord/510385886869979136.svg">
		</a>
		<a href="https://www.github.com/timgrossmann/InstaPy#backer">
		<img src="https://opencollective.com/instapy/backers/badge.svg">
		</a>
		<a href="https://www.github.com/timgrossmann/InstaPy#sponsors">
		<img src="https://opencollective.com/instapy/sponsors/badge.svg">
		</a>  
		<a href="https://github.com/breuerfelix/instapy-gui/blob/master/LICENSE">
		<img src="https://img.shields.io/github/license/breuerfelix/instapy-gui.svg" />
		</a>
	</p>
</p>

## installation

### requirements

* install [python 3](https://www.python.org/downloads/)
* sign up on [instapy.io](https://instapy.io)

### register a bot

#### windows-1-click-install

* download [update.bat](https://raw.githubusercontent.com/breuerfelix/instapy-gui/master/services/instapy/update.bat) and save it
  * you can copy your old assets folder into this folder aswell to reuse your database / cookies / etc.
* double-click `update.bat`
* double-click `setup.bat`
  * answer all the questions
* double-click `startingClient.bat` To take off!

#### linux/mac-1-click-install

* download [update.sh](https://raw.githubusercontent.com/breuerfelix/instapy-gui/master/services/instapy/update.sh) and save it
  * you can copy your old assets folder into this folder aswell to reuse your database / cookies / etc.
* execute `bash update.sh`
* execute `bash setup.sh`
  * answer all the questions
* execute `bash startClient.sh` To take off!

#### step-by-step guide

* download [all files here](https://github.com/breuerfelix/instapy-gui/tree/master/services/instapy) and save them to a folder on your system
  * you can copy your old assets folder into this folder aswell to reuse your database / cookies / etc.
* navigate to the folder in the console
* you should create a new python [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) because we use a modified InstaPy version
* run `pip install -r requirements.txt`
  * use `pip3` if you are on linux or mac
* create a file named `.env` or `instapy.env` with the following content

```env
INSTAPY_USER=instapy.io_username
INSTAPY_PASSWORD=instapy.io_password
IDENT=choose_any_name_to_indentify_this_instance
```

* run `python start.py`
  * use `python3` if you are on linux or mac
* go to [instapy.io](https://instapy.io) and take off!

##### adjustments for raspberry pi

* activate the virtual enviroment
* run following commands in the console

```bash
python3 -m pip uninstall instapy-chromedriver
python3 -m pip install --user instapy-chromedriver==2.36.post0
```

if this is not working try the following:

* cd into instpay-client folder

```bash
mkdir assets && cd assets
wget https://github.com/electron/electron/releases/download/v3.0.0-beta.5/chromedriver-v3.0.0-beta.5-linux-armv7l.zip
unzip chromedriver-v3.0.0-beta.5-linux-armv7l.zip
chmod 755 chromedriver
chmod +x chromedriver
sudo apt-get remove chromium
```

### register more bots

if you are on a different machine just follow the steps [register a bot](#register-a-bot) again.

* copy the whole client folder to a different folder
* edit `.env` or `instapy.env`
  * change `IDENT=...` to something new
* start the new client
* in the start panel of instapy.io you now have 2 bots in the select bot dropdown menu

## guides

### video tutorials

**[full manual installation on windows 10](https://drive.google.com/open?id=1ZafLOa0ShSXva61eQwFAePSVBC0Suc9p) by [@LexLinux](https://github.com/lexlinux)**  
**[1-click installation on windows 10](https://streamable.com/6h6d8) by [@HCWcoder](https://github.com/HCWcoder)**  
**[official instapy guide on udemy](https://www.udemy.com/instapy-guide/?couponCode=INSTAPY_OFFICIAL)**

## screenshots

![templates](docs/templates.png)  
![start](docs/start.png)

## roadmap

* edit name / description of template and setting
* copy template and setting from an existing one
* scheduler
* change account info
* forgot password
* analytics

## support

### do you need help ?

if you should encounter any issue, please first [search for similar issues](https://github.com/breuerfelix/instapy-gui/issues) and only if you can't find any, create a new issue or use the [discord channel](https://discord.gg/FDETsht) for help.

<a href='https://discord.gg/FDETsht'>
  <img hspace='3' alt='discord' src='https://camo.githubusercontent.com/e4a739df27356a78e9cae2e2dda642d118567e7c/68747470733a2f2f737465616d63646e2d612e616b616d616968642e6e65742f737465616d636f6d6d756e6974792f7075626c69632f696d616765732f636c616e732f32373039303534312f386464356339303766326130656563623733646336613437373666633961323538373865626364642e706e67' width=214/>
</a>

### do you want to support us ?

<a href="https://opencollective.com/instapy/donate" target="_blank">
  <img hspace="10" src="https://opencollective.com/instapy/contribute/button@2x.png?color=blue" width=300 />
</a>

---

_we love lowercase_
