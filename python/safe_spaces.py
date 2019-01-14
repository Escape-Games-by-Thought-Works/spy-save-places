"""Solve the spy game!"""

class SafetyFinder:

    MAP_SIZE = 10

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
            x = ord(agent[0]) - ord('A')
            y = int(agent[1:]) - 1

            coordinates.append([x, y])

        return coordinates

    def convert_coordinates_to_alphanumeric(self, agents):
        alphanumperics = []
        for agent in agents:
            alphanumperics.append(chr(agent[0] + ord('A')) + str(agent[1]+1))

        return alphanumperics

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """

        bestPlaceMinDistance = -1;
        bestPlaces = []
        for yi in range(self.MAP_SIZE):
            for xi in range(self.MAP_SIZE):
                minDistance = self.MAP_SIZE * self.MAP_SIZE
                for agent in agents:
                    distance = abs((agent[0] - xi)) + abs((agent[1] - yi))
                    if distance < minDistance:
                        minDistance = distance

                if minDistance < bestPlaceMinDistance:
                    continue

                if minDistance == bestPlaceMinDistance:
                    bestPlaces.append([xi, yi])
                    continue

                bestPlaceMinDistance = minDistance
                bestPlaces = [[xi, yi]]

        return bestPlaces

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

        if len(agents) == 0:
            return  'The whole city is safe for Alex! :-)'

        if self.is_agent_outside_map(agents[0]):
            return  'The whole city is safe for Alex! :-)'

        safeSpaces = self.find_safe_spaces(agents)

        if len(safeSpaces) == self.MAP_SIZE ** 2:
            return "There are no safe locations for Alex! :-("

        return self.convert_coordinates_to_alphanumeric(safeSpaces)

    def is_agent_outside_map(self, agent):
        return agent[0] >= self.MAP_SIZE or agent[1] >= self.MAP_SIZE
