const gridSize = 10;

// This is where you implement your solution
const convertCoordinates = stringAgents => {
  return stringAgents.map(stringToNumArray);
};

const findSafePlaces = numAgents => {
  const construcedPlaces = constructAllPlaces();
  return construcedPlaces
    .map(place => addDistanceToNearestAgent(place, numAgents))
    .filter(placesMaxDistances)
    .map(place => place.coordinates);
};

const adviceForAlex = stringAgents => {
  const allowedAgents = stringAgents.filter(
    isInsideTheCity
  );

  const numAgents = convertCoordinates(allowedAgents);

  if (numAgents.length === 0) {
    return "The whole city is safe for Alex! :-)";
  }

  const safePlaces = findSafePlaces(numAgents);
  if (safePlaces.length === 0)
    return "There are no safe locations for Alex! :-(";
  return safePlaces.map(numToStringCoordinate);
};


// convert numerical index to string index  [0,0] -> ['A1']
const numToStringCoordinate = numCoordinate => {
  const row = String.fromCharCode(numCoordinate[0] + 65);
  const column = numCoordinate[1] + 1;
  return row + column;
};

// convert string index to numerical index  ['A1'] -> [0,0]
const stringToNumArray = stringCoordinate => {
  const column = stringCoordinate.slice(1) - 1; // start counting from 0
  const row = stringCoordinate.charCodeAt(0) - 65; //transform char to index
  return [row, column];
};




//calculate the abs distance (steps)
const getDistance = (agent, place) => {
  return (
    Math.abs(place.coordinates[0] - agent[0]) +
    Math.abs(place.coordinates[1] - agent[1])
  );
};
//is coordinate inside or ouside the city?
isInsideTheCity = coordinate => {
  const row = coordinate.slice(0, 1);
  const col = coordinate.slice(1);
  return row.match(/^[A-J]$/) && col >= 1 && col <= 10;
};


const getDistanceToClosestAgent = (agents, coordinate) => {
  return agents
    .map(agent => getDistance(agent, coordinate))
    .reduce(minDistance);
};


const addDistanceToNearestAgent = (place, agentPositions) => {
  place.distanceToNearestAgent = getDistanceToClosestAgent(
    agentPositions,
    place
  );
  return place;
};

//return the minimum distance
const minDistance = (min, distance) => {
  return distance < min ? distance : min;
};


//construct all combinatorial possible place coordinates for a 10x10 grid
const constructAllPlaces = () => {
  let construcedPlaces = [];
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      construcedPlaces.push({ coordinates: [i, j] });
    }
  }
  return construcedPlaces;
};

//filer the places with the maximum distance
const placesMaxDistances = (place, _ , construcedPlaces) => {
  const maxDistance = construcedPlaces.reduce(getMaxDistance, 0);
  if (maxDistance === 0) return false;
  return place.distanceToNearestAgent === maxDistance;
};

const getMaxDistance = (max, place) => {
  return place.distanceToNearestAgent > max
    ? place.distanceToNearestAgent
    : max;
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
