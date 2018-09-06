class Escapist
  COORDINATE_PATTERN = /\A(?<x>[A-J])(?<y>[0-9]{1,2})\z/i

  def convert_coordinates(agents)
    agents.map do |agent|
      decode_coordinates(agent)
    end
  end

  def find_safe_spaces(agents)
    dangerous_agents = calculate_dangerous_agents(agents)
    heatmap = calculate_heatmap(dangerous_agents)
    max_distance = calculate_max_distance(heatmap)

    return [] if max_distance == 0

    heatmap
      .find_all { |cell| cell[1] == max_distance }
      .map { |cell| cell[0] }
  end

  def advice_for_alex(agents)
    safe_places = find_safe_spaces(convert_coordinates(agents))

    if safe_places.count == 100
      return "The whole city is safe for Alex! :-)"
    end

    if safe_places.empty?
      return "There are no safe locations for Alex! :-("
    end

    return safe_places.map { |safe_place| encode_coordinates(safe_place) }
  end


  private


  def calculate_dangerous_agents(agents)
    agents.reject do |agent|
      agent.any? { |coordinate| coordinate > 10 }
    end
  end

  def calculate_heatmap(agents)
    cells.map do |cell|
      [cell, min_distance_to_agents(cell, agents)]
    end
  end

  def cells
    Array(0..9).product(Array(0..9))
  end

  def min_distance_to_agents(cell, agents)
    agents
      .map { |agent| manhattan_distance(agent, cell) }
      .min
  end

  def calculate_max_distance(heatmap)
    heatmap
      .max_by { |cell| cell[1] }
      .last
  end

  def decode_coordinates(coordinates)
    coordinates.match(COORDINATE_PATTERN) do |matchdata|
      x = matchdata.named_captures["x"].ord - "A".ord
      y = Integer(matchdata.named_captures["y"], 10) - 1

      [x, y]
    end
  end

  def encode_coordinates(coordinates)
    x = (coordinates[0] + "A".ord).chr
    y = coordinates[1] + 1

    "#{x}#{y}"
  end

  def manhattan_distance(v1, v2)
    v1.zip(v2)
      .map { |u, v| (u - v).abs }
      .inject(:+)
  end
end
