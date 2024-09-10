# 🧩 PLUGINS-LAB: PLUG IT LIKE IT'S HOT! 🔥

Welcome to the **PLUGINS-LAB**! 🎉 This is where we turn boring old code into dynamic, flexible, and insanely modular applications using plugins and autodiscovery. From Click command line tools to FastAPI web magic, this lab is all about making your code do the hard work for you. 😎

## What's the Big Deal? 🤔

Why plugins? Why autodiscovery? Simple:

- **Modularity**: Keep your code clean, organized, and reusable.
- **Scalability**: Easily extend your apps without touching the core code.
- **Fun**: Who doesn't love a good experiment? 🔬

In this lab, we're testing out all the crazy, genius, and maybe slightly absurd ways to make our Click and FastAPI apps discover plugins automatically—because life's too short for static code! 🚀

## What We're Cooking Up 🧑‍🍳

Here's what you'll find (and what we're tinkering with) inside this folder:

- **Click Commands**: Auto-magically discoverable commands that bring power to your terminal!
- **FastAPI Extensions**: Dynamic API endpoints that just show up without lifting a finger. 🪄
- **Namespace Packages**: Because sharing is caring, even when it's code.
- **Machine Learning Models**: Integrate ML models seamlessly with both CLI and API through autodiscovery.

## Project Structure 🏗️

We’ve created a project named **Modulus** that's machine learning-oriented, using the `modulus` namespace. Here's how we're organizing things:

- **API Project**: A dedicated project for exposing your models and functionality via FastAPI.
- **CLI Project**: A separate project for command-line interactions using Click, complete with plugin discovery.
- **Shared Code Project**: A common codebase that both the API and CLI projects can utilize.
- **Models**:
  - **`models/model-decision-tree`**: A classic decision tree model.
  - **`models/model-linear-regression`**: A straightforward linear regression model.

Both the CLI and API will use discovery to find and load models dynamically from the `modulus` namespace.

## How to Get Started 🛠️

1. **Clone the Lab**: You've already got the whole playground, but make sure to check this folder out specifically!
  
    ```bash
    git clone https://github.com/goabonga/plugins-lab.git
    cd plugins-lab
    ```

2. **Explore the Madness**: Poke around, run some code, and see what we've cooked up.

3. **Test Your Own Plugins**: Got a wacky plugin idea? Try it out here. Break stuff. Fix stuff. Learn stuff. Repeat.

4. **Contribute**: If your experiment yields something awesome (or hilariously catastrophic), don’t keep it to yourself! Fork, tweak, and send a PR. We’re all here to learn from each other! 🤝

## Why Click and FastAPI? ⚡

- **Click**: Command line apps are the unsung heroes of the dev world, and plugins make them sing like a choir.
- **FastAPI**: Because APIs are cool, but self-extending APIs are cooler. 🌐
- **Modulus**: Seamless integration of machine learning models, ready to be discovered and used by CLI and API alike.

## Ideas We're Playing With 🤯

- **Dynamic Plugin Loading**: No more static imports; let your code find what it needs!
- **Autodiscovery with Namespace Packages**: Plug-and-play architecture? Yes, please!
- **Machine Learning Model Discovery**: Automatically find and utilize models within the `modulus` namespace.
- **Seamless Integration**: Get your plugins to play nice with both CLI and Web—without the fuss.

---

⚠️ **Warning**: Experiments here may lead to uncontrollable laughter, unintended genius, or a strong urge to refactor your entire codebase. Handle with care! 😜

Enjoy the PLUGINS-LAB, and remember: the only limit is your imagination (and maybe some Python syntax errors)! 🧙‍♂️✨
