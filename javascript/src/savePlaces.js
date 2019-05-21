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

const findSafePlaces = (agents) => {
  return "findSafePlaces"
}

const adviceForAlex = (agents) => {
  return "adviceForAlex"
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
