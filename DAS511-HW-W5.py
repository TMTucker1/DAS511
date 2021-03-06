
# Problem 1 (2 points)
# Assign the 'name' variable an object that is your name of type str.

name = "Sports Players"

# Problem 2 (2 points)
# Create a class and implement it for your problem of interest
class Player:
    def __init__(self, first_name: str, last_name: str, age: int, team: str):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._team = team

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @property
    def team(self):
        return self._team

    @first_name.setter
    def first_name(self, fname):
        self._first_name = fname

    @last_name.setter
    def last_name(self, lname):
        self._last_name = lname

    @age.setter
    def age(self, age):
        self._age = age

    @team.setter
    def team(self, team):
        self._team = team

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} ({self.age} years), {self.team}'


# Problem 3 (2 points)
# Create another class and implement it for your problem of interest
class FootBallPlayer(Player):
    def __init__(self, first_name: str, last_name: str, age: int, team: str,
                 goals: int, caps: int, assists: int):
        super(FootBallPlayer, self).__init__(first_name, last_name, age, team)
        self._goals = goals
        self._caps = caps
        self._assists = assists

    @property
    def goals(self):
        return self._goals

    @property
    def caps(self):
        return self._caps

    @property
    def assists(self):
        return self._assists

    @goals.setter
    def goals(self, goal):
        self._goals = goal

    @caps.setter
    def caps(self, caps):
        self._caps = caps

    @assists.setter
    def assists(self, assists):
        self._assists = assists

    def __str__(self):
        result_str = super().__str__()
        result_str += f"\nGoals: {self.goals}"
        result_str += f"\nCaps: {self.caps}"
        result_str += f"\nAssists: {self.assists}"

        return result_str


# Problem 4 (2 points)
# Create another class and implement it for your problem of interest
class BaseBallPlayer(Player):
    def __init__(self, first_name: str, last_name: str, age: int, team: str,
                 plate_appearances: int, hits: int, runs_scored: int, strike_outs: int, walks: int):
        super(BaseBallPlayer, self).__init__(first_name, last_name, age, team)
        self._plate_appearances = plate_appearances
        self._hits = hits
        self._runs_scored = runs_scored
        self._strike_outs = strike_outs
        self._walks = walks

    @property
    def plate_appearances(self):
        return self._plate_appearances

    @property
    def hits(self):
        return self._hits

    @property
    def runs_record(self):
        return self._runs_scored

    @property
    def strike_outs(self):
        return self._strike_outs

    @property
    def walks(self):
        return self._walks

    @plate_appearances.setter
    def plate_appearances(self, plate_appearances):
        self._plate_appearances = plate_appearances

    @hits.setter
    def hits(self, hits):
        self._hits = hits

    @runs_record.setter
    def runs_record(self, record):
        self._runs_scored = record

    @strike_outs.setter
    def strike_outs(self, outs):
        self._strike_outs = outs

    @walks.setter
    def walks(self, walks):
        self._walks = walks

    def __str__(self):
        result = super().__str__()
        result += f'\nPlate Appearances: {self._plate_appearances}\n'
        result += f'Hits: {self.hits}\n'
        result += f'Runs Record: {self._runs_scored}\n'
        result += f'Strike outs: {self._strike_outs}\n'
        result += f'Walks: {self._walks}'

        return result
# If you need to, you can create any additional classes or functions here as well.


# Problem 5 (2 points) & # Problem 6 (2 points) & Problem 7 (2 points)
#  Assign a variable named 'obj_3' an example instance of one of your classes
#  that extends another class I gave you 8 instead of 3

obj_1 = Player()
obj_2 = BaseBallPlayer()
obj_3 = FootBallPlayer()

if __name__ == '__main__':
    # creating 5 Baseball players
    Player1 = BaseBallPlayer("Rocky", "Tucker", 11, "STL BEARS", 10, 6, 2, 1, 1)
    Player2 = BaseBallPlayer("Jaxton", "Harris", 15, "PACIFIC HS", 7, 2, 2, 1, 3)
    Player3 = BaseBallPlayer("Donovan", "Emberton", 12, "STL BEARS", 12, 7, 6, 1, 1)
    Player4 = BaseBallPlayer("Thomas", "Smith", 14, "FESTUS HS", 4, 0, 2, 5, 1)
    Player5 = BaseBallPlayer("Wyatt", "Coleman", 14, "PACIFIC HS", 10, 4, 2, 1, 2)

    # creating 5 FootBallPlayers
    Player6 = FootBallPlayer("Lionel", "Messi", 31, "Barcelona FC", 105, 200, 120)
    Player7 = FootBallPlayer("Christiano", "Ronaldo", 33, "Juventus", 115, 190, 100)
    Player8 = FootBallPlayer("Neymar", "Jr.", 25, "Paris St. Germain", 76, 150, 95)
    Player9 = FootBallPlayer("Kylian", "MBappe", 31, "Manchester Utd", 55, 78, 123)
    Player10 = FootBallPlayer("Gareth", "Bale", 31, "Real Madrid FC", 90, 170, 130)

    # printing out the baseball players and football players
    print('List of Baseball Players')
    print(Player1)
    print(Player2)
    print(Player3)
    print(Player4)
    print(Player5)

    print('\nList of Football Players')
    print(Player6)
    print(Player7)
    print(Player8)
    print(Player9)
    print(Player10)



