const convertFromBoardCoordinates = (sBoardCoords) => {
  let aMatches = sBoardCoords.match(/([A-J])(\d+)/)
  return [aMatches[1].charCodeAt() - 65, aMatches[2] - 1];
}

const convertToBoardCoordinates = (aCoords) => {
  return String.fromCharCode(aCoords[0] + 65) + (aCoords[1] + 1);
}

const convertCoordinates = (agents) => {
  let aCoords = [];
  
  if (Array.isArray(agents)) {
    aCoords = agents
      .map(sAgent => convertFromBoardCoordinates(sAgent))
      .filter(aCoord => aCoord[0] >= 0 && aCoord[0] < 10 && aCoord[1] >= 0 && aCoord[1] < 10);
  }

  return aCoords;
}

const findClosestAgentDistance = (x, y, aAgentCoords) => {
  let aAgentDistances = aAgentCoords.map(aAgentCoord => Math.abs(x - aAgentCoord[0]) + Math.abs(y - aAgentCoord[1])); 
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
  let aSafeCoords = findSafePlaces(convertCoordinates(agents)).map(convertToBoardCoordinates);

  // no agents
  if (aSafeCoords.length === 100) {
    return "The whole city is safe for Alex! :-)";
  }

  // city filled with agents
  if (aSafeCoords.length === 0) {
    return "There are no safe locations for Alex! :-(";
  }

  return aSafeCoords;
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
