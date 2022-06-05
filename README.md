<h1 align="center">linecord</h1>

all developers have non developers friends who use discord. this discord client is for those developers who prefer command line interfaces but still want to communicate with non-developer friends. 

ever since i started using vim instead of regular text editors such as sublime text or vs code, i fell in love with cli tools and prefer them to regular tools. yes, i know there are some discord cli clients out there, but a lot have been depricated and have bugs. 

this is why i, with the help of the opensource community (hopefully) will create a fully-functional and clean discord client.

<p align="center">
  <br>
  <img src="https://raw.githubusercontent.com/sababot/disline/master/docs/images/Screenshot%202022-06-04%20at%2019.55.37.png" />
</p>

# overview
linecord, the light, fast and small command line iterface discord client. disline uses [requests](https://pypi.org/project/requests/) to make [discord api](https://discord.com/developers/docs/reference) calls and [curses](https://docs.python.org/3/howto/curses.html) for the terminal user interface.

- [installation](#installation)
  - [pre-built binaries](#pre-built-binaries)
  - [from source](#from-source)
- [login](#login)
- [bugs](#bugs)
  - [known bugs](#known-bugs)

# installation
there are two ways of installing linecord; using prebuilt binaries or building from source:

### pre-built binaries
linecord will soon come to package managers such as apt, pacman and brew. however, for now you have to download the package from [releases](https://github.com/sababot/disline/releases)

### from source
first open up a terminal and clone this repository:

```
git clone https://github.com/sababot/disline.git
cd linecord
```

then install all the requirements:

```
sudo pip3 install requests curses
```

to run linecord

```
cd cli
python3 main.py
```

# login
currently, you can only login to linecord using your user token. see this [guide](https://github.com/Bios-Marcel/cordless/wiki/Retrieving-your-token) to find your user token or this [script](https://github.com/wodxgod/Discord-Token-Grabber) to scrape your user token from your computer.

soon email and password login will be implemented.

# bugs
in the early stages of the project, expect a lot of bugs, slowly, they will get fixed until we have an almost bugless client.

### known bugs
1. ```roles not shown in members section```

2. ```channels not indented```

3. ```ocasionally, the starting screen gets stuch```

### report
please feel free to report a bug by making an issue, and if you know how to fix it make pull request (hugely appreciated).
