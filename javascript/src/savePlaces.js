// This is where you implement your solution
const xCoordinates = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
const yCoordinates = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];

const convertCoordinates = agents => {
  if (!agents) {
    throw new Error("Not a valid agent!");
  }
  if (agents.length) {
    return agents.map(agent => [
        xCoordinates.indexOf(agent[0]),
        yCoordinates.indexOf(agent.substr(1, agent.length - 1))
      ]);
  } else {
    return [];
  }
};

const convertSafePlaces = coordinates => {
  return coordinates.map(coordinate => xCoordinates[coordinate[0]] + yCoordinates[coordinate[1]]);
};

const findSafePlaces = agents => {
  const allCoordinatesWithoutAgents = coordinateSystem(10)
      .filter(coordinate => !coordinateIsInArray(coordinate, agents));
  if (allCoordinatesWithoutAgents.length) {
    const coordinatesRelativeToAgents = allCoordinatesWithoutAgents
        .map(coordinate => withClosestAgent(coordinate, agents));
    const maxDistanceToAnAgent = coordinatesRelativeToAgents
        .map(spot => spot.distanceToClosestAgent)
        .reduce((distance1, distance2) => Math.max(distance1, distance2));
    return coordinatesRelativeToAgents
        .filter(spot => spot.distanceToClosestAgent === maxDistanceToAnAgent)
        .map(spot => spot.coordinate);
  } else {
    return [];
  }
};

const withClosestAgent = (coordinate, agents) => {
    const distanceToClosestAgent = agents
        .map(agent => manhattanDistance(coordinate, agent))
        .reduce((firstDistance, secondDistance) => Math.min(firstDistance, secondDistance));
    return {coordinate: coordinate, distanceToClosestAgent: distanceToClosestAgent};
};

const coordinateSystem = (size) => {
  let coordinates = [];
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      coordinates.push([i, j]);
    }
  }
  return coordinates;
};

const manhattanDistance = (firstPoint, secondPoint) => {
  return Math.abs(secondPoint[0] - firstPoint[0]) +
      Math.abs(secondPoint[1] - firstPoint[1]);
};

const adviceForAlex = agents => {
  if (!agents.length || nobodyOnPatrol(agents)) {
    return "The whole city is safe for Alex! :-)"
  }
  let safePlaces = findSafePlaces(convertCoordinates(agents));
  if (!safePlaces.length) {
    return "There are no safe locations for Alex! :-(";
  } else {
    return convertSafePlaces(safePlaces);
  }
};

const coordinateIsInArray = (coordinate, array) => {
  return array.map(arrayElement => JSON.stringify(arrayElement)).includes(JSON.stringify(coordinate));
};

const nobodyOnPatrol = (agents) => {
  const agentCoordinates = convertCoordinates(agents);
  const cityCoordinates = coordinateSystem(10);
  return agentCoordinates.filter(coordinate => coordinateIsInArray(coordinate, cityCoordinates)).length === 0;
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
