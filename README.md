# MS Console

<img src="media/make_logo_new.png" title="Makeschool Icon"></a>

## Description

A suite of tools that makes your MakeSchool life easier!

![Success](/media/success.gif)

### Prerequisites

What things you need to install the software and how to install them

```bash
- Homebrew
or
- Pipenv
- Python 3.4+
```

## Getting Started

### Homebrew

```bash
# tap the repo
brew tap tempor1s/msconsole https://github.com/tempor1s/msconsole
# install the CLI tool
brew install msconsole
# get a list of all the commands
ms
# checkin command example
ms checkin BRAVE
```

After running the checkin command and you sign in you should see a message from the MakeSchool website in the CLI that notifies you what was returned.

![Checkin](/media/checkin.gif)

### Non-Brew Users

```bash
# install pipenv
sudo pip install pipenv
# clone repository
git clone https://github.com/tempor1s/msconsole
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# change your directory to `checkin`
cd msconsole
# test the script - should return a list of all available commands
python3 main.py
# example - this should check you into your MakeSchool class
python3 main.py checkin <CODE>
```

After running the checkin command and you sign in you should see a message from the MakeSchool website in the CLI that notifies you what was returned.

![Example](/media/example.gif)

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Built With

-   [Requests](https://2.python-requests.org/en/master/) - HTTP library
-   [lxml](https://lxml.de/) - XML and HTML parsing library
-   [keying](https://pypi.org/project/keyring/) - For storing credentials in Keychain

## Authors

-   **Ben Lafferty** - _Initial idea / CLI implementation_ - [tempor1s](https://github.com/tempor1s)
-   **Gary Frederick** - _Initial work_ / _Server Calls_ - [imthaghost](https://github.com/imthaghost)
-   **Tasfia Addrita** - _Calendar_ - [TasfiaAddrita](https://github.com/TasfiaAddrita)

See also the list of [contributors](https://github.com/tempor1s/msconsole/contributors) who participated in this project.
