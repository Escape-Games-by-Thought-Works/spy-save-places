// This is where you implement your solution

// Generally used constants
const letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const coordinateNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const maxDistance = 18;

/**
 * Converts all agents to their coordinates.
 *
 * For example ['B6', 'C2', 'J7'] => [[1, 5], [2, 1], [9, 6]]
 *
 * @param {Array} agents array with positions
 * @returns {Array} agents array with coordinates
 */
const convertCoordinates = (agents) => {
  return agents.map(agent => {
    const letter = agent.substr(0,1);
    const number = parseInt(agent.substr(1,2));
    const xCoordinate = letters.indexOf(letter);
    const yCoordinate = numbers.indexOf(number);

    return ([xCoordinate, yCoordinate]);
  });
};

/**
 * Converts all coordinates to places.
 *
 * For example [[1, 5], [2, 1], [9, 6]] => ['B6', 'C2', 'J7']
 *
 * @param {Array} coordinates array
 * @returns {Array} places array
 */
const convertToPlaces = (coordinates) => {
  return coordinates.map(coordinate => letters[coordinate[0]] + numbers[coordinate[1]]);
};

/**
 * Find safe places for the given agents array
 *
 * @param {Array} agents as coordinates
 * @returns {Array} safe places as coordinates
 */
const findSafePlaces = (agents) => {

  let distanceGrid = [];
  let safePlaces = [];
  let safePlaceDistance = 0;

  // calculate distances and safe in distanceGrid
  // & check safePlaceDistanceUnit if still the max distance
  for (let x of coordinateNumbers) {
    // init row
    distanceGrid.push(new Array(10));

    // find shortest distances and check safePlaceDistanceUnit, if this place is safer than those before
    for (let y of coordinateNumbers) {
      distanceGrid[x][y] = findShortestAgentDistance(agents, x, y);
      safePlaceDistance = Math.max(safePlaceDistance, distanceGrid[x][y]);
    }
  }

  // get places with safePlaceDistanceUnit as distance in the distanceGrid
  for (let x of coordinateNumbers) {
    for (let y of coordinateNumbers) {
      // if there are safe places and this is one of them, add to safe places
      if (safePlaceDistance !== 0 && distanceGrid[x][y] === safePlaceDistance) {
        safePlaces.push([x, y]);
      }
    }
  }

  return safePlaces;
};

/**
 * Find shortest distance to next agent for given agents and place.
 *
 * @param {Array} agents array of coordinates
 * @param {number} x x-coordinate of place
 * @param {number} y y-coordinate of place
 * @returns {number} shortest distance to next agent for this place
 */
const findShortestAgentDistance = (agents, x, y) => {
  let shortestDistance = maxDistance;
  agents.forEach(agent => {
    // if agent is on the grid
    if (agent[0] >= 0 && agent[0] < 10 && agent[1] >= 0 && agent[1] < 10) {
      // override shortest distance if less than before
      shortestDistance = Math.min(distance([x, y], agent), shortestDistance);
    }
  });
  return shortestDistance;
};

/**
 * Distance of to places in steps. Only horizontal and vertical moves are allowed, no diagonal ones.
 *
 * For example:
 *    [1, 1] [1, 1] => 0
 *    [1, 1] [2, 2] => 2
 *    [2, 2] [1, 1] => 2
 * @param placeA
 * @param placeB
 * @returns {number}
 */
const distance = (placeA, placeB) => {
  return Math.abs(placeA[0] - placeB[0]) + Math.abs(placeA[1] - placeB[1]);
};

/**
 * Give advice to Alex. Either:
 *  - 'The whole city is safe for Alex! :-)' if all places are safe
 *  - 'There are no safe locations for Alex! :-(' if there are no safe places = agents everywhere
 *  - array of safe places
 *
 * @param {Array} agents places
 * @returns either a string with advice or an array of safe places
 */
const adviceForAlex = (agents) => {

  const safePlaces = findSafePlaces(convertCoordinates(agents));

  if (safePlaces.length === 100) {
    return 'The whole city is safe for Alex! :-)';

  } else if (safePlaces.length === 0) {
    return 'There are no safe locations for Alex! :-(';
  }

  return convertToPlaces(safePlaces);
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
