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
   * @param {Position} blockA
   * @param {Position} blockB
   * @returns {number}
   */
  static getDistanceBetween([blockACol, blockARow], [blockBCol, blockBRow]) {
    const colDistance = Math.abs(blockACol - blockBCol);
    const rowDistance = Math.abs(blockARow - blockBRow);
    return colDistance + rowDistance;
  }

  /**
   * Constructs a city having this amount of columns and rows
   * @param {number} dim the city's amount of columns / rows
   */
  constructor(dim) {
    /**
     * The city's amount of columns / rows
     * @type {number}
     */
    this.dim = dim;

    /**
     * @type {Map<Position, number>} A map of the city blocks and the smallest distance to an agent
     */
    this.cityMap = new Map();

    // Initialize the city block map with a negative distance
    for (let i = 0; i < this.dim; i++) {
      for (let j = 0; j < this.dim; j++) {
        this.cityMap.set([i, j], -1);
      }
    }
  }

  /**
   * Filters out all blocks outside the city's grid
   * @param {Position[]} blocks blocks to be filtered
   * @returns {Position[]} blocks inside the city
   */
  getBlocksInsideCity(blocks) {
    return blocks.filter(([col, row]) => {
      return col < this.dim && row < this.dim;
    });
  }

  /**
   * Given the list of agents passed to this method, the smallest distance to an agent 
   * is calculated for each city block and stored in the city's map
   * @param {Position[]} agents agent positions
   */
  placeAgents(agents) {
    [...this.cityMap.keys()].forEach(block => {
      const agentDistances = agents.map(agent =>
        City.getDistanceBetween(block, agent)
      );
      this.cityMap.set(block, Math.min(...agentDistances));
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
 * Create city instance
 */
const city = new City(10);

/**
 *
 * @param {string[]} agents
 * @returns {Position[]}
 */
const convertCoordinates = agents => {
  return agents.map(agent => {
    const colStr = agent.substr(0, 1);
    const col = colStr.charCodeAt(0) - 65;
    const rowStr = agent.substr(1);
    const row = parseInt(rowStr) - 1;
    return [col, row];
  });
};

/**
 * TODO
 * @param {Position[]} agents
 * @returns {Position[]}
 */
const findSafePlaces = agents => {
  city.placeAgents(agents);
  return city.getSafePlaces();
};

/**
 * TODO
 * @param {string[]} agents
 * @returns {string | string[]}
 */
const adviceForAlex = agents => {
  const agentPositions = convertCoordinates(agents);
  const agentPositionsInCity = city.getBlocksInsideCity(agentPositions);
  if (agentPositionsInCity.length === 0) {
    return "The whole city is safe for Alex! :-)";
  }
  const safePlaces = findSafePlaces(agentPositionsInCity);
  if (safePlaces.length === 0) {
    return "There are no safe locations for Alex! :-(";
  }
  return convertToCoordinates(safePlaces);
};

/**
 * TODO
 * @param {Position[]} agents
 */
const convertToCoordinates = agents => {
  return agents.map(([col, row]) => {
    return `${convertColumn(col)}${convertRow(row)}`;
  });
};

/**
 * TODO
 * @param {number} colNumber
 */
const convertColumn = colNumber => {
  return String.fromCharCode(colNumber + 65);
};

/**
 * TODO
 * @param {number} rowNumber
 */
const convertRow = rowNumber => {
  return (rowNumber + 1).toString();
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
