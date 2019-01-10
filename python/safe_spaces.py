"""Solve the spy game!"""
class SafetyFinder:
    """A class that contains everything we need to find the
    safest places in the city for Alex to hide out
    """
    max_size = 10

    def convert_coordinates(self, agents):
        """This method should take a list of alphanumeric coordinates (e.g. 'A6')
        and return an array of the coordinates converted to arrays with zero-indexing.
        For instance, 'A6' should become [0, 5]

        Arguments:
        agents -- a list-like object containing alphanumeric coordinates.

        Returns a list of coordinates in zero-indexed vector form.
        """
        res = []
        for element in agents:
            x = ord(element[0])-ord('A')
            y = int(element[1:]) - 1 #converts to 0-index
            res.append([x, y])
        
        return res

    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and find
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        best_dist = -1;
        bests = []
        for yi in range(self.max_size):
            for xi in range(self.max_size):
                minDistance = self.max_size * self.max_size
                for a in agents:
                    distancePa = abs((a[0] - xi)) + abs((a[1] - yi))
                    if distancePa < minDistance:
                        minDistance = distancePa

                if minDistance < best_dist:
                    continue

                if minDistance == best_dist:
                    bests.append([xi, yi])
                    continue

                best_dist = minDistance
                bests = [[xi, yi]]

        return bests

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
        wholeCityStr = "The whole city is safe for Alex! :-)"
        if len(agents)==0: return wholeCityStr
        coord = self.convert_coordinates(agents)[0]               
        if (coord[0]>=self.max_size) or (coord[1] >= self.max_size) or (coord[0]<0) or (coord[1]<0):
            return wholeCityStr
    
        safe_places = self.find_safe_spaces(self.convert_coordinates(agents)) 

        if len(safe_places) == self.max_size**2:
            return "There are no safe locations for Alex! :-("

        print(safe_places)
        results = []
        for element in safe_places:
            letter = chr(element[0] + ord('A'))
            nmb = str(element[1]+1)
            string = letter + nmb
            results.append(string)

        return results
        pass
