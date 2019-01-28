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

const citySizeX = 10;
const citySizeY = 10;

const findSafePlaces = (agents) => {
  const distanceUpperLimit = citySizeX + citySizeY;
  var cityArray = new Array(citySizeX).fill(null).map(()=>new Array(citySizeY).fill(distanceUpperLimit));
  console.log(cityArray);

  var x, y, i;

  // Iterate over fields and calculate their minimum distance to each agent
  for (x = 0; x < citySizeX; x++) {
    for (y = 0; y < citySizeY; y++) {
      for (i = 0; i < agents.length; i++) {
        const distanceToAgentX = Math.abs(agents[i][0] - x);
        const distanceToAgentY = Math.abs(agents[i][1] - y);
        const distanceToAgent = distanceToAgentX + distanceToAgentY;
        const minDistanceToAgents = cityArray[x][y];
        if (distanceToAgent < minDistanceToAgents) {
          cityArray[x][y] = distanceToAgent;
        }
      }
    }
  }
  console.log(cityArray);

  // Find maximum distance value (safe distance)
  var safeDistance = 0;
  for (x = 0; x < citySizeX; x++) {
    for (y = 0; y < citySizeY; y++) {
      if (cityArray[x][y] > safeDistance) {
        safeDistance = cityArray[x][y];
      }
    }
  }

  // Identify safe places (indices with values equal to safe distance)
  var safePlaces = [];

  for (x = 0; x < citySizeX; x++) {
    for (y = 0; y < citySizeY; y++) {
      if (cityArray[x][y] === safeDistance) {
        if (safePlaces === []) {
          safePlaces = [[x, y]];
        } else {
          safePlaces.push([x, y]);
        }
      }
    }
  }
  console.log(safePlaces);
  return safePlaces;
}


const adviceForAlex = (agents) => {
  return "adviceForAlex"
}


module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
