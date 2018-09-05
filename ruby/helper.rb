# World size
WORLD_WIDTH = 10
WORLD_HEIGHT = 10

# Initial values for world
INITIAL_FIELD_VALUE = 1000
AGENT_FIELD_VALUE = -1

# Checks if the given agents are placed in the city
#
# @param [Array] agents List of agents
# @returns Filtered agents
def filter_agents(agents) 
  filtered_agents = []
  agents.each { |agent|
    coord = agent.coords

    if coord[0] >= 0 && coord[0] <= WORLD_WIDTH - 1 && 
      coord[1] >= 0 && coord[1] <= WORLD_HEIGHT - 1
      filtered_agents.push(agent)
    end
  }

    filtered_agents
end

# Returns a new two dimension weighted map with the placed agents
# * -1 for fields with agents
# * 1000 for empty fields
# 
# @param [Array] agents Array of agent positions
#
# @return Two dimension array 
def map_with(agents) 
  map = Array.new(WORLD_HEIGHT) { 
    Array.new(WORLD_WIDTH, INITIAL_FIELD_VALUE) 
  } 

  agents.each { |agent|
    map[agent[0]][agent[1]] = AGENT_FIELD_VALUE
  }

  map
end

# Updates the distances of each field in the map to an agent
#
# @param [Array] map Two dimension map
# @param [Array] agents Positions of agents as x, y value
## @return Two dimension array 
def distance_map_of(map, agents) 
  agents.each { |agent|
    map.each_with_index do |x, xi|
      x.each_with_index do |y, yi|
        value = map[xi][yi]
        distance = (xi - agent[0]).abs + (yi - agent[1]).abs

        if distance < value
          map[xi][yi] = distance
        end
      end
    end   
  }

  map
end

# Calculates the fields with the max distance to an agent
# 
# @param [Array] map Two dimension array with placed agents
# @return 
def max_distance_positions_of(map) 
  positions = []
  max_value = map.flatten.max

  map.each_with_index do |x, xi|
    x.each_with_index do |y, yi|
      value = map[xi][yi]

      if value == max_value 
        positions.push([xi, yi])
      end
    end
  end 

  positions
end
