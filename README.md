Create a new uv project on your computer.
uv init your-project-name
cd your-project-name

Pin your project's Python version to 3.13
uv python pin 3.13

Create a virtual environment at the top level of your project directory:
uv venv

Activate the virtual environment:
source .venv/bin/activate

You should see (your-project-name) at the beginning of your terminal prompt – for example, mine is:

(Asteroids) wagslane@MacBook-Pro-2 Asteroids %

Make sure that your virtual environment is activated when running the game or using the bootdev CLI.

Add the pygame library as a project dependency:
uv add pygame==2.6.1

This tells Python that this project requires pygame with an exact version of 2.6.1.

Make sure pygame is installed:
uv run -m pygame
