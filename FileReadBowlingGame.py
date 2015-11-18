import string
from BowlingGame import Game
FileName = open("testscores.txt", "r")
gameList = []
for line in FileName:
    lineScores = line.strip()
    gameList = line.split(",")
    gameList = [int(element) for element in gameList]
    #print(gameList)
    FinalScore = gameList.pop()
    Round = Game()
    for pins in gameList:
        Round.roll(pins)
    print("Final Score given is: ", FinalScore, "Actual Score is: ", Round.score(), "score is correct", FinalScore == Round.score())