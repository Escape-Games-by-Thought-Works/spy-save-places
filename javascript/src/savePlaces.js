/**
 * @typedef Position
 * @type {number[]}
 */

/**
 * City consisting of blocks arranged in columns and rows.
 * The amount of columns equals the amount of rows.
 */
class City {
  /**
   * Calculates the distance between 2 blocks in a city
   * @param {Position} blockAPosition
   * @param {Position} blockBPosition
   * @returns {number}
   */
  static getDistanceBetween(
    [blockAColNumber, blockARowNumber],
    [blockBColNumber, blockBRowNumber]
  ) {
    const colDistance = Math.abs(blockAColNumber - blockBColNumber);
    const rowDistance = Math.abs(blockARowNumber - blockBRowNumber);
    return colDistance + rowDistance;
  }

  /**
   * Constructs a city having this amount of columns and rows
   * @param {number} blockAmount the city's amount of columns / rows
   */
  constructor(blockAmount) {
    /**
     * The city's amount of columns / rows
     * @type {number}
     */
    this.blockAmount = blockAmount;

    /**
     * @type {Map<Position, number>} A map of the city blocks and the smallest distance to an agent
     */
    this.cityMap = new Map();

    // Initialize the city block map with a negative distance
    for (let colNumber = 0; colNumber < this.blockAmount; colNumber++) {
      for (let rowNumber = 0; rowNumber < this.blockAmount; rowNumber++) {
        this.cityMap.set([colNumber, rowNumber], -1);
      }
    }
  }

  /**
   * Filters out all blocks outside the city's grid
   * @param {Position[]} blockPositions blocks to be filtered
   * @returns {Position[]} blocks inside the city
   */
  getOnlyPositionsInCity(blockPositions) {
    return blockPositions.filter(([col, row]) => {
      return col < this.blockAmount && row < this.blockAmount;
    });
  }

  /**
   * Given the list of agents passed to this method, the smallest distance to an agent
   * is calculated for each city block and stored in the city's map
   * @param {Position[]} agentPositions agent positions
   */
  placeAgents(agentPositions) {
    [...this.cityMap.keys()].forEach(blockPosition => {
      const agentDistances = agentPositions.map(agentPosition =>
        City.getDistanceBetween(blockPosition, agentPosition)
      );
      this.cityMap.set(blockPosition, Math.min(...agentDistances));
    });
  }

  /**
   * Calculates which blocks are safest
   * @returns {Position[]} a list of blocks having the greatest distance to an agent
   */
  getSafePlaces() {
    const maxAgentDistance = Math.max(...this.cityMap.values());
    return [...this.cityMap.entries()]
      .filter(([, distance]) => distance > 0 && distance === maxAgentDistance)
      .map(([position]) => position);
  }
}

/**
 * City instance with 10 columns and 10 rows
 */
const city = new City(10);

/**
 * Converts block coordinates coded in a string consisting of a capital letter and a number
 * to a Position (i.e. an array containing the column and the row number of a block)
 * @param {string[]} agentCoordinatesList
 * @returns {Position[]}
 */
const convertCoordinates = agentCoordinatesList => {
  return agentCoordinatesList.map(agentCoordinates => {
    const colCoordinate = agentCoordinates.substr(0, 1);
    const colNumber = colCoordinate.charCodeAt(0) - 65;
    const rowCoordinate = agentCoordinates.substr(1);
    const rowNumber = parseInt(rowCoordinate) - 1;
    return [colNumber, rowNumber];
  });
};

/**
 * Returns the safest positions in a city (as a list) for a given list of agent positions
 * @param {Position[]} agentPositions
 * @returns {Position[]}
 */
const findSafePlaces = agentPositions => {
  city.placeAgents(agentPositions);
  return city.getSafePlaces();
};

/**
 * Returns the coordinates of the safest positions in a city for a given list of agent coordinates.
 * If there is no agent in the city or the city is full of agents then a corresponding message is returned.
 * @param {string[]} agentCoordinates
 * @returns {string | string[]}
 */
const adviceForAlex = agentCoordinates => {
  const agentPositions = convertCoordinates(agentCoordinates);
  const agentPositionsInCity = city.getOnlyPositionsInCity(agentPositions);
  if (agentPositionsInCity.length === 0) {
    return "The whole city is safe for Alex! :-)";
  }
  const safePlaces = findSafePlaces(agentPositionsInCity);
  if (safePlaces.length === 0) {
    return "There are no safe locations for Alex! :-(";
  }
  return convertPositions(safePlaces);
};

/**
 * Converts positions to coordinates coded in a string consisting of a capital letter and a number
 * @param {Position[]} agentPositions
 */
const convertPositions = agentPositions => {
  return agentPositions.map(([colNumber, rowNumber]) => {
    return `${convertPositionColumn(colNumber)}${convertPositionRow(
      rowNumber
    )}`;
  });
};

/**
 * Converts a column number used in a position to a capital letter
 * @param {number} colNumber
 */
const convertPositionColumn = colNumber => {
  return String.fromCharCode(colNumber + 65);
};

/**
 * Converts a row number used in a positon to a human legible row number string
 * @param {number} rowNumber
 */
const convertPositionRow = rowNumber => {
  return (rowNumber + 1).toString();
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};

