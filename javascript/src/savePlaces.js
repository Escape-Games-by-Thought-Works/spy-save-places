// This is where you implement your solution 
const convertCoordinates = (agents) => {
  let aCoords = [];
  
  if (Array.isArray(agents)) {
    aCoords = agents
      .map(sAgent => sAgent.match(/([A-J])(\d+)/))
      .map(aMatches => [aMatches[1].charCodeAt() - 65, aMatches[2] - 1]);
  }

  return aCoords;
}

const findClosestAgentDistance = (x, y, aAgentCoords) => {
  let aAgentDistances = aAgentCoords.map(aAgentCoord => Math.abs(x - aAgentCoord[0]) + Math.abs(y - aAgentCoord[1])); 
  console.log(aAgentDistances);
  console.log(Math.min(...aAgentDistances));
  return Math.min(...aAgentDistances);
}

const findSafePlaces = (agents) => {
  let aSafePlaces = [];
  let iSafeDistance = 1;

  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 10; j++) {
      let iClosestAgentDistance = findClosestAgentDistance(i, j, agents);
      if (iClosestAgentDistance > iSafeDistance) {
        // increase what distance we consider a SAFE distance
        iSafeDistance = iClosestAgentDistance;
        aSafePlaces = [[i, j]];
      } else if (iClosestAgentDistance === iSafeDistance) {
        // add location to safe places
        aSafePlaces.push([i, j]);
      }
    }
  }

  return aSafePlaces;
}

const adviceForAlex = (agents) => {
  return "adviceForAlex"
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
