const mapSize = 10;
const ACharCode = 'A'.charCodeAt(0);

const convertCoordinates = (agents) => {
  const coords = [];
  agents.forEach((o) => {
    const x = o.charCodeAt(0) - ACharCode;
    const y = parseInt(o.substr(1), 10) - 1;

    if (x >= 0 && x < mapSize && y >= 0 && y < mapSize) {
      coords.push([x, y]);
    }
  });
  return coords;
};
const toMapCoordinates = (coordinate) => {
  const x = String.fromCharCode(ACharCode + coordinate[0]);
  const y = coordinate[1] + 1;
  return x + y;
};

// calculates manhattan distnace between two coordinates on the map
const manhattanDistance = (coord1, coord2) => Math.abs(coord1.x - coord2.x) + Math.abs(coord1.y - coord2.y);

// creates a map with the agent's manhattan distance to each coordinate
const getAgentMap = (agent) => {
  const agentCoord = { x: agent[0], y: agent[1] };
  const map = [];
  for (let x = 0; x < mapSize; x++) {
    map[x] = [];
    for (let y = 0; y < mapSize; y++) {
      map[x][y] = manhattanDistance(agentCoord, { x, y });
    }
  }
  return map;
};

const findSafePlaces = (agents) => {
  const maps = agents.map(agent => getAgentMap(agent));
  const masterMap = [];
  let safestDistance = 0;

  // merge agent maps with lowest distance
  for (let x = 0; x < mapSize; x++) {
    masterMap[x] = [];
    for (let y = 0; y < mapSize; y++) {
      const agentDistancesAtPoint = maps.map(map => map[x][y]);
      const closestAgentDistance = Math.min.apply(null, agentDistancesAtPoint);
      safestDistance = Math.max(safestDistance, closestAgentDistance);
      masterMap[x][y] = closestAgentDistance;
    }
  }

  // if agent is located at safest coordinate, no safe places.
  if (safestDistance === 0) {
    return [];
  }

  // find coordinates equal to safest distance
  const safestPlaces = [];
  for (let x = 0; x < mapSize; x++) {
    for (let y = 0; y < mapSize; y++) {
      if (masterMap[x][y] === safestDistance) {
        safestPlaces.push([x, y]);
      }
    }
  }
  return safestPlaces;
};

const adviceForAlex = (agents) => {
  const agentCoords = convertCoordinates(agents);
  if (agentCoords.length === 0) {
    return 'The whole city is safe for Alex! :-)';
  }
  const safePlaces = findSafePlaces(agentCoords).map(coord => toMapCoordinates(coord));
  if (safePlaces.length === 0) {
    return 'There are no safe locations for Alex! :-(';
  }
  return safePlaces;
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex,
};
