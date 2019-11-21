# Make Checkin

<img src="media/make_logo_new.png" title="Makeschool Icon"></a>

## Description

Are you lazy and don't want to go to your dashboard and plug in the acccess token to mark your attendance as present, well try Make Checkin.

![Success](/media/success.gif)

### Prerequisites

What things you need to install the software and how to install them

```bash
- Homebrew
or
- Pipenv
```

## Getting Started

### Homebrew

This also assumes that you have Homebrew installed on your system.

```bash
# Tap the repo
brew tap tempor1s/make-checkin https://github.com/tempor1s/make-checkin
# Install the CLI tool
brew install makecheckin
# Checkin to your class!
checkin <CODE>
# example
checkin BRAVE
```

After entering the command you should see a message from the MakeSchool website in the CLI that notifies you what was returned.

![Checkin](/media/checkin.gif)

### Non-Brew Users

```bash
# install pipenv
sudo pip install pipenv
# clone repository
git clone https://github.com/tempor1s/make-checkin
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# start script
python3 checkin.py <CODE>
# example
python3 checkin.py BRAVE
```

After entering the command you should see a message from the MakeSchool website in the CLI that notifies you what was returned.

![Example](/media/example.gif)

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Built With

-   [Requests](https://2.python-requests.org/en/master/) - HTTP library
-   [lxml](https://lxml.de/) - XML and HTML parsing library

## Authors

-   **Ben Lafferty** - _Initial idea / CLI implementation_ - [tempor1s](https://github.com/tempor1s)
-   **Gary Frederick** - _Initial work_ / _Server Calls_ - [imthaghost](https://github.com/imthaghost)

See also the list of [contributors](https://github.com/tempor1s/make-checkin/contributors) who participated in this project.
