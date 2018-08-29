"""Solve the spy game!"""

import itertools
import numpy


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    # Size of the city, assuming square layout
    CITY_SIZE = 10

    @classmethod
    def convert_coordinates(cls, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        return list(map(cls._convert_alphanumeric_to_vector_coordinates, agents))

    @classmethod
    def find_safe_spaces(cls, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        agents = cls._get_agents_within_city(agents)
        if not agents:
            return list(cls._iter_city_location_indices())
        city_locations = numpy.zeros([cls.CITY_SIZE, cls.CITY_SIZE], int)
        for current_location in cls._iter_city_location_indices():
            minimum_agent_distance = min([cls._calculate_distance(agent, current_location) for agent in agents])
            city_locations[current_location] = minimum_agent_distance
        maximum_distance = numpy.amax(city_locations)
        if maximum_distance == 0:
            return []
        safe_spaces = zip(*numpy.where(city_locations == maximum_distance))
        return [list(safe_space) for safe_space in safe_spaces]

    @classmethod
    def advice_for_alex(cls, agents):
        """This method will take an array with agent locations and offer advice
        to Alex for where she should hide out in the city, with special advice for
        edge cases.

        Arguments:
        agents -- a list-like object containing the map coordinates of the agents.
            Each entry should be formatted in alphanumeric form, e.g. A10, E6, etc.

        Returns either a list of alphanumeric map coordinates for Alex to hide in,
        or a specialized message informing her of edge cases
        """
        agents = cls.convert_coordinates(agents)
        safe_spaces = cls.find_safe_spaces(agents)
        if not safe_spaces:
            return 'There are no safe locations for Alex! :-('
        if len(safe_spaces) == cls.CITY_SIZE ** 2:
            return 'The whole city is safe for Alex! :-)'
        return list(map(cls._convert_vector_to_alphanumeric_coordinates, safe_spaces))

    @classmethod
    def _iter_city_location_indices(cls):
        """Iterate over all location indices in the city"""
        return itertools.product(range(cls.CITY_SIZE), range(cls.CITY_SIZE))

    @staticmethod
    def _convert_alphanumeric_to_vector_coordinates(single_coordinate):
        letter_part = single_coordinate[0].upper()
        first_component = ord(letter_part) - ord('A')

        number_part = single_coordinate[1:]
        second_component = int(number_part) - 1
        return [first_component, second_component]

    @staticmethod
    def _convert_vector_to_alphanumeric_coordinates(coordinate):
        """Convert coordinates in indexed vector form back to alphanumeric coordinates (e.g. 'A6')"""
        return chr(coordinate[0] + ord('A')) + str(coordinate[1] + 1)

    @staticmethod
    def _calculate_distance(point1, point2):
        """Calculate Manhattan distance between 2 points"""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    @classmethod
    def _get_agents_within_city(cls, agents):
        return list(filter(cls._is_inside_city, agents))

    @classmethod
    def _is_inside_city(cls, point):
        """Checks if a given point lies within the city"""
        return all(map(lambda component: 0 <= component < cls.CITY_SIZE, point))