# Problems 8 through 14 are worth 4 points each.
#    For each problem you must implement a test method in the following
#     TestCase class. Each method name should be unique and start with 'test_'.
#     Each method should test something different about the classes you created
#     above. Use unittest.TestCase's assert methods to check your implementation.
#     You will get 2 points for each test method created. You will get 2
#     additional points for each of these tests that complete successfully.
#     See https://docs.python.org/3/library/unittest.html for examples.

import unittest
import sys
import inspect
###################################################
#DO NOT MODIFY this class's name or what it extends
###################################################
class MyTestCases(unittest.TestCase):

    # Problem 8
    # add test case method
    def test_players(self):
        self.assertTrue(Player is not None)
    
    # Problem 9
    # add test case method
    def test_BaseBall_Players(self):
        self.assertTrue(BaseBallPlayer.last_name, str)
        self.assertTrue(BaseBallPlayer.first_name, str)
        self.assertTrue(BaseBallPlayer.team, str)
        
       
    # Problem 10
    # add test case method
    def test_FootBall_Players(self):
        self.assertTrue(FootBallPlayer.firsl_name, str)
        self.assertTrue(FootBallPlayer.last_name, str)
        self.assertTrue(FootBallPlayer.team, str)
    # Problem 11
    # add test case method
    def test_BaseBall_team_stats(self):
         self.assertTrue(isinstance(BaseBallPlayer.hits, int))
         self.assertTrue(isinstance(BaseBallPlayer.age, int))
         self.assertTrue(isinstance(BaseBallPlayer.plate_appearances, int))
         self.assertTrue(isinstance(BaseBallPlayer.runs_record, int))
         self.assertTrue(isinstance(BaseBallPlayer.walks, int))
         self.assertTrue(isinstance(BaseBallPlayer.strike_outs, int))
    # Problem 12
    # add test case method
    def test_Football_stats(self):
        self.assertTrue(isinstance(FootBallPlayer.age, int))
        self.assertTrue(isinstance(FootBallPlayer.goals, int))
        self.assertTrue(isinstance(FootBallPlayer.assists, int))
        self.assertTrue(isinstance(FootBallPlayer.caps, int))
    # Problem 13
    # add test case method
      
    # Problem 14
    # add test case method

    ##################################################
    #DO NOT MODIFY any of these test case methods
    ##################################################

    def get_classes(self):
        clses = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member is not MyTestCases)
        return clses

    def test_name_assigned(self):
        m = sys.modules[__name__]
        name = getattr(m,"name",None)
        self.assertTrue(name is not None)
        self.assertTrue(isinstance(name,str))
        self.assertTrue(len(name) > 0)

    def test_one_class_created(self):
        self.assertTrue(len(self.get_classes()) >= 1)

    def test_two_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 2)

    def test_three_classes_created(self):
        self.assertTrue(len(self.get_classes()) >= 3)

    def test_obj_1_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_1 is not None)
        self.assertTrue(isinstance(obj_1,tuple([cls[1] for cls in clses])))

    def test_obj_2_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_2 = getattr(m,"obj_2",None)
        obj_1 = getattr(m,"obj_1",None)
        self.assertTrue(obj_2 is not None)
        self.assertTrue(isinstance(obj_2,tuple([cls[1] for cls in clses])))
        self.assertNotEqual(type(obj_2),type(obj_1))

    def test_obj_3_instance_created(self):
        clses = self.get_classes()
        m = sys.modules[__name__]
        obj_3 = getattr(m,"obj_3",None)
        self.assertTrue(obj_3 is not None)
        self.assertTrue(isinstance(obj_3,tuple([cls[1] for cls in clses])))
        bases = tuple(b for b in type(obj_3).__bases__ if b is not object)
        print(dir(obj_3))
        self.assertTrue(len(bases) > 0)
        
##################################################
#DO NOT MODIFY any of the code below!
##################################################
if __name__ == "__main__":
    unittest.main()

