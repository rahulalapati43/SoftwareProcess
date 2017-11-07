from unittest import TestCase
from IndigoGirls.recommendGame import recommendGame

class RecommendGameTest(TestCase):
    # def test100_010_shouldvalidateMoves(self):
    #     inputDictionary = {}
    #     resultDictionary = {}
    #     resultDictionary["moves"] = 0
    #     outputDictionary = recommendGame(inputDictionary)
    #     self.assertEquals(resultDictionary, outputDictionary)

    def test100_020_shouldvalidateMovesInt(self):
        inputDictionary = {}
        inputDictionary["moves"] = '2'
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: moves is not an integer"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)

    def test100_030_shouldvalidateMovesGE0(self):
        inputDictionary = {}
        inputDictionary["moves"] = -1
        resultDictionary = {}
        resultDictionary["gameStatus"] = "error: moves must be GE 0"
        outputDictionary = recommendGame(inputDictionary)
        self.assertEquals(resultDictionary, outputDictionary)