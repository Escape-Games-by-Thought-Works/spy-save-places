import math
from functools import reduce

"""Solve the spy game!"""

class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """
    def __init__(self):
        self.abc = [char for char in "abcdefghijklmnopqrstuvwxyz".upper()]


    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        return [[self.abc.index(agent[0]), int(agent[1:]) - 1] for agent in agents]


    def convert_back(self, agents):
        """converts the agents back into alphanumeric coordinates"""
        return [str(self.abc[agent[0]]) + str(agent[1] + 1) for agent in agents]


    def lowest_dist(self, point, agents):
        """returns the lowest possible distance to an agent"""
        dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
        return reduce(lambda x, y: x if x < y else y, [dist(point, agent) for agent in agents])


    def in_city(self, agent):
        return (lambda agent: True if agent[0] < 10 and agent[1] < 10 else False)(agent)


    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        self.distances = {}
        points = [[x, y] for x in range(10) for y in range(10)]
        for point in points:
            dist = self.lowest_dist(point, agents)
            self.distances.setdefault(dist, [])
            self.distances[dist].append(point)
        self.max_key = sorted([key for key in self.distances.keys()])[-1]
        return self.distances[self.max_key]

        
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
        if not agents: return "The whole city is safe for Alex! :-)"
        agents = self.convert_coordinates(agents)
        safe_places = self.find_safe_spaces(agents)
        if not self.max_key: return "There are no safe locations for Alex! :-("
        if not reduce(lambda x, y: x if x else y, [self.in_city(agent) for agent in agents]): return "The whole city is safe for Alex! :-)"
        return self.convert_back(safe_places)
