## Setting up development environment

### Prerequisites

Must:
- [docker](https://docs.docker.com/get-docker/)

Optional:
- [vscode](https://code.visualstudio.com/Download) (with the following extentions)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
  - [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
- [cygwin](https://www.cygwin.com/) (to run `make` on Windows)

### Coding

> Use the [devcontainer](https://code.visualstudio.com/docs/remote/containers) feature of vscode to avoid messing up with the installation of python packages.

Start vscode, run the `Remote-Containers: Open Folder in Container...` command from the `Command Palette (F1)` or quick actions Status bar item, and select the project folder.

vscode will create a docker image and container with the Dockerfile in the root and attach to the the container.

### Debugging Flask app

1. Swith to the `Run and Debug` tab (`⇧⌘D` / `ctrl+shift+d`)
1. Run `Python: Flask`

### Debugging general Python script

1. Swith to the `Run and Debug` tab (`⇧⌘D` / `ctrl+shift+d`)
1. Run `Python: Current File`
1. (Interactive): Right click -> `Run Current File in Interactive Window`

### Start the `dev` sever locally

In cygwin/*nix termial (where `make` is installed):

``` sh
make up_dev
```

In PowerShell terminal (where `make` is unavailable):

``` bat
docker compose up -d web
```
