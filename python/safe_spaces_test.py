"""Run unittests for the ThoughtWorks spy game"""
import unittest

from safe_spaces import SafetyFinder, Board


class SafetyFinderTest(unittest.TestCase):
    """A class that contains the unit tests that adhere to the game spec"""

    def test_convert_coordinates_does_not_accept_coordinates_with_bad_format(self):
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["12"])
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["a2"])
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["AA"])
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["A0"])
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["A11"])
        self.assertRaises(ValueError, SafetyFinder().convert_coordinates, ["A1A"])

    # Level 1 -- Test for conversion from alphanumeric coordinates to vectors
    def test_empty_coordinates(self):
        """Test that the code adequately handles empty lists
        """
        self.assertEqual(SafetyFinder().convert_coordinates([]), [])

    def test_single_coordinate(self):
        """Test for accurate conversion from a single alphanumeric coordinate
        to an indexed vector coordinate.
        """
        self.assertEqual(SafetyFinder().convert_coordinates(['F3']),
                         [[5, 2]])

    def test_multiple_coordinates(self):
        """Test for accurate conversion from a list of alphanumeric coordinates
        to a list of indexed vector coordinates.
        """
        agents = ['B6', 'C2', 'J7']
        self.assertEqual(SafetyFinder().convert_coordinates(agents),
                         [[1, 5], [2, 1], [9, 6]])

    def test_double_digits(self):
        """Ensure that alphanumeric coordinates with two digit numbers
        are properly converted
        """
        self.assertEqual(SafetyFinder().convert_coordinates(['J10']),
                         [[9, 9]])

    # Level 2 -- Find safe spaces in the city based on agent locations
    def test_safe_spaces_round1(self):
        """Test for six agents at specified locations"""
        agents = [[1, 1], [3, 5], [4, 8], [7, 3], [7, 8], [9, 1]]
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted([[0, 9], [0, 7], [5, 0]]))

    def test_safe_spaces_round2(self):
        """Test for six agents at different specified locations"""
        agents = [[0, 0], [0, 9], [1, 5], [5, 1], [9, 0], [9, 9]]
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted([[5, 7], [6, 6], [7, 5]]))

    def test_safe_spaces_round3(self):
        """Test for one agent at a specified location"""
        agents = [[0, 0]]
        self.assertEqual(sorted(SafetyFinder().find_safe_spaces(agents)),
                         sorted([[9, 9]]))

    # Level 3 -- Handling edge cases and offering recommendations
    def test_no_agents(self):
        """Tests for no agents in the city"""
        self.assertEqual(SafetyFinder().advice_for_alex([]),
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
        self.assertEqual(SafetyFinder().advice_for_alex(agents),
                         'There are no safe locations for Alex! :-(')

    def test_advice_round1(self):
        """Test for six agents at specified locations"""
        agents = ['B2', 'D6', 'E9', 'H4', 'H9', 'J2']
        self.assertEqual(sorted(SafetyFinder().advice_for_alex(agents)),
                         sorted(['A10', 'A8', 'F1']))

    def test_advice_round2(self):
        """Test for seven agents at specified locations"""
        agents = ['B4', 'C4', 'C8', 'E2', 'F10', 'H1', 'J6']
        self.assertEqual(sorted(SafetyFinder().advice_for_alex(agents)),
                         sorted(['A1', 'A10', 'E6', 'F5', 'F6', 'G4', 'G5',
                                 'G7', 'H8', 'I9', 'J10']))

    def test_advice_round3(self):
        """Test for a different six agents at specified locations"""
        agents = ['A1', 'A10', 'B6', 'F2', 'J1', 'J10']
        self.assertEqual(sorted(SafetyFinder().advice_for_alex(agents)),
                         sorted(['F8', 'G7', 'H6']))

    def test_advice_round4(self):
        """Test when only a single agent remains in the city"""
        agents = ['A1']
        self.assertEqual(sorted(SafetyFinder().advice_for_alex(agents)),
                         sorted(['J10']))

    def test_agent_outside_map(self):
        """Test when only a single agent remains in the city"""
        agents = ['A12']
        self.assertEqual(SafetyFinder().advice_for_alex(agents),
                         'The whole city is safe for Alex! :-)')


class BoardTest(unittest.TestCase):
    def test_board_dimensions_are_correct(self):
        sut = Board()
        self.assertEqual(len(sut.data), 10)
        self.assertEqual(len(sut.data[0]), 10)
        self.assertIsNone(sut.data[0][9])

    def test_agents_are_correctly_placed_and_stored_as_new(self):
        sut = Board()
        agents = [[0, 0], [3, 4]]
        sut.place_agents(agents)

        self.assertEqual(sut._get(agents[0]), 0)
        self.assertEqual(sut._get(agents[1]), 0)

        self.assertEqual(sut.changed_positions, agents)

    def test_all_coordinates_returned_as_neighbors_for_central_coordinate(self):
        result = Board.get_neighbors_for([5, 5])
        self.assertEqual(len(result), 8)

        self.assertIn([4, 4], result)  # northwest
        self.assertIn([4, 5], result)  # west
        self.assertIn([4, 6], result)  # southwest

        self.assertIn([5, 4], result)  # north
        self.assertIn([5, 6], result)  # south

        self.assertIn([6, 4], result)  # northeast
        self.assertIn([6, 5], result)  # east
        self.assertIn([6, 6], result)  # southeast

    def test_no_west_coordinates_are_returned_for_left_column(self):
        result = Board.get_neighbors_for([0, 5])
        self.assertEqual(len(result), 5)

        self.assertIn([0, 4], result)  # north
        self.assertIn([0, 6], result)  # south

        self.assertIn([1, 4], result)  # northeast
        self.assertIn([1, 5], result)  # east
        self.assertIn([1, 6], result)  # southeast

    def test_corner_coordinate_has_only_three_neighbors(self):
        result = Board.get_neighbors_for([9, 9])
        self.assertEqual(len(result), 3)

        self.assertIn([8, 9], result)  # west
        self.assertIn([8, 8], result)  # southwest

        self.assertIn([9, 8], result)  # south

    def test_changed_position_are_cleared_after_taking(self):
        sut = Board()
        sut._set([5, 5], 3)
        positions = sut.take_changed_positions()
        self.assertIn([5, 5], positions)

        new_positions = sut.take_changed_positions()
        self.assertEqual(len(new_positions), 0)


if __name__ == '__main__':
    unittest.main()
