"""Solve the spy game!"""
import numpy


class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out

    This solution is roughly modeled after the IODA architecture from Ralf Westphal
    and using many advice from the Clean Code sessions from Robert C. Martin
    """

    def __init__(self, city_rows=10, city_columns=10):
        """
        Initialize some constants we need in the calculations

        Arguments:
        city_rows -- variable width of the city map with default value
        city_columns -- variable height of the city map with default value
        """
        self.city_rows = city_rows
        self.city_columns = city_columns
        self.totally_safe_distance = self.city_rows + self.city_columns - 1  # One bigger then distance from one corner of the city to the other

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        return [[ord(agent[0])-ord("A"), int(agent[1:])-1] for agent in agents]

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        _, safe_spaces = self._find_distance_and_safe_spaces(agents)
        return safe_spaces

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
        agents = self.convert_coordinates(agents)
        distance, safe_spaces = self._find_distance_and_safe_spaces(agents)
        response = self._calculate_response_for_alex(distance, safe_spaces)
        return response

    def _find_distance_and_safe_spaces(self, agents):
        """This method will take a list of agent location as coordinates in zero-indexed vector form
        and return the longest distance between safe spaces and agents and a list of safe spaces.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns the longest possible distance to an agent and a list of safe spaces
        """
        city_map = numpy.full((self.city_rows, self.city_columns), self.totally_safe_distance)
        self._fill_map_with_distance_to_agents(city_map, agents)
        longest_distance = self._find_longest_distance(city_map)
        safe_spaces = self._filter_coordinates_with_longest_distance(city_map, longest_distance)
        return longest_distance, safe_spaces

    def _fill_map_with_distance_to_agents(self, city_map, agents):
        """This method will take a city_map as a 2d array and a list of agent location as coordinates in zero-indexed vector form
        and fill the city_map with the distance to the closest agent for any coordinate in the map.

        Arguments:
        city_map -- a 2d array of the city initialized to a distance one longer then the longest possible distance
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.
        """
        for agent in agents:
            for row in range(self.city_rows):
                for column in range(self.city_columns):
                    distance_row = row - agent[0]
                    distance_column = column - agent[1]
                    distance = abs(distance_row) + abs(distance_column)
                    city_map[column, row] = min(city_map[column, row], distance)

    def _find_longest_distance(self, city_map):
        """This method will take a city_map as a 2d array and return the longest distance it finds.

        Arguments:
        city_map -- a 2d array of the city

        Returns the longest possible distance to an agent
        """
        longest_distance = 0
        for row in range(self.city_rows):
            for column in range(self.city_columns):
                longest_distance = max(longest_distance, city_map[column, row])
        return longest_distance

    def _filter_coordinates_with_longest_distance(self, city_map, longest_distance):
        """This method will take a city_map as a 2d array and the longest distance to an agent
        and return a list of safe spaces.

        Arguments:
        city_map -- a 2d array of the city
        longest_distance -- longest distance in city_map

        Returns a list of safe spaces
        """
        safe_spaces = []
        for row in range(self.city_rows):
            for column in range(self.city_columns):
                if city_map[column, row] == longest_distance:
                    safe_spaces.append([row, column])
        return safe_spaces

    def _calculate_response_for_alex(self, distance, safe_spaces):
        """This method should take the distance between the safe spaces and the agents and an array of arrays with zero-indexing coordinates (e.g. [0, 5])
        and return either a text response for the corner cases or a list of alphanumeric coordinates (e.g. 'A6') of safe places.
        For instance, [0, 5] should become 'A6'

        Arguments:
        distance -- distance between the safe spaces and the agents
        agents -- a list-like object containing zero-indexing coordinates of safe places.

        Returns a list of safe spaces coordinates in alphanumeric vector form.
        """
        if distance == self.totally_safe_distance:
            return "The whole city is safe for Alex! :-)"
        if distance == 0:
            return "There are no safe locations for Alex! :-("
        return self._convert_agents(safe_spaces)

    @staticmethod
    def _convert_agents(agents):
        """This method should take an array of arrays with zero-indexing coordinates (e.g. [0, 5])
        and return a list of coordinates converted to alphanumeric coordinates.
        For instance, [0, 5] should become 'A6'

        Arguments:
        agents -- a list-like object containing zero-indexing coordinates.

        Returns a list of coordinates in alphanumeric vector form.
        """
        return [chr(agent[0] + ord("A")) + str(agent[1] + 1) for agent in agents]
