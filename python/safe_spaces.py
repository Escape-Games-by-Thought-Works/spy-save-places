"""Solve the spy game!"""

import itertools
import numpy


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    CITY_SIZE = 10  # Size of the city, assuming square layout

    MESSAGE_NO_LOCATION_SAFE = 'There are no safe locations for Alex! :-('
    MESSAGE_ALL_LOCATIONS_SAFE = 'The whole city is safe for Alex! :-)'

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
            return cls.MESSAGE_NO_LOCATION_SAFE
        if cls._contains_all_locations_in_city(safe_spaces):
            return cls.MESSAGE_ALL_LOCATIONS_SAFE
        return list(map(cls._convert_vector_to_alphanumeric_coordinates, safe_spaces))

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
        agents = cls._filter_agents_within_city(agents)
        if not agents:
            return list(cls._iter_city_location_indices())
        safe_spaces = cls._find_locations_with_highest_distance_from_closest_agent(agents)
        return safe_spaces

    @classmethod
    def _find_locations_with_highest_distance_from_closest_agent(cls, agents):
        location_distances_to_closest_agent = numpy.zeros([cls.CITY_SIZE, cls.CITY_SIZE], int)
        for current_location in cls._iter_city_location_indices():
            closest_agent_distance = min([cls._calculate_distance(agent, current_location) for agent in agents])
            location_distances_to_closest_agent[current_location] = closest_agent_distance
        maximum_lowest_distance = numpy.amax(location_distances_to_closest_agent)
        if maximum_lowest_distance == 0:  # Agents everywhere
            return []
        most_distant_locations = zip(*numpy.where(location_distances_to_closest_agent == maximum_lowest_distance))
        return list(map(list, most_distant_locations))  # Convert tuples to lists

    @classmethod
    def _iter_city_location_indices(cls):
        """Iterate over all location indices in the city"""
        return itertools.product(range(cls.CITY_SIZE), range(cls.CITY_SIZE))

    @staticmethod
    def _convert_alphanumeric_to_vector_coordinates(alpha_coordinates):
        """Convert alphanumeric coordinates (e.g. 'A6') to coordinates in indexed vector form (e.g. [0,5])"""
        letter = alpha_coordinates[0].upper()
        x_coordinate = ord(letter) - ord('A')  # Convert letter to number
        y_coordinate = int(alpha_coordinates[1:]) - 1
        return [x_coordinate, y_coordinate]

    @staticmethod
    def _convert_vector_to_alphanumeric_coordinates(vector_coordinates):
        """Convert coordinates in indexed vector form (e.g. [0,5]) to alphanumeric coordinates (e.g. 'A6')"""
        letter = chr(vector_coordinates[0] + ord('A'))  # Convert number to letter
        return letter + str(vector_coordinates[1] + 1)

    @staticmethod
    def _calculate_distance(point1, point2):
        """Calculate Manhattan distance between 2 points"""
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    @classmethod
    def _filter_agents_within_city(cls, agents):
        """Return only those agents which are located inside the city"""
        return list(filter(cls._is_inside_city, agents))

    @classmethod
    def _is_inside_city(cls, point):
        """Checks if a given point lies within the city"""
        return all(map(lambda coordinate: 0 <= coordinate < cls.CITY_SIZE, point))

    @classmethod
    def _contains_all_locations_in_city(cls, locations):
        """Check if the given locations make up all existing locations in the city.
        Given locations assumed to be unique and inside the city boundaries."""
        return len(locations) == cls.CITY_SIZE ** 2
