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
  var cityArray = new Array(citySizeX).fill(null).map(()=>new Array(citySizeY).fill(null));
  console.log(cityArray);
  var x, y, i;

  // Add agent locations
  for (x = 0; x < citySizeX; x++) {
    for (y = 0; y < citySizeY; y++) {
      for (i = 0; i < agents.length; i++) {
        if (x === agents[i][0] && y === agents[i][1]) {
          cityArray[x][y] = 0;
        }
      }
    }
  }
  // console.log(cityArray);

  var maximumDistance = 0;

  // Walking from left to right
  const leftDistances = calculateLeftDistances(cityArray, agents);
  // console.log(leftDistances);

  // Walking from right to left
  const rightDistances = calculateRightDistances(cityArray, agents);
  // console.log(rightDistances);

  // Walking from top to bottom
  const topDistances = calculateTopDistances(cityArray, agents);
  // console.log(topDistances);

  // Walking from bottom to top
  const bottomDistances = calculateBottomDistances(cityArray, agents);
  // console.log(bottomDistances);

  // Calculate minimum distances to agents
  const minDistances = calculateMinDistances(leftDistances, rightDistances, topDistances, bottomDistances);
  // console.log(minDistances);

  // Find maximum distance from agent
  const safeDistance = Math.max(...minDistances);
  // console.log(safeDistance);

  var safePlaces = [];

  for (var x = 0; x < citySizeX; x++) {
    for (var y = 0; y < citySizeY; y++) {
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


function calculateLeftDistances(cityArray, agents) {
  var agentDistanceLeft;
  for (x = 0; x < citySizeX; x++) {
    agentDistanceLeft = 0;
    var agentDiscoveredInLine = false;
    for (y = 0; y < citySizeY; y++) {
      if (agentDiscoveredInLine) {
        agentDistanceLeft++;
      }

      for (i = 0; i < agents.length; i++) {

        if (x === agents[i][0] && y === agents[i][1]) {
          agentDiscoveredInLine = true;
          agentDistanceLeft = 0;
        }

      }
      cityArray[x][y] = agentDistanceLeft;
    }
  }
  return cityArray;
}

function calculateRightDistances(cityArray, agents) {
  var agentDistanceRight = 0;
  for (var x = 0; x < citySizeX; x++) {
    agentDistanceRight = 0;
    var agentDiscoveredInLine = false;
    for (var y = citySizeY - 1; y >= 0; y--) {
      if (agentDiscoveredInLine) {
        agentDistanceRight++;
      }
      for (var i = 0; i < agents.length; i++) {

        if (x === agents[i][0] && y === agents[i][1]) {
          agentDiscoveredInLine = true;
          agentDistanceRight = 0;
        }

      }
      cityArray[x][y] = agentDistanceRight;
    }
  }
  return cityArray;
}

function calculateTopDistances(cityArray, agents) {
  var agentDistanceTop = 0;
  for (var y = 0; y < citySizeY; y++) {
    agentDistanceTop = 0;
    var agentDiscoveredInColumn = false;
    for (var x = 0; x < citySizeX; x++) {
      if (agentDiscoveredInColumn) {
        agentDistanceTop++;
      }
      for (var i = 0; i < agents.length; i++) {

        if (x === agents[i][0] && y === agents[i][1]) {
          agentDiscoveredInColumn = true;
          agentDistanceTop = 0;
        }

      }
      cityArray[x][y] = agentDistanceTop;
    }
  }
  return cityArray;
}

function calculateBottomDistances(cityArray, agents) {
  var agentDistanceBottom = 0;
  for (var y = 0; y < citySizeY; y++) {
    agentDistanceBottom = 0;
    var agentDiscoveredInColumn = false;
    for (var x = citySizeX - 1; x >= 0; x--) {
      if (agentDiscoveredInColumn) {
        agentDistanceBottom++;
      }
      for (var i = 0; i < agents.length; i++) {

        if (x === agents[i][0] && y === agents[i][1]) {
          agentDiscoveredInColumn = true;
          agentDistanceBottom = 0;
        }

      }
      cityArray[x][y] = agentDistanceBottom;
    }
  }
  return cityArray;
}

function calculateMinDistances(leftDistances, rightDistances, topDistances, bottomDistances) {
  var cityArray = new Array(citySizeX).fill(null).map(()=>new Array(citySizeY).fill(null));
  for (var x = 0; x < citySizeX; x++) {
    for (var y = 0; y < citySizeY; y++) {
      cityArray[x][y] = Math.min(leftDistances[x][y], rightDistances[x][y], topDistances[x][y], bottomDistances[x][y]);
    }
  }
  return cityArray;
}

const adviceForAlex = (agents) => {
  return "adviceForAlex"
}



module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
