"""Solve the spy game!"""
from typing import List, Optional


class Board:
    __DIMENSIONS = 10

    def __init__(self):
        # Data will be a nxn matrix that hold the distance to the nearest agent, or None if it has not yet been computed
        self.data = []
        for i in range(0, Board.__DIMENSIONS):
            this_row = [None] * Board.__DIMENSIONS
            self.data.append(this_row)

        self.changed_positions = []

    def place_agents(self, agents: List[List[int]]):
        """ Place the initial agents. """
        for this_agent in agents:
            self._set(this_agent, value=0)

    def _set(self, field: List[int], value: int):
        x, y = field[0], field[1]
        self.data[x][y] = value
        self.changed_positions.append(field)

    def _get(self, field: List[int]):
        x, y = field[0], field[1]
        return self.data[x][y]

    def has_changed(self):
        return len(self.changed_positions) == 0

    def take_changed_positions(self):
        result = self.changed_positions
        self.changed_positions = []
        return result

    @staticmethod
    def get_neighbors_for(coord: List[int]):
        """ Returns the coordinates of the neighbours of a field. """
        result = []
        x, y = coord[0], coord[1]

        is_top_row = (y == 0)
        is_bottom_row = (y == (Board.__DIMENSIONS-1))
        is_left_column = (x == 0)
        is_right_column = (x == (Board.__DIMENSIONS-1))

        # we use directions for simpler assignment
        # northwest
        if not is_left_column:
            if not is_top_row:
                result.append([x-1, y-1])

        # north
        if not is_top_row:
            result.append([x, y-1])

        # northeast
        if not is_right_column:
            if not is_top_row:
                result.append([x+1, y-1])

        # east
        if not is_right_column:
            result.append([x + 1, y])

        # southeast
        if not is_bottom_row:
            if not is_right_column:
                result.append([x+1, y+1])

        # south
        if not is_bottom_row:
            result.append([x, y+1])

        # southwest
        if not is_left_column:
            if not is_bottom_row:
                result.append([x-1, y+1])

        # west
        if not is_left_column:
            result.append([x-1, y])

        return result


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    def convert_coordinates(self, agents: List[str]) -> List[List[int]]:
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.

        Raises:
            ValueError when the coordinates are not in the correct format.
        """
        self._raise_if_input_coordinates_are_bad(agents)
        result = []

        for agent in agents:
            letter_coord = SafetyFinder._letter_to_coordinate(agent[0])
            number = int(agent[1:])
            result.append([letter_coord, number-1])

        return result

    @staticmethod
    def _letter_to_coordinate(letter: str) -> Optional[int]:
        """ Converts a letter to a coordinate. Returns None when the letter is not a valid input. """
        try:
            coordinate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'].index(letter)
            return coordinate
        except ValueError:
            return None

    @staticmethod
    def _raise_if_input_coordinates_are_bad(agents):
        if agents is None:
            raise TypeError("agents is None")
        for agent in agents:
            if len(agent) < 2:
                raise ValueError(f"Coordinate '{agent}' is not in the form [A-J][1-10]")
            letter = agent[0]
            letter_coord = SafetyFinder._letter_to_coordinate(letter)
            if letter_coord is None:
                raise ValueError(f"First part of '{agent}' must an uppercase letter between A and J")
            number_str = agent[1:]
            if not number_str.isdigit():
                raise ValueError(f"Second part of '{agent}' must be a number")
            number_int = int(number_str)
            if number_int <= 0 or number_int > 10:
                raise ValueError(f"Second part of '{agent}' must be a number between 1 and 10")

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        pass

    def advice_for_alex(self, agents):
        """This method will take an array with agent locations and offer advice
        to Alex for where she should hide out in the city, with special advice for
        edge cases.

        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.

        Returns either a list of alphanumeric map coordinates for Alex to hide in,
        or a specialized message informing her of edge cases
        """
        pass
