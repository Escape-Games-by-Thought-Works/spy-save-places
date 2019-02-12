const cityArea = 10 * 10;

// Second Level
const calculateDistance = ([ entity1X, entity1Y ], [ entity2X, entity2Y ]) =>
  Math.abs(entity1X - entity2X) + Math.abs(entity1Y - entity2Y);

const calculateCoordinates = (linearIndex) => [ Math.floor(linearIndex / 10), linearIndex % 10 ];

const isAgentInCity = (agentCoordinates) => {
  if (agentCoordinates.some(c => c < 0)) return false;
  if (agentCoordinates.some(c => c > 10)) return false;
  return true;
};

const isAgentCloserTo = (currentLocation) => (previousMinDistance, agent) => {
    const distance = calculateDistance(currentLocation, agent);
    return distance < previousMinDistance ? distance : previousMinDistance
};


const findSafePlaces = (agents) => {
  const agentsInCity = agents.filter(isAgentInCity);

  const { result } = new Array(cityArea).fill().reduce(({ maxDistance, result }, _, i) => {
    const currentLocation = calculateCoordinates(i);

    const distance = agentsInCity.reduce(isAgentCloserTo(currentLocation), cityArea);

    if (maxDistance > distance)
      return { maxDistance, result };
    if (maxDistance < distance)
      return { maxDistance: distance, result: [ currentLocation ] };
    if (maxDistance === distance)
      return { maxDistance, result: [ ...result, currentLocation ] };
  }, { maxDistance: 1, result: [] });

  return result;
}

module.exports = {
    cityArea,
    findSafePlaces
};

