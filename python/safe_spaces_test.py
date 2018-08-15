"""Run unittests for the ThoughtWorks spy game"""
import unittest

from safe_spaces import SafetyFinder

@unittest.skip("Comment or delete this line to solve the challenge with python")
class SafetyFinderTest(unittest.TestCase):
    """A class that contains the unit tests that adhere to the game spec"""

    def test_convert_coordinates(self):
        """Test for accurate conversion from alphanumeric coordinates
        to indexed vector coordinates.
        """
        self.assertEqual(SafetyFinder().convert_coordinates(['A5']),
                         [[0, 5]])

    def test_no_agents(self):
        """Tests for no agents in the city"""
        self.assertEqual(SafetyFinder().find_safe_spaces([]),
                         'The whole city is safe for Alex! :-)')

    def test_agents_everywhere(self):
        """Tests for agents everywhere in the city. Oh no!!"""
        agents = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
                  'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
                  'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
                  'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
                  'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
                  'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
                  'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
                  'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
                  'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
                  'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']
        self.assertEqual(SafetyFinder().find_safe_spaces(agents),
                         'There are no safe locations for Alex! :-(')

    def test_round1(self):
        """Test for six agents at specified locations"""
        agents = ['B2', 'D6', 'E9', 'H4', 'H9', 'J2']
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted(['A10', 'A8', 'F1']))

    def test_round2(self):
        """Test for seven agents at specified locations"""
        agents = ['B4', 'C4', 'C8', 'E2', 'F10', 'H1', 'J6']
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted(['A1', 'A10', 'E6', 'F5', 'F6', 'G4', 'G5',
                                 'G7', 'H8', 'I9', 'J10']))

    def test_round3(self):
        """Test when only a single agent remains in the city"""
        agents = ['A1']
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted(['J10']))


if __name__ == '__main__':
    unittest.main()
