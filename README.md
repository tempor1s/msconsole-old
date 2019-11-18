<a href="https://www.google.com/search?q=twitter+icon&source=lnms&tbm=isch&sa=X&ved=0ahUKEwingJCUgvPlAhWYsp4KHWpXBVYQ_AUIEigB&biw=1440&bih=788#imgrc=4-NyAF10t5J6BM:"><img src="img/make.jpg" title="Makeschool Icon"></a>

makeBroots

## Description

Are you lazy and don't want to go to your dashboard and plug in the acccess token to make your attendance as present, welp here you go.
There is also a Brute force implementation of marking yourself present for the MakeSchool attendence tracker if you don't know the access code.

Never be marked tardy again! :)

![Word Generation](/static/img/gen.gif)

### Prerequisites

What things you need to install the software and how to install them

```bash
- brew
- python 3.4+
- pipenv
```

## Getting Started

The python modules were configured in a virtual enviornment with `pipenv`:

#### macOS Mojave 10.0+

```bash
# (if you have pipenv installed skip this step)
brew install pipenv
# clone repository
git clone https://github.com/imthaghost/makeBroot
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# start script
python3 broot.py
```

#### apt systems Ubuntu, Debian, Mint, Etc

```bash
# install pipenv
sudo pip install pipenv
# clone repository
git clone https://github.com/imthaghost/makeBroot
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# start script
python3 broot.py
```

This also assumes that you have `brew` installed. After cloning the repository in desired directory we run the command `pipenv shell` to initialize and activate our virtual enviornment. Unless specified pipenv will default to whatever virtualenv defaults to. We then allow pipenv to find and install the necessary modules for our server. All modules can be viewed inside the file `Pipfile` under the [packages] section.

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Built With

-   [Selenium](http://flask.palletsprojects.com/en/1.1.x/) - Web Browser Automation Tool

## Authors

-   **Gary Frederick** - _Initial work_ - [imthaghost](https://github.com/imthaghost)

See also the list of [contributors](https://github.com/imthaghost/makeBroot/contributors) who participated in this project.

## Acknowledgments

-   Hat tip to my professors [Meredith](https://github.com/neptunius) and [Danni](https://github.com/neptunius)
