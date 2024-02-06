<div align="center" markdown="1">

<img src="./docs/pictures/microservice-auth_logo_bg-grey.png" alt="Microservice Auth Logo" width="300"/>

</div>

# Microservice Auth

<div align="center" markdown="1">

[![GitHub repo license](https://img.shields.io/github/license/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=License)](https://www.gnu.org/licenses/gpl-3.0.fr.html)&#160;
[![GitHub repo forks](https://img.shields.io/github/forks/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Forks)](https://github.com/Empire-of-Minds/microservice-auth/network)&#160;
[![GitHub repo stars](https://img.shields.io/github/stars/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Stars)](https://github.com/Empire-of-Minds/microservice-auth/stargazers)&#160;
[![GitHub repo contributors](https://img.shields.io/github/contributors-anon/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Contributors)](https://github.com/Empire-of-Minds/microservice-auth/graphs/contributors)&#160;
[![GitHub repo size](https://img.shields.io/github/repo-size/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/Empire-of-Minds/microservice-auth/archive/refs/heads/main.zip)

</div>

## Quick Introduction

Microservice Auth is a simple and lightweight microservice that provides authentication and authorization functionalities. It is designed to be used in a microservices architecture. It is based on the OAuth2 protocol and JWT tokens.

## Table of Contents

- [Quick Introduction](#quick-introduction)
- [Table of Contents](#table-of-contents)

## Project Description

Microservice Auth is a simple and lightweight microservice that provides authentication and authorization functionalities. It is designed to be used in a microservices architecture. It is based on the OAuth2 protocol and JWT tokens.

It is written in _Python_ and uses the **FastAPI** framework. It uses the `python-jose` library to handle **JWT** tokens and the `passlib` library to handle password hashing.

## Development

<div align="center" markdown="1">

[![GitHub repo last commit](https://img.shields.io/github/last-commit/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Last%20Commit)](https://github.com/Empire-of-Minds/microservice-auth/graphs/commit-activity)&#160;
[![GitHub repo issues](https://img.shields.io/github/issues/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Issues)](https://github.com/Empire-of-Minds/microservice-auth/issues)&#160;
[![GitHub repo pull requests](https://img.shields.io/github/issues-pr/Empire-of-Minds/microservice-auth?style=flat&logo=github&logoColor=whitesmoke&label=Pull%20Requests)](https://github.com/Empire-of-Minds/microservice-auth/pulls)

</div>

### How to Install

#### Requirements

- [Git](https://git-scm.com) : Git is a distributed version-control system for tracking changes in source code during software development.
- [Cocogitto](https://docs.cocogitto.io) : Cocogitto is a tool that checks the commit messages and prevents you from pushing commits that do not follow the conventional commits guidelines. You can install it by following the instructions on their [GitHub repository](https://github.com/cocogitto/cocogitto?tab=readme-ov-file#installation).
- [Docker](https://docs.docker.com) : Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
- [Docker Compose V2](https://docs.docker.com/compose/) : Compose is a tool for defining and running multi-container Docker applications (If you are using Docker Desktop, you already have Docker Compose V2).
- [Taskfile](https://taskfile.dev) : Taskfile is a task runner / simpler Make alternative written in Go. You can install it by following the instructions on their [Website](https://taskfile.dev/installation).

- [VSCode](https://code.visualstudio.com) : Visual Studio Code is a source-code editor made by Microsoft for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.
  <br>
  We're using the [Dev Container](https://code.visualstudio.com/docs/remote/containers) feature of VSCode to develop inside a containerized environment. This allows us to have a consistent development environment across all developers and to avoid the "_It works on my machine_" problem.
  - All extensions that you will need outside of the container are listed in the [`.vscode/extensions.json`](.vscode/extensions.json) file. You can install them by clicking on the "**_Install recommended extensions_**" button that will appear in the bottom right corner of your screen when you open the in VSCode.
  - All extensions that you will need inside of the container are listed in the [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json) file. You don't need to install them, they will be automatically installed when you open the project in VSCode with the Dev Container feature. Use the "**_Reopen in Container_**" button that will appear in the bottom right corner of your screen when you open the project in VSCode or by using the command palette (`Ctrl+Shift+P`) and typing "**_Dev Container: Reopen in Container_**".

### Installation

#### Clone the repository

Register your SSH key in your GitHub account and clone the repository :

> [!NOTE]
> Please use the SSH link since it is more secure than the HTTPS link.

```bash
git clone git@github.com:Empire-of-Minds/microservice-auth.git
```

and go to the project directory before switching to the `staging` branch:

```sh
cd microservice-auth && git switch staging
```

This project uses conventional commits to manage the versioning of the project. You can find more information about conventional commits [here](https://www.conventionalcommits.org/en/v1.0.0/).

In order to enforce conventional commits, we use **_[cocogitto](https://docs.cocogitto.io)_** which is a tool that checks the commit messages and prevents you from pushing commits that do not follow the conventional commits guidelines.

> [!NOTE]
> Once you have installed **_cocogitto_**, you will have to run the command `cog install-hook` in the root directory of the project to install the hook that will check your commits.

If you don't want to install **_cocogitto_**, you can still use this repository but you will have to manually check that your commits follow the conventional commits guidelines or you can use the VSCode extension [Conventional Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits) which will help you write conventional commits.

#### Environment variables

Use the `task` command to create the `.env` files :

```sh
task project:init-env
```

#### Build the Docker images and start the containers

Use the `task` command to build the Docker images and start the containers :

```sh
task docker:build docker:up
```

#### Start developing

You can now start developing inside the containerized environment by opening the project in **VSCode**.

1. Open the project in VSCode with the `code .` command.

2. Install the extensions listed in the [`.vscode/extensions.json`](.vscode/extensions.json) file by clicking on the "**_Install recommended extensions_**" button that will appear in the bottom right corner of your screen when you open the project in VSCode.

3. Use the "**_Reopen in Container_**" button that will appear in the bottom right corner of your screen when you open the project in VSCode or by using the command palette (`Ctrl+Shift+P`) and typing "**_Dev Container: Reopen in Container_**".

4. You can now start developing inside the containerized environment.

### How to Contribute

If you want to contribute to this repository, you can do so by creating a pull request. However, before creating a pull request, please make sure that your contribution is relevant and that it does not break anything.
