<h1 align="center">Welcome to msConsole 👋</h1>
<img src="docs/media/make_logo_new.png" title="Makeschool Icon"></a>
<p>
 <a href="https://github.com/tempor1s/msconsole/commits/master">
    <img alt="commits" src="  https://img.shields.io/github/contributors/tempor1s/msconsole" target="_blank" />

  </a>
    <a href="https://github.com/tempor1s/msconsole/commits/master">
    <img alt="commits" src="https://img.shields.io/github/commit-activity/w/tempor1s/msconsole?color=green" target="_blank" />

  </a> 
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
   <a href="https://github.com/imthaghost/gitmoji-changelog">
    <img src="https://img.shields.io/badge/changelog-gitmoji-brightgreen.svg" alt="gitmoji-changelog">
  </a>
  
</p>

> A suite of tools that makes your MakeSchool life easier!

### Prerequisites

What things you need to install the software and how to install them

```bash
- Homebrew
or
- Pipenv
- Python 3.4+
```

## 🚀 Getting Started

### Homebrew

```bash
# tap the repo
brew tap tempor1s/msconsole https://github.com/tempor1s/msconsole
# install the CLI tool
brew install msconsole
# get a list of all the commands
ms
```

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
# change your directory to `msconsole`
cd msconsole
# test the script - should return a list of all available commands
python3 main.py
```

## To Do

-   [x] Restructure to fit modular style
-   [x] Better file and script organization
-   [ ] Complete meet module
-   [ ] Complete console module
-   [ ] Complete library module
-   [ ] Create Makschool Ascii Banner
-   [x] Restructure checkin module into module folder
-   [x] Refactor utils into a folder with different scripts
-   [x] Refactor utils file into multiple files for better scaling
-   [ ] Refactor checkin credentials so that they are used application-wide (maybe login as well)

## Built With

-   [Requests](https://2.python-requests.org/en/master/) - HTTP library
-   [lxml](https://lxml.de/) - XML and HTML parsing library
-   [keying](https://pypi.org/project/keyring/) - Storing and accessing passwords library
-   [clint](https://pypi.org/project/clint/) - Suite of tools for developing CLI applications.
-   [docopt](http://docopt.org/) - For making our CLI beautiful :)

# Contribution Guidlines

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

-   Reporting a bug
-   Discussing the current state of the code
-   Submitting a fix
-   Proposing new features
-   Becoming a maintainer

## We Develop with Github

We use github to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests

Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests:

1. Fork the repo and create your branch from `master`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/briandk/transcriptase-atom/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](); it's that easy!

## Write bug reports with detail, background, and sample code

[This is an example](http://stackoverflow.com/q/12488905/180626) of a bug report I found, and I think it's not a bad model. Here's [another example from Craig Hockenberry](http://www.openradar.me/11905408), an app developer whom I greatly respect.

**Great Bug Reports** tend to have:

-   A quick summary and/or background
-   Steps to reproduce
    -   Be specific!
    -   Give sample code if you can. [My stackoverflow question](http://stackoverflow.com/q/12488905/180626) includes sample code that _anyone_ with a base R setup can run to reproduce what I was seeing
-   What you expected would happen
-   What actually happens
-   Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People _love_ thorough bug reports. I'm not even kidding.

## Use a Consistent Coding Style

I'm again borrowing these from [Facebook's Guidelines](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md)

-   4 spaces for indentation rather than tabs (or tabs that convert to spaces)
-   You can try running `pipenv install autopep8 --dev` for style unification

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/imthaghost"><img src="https://avatars3.githubusercontent.com/u/46610773?s=460&v=4" width="75px;" alt="Gary Frederick"/><br /><sub><b>Tha Ghost</b></sub></a><br /><a href="https://github.com/tempor1s/msconsole/commits?author=imthaghost" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/tempor1s"><img src="https://avatars3.githubusercontent.com/u/29741401?s=460&v=4" width="75px;" alt="Ben Lafferty"/><br /><sub><b>Ben Lafferty</b></sub></a><br /><a href="https://github.com/tempor1s/msconsole/commits?author=tempor1s" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/tasfiaaddrita"><img src="https://avatars3.githubusercontent.com/u/5863693?s=460&v=4" width="75px;" alt="Tasfia"/><br /><sub><b>Tasfia Addrita</b></sub></a><br /><a href="https://github.com/tempor1s/msconsole/commits?author=TasfiaAddrita" title="Code">💻</a></td>
  </tr>
