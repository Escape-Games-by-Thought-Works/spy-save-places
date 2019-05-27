const NO_AGENTS_IN_CITY = "The whole city is safe for Alex! :-)";
const NO_SAFE_LOCATIONS = "There are no safe locations for Alex! :-(";

const gridsX = "J".charCodeAt(0) - 65;
const gridsY = 9;

let maxDistanceUntilNow;
let safePlaces = [];

// This is where you implement your solution
const convertCoordinates = agents => {
  return (agentMapped = agents.map(agent => {
    return [
      agent.substring(0).charCodeAt(0) - 65,
      parseInt(agent.substring(1), 10) - 1
    ];
  }));
};

const findSafePlaces = agents => {
  for (var i = 0; i <= gridsX; i++) {
    let _safePlaces = [];
    for (var j = 0; j <= gridsY; j++) {
      distanceToCloseAgent = checkDistanceToAgents(agents, [i, j]);

      if (!maxDistanceUntilNow) {
        maxDistanceUntilNow = distanceToCloseAgent;
        _safePlaces.push([i, j]);
        continue;
      }

      if (
        distanceToCloseAgent > maxDistanceUntilNow ||
        distanceToCloseAgent == maxDistanceUntilNow
      ) {
        if (distanceToCloseAgent > maxDistanceUntilNow) {
          _safePlaces.length = 0;
        }

        maxDistanceUntilNow = distanceToCloseAgent;
        _safePlaces.push([i, j]);
      }
    }
    if (_safePlaces.length !== 0) {
      addToSafePlaces(_safePlaces);
    }
  }
  // console.log(safePlaces);
  return safePlaces;
};

const addToSafePlaces = _safePlaces => {
  _safePlaces.forEach(_safePlace => safePlaces.push(_safePlace));
};

const checkDistanceToAgents = (agents, location) => {
  let minDistance;

  for (var k = 0; k <= agents.length - 1; k++) {
    let agent = agents[k];

    if (agent[0] == location[0] && agent[1] == location[1]) {
      // problem here
      continue;
    } //same as agent

    distToAgent =
      Math.abs(agent[0] - location[0]) + Math.abs(agent[1] - location[1]);

    if (1 == location[0] && 1 == location[1]) {
      console.log(distToAgent, location, agent);
    }
    if (minDistance) {
      distToAgent = Math.min(minDistance, distToAgent);
    }

    minDistance = distToAgent;
  }
  // console.log("distToAgent", distToAgent, location);

  return distToAgent;
};

const adviceForAlex = agents => {
  //1. convert agents to coordinates
  const agentCoordinates = convertCoordinates(agents);

  if (agentCoordinates.length == 0) {
    return NO_AGENTS_IN_CITY;
  }

  return "adviceForAlex";
};

const testing = () => {
  const agents = [[1, 1], [3, 5], [4, 8], [7, 3], [7, 8], [9, 1]];

  findSafePlaces(agents);
};

testing();

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
