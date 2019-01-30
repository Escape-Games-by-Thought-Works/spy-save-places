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
        positions = []
        for coordinate in agents:
            positions.append([ord(coordinate[0])-ord("A"), int(coordinate[1:])-1])
        return positions

    def convert_coordinates_reverse(self, agents):
        positions = []
        for coordinate in agents:
            positions.append(chr(coordinate[0]+ord("A")) + str(coordinate[1]+1))
        return positions

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        _, safe_spaces = self.find_safe_spaces_with_distance(agents)
        return safe_spaces

    def find_safe_spaces_with_distance(self, agents):
        city_length = 10
        maxvalue = 2 * city_length - 1;  # From one corner of the city to the other
        map = numpy.full((city_length, city_length), maxvalue)

        # Now fill the map with distances for each agent if it is smaller then already set
        for agent in agents:
            for row in range(10):
                for column in range(10):
                    distance_row = row - agent[0]
                    distance_column = column - agent[1]
                    distance = abs(distance_row) + abs(distance_column)
                    map[column, row] = min(map[column, row], distance)

        # Now find the longest distance
        longest_distance = 0
        for row in range(10):
            for column in range(10):
                longest_distance = max(longest_distance, map[column, row])

        # Filter coordinates with longest distance
        coordinates = []
        for row in range(10):
            for column in range(10):
                if map[column, row] == longest_distance:
                    coordinates.append([row, column])
        print(map)
        print(longest_distance)
        print(coordinates)

        return longest_distance, coordinates

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

        if distance == 19:
            return "The whole city is safe for Alex! :-)"
        if distance == 0:
            return "There are no safe locations for Alex! :-("

        safe_spaces = self.convert_coordinates_reverse(safe_spaces_indexed)
        print(safe_spaces)
        return safe_spaces

