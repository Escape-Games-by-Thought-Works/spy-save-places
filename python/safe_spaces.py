"""Solve the spy game!"""


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
        longest_distance = 0
        safe_spaces = []
        # Iterate over every coordinates in the map
        for row in range(self.city_rows):
            for column in range(self.city_columns):
                current_distance = self._shortest_agents_distance(row, column, agents)
                longest_distance, safe_spaces = self._update_safe_spaces(row, column, current_distance, longest_distance, safe_spaces)
        return longest_distance, safe_spaces

    def _shortest_agents_distance(self, row, column, agents):
        """This method will take a row and column on the map and a list of agent location as coordinates in zero-indexed vector form
        and return the shortest possible distance to the agents from the position on the map.

        Arguments:
        row -- the current row in the city
        column -- the current column in the city
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns the shortest possible distance to the agents from the position on the map
        """
        shortest_distance = self.totally_safe_distance
        for agent in agents:
            shortest_distance = min(shortest_distance, self._agent_distance(row, column, agent))
        return shortest_distance

    @classmethod
    def _agent_distance(cls, row, column, agent):
        """This method will take a row and column on the map and an agent location as coordinates in zero-indexed vector form
        and return the distance to the agent from the position on the map.

        Arguments:
        row -- the current row in the city
        column -- the current column in the city
        agent -- the coordinates of an agent.

        Returns the distance to the agent from the position on the map
        """
        distance_row = row - agent[0]
        distance_column = column - agent[1]
        distance = abs(distance_row) + abs(distance_column)
        return distance

    @classmethod
    def _update_safe_spaces(cls, row, column, current_distance, longest_distance, safe_spaces):
        """This method will take a row and column on the map and the current distance to the nearest agent
        and the longest distance to agents found so far and a list of safe spaces found so far as coordinates in zero-indexed vector form
        and return the new longest distance to agents and safe spaces.

        Arguments:
        row -- the current row in the city
        column -- the current column in the city
        current_distance -- current distance to nearest agent for coordinates
        longest_distance -- longest distance to agents found so far
        safe_spaces -- safe spaces found so far for longest_distance

        Returns the new longest distance to the agents and safe spaces
        """
        if cls.is_safe_distance(current_distance) and current_distance == longest_distance:
            safe_spaces.append([row, column])
        if current_distance > longest_distance:
            longest_distance = current_distance
            safe_spaces = [[row, column]]
        return longest_distance, safe_spaces

    @classmethod
    def is_safe_distance(cls, current_distance):
        return current_distance > 0

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

    @classmethod
    def _convert_agents(cls, agents):
        """This method should take an array of arrays with zero-indexing coordinates (e.g. [0, 5])
        and return a list of coordinates converted to alphanumeric coordinates.
        For instance, [0, 5] should become 'A6'

        Arguments:
        agents -- a list-like object containing zero-indexing coordinates.

        Returns a list of coordinates in alphanumeric vector form.
        """
        return [chr(agent[0] + ord("A")) + str(agent[1] + 1) for agent in agents]
