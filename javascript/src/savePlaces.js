const NO_AGENTS_IN_CITY = "The whole city is safe for Alex! :-)";
const NO_SAFE_LOCATIONS = "There are no safe locations for Alex! :-(";

const gridsX = "J".charCodeAt(0) - 65;
const gridsY = 9;

const isValid = agentCoord => {
  if (agentCoord[0] > gridsX || agentCoord[1] > gridsY + 1) {
    return false;
  }
  return agentCoord;
};

const convertCoordinates = agents => {
  let agentMapped = agents.map(agent => {
    let agentCoord = [
      agent.substring(0).charCodeAt(0) - 65,
      parseInt(agent.substring(1), 10) - 1
    ];

    return isValid(agentCoord) ? agentCoord : false;
  });

  return agentMapped.filter(agent => agent !== false);
};

const createTheCity = () => {
  let matrix = [];
  for (var i = 0; i <= gridsX; i++) {
    for (var j = 0; j <= gridsY; j++) {
      matrix.push([i, j]);
    }
  }
  return matrix;
};

const isAgentLocation = (location, agents) => {
  return JSON.stringify(agents).includes(location);
};

const findSafePlaces = agents => {
  let safePlaces = [];
  let maxDistanceUntilNow = 0;

  let locations = createTheCity().filter(
    location => !isAgentLocation(location, agents)
  );

  locations.forEach(location => {
    let distanceToCloseAgent = checkDistanceToAgents(agents, location);

    if (
      distanceToCloseAgent > maxDistanceUntilNow ||
      distanceToCloseAgent == maxDistanceUntilNow
    ) {
      if (distanceToCloseAgent == maxDistanceUntilNow) {
        safePlaces.push(location);
      } else if (distanceToCloseAgent > maxDistanceUntilNow) {
        safePlaces = [];
        safePlaces.push(location);
        maxDistanceUntilNow = distanceToCloseAgent;
      }
    }
  });
  return safePlaces;
};

const checkDistanceToAgents = (agents, location) => {
  let minDistance;

  for (var k = 0; k <= agents.length - 1; k++) {
    let agent = agents[k];

    distToAgent =
      Math.abs(agent[0] - location[0]) + Math.abs(agent[1] - location[1]);

    if (minDistance !== undefined) {
      distToAgent = Math.min(minDistance, distToAgent);
    }

    minDistance = distToAgent;
  }

  return distToAgent;
};

const mapToAddress = locations => {
  return locations.map(
    location => String.fromCharCode(location[0] + 65) + (location[1] + 1)
  );
};

const adviceForAlex = agents => {
  const agentCoordinates = convertCoordinates(agents);

  if (agentCoordinates.length == 0) {
    return NO_AGENTS_IN_CITY;
  }

  const safeLocations = findSafePlaces(agentCoordinates);
  if (safeLocations.length == 0) {
    return NO_SAFE_LOCATIONS;
  }

  return mapToAddress(safeLocations);
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
