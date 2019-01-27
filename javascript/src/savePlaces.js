// This is where you implement your solution 
const convertCoordinates = (agents) => {
  const numberOfAgents = agents.length;
  if (numberOfAgents === 0) {
    return [];
  } else {
    var convertedAgents = [];
    for (var i = 0; i < numberOfAgents; i++) {
      var currentAgent = Array(2);
      currentAgent[0] = agents[i].charCodeAt(0) - 'A'.charCodeAt(0);

      if (agents[i].length > 2) {
        currentAgent[1] = (agents[i].charAt(1) + agents[i].charAt(2)).valueOf() - 1;
      } else {
        currentAgent[1] = agents[i].charAt(1).valueOf() - 1;
      }

      if (i === 0) {
        convertedAgents = [currentAgent];
      } else {
        convertedAgents[i] = currentAgent;
      }
    }
    return convertedAgents;
  }
}

const findSafePlaces = (agents) => {
  var cityArray = Array(10, 10);
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
