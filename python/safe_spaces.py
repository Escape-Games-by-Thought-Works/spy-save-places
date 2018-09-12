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
        convertedAgents = [ ]
        for agent in agents:
            x = ord(agent[0])-ord('A')
            if x<0 : raise IndexError('Bad X value {} in {} from {}'.format(x, agent, agents))
            y=int(agent[1:])-1
            if y<0 : raise IndexError('Bad Y value {} in {} from {}'.format(y, agent, agents))
            convertedAgents.append([x,y])
        return convertedAgents
    
    def convert_coordinates_back(self, agents):
        """This method should take a list of coordinates arrays (e.g. [0, 5]) with zero-indexing
        and return an array of alphanumeric coordinates (e.g. 'A6').
        For instance, [[0,5]] should become ['A6'].

        Arguments:
        agents -- a list of coordinates in zero-indexed vector form.

        Returns a list-like object containing alphanumeric coordinates.
        """
        convertedAgents = [ ]
        for agentXY in agents:
            x,y = agentXY
            convertedX = "ABCDEFGHIJ"[x]
            convertedY = y+1
            convertedXY = "{}{}".format(convertedX, convertedY)
            convertedAgents.append(convertedXY)
        return convertedAgents
    
    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        safePlaces = []
        maxMinDistance = 1
        for x in range(0,10) :
            for y in range(0,10):
                minDistance = 9999
                for agent in agents:
                    [ax,ay] = agent
                    if ax<10 and ay<10 :
                        distance = abs(ax - x) + abs(ay - y)
                        if distance < minDistance: minDistance = distance
                if minDistance > maxMinDistance :
                    maxMinDistance = minDistance
                    safePlaces = []
                if minDistance == maxMinDistance : safePlaces.append([x,y])
        return safePlaces

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
        agentCoordinates = self.convert_coordinates(agents)
        safePlaces = self.find_safe_spaces(agentCoordinates)
        safePlacesCount = len(safePlaces)
        if safePlacesCount == 0 : return 'There are no safe locations for Alex! :-('
        if safePlacesCount == 100 : return 'The whole city is safe for Alex! :-)'
        return self.convert_coordinates_back(safePlaces)
