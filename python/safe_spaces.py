"""Solve the spy game!"""

import numpy as np
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
        alphanum_coords -- a string representing alphanumeric coordinates, e.g. 'F5'

        Returns a list with two numbers representing the corresponding coordinates

        Throws a ValueError if alphanum_coords is not valid
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
        alphanum_coords -- a string representing alphanumeric coordinates, e.g. 'F5'

        Throws a ValueError if alphanum_coords is not valid
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
        coords -- a list with two numbers representing coordinates, e.g. [1, 2]

        Returns a string representing the corresponding alphanumeric coordinates, e.g. 'F5'

        Throws a ValueError if coords is not valid
        """
        cls.validate_coordinates(coords)
        row, col = coords
        return '{}{}'.format(chr(row + cls.ORD_AND_CHR_OFFSET), col + 1)

    @staticmethod
    def validate_coordinates(coords):
        """Validates the given coordinates

        Arguments:
        coords -- a list with two numbers representing coordinates, e.g. [1, 2]

        Throws a ValueError if coords is not valid
        """
        if not isinstance(coords, list) or len(coords) != 2:
            raise ValueError('"coords" must be a list of length 2 (was {})'.format(coords))
        row, col = coords
        if not isinstance(row, int) or row < 0:
            raise ValueError('row must be an integer greater than or equal to 0')
        if not isinstance(col, int) or col < 0:
            raise ValueError('col must be an integer greater than or equal to 0')


class Agent:
    """An agent looking for Alex"""

    def __init__(self, coords):
        """Creates a new Agent from coordinates
        
        Arguments:
        coords -- a list with two numbers representing coordinates, e.g. [1, 2]
        """
        CoordinateUtils.validate_coordinates(coords)
        self.coordinates = coords
        
    @classmethod
    def from_alphanumeric_coordinates(cls, alphanum_coords):
        """Creates a new Agent from alphanumeric coordinates

        Arguments:
        alphanum_coords -- a string representing alphanumeric coordinates, e.g. 'F5'

        Returns a new Agent instance at the corresponding coordinates
        """
        return Agent(CoordinateUtils.to_coordinates(alphanum_coords))

    def __hash__(self):
        return hash('r{}'.format(self.coordinates[0])) ^ hash('c{}'.format(self.coordinates[1]))

    def __eq__(self, other):
        return isinstance(other, Agent) and hash(self) == hash(other)

    def __repr__(self):
        return '[{}, {}]'.format(self.coordinates[0], self.coordinates[1])


class City:
    """A city where Alex needs to find safe places to hide out from the agents"""

    def __init__(self, size):
        """Creates a new City of the given size

        Arguments:
        size -- an integer specifying the size of the city, e.g. 10 for a 10x10 grid
        """
        if not isinstance(size, int) or size < 1:
            raise ValueError('"size must be an integer greater than or equal to 1')
        self.size = size

    def get_safe_places_for_agents(self, agents):
        """Find safe places for Alex in the city with respect to a given list of Agents

        The idea here is to first compute the distances to each agent separately and then
        merge all the distances using numpy array operations. The merge of two such distance
        matrices is the pair-wise minimum of both matrices, e.g. for a city of size 5:

        2 1 . 1 2       3 2 3 4 5       2 1 . 1 2
        3 2 1 2 3       2 1 2 3 4       2 1 1 2 3
        4 3 2 3 4   +   1 . 1 2 3   =   1 . 1 2 3
        5 4 3 4 5       2 1 2 3 4       2 1 2 3 4
        6 5 4 5 6       3 2 3 4 5       3 2 3 4 5

        Arguments:
        agents -- a list of Agents

        Returns a list of coordinates representing safe places
        """
        if not isinstance(agents, Iterable) or isinstance(agents, str):
            raise ValueError('"agents" must be list-like (was {})'.format(agents))

        distances = [self.__get_distances_for_agent(agent) for agent in agents]
        merged_distances = np.asarray(distances).min(0)
        safe_places = np.argwhere(merged_distances == np.amax(merged_distances))

        return safe_places.tolist()

    def __get_distances_for_agent(self, agent):
        """Computes the distances of Alex from a given agent in the city

        Arguments:
        agent -- an Agent

        Returns a numpy array representing the distance matrix for all coordinates in the city
            with respect to the given agent
        """
        if not isinstance(agent, Agent):
            raise ValueError('"agent" must be an Agent (was {})'.format(agent))

        row, col = agent.coordinates
        grid = []
        for curRow in range(0, self.size):
            distance = abs(curRow - row)
            leftDistance = col + distance
            rightDistance = self.size - col + distance
            grid.append(
                list(range(leftDistance, distance, -1))
                + [distance]
                + list(range(distance + 1, rightDistance))
            )

        return np.array(grid)

    def is_agent_within_boundaries(self, agent):
        """Checks if the given agent is in city

        Arguments:
        agent -- an agent

        Returns a boolean stating whether or not the agent is in the city
        """
        row, col = agent.coordinates

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

        return [
            Agent.from_alphanumeric_coordinates(alphanum_coords).coordinates
            for alphanum_coords in agents
        ]

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        return self.CITY.get_safe_places_for_agents([Agent(coords) for coords in agents])

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

        distinct_valid_agents = set(filter(
            lambda agent: self.CITY.is_agent_within_boundaries(agent),
            map(
                lambda alphanum_coords: Agent.from_alphanumeric_coordinates(alphanum_coords),
                agents
            )
        ))
        if len(distinct_valid_agents) == 0:
            return self.MSG_BEST_CASE
        if len(distinct_valid_agents) == self.CITY.size ** 2:
            return self.MSG_WORST_CASE

        return [
            CoordinateUtils.to_alphanumeric_coordinates(coords)
            for coords in self.CITY.get_safe_places_for_agents(distinct_valid_agents)
        ]
