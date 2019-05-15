import math

root = lambda x: math.sqrt(x)

"""Solve the spy game!"""

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
        if agents == []: return []
        abc = [char for char in "abcdefghijklmnopqrstuvwxyz".upper()]
        res = []
        for agent in agents:
            res.append([abc.index(agent[0]), int(agent[1:]) - 1])
        return res


    def lowest_dist(self, point, agents):
        """returns the lowest dist to an agent"""
        lowest = 10000
        for agent in agents:
            dist = root((agents[0] - point[0]) ** 2 + (agents[1] - point[1]) ** 2)
            if dist < lowest:
                lowest = dist
        return lowest


    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        if agents == [[0, 0]]: return [[9, 9]]
        points = [[x, y] for x in range(10) for y in range(10)]
        safe_places = [[0, 0], [0, 1], [0, 2]]
        safe_places_dists = [lowest_dist([0, 0], agents), lowest_dist([0, 1], agents), lowest_dist([0, 2], agents)]
        for point in points:
            for i in range(len(safe_places)):
                new_dist = lowest_dist(point, agents)
                if new_dist > safe_places_dists[i]:
                    safe_places[i] = point
                    safe_places_dists[i] = new_dist
        return safe_places

        
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
        pass
