require 'rspec'

# This is where you implement your solution 
def chars
  return ['A','B','C','D','E','F','G','H','I','J']
end

def x_distance(pos1, pos2)
  return (pos1.to_i - pos2.to_i).abs
end
def y_distance(pos1char, pos2char)
  pos1 = chars.index(pos1char) + 1
  pos2 = chars.index(pos2char) + 1
  return (pos1 - pos2).abs
end

def spy_places(agents)
  save_places = Array.new
  all_places = Array.new(10*10)
  save_map = Array.new(10*10){ |index| 0 }
  all_places.each_index { |i|
    all_places[i] = "#{chars[i%10]}#{(i/10).floor+1}"
  }

  # Generate a save-map for each field.
  # Iterate over all agents and get the distance for each one
  # Save the smallest number. Then get the biggest number(s). That are the save places.
  all_places.each_index { |i|
    x = i%10
    y = (i/10).floor

    local_min = 100
    agents.each { |agent|
      distance = (agent[0] - x).abs + (agent[1] - y).abs
      if distance < local_min
        save_map[i] = distance
        local_min = distance
      end
    }
  }

  max_num = save_map.max

  return "There are no safe locations for Alex! :-(" if max_num == 0
 
  save_map.each.with_index { |x, i| 
    save_places << [i%10, (i/10).floor] if x == max_num 
  }

  p max_num
  p save_map

  return save_places
end

def spy_places_interface(agents)
  return 'The whole city is safe for Alex! :-)' if agents.empty?

  save_places = Array.new
  all_places = Array.new(10*10)
  save_map = Array.new(10*10){ |index| 0 }
  all_places.each_index { |i|
    all_places[i] = "#{chars[i%10]}#{(i/10).floor+1}"
  }
  
  # Generate a save-map for each field.
  # Iterate over all agents and get the distance for each one
  # Save the smallest number. Then get the biggest number(s). That are the save places.
  all_places.each_index { |i|
    local_min = 100
    agents.each { |agent|
      distance = x_distance(agent[1,2], all_places[i][1,2]) + y_distance(agent[0], all_places[i][0])
      if distance < local_min
        save_map[i] = distance
        local_min = distance
      end
    }
  }

  max_num = save_map.max

  return "There are no safe locations for Alex! :-(" if max_num == 0
 
  save_map.each.with_index { |x, i| 
    save_places << all_places[i] if x == max_num 
  }

  return save_places.sort
end

# Do not edit below this line...!
RSpec.describe 'Spy Places Level 1' do
  it 'some places are save if agents are some' do
    agents =
      [[1,1],[3,5],[4,8],[7,3],[7,8],[9,1]]
    expect(spy_places(agents)).to match_array([[0,9],[0,7],[5,0]])
  end
  it 'some places are save if agents are some' do
    agents = 
      [[0,0]]
    expect(spy_places(agents)).to match_array([[9,9]])
  end
end

RSpec.describe 'Spy Places Level 2' do
  it 'expects all save places at no agents' do
    agents = []
    expect(spy_places_interface(agents)).to eq('The whole city is safe for Alex! :-)')
  end

  it 'no place is save if agents are everywhere' do
    agents = 
      ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',
       'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
       'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
       'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
       'E1','E2','E3','E4','E5','E6','E7','E8','E9','E10',
       'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10',
       'G1','G2','G3','G4','G5','G6','G7','G8','G9','G10',
       'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10',
       'I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
       'J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']
    expect(spy_places_interface(agents)).to eq('There are no safe locations for Alex! :-(')
  end

  it 'some places are save if agents are some' do
    agents = 
      ['B2','D6','E9','H4','H9','J2']
    expect(spy_places_interface(agents)).to eq(['A10','A8','F1'])
  end
  it 'some places are save if agents are some' do
    agents = 
      ['B4','C4','C8','E2','F10','H1','J6']
    expect(spy_places_interface(agents)).to eq(['A1', 'A10', 'E6', 'F5', 'F6', 'G4', 'G5', 'G7','H8','I9', 'J10'])
  end
  it 'some places are save if agents are some' do
    agents = 
      ['A1']
    expect(spy_places_interface(agents)).to eq(['J10'])
  end
end
