import bs4
import json
from selenium import webdriver

# global variables
ignore: list[str] = []
results: list[str] = []
initialGame: str
depth: int

# function to create new selenium browser
def newChromeBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)

# function to get all recommended games of a game
def getRec(gameLink: str, iteration: int = 0):
    # check if iteration exceeds depth
    if (iteration >= depth):
        if (not gameLink in results):
            results.append(gameLink)
    else:
        # get and render webpage html
        link = gameLink + "#!/about"
        browser = newChromeBrowser()
        browser.get(link)

        # parse and search with beautifulsoup
        souped = bs4.BeautifulSoup(browser.page_source, "lxml")
        query = souped.find_all("a", {"class": "game-card-link"})

        # add found games to results and recursively find new games
        for item in query:
            foundLink = item["href"].split("?")[0]
            if (not foundLink in results):
                results.append(foundLink)
            getRec(foundLink, iteration=(iteration + 1))

# main function
def find():
    # declare global variables
    global results
    global ignore
    global initialGame
    global depth

    # load games to ignore
    with open("./ignore.txt", "r") as ignoreFile:
        for link in ignoreFile.readlines():
            ignore.append(link.rstrip("\n"))
        ignoreFile.close()
    
    # load settings
    with open("./settings.json", "r") as settings:
        data = json.load(settings)
        initialGame = data["initialGame"]
        depth = data["depth"]
        settings.close()

    # open browser
    chromeBrowser = newChromeBrowser()

    # get all recommended games
    getRec(initialGame)

    # remove ignored games
    for ignored in ignore:
        if (ignored in results):
            results.remove(ignored)

    # write found games to results.txt
    with open("./results.txt", "w") as resultFile:
        for result in results:
            resultFile.write(result + "\n")
        resultFile.close()

    # close browser
    chromeBrowser.close()

    # output finish message
    print("\n\nSCRIPT HAS FINISHED RUNNING!")

if __name__ == "__main__":
    find()
