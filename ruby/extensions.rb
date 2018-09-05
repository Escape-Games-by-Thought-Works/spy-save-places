class String
  # Char of the agent positon
  def field_char
    self[0,1]
  end
  
  # Number of the agent positon
  def field_number
    self[1..-1]
  end

  # Transformed x coordinate of agent position
  def x_coord
    self.field_char.downcase.ord - 'a'.ord
  end

  # Transformed y coordinate of agent position
  def y_coord
    self.field_number.to_i - 1
  end

  # Combined x, y coordinate of agent positon
  def coords 
    [x_coord, y_coord]
  end
end

class Array
  # Textual position of array field
  def position
    field_char = (self[0] + 'A'.ord).chr
    field_number = self[1] + 1

    "#{field_char}#{field_number}"
  end
end
