import pytest

from generating_data.dice import Die

class TestInitialization:
    def test_default(self):
        die = Die()
        assert die.numSides == 6
        
    def test_no_sides(self):
        # There are no such thing as zero sided Dice.
        with pytest.raises(ValueError):
            die = Die(0)

    def test_negative_sides(self):
        # There are no such thing as negative sided Dice.
        with pytest.raises(ValueError):
            die = Die(-1)
            
    def test_nonzero_sides(self):
        die = Die(1)
        die500 = Die(500)
        assert (die.numSides == 1 and 
                die500.numSides == 500)


    def test_not_numeric(self):
        # Not going to test any others because implementation is a type check.

        with pytest.raises(TypeError):
            die = Die('False')

        with pytest.raises(TypeError):
            die = Die('what')

        with pytest.raises(TypeError):
            die = Die(True)

class TestRoll:
    def rollsValid(self):
        NUMSIDES = 50
        die = Die(NUMSIDES)
        # Roll the dice NUMSIDES * 10000 times to be as sure as possible
        for i in range(NUMSIDES*10000):
            current = die.roll()
            assert current in range(1,NUMSIDES+1)