"""Solve the spy game!"""
import numpy

class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        coordinates = []
        for agent in agents:
            coordinates.append([ord(agent[0])-ord("A"), int(agent[1:])-1])
        return coordinates

    def convert_coordinates_back(self, agents_indexed):
        """This method should take an array of arrays with zero-indexing coordinates (e.g. [0, 5])
        and return a list of coordinates converted to alphanumeric coordinates.
        For instance, [0, 5] should become 'A6'

        Arguments:
        agents_indexed -- a list-like object containing zero-indexing coordinates.

        Returns a list of coordinates in alphanumeric vector form.
        """
        positions = []
        for agent_indexed in agents_indexed:
            positions.append(chr(agent_indexed[0]+ord("A")) + str(agent_indexed[1]+1))
        return positions

    def find_safe_spaces(self, agents_indexed):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents_indexed -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        _, safe_spaces = self.find_safe_spaces_with_distance(agents_indexed)
        return safe_spaces

    def find_safe_spaces_with_distance(self, agents_indexed):
        city_length = 10
        maxvalue = 2 * city_length - 1;  # From one corner of the city to the other
        map = numpy.full((city_length, city_length), maxvalue)

        # Now fill the map with distances for each agent if it is smaller then already set
        for agent_indexed in agents_indexed:
            for row in range(10):
                for column in range(10):
                    distance_row = row - agent_indexed[0]
                    distance_column = column - agent_indexed[1]
                    distance = abs(distance_row) + abs(distance_column)
                    map[column, row] = min(map[column, row], distance)

        # Now find the longest distance
        longest_distance = 0
        for row in range(10):
            for column in range(10):
                longest_distance = max(longest_distance, map[column, row])

        # Filter coordinates with longest distance
        safe_spaces_indexed = []
        for row in range(10):
            for column in range(10):
                if map[column, row] == longest_distance:
                    safe_spaces_indexed.append([row, column])
        return longest_distance, safe_spaces_indexed

    def calculate_response_for_alex(self, distance, safe_spaces_indexed):
        if distance == 19:
            return "The whole city is safe for Alex! :-)"
        if distance == 0:
            return "There are no safe locations for Alex! :-("
        return self.convert_coordinates_back(safe_spaces_indexed)

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
        agents_indexed = self.convert_coordinates(agents)
        distance, safe_spaces_indexed = self.find_safe_spaces_with_distance(agents_indexed)
        response = self.calculate_response_for_alex(distance, safe_spaces_indexed)
        return response

