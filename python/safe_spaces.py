"""Solve the spy game!"""

import re

from collections import Iterable



class CoordinateUtils:
    """A utility class to deal with coordinates"""

    ORD_AND_CHR_OFFSET = 65
    RE_ALPHANUM_COORDS = re.compile(r'(?P<ROW>[A-J])(?P<COL>\d+)')

    @classmethod
    def to_coordinates(cls, alphanum_coords):
        """Converts alphanumeric coordinates into a list of numeric coordinates

        Arguments:
        alphanum_coords -- a string representing alphanumeric coordinates, e.g. 'F5'.

        Returns a list with two numbers representing the corresponding coordinates.

        Throws a ValueError if alphanum_coords is not valid.
        """
        cls.validate_alphanumeric_coordinates(alphanum_coords)
        reMatch = cls.RE_ALPHANUM_COORDS.match(alphanum_coords)
        row = ord(reMatch.group('ROW')) - cls.ORD_AND_CHR_OFFSET
        col = int(reMatch.group('COL')) - 1
        return [row, col]

    @classmethod
    def validate_alphanumeric_coordinates(cls, alphanum_coords):
        """Validates the given alphanumeric coordinates

        Arguments:
        alphanum_coords -- a string representing alphanumeric coordinates, e.g. 'F5'.

        Throws a ValueError if alphanum_coords is not valid.
        """
        if not isinstance(alphanum_coords, str):
            raise ValueError('alphanum_coords must be a string (was {})'.format(alphanum_coords))
        if not cls.RE_ALPHANUM_COORDS.match(alphanum_coords):
            raise ValueError("alphanum_coords must match the following pattern: r'{}' (was '{}')"
                .format(cls.RE_ALPHANUM_COORDS.pattern, alphanum_coords))

    @classmethod
    def to_alphanumeric_coordinates(cls, coords):
        """Converts the given coordinates into alphanumeric coordinates

        Arguments:
        coords -- coordinates in indexed vector form, e.g. [1, 2].

        Returns a string representing the corresponding alphanumeric coordinates, e.g. 'F5'.

        Throws a ValueError if coords is not valid.
        """
        cls.validate_coordinates(coords)
        row, col = coords
        return '{}{}'.format(chr(row + cls.ORD_AND_CHR_OFFSET), col + 1)

    @staticmethod
    def validate_coordinates(coords):
        """Validates the given coordinates

        Arguments:
        coords -- coordinates in indexed vector form, e.g. [1, 2].

        Throws a ValueError if coords is not valid
        """
        if not isinstance(coords, list) or len(coords) != 2:
            raise ValueError('"coords" must be a list of length 2 (was {})'.format(coords))
        row, col = coords
        if not isinstance(row, int) or row < 0:
            raise ValueError('row must be an integer greater than or equal to 0')
        if not isinstance(col, int) or col < 0:
            raise ValueError('col must be an integer greater than or equal to 0')

class City:

    __MIN_SAFE_DISTANCE = 1  # 0 distances are unsafe

    def __init__(self, size):
        self.size = size
        self.max_distance = size * 2 - 2

    def get_safe_places(self, agents):
        safest_distance = self.__MIN_SAFE_DISTANCE
        safest_points = []
        for point in self.__iter_points():
            single_point_safest_distance = self.__get_single_point_safest_distance(point, agents)
            if single_point_safest_distance == safest_distance:
                safest_points.append(point)
            elif single_point_safest_distance > safest_distance:
                safest_points = [point]
                safest_distance = single_point_safest_distance
        return safest_points

    def __iter_points(self):
        size_range = range(0, self.size)
        for row in size_range:
            for col in size_range:
                yield [row, col]
    
    def __get_single_point_safest_distance(self, point, agents):
        safest_distance = self.max_distance
        for agent in agents:
            distance = self.__get_distance(point, agent)
            if distance < safest_distance:
                safest_distance = distance
        return safest_distance

    @staticmethod
    def __get_distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def is_agent_within_boundaries(self, agent):
        """Checks if the given agent is in city

        Arguments:
        agent -- map coordinates of an agent.
            Should be formatted in indexed vector form,
            e.g. [0, 5].

        Returns a boolean stating whether or not the agent is in the city.
        """
        row, col = agent
        return 0 <= row < self.size and 0 <= col < self.size


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    CITY = City(10)
    MSG_BEST_CASE = 'The whole city is safe for Alex! :-)'
    MSG_WORST_CASE = 'There are no safe locations for Alex! :-('

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        if not isinstance(agents, Iterable) or isinstance(agents, str):
            raise ValueError('"agents" must be list-like (was {})'.format(agents))

        return [CoordinateUtils.to_coordinates(alphanum_coords) for alphanum_coords in agents]

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        return self.CITY.get_safe_places(agents)

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
        if not isinstance(agents, Iterable) or isinstance(agents, str):
            raise ValueError('"agents" must be list-like (was {})'.format(agents))

        distinct_agents_in_city = self.__get_distinct_agents_in_city(agents)
        if len(distinct_agents_in_city) == 0:
            return self.MSG_BEST_CASE
        if len(distinct_agents_in_city) == self.CITY.size ** 2:
            return self.MSG_WORST_CASE

        return [
            CoordinateUtils.to_alphanumeric_coordinates(coords)
            for coords in self.CITY.get_safe_places(distinct_agents_in_city)
        ]

    def __get_distinct_agents_in_city(self, agents):
        """Determines distinct agents which are in the city

        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.

        Returns a list of agent coordinates in indexed vector form.
        """
        distinct_agents_in_city = set()
        for agent in self.convert_coordinates(agents):
            if (self.CITY.is_agent_within_boundaries(agent)):
                distinct_agents_in_city.add(tuple(agent))
        return [list(agent) for agent in distinct_agents_in_city]

