"""Solve the spy game!"""
import itertools
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

            if ord(agent[0]) < 97:
                convert_ascii = 65
            else:
                convert_ascii = 97

            x = ord(agent[0])-convert_ascii
            y = int(agent[1:])-1
            if x<= 10 and y <= 10:
                coordinates.append([x, y])
        return coordinates

    def unconvert_coordinates(self, agents):

        coordinates = []
        for agent in agents:
            x = str(""+chr(agent[0]+65))
            y = str(agent[1]+1)
            coordinates.append(x + y)
        return coordinates

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        distances = [[0 for x in range(10)] for y in range(10)]

        for (x,y) in itertools.product(range(10), range(10)):

            distances_to_agents = []
            for agent in agents:
                distances_to_agents.append(self.distance([x,y], agent))
            dist = min(distances_to_agents)
            distances[x][y] = dist
        longest_distance = max(map(max,distances))
        return([[ix,iy] for ix, row in enumerate(distances) for iy, i in enumerate(row) if i == longest_distance])

    def distance(self, p0, p1):
        """ Compute distance between two coordinates """
        return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])

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

        if not agents:
            return 'The whole city is safe for Alex! :-)'
        if len(agents) == 100:
            return 'There are no safe locations for Alex! :-('

        return self.unconvert_coordinates(self.find_safe_spaces(agents))
