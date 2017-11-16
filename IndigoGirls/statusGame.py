import math
from IndigoGirls.swipeGame import swipeGame

def statusGame(messageDictionary):

    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"],int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif (messageDictionary["board"]["columnCount"] <= 1 or messageDictionary["board"]["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"],int) == False):
        outputDictionary["gameStatus"] ="error: rowCount is not an integer"

    elif (messageDictionary["board"]["rowCount"] <= 1 or messageDictionary["board"]["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif ("tile" not in messageDictionary.keys()):
        messageDictionary["tile"] = 2 ** round(messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"] * 0.6875)

    elif (isinstance(messageDictionary["tile"],int) == False):
        outputDictionary["gameStatus"] = "error: tile is not an integer"

    elif (messageDictionary["tile"] < 2):
        outputDictionary["gameStatus"] = "error: invalid tile value"

    elif (messageDictionary["tile"] > 2 ** (messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"])):
        outputDictionary["gameStatus"] = "error: invalid tile value"

    elif ("grid" not in messageDictionary["board"].keys()):
        outputDictionary["gameStatus"] = "error: missing grid"

    elif ("grid" in messageDictionary["board"].keys()):
        rowcolCountprod = (messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"])
        gridLength = len(messageDictionary["board"]["grid"])
        if (rowcolCountprod != gridLength):
            outputDictionary["gameStatus"] = "error: invalid grid length"

        elif (rowcolCountprod == gridLength):
            for index in range(0,rowcolCountprod):
                if (isinstance(messageDictionary["board"]["grid"][index],int) == False):
                    outputDictionary["gameStatus"] = "error: invalid grid Elements"

            if (outputDictionary["gameStatus"] != "error: invalid grid elements"):
                for index in range(0,rowcolCountprod):
                    if (messageDictionary["board"]["grid"][index] < 0):
                        outputDictionary["gameStatus"] = "error: grid Elements must be GE 0"

            if (outputDictionary["gameStatus"] != "error: grid Elements must be GE 0"):
                countGT0 = 0
                for index in range(0,rowcolCountprod):
                    if (messageDictionary["board"]["grid"][index] > 0):
                        countGT0 = countGT0 + 1

                if countGT0 < 2:
                    outputDictionary["gameStatus"] = "error: No fewer than two items can be GT 0"


    if (outputDictionary["gameStatus"] == "underway"):
        rowcolCountprod = messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"]
        winningTile = int(math.log(messageDictionary["tile"], 2))
        for index in range(0,rowcolCountprod):
            if (messageDictionary["board"]["grid"][index]  >= winningTile):
                outputDictionary["gameStatus"] = "win"

        if (outputDictionary["gameStatus"] != "win"):
            inputDictionary = {}
            boardDictionary = {}

            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            inputDictionary["op"] = "status"

            inputDictionary["direction"] = "left"
            leftDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "right"
            rightDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "up"
            upDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "down"
            downDictionary = swipeGame(inputDictionary)

            if ((leftDictionary["gameStatus"] == "error: no tiles can be shifted") and (rightDictionary["gameStatus"] == "error: no tiles can be shifted") and
                    (upDictionary["gameStatus"] == "error: no tiles can be shifted") and (downDictionary["gameStatus"] == "error: no tiles can be shifted")):
                outputDictionary["gameStatus"] = "lose"

            else:
                outputDictionary["gameStatus"] = "underway"


    return outputDictionary
