# RblxGameFinder

## About this project

Finding games on Roblox can be hard and tedious, especially when the front page is filled with overrated games. This project aims to provide a solution to the tedious search for games. RblxGameFinder is a web scraper written in Python that finds roblox games for you, by recursively finding recommended games based on an initial game.

## How to use
- Change the link of the Roblox game as well as the search depth in the settings.json file to your liking.

- Any depth above 4 isn't really recommended unless you have decent internet & computing power.

- You can change the delay at which each game is searched, but the default value is recommended.

- Moreover, put any games that you've played already or do not want to play in the ignore.txt file, each separated by a new line.

- The script will place games that it has found into the results.txt file. No need to clear its contents every time you run the script.

- Run the batch file to run the script.

- You will need Python, and it must be added to PATH to run the script

## Technical stuff
Written with Python version 3.12.4

External Package Dependencies: BeautifulSoup4, Selenium, lxml 