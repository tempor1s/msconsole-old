# Make Checkin

<img src="media/logo.png" title="Makeschool Icon"></a>

## Description

Are you lazy and don't want to go to your dashboard and plug in the acccess token to mark your attendance as present, well try Make Checkin.

![Success](/media/success.gif)

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

#### apt systems Ubuntu, Debian, Mint, Etc

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

This also assumes that you have `brew` installed. After cloning the repository in desired directory we run the command `pipenv shell` to initialize and activate our virtual enviornment. Unless specified pipenv will default to whatever virtualenv defaults to. We then allow pipenv to find and install the necessary modules for our server. All modules can be viewed inside the file `Pipfile` under the [packages] section.

## How to Run Script

It is essential that you are on the connected the `MakeStudent` SSID. (wifi) After installation and setup you can run the simple command as followed:

```bash
# replace code with your class code
python3 checkin.py <CODE>
# as followed
python checkin.py BRAVE
```

![Example](/media/example.gif)

After entering command you should see a message from the MakeSchool website in the CLI that notifies you what was returned.

## Making Executable File To Run As Single Command

#### macOS Mojave 10.0+

```bash
# make the python script executable
sudo chmod u+x checkin.py
# test to see if its an executable by running
./checking.py Test
# add the directory of where your script lives to your path
export PATH=/path/to/checkin.py:$PATH
# example
export PATH=~/scripts/checkin.py:$PATH
# If you want the command to be globally accessable in your shell, you'll have to export the path in .bashrc or .bash_profile.
# If you are using zsh it it would be the .zshrc file
vim .zshrc
# add the new path variable into the files
export PATH=$HOME/bin:/usr/local/bin:/path/to/checkin.py:$PATH
# you can see an example below
# we now need to globally installed the python modules used for this script
# install requests
pip3 install requests
# install lxml
pip3 install lxml
# we should now be able to run the checkin.py file from anywhere
checkin.py Test
# lets also make an alias to make it cleaner, open your shell configuration file .bashrc or .zshrc
vim .zshrc
# add the following line to make an alias to the command
alias checkin='checkin.py'
# see example below
```

![ZSH Example](/media/zsh.png)
![Alias Example](/media/alias.png)

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Built With

-   [Requests](https://2.python-requests.org/en/master/) - HTTP library
-   [lxml](https://lxml.de/) - XML and HTML parsing library
-   [Selenium](https://selenium.dev/) - Web Browser Automation for Visualization

## Authors

-   **Ben Lafferty** - _Initial idea / CLI implementation_ - [tempor1s](https://github.com/tempor1s)
-   **Gary Frederick** - _Initial work_ / _Server Calls_ - [imthaghost](https://github.com/imthaghost)

See also the list of [contributors](https://github.com/tempor1s/make-checkin/contributors) who participated in this project.
