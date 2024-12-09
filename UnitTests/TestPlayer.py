from UnitTests.TileGenerationTest import TileGenerationTest
from UnitTests.WinConditionTest import WinConditionTest
from UnitTests.LossConditionTest import LossConditionTest

class TestPlayer:
    def __init__(self):
        pass

    def Main():
        for test in [TileGenerationTest, WinConditionTest, LossConditionTest]:
            print("")
            test.introduceTest()
            test.testDisplay()

TestPlayer.Main()
input ("Press Enter to close...")