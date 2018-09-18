const gridSize = 10;

// This is where you implement your solution
const convertCoordinates = stringAgents => {
// convert string index to numerical index  ['A1'] -> [0,0]
  const stringToNumArray = stringCoordinate => {
    const column = stringCoordinate.slice(1) - 1; // start counting from 0
    const row = stringCoordinate.charCodeAt(0) - 65; //transform char to index
    return [row, column];
  };  
  return stringAgents.map(stringToNumArray);
};

const findSafePlaces = numAgents => {
  //construct all combinatorial possible place coordinates for a 10x10 grid
  let construcedPlaces = [];
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      construcedPlaces.push({ coordinates: [i, j] });
    }
  }


  //filer the places with the maximum distance
  const placesMaxDistances = (place, _ , construcedPlaces) => {
    const maxDistance = construcedPlaces.reduce(
      (max, place) => (place.distanceToNearestAgent > max
        ? place.distanceToNearestAgent
        : max), 
      0);
    if (maxDistance === 0) return false;
    return place.distanceToNearestAgent === maxDistance;
  };  

  const addDistanceToNearestAgent = (place, agentPositions) => {
    const distanceToClosestAgent = (agents, coordinate) => {
      //calculate the abs distance (steps)
      const getDistance = (agent, place) => {
        const distCol = Math.abs(place.coordinates[0] - agent[0]);
        const distRow = Math.abs(place.coordinates[1] - agent[1]);
        return distCol + distRow;
      };
      return agents
        .map(agent => getDistance(agent, coordinate))
        .reduce((min, distance) => distance < min ? distance : min); //return min distance
        
    }
    place.distanceToNearestAgent = distanceToClosestAgent(agentPositions, place);
    return place;
  };

  return construcedPlaces
    .map(place => addDistanceToNearestAgent(place, numAgents))
    .filter(placesMaxDistances)
    .map(place => place.coordinates);
};

const adviceForAlex = stringAgents => {
  //is coordinate inside or ouside the city?
  isInsideTheCity = coordinate => {
    const row = coordinate.slice(0, 1);
    const col = coordinate.slice(1);
    return row.match(/^[A-J]$/) && col >= 1 && col <= 10;
  };  

  // convert numerical index to string index  [0,0] -> ['A1']
  const numToStringCoordinate = numCoordinate => {
    const row = String.fromCharCode(numCoordinate[0] + 65);
    const column = numCoordinate[1] + 1;
    return row + column;
  };
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


module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
