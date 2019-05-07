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
        ans = []
        if(agents == []):
            return agents
        elif(isinstance(agents[0],str)):
            for agent in agents:
                ycoord = ord(agent[0]) - 65
                xcoord = int(agent[1:]) - 1
                ans.append([ycoord,xcoord])
            return ans
        else:
            for agent in agents:
                ycoord = chr(agent[0] + 65)
                xcoord = str(agent[1] + 1)
                ans.append(ycoord + xcoord)
            return ans
         
    def agent_filter(self,agent):
        """This method returns true if zero-indexed coordinates are on a 
        10 x 10 field and false if they aren't. For example, the output for
        (5,0) should be true, but for (-3,8) or (10,10) it should be false.   

        Arguments:
        agent -- a two-element list or tuple containing the zero-indexed coordinates.

        Returns true, iff the coordinates are on a 10 x 10 field.
        """
        return agent[0] > -1 and agent[0] < 10 and agent[1] > -1 and agent[1] < 10
    
    def propagate_agents(self, added_agents, all_agents):
        """This method takes in a set of coordinates all_agents and returns a 
        set of all coordinates with a manhattan-distance of one of any of the 
        given coordinates that are not already member of all_agents. Since those
        new coordinates can be determined just by the set of coordinates that were 
        most recently added those are also passed as added_agents.

        Arguments:
        added_agents -- a set of zero-indexed coordinates of the agents added 
        in the last step. added_agents has to be a subset of all_agents. If it
        is unknown, which agents were previously added, added_agents should be
        set to all_agents.
        all_agents -- a set of zero-indexed coordinates of all currently 
        existing agents.

        Returns a set of all agents coordinates that should be added next.
    
        """
        new_agents = set()
        for agent in added_agents:
            new_agents.update([(agent[0]-1,agent[1]),
                               (agent[0]+1,agent[1]),
                               (agent[0],agent[1]-1),
                               (agent[0],agent[1]+1)])
            new_agents = set(filter(self.agent_filter, new_agents))
        return new_agents.difference(all_agents)
    
    
    def find_safe_spaces(self, agents):
        """This method will take an array with agent locations and finds
        the safest places in the city for Alex to hang out.

        Arguments:
        agents -- a list-like object containing the map coordinates of agents.
            Each entry should be formatted in indexed vector form,
            e.g. [0, 5], [3, 7], etc.

        Returns a list of safe spaces in indexed vector form.
        """
        added_agents = set(map(tuple, agents))
        all_agents = added_agents.copy()
        while(len(all_agents) < 100):
            added_agents = self.propagate_agents(added_agents, all_agents)
            all_agents.update(added_agents)
        return sorted(list(map(list, added_agents)))
        
        
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
        agents = filter(self.agent_filter, self.convert_coordinates(agents))
        if(agents == []):
            return "The whole city is safe for Alex! :-)"
        elif(len(agents) >= 100):
            return "There are no safe locations for Alex! :-("
        return self.convert_coordinates(self.find_safe_spaces(agents))

            
