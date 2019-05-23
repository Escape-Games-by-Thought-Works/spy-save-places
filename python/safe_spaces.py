"""Solve the spy game!"""

from queue import Queue

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

        if len(agents):
            coordinates = [[ord(a[0])-65, int(a[1:len(a)])-1] for a in agents]

        return coordinates

    def convert_numeric_coordinates(self, agents):
        coordinates = []

        if len(agents):
            coordinates = [str(chr((a[0]+65))) + str(a[-1]+1) for a in agents]

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

        # Utility function that returns next vertical and horizontal cells
        # starting from curr_step cell.
        # Only cells that are in the grid are returned.
        def next_steps(curr_step):
            steps = []
            r = curr_step[0]
            c = curr_step[1]

            if 0 <= r-1 <= 9:
                steps.append([r-1, c])

            if 0 <= r+1 <= 9:
                steps.append([r+1, c])

            if 0 <= c-1 <= 9:
                steps.append([r, c-1])

            if 0 <= c+1 <= 9:
                steps.append([r, c+1])

            return steps

        # Queue of the steps that needs to be visit.
        q_to_check = Queue()
        # Dictionary that models the grid/map.
        maps = {"{}{}".format(k[0], k[1]): -1 for k in agents}

        list(map(q_to_check.put, agents))

        # Until there are cells to visit...
        while not q_to_check.empty():
            curr_cell = q_to_check.get()
            curr_value = maps["{}{}".format(curr_cell[0], curr_cell[1])]

            next_value = 1

            if curr_value != -1:
                next_value = curr_value + 1

            steps = next_steps(curr_cell)

            for s in steps:
                position = "{}{}".format(s[0], s[1])

                if position in maps:
                    next_cell_value = maps[position]
                    if next_cell_value != -1 and next_cell_value-curr_value >= 2:
                        maps[position] = next_value
                        q_to_check.put(s)
                else:
                    maps[position] = next_value
                    q_to_check.put(s)

        max_v = max(maps.values())
        out = []
        for k, v in maps.items():
            if v == max_v:
                out.append(k)

        return [[int(x[0]), int(x[1])] for x in out]

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

        def out_of_grid(agents):
            coordinates = self.convert_coordinates(agents)

            for c in coordinates:
                if c[0] > 9 or c[1] > 9:
                    return True
            return False

        if not len(agents):
            result = 'The whole city is safe for Alex! :-)'

        elif len(agents) == 100:
            result = 'There are no safe locations for Alex! :-('

        elif out_of_grid(agents):
            result = 'The whole city is safe for Alex! :-)'

        else:
            result = self.convert_numeric_coordinates(self.find_safe_spaces(self.convert_coordinates(agents)))

        return result
