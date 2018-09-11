"""Solve the spy game!"""
import numpy as np


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

        return [[ord(i[0]) - ord('A'), int(i[1:]) - 1]
                for i in agents]

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """

        distance_matrix = np.full((10, 10), 100, dtype=int)

        for agent_position in agents:
            for x in range(10):
                for y in range(10):
                    distance = abs(x - agent_position[0]) + abs(y - agent_position[1])
                    if distance < distance_matrix[x][y]:
                        distance_matrix[x][y] = distance

        list_of_tuples = np.where(distance_matrix == distance_matrix.max())

        return [[x, y] for x, y in zip(list_of_tuples[0], list_of_tuples[1])]

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
        if len(agents) == 100:
            return 'There are no safe locations for Alex! :-('
        if len(agents) == 0:
            return 'The whole city is safe for Alex! :-)'

        converted_coordinates = self.convert_coordinates(agents)
        for i in converted_coordinates:
            if i[0] < 0 or i[1] > 9 or i[0] > 9 or i[1] < 0:
                return 'The whole city is safe for Alex! :-)'
        result = self.find_safe_spaces(converted_coordinates)

        return [f'{chr(i[0]+ord("A"))}{i[1]+1}' for i in result]
