import numpy as np
"""Solve the spy game!"""

class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """

    GRID_SIZE = 10

    # Convert A1 -> [0, 0]
    def convert_coordinate(self, agent):
        return [ord(agent[:1]) - ord('A'), int(agent[1:]) - 1]

    # Revert [0, 0] -> A1
    def revert_coordinates(self, agent):
        return chr(ord('A') + agent[0]) + str(agent[1] + 1)

    # Check if agent is in the map
    def validate_agent(self, agent):
        return 0 <= agent[0] <= 9 and 0 <= agent[1] <= 9

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        return list(map(self.convert_coordinate, agents))

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        # Calculate manhattan distance of (x, y) to agent a
        def dist(x, y, a):
            return abs(x - a[0]) + abs(y - a[1])

        # Calculate minimum distance of all agents from a coordinate (x, y)
        def min_agent_dist(x, y, agents):
            dists = sorted((dist(x, y, a) for a in agents))
            return dists[0]

        # Create the grid as 10 * 10 matrix
        grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE))
        # Calculate minimum agent distance for each point
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] = min_agent_dist(x, y, agents)

        # Return the list of maximum distances
        return list(map(lambda a: [a[1], a[0]], zip(*np.array(np.where(grid == grid.max())))))

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
        # Convert all the coordinates
        agents = map(self.convert_coordinate, agents)
        # Remove invalid agents
        agents = list(filter(self.validate_agent, agents))
        if not agents:
            return 'The whole city is safe for Alex! :-)'

        if len(agents) == self.GRID_SIZE * self.GRID_SIZE:
            return 'There are no safe locations for Alex! :-('

        safe_spaces = self.find_safe_spaces(agents)
        return list(map(self.revert_coordinates, safe_spaces))
