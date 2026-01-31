# Setup Guide

## Pin your project's Python version to 3.13

`uv python pin 3.13`

## Create a virtual environment at the top level of your project directory:

`uv venv`

## Activate the virtual environment:

`source .venv/bin/activate`

## install all dependencies

`uv install`


## ToDo
-  Add a scoring system
-  Implement multiple lives and respawning
-  Add an explosion effect for the asteroids
-  Add acceleration to the player movement
-  Make the objects wrap around the screen instead of disappearing
-  Add a background image
-  Create different weapon types
-  Make the asteroids lumpy instead of perfectly round
-  Make the ship have a triangular hit box instead of a circular one
-  Add a shield power-up
-  Add a speed power-up
-  Add bombs that can be dropped