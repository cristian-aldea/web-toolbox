# web-toolbox

Web-toolbox is a boilerplate project for developing a simple and modern static website with TypeScript, SCSS and HTML.

It provides basic configuration and assets, and is meant to be paired with your build tooling of choice.

It's currently tuned for use with [Vite](https://vitejs.dev/), but this might change in the future.

## Setup

To get started, first create your new project. Then, add web-toolbox as a git submodule:

```bash
git submodule add -b main https://github.com/cristian-aldea/web-toolbox.git
```

Run the setup script, making sure you have a clean git working tree:

```bash
# in root dir of your new project
python web-toolbox/setup.py
```

Install the required packages for linting, as described at: <https://typescript-eslint.io/docs/linting/>

```bash
npm install --save-dev eslint typescript @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-config-prettier
```

Install sass:

```bash
npm install --save-dev sass
```

Finally, setup a script to run the linting:

```json
{
  "scripts": {
    "lint": "eslint ./src/ --ext .js,.jsx,.ts,.tsx"
  }
}
```

## Updates

To update the web-toolbox from within your project, run:

```bash
cd web-toolbox
git checkout main
git pull
```

you can then rerun the setup script to get the latest configuration
