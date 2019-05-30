// This is where you implement your solution
const convertCoordinates = agents => {
  let result = [];
  for (let i = 0; i < agents.length; i++) {
    let first = agents[i].charCodeAt(0) - 65;
    let second = parseInt(agents[i].substring(1)) - 1;
    result.push([first, second]);
  }
  return result;
};

const findSafePlaces = agents => {
  const checkedAgents = checkAgents(agents);
  let result = [];
  let maxDist = -1;
  for (let x = 0; x < 10; x++) {
    for (let y = 0; y < 10; y++) {
      const place = [x, y];

      const min = minDistance(place, checkedAgents);
      if (min == 0) {
        // agent is on this place
      } else {
        if (min > maxDist) {
          // rest result if we found a place which is better
          maxDist = min;
          result = [];
        }

        if (min == maxDist) {
          result.push(place);
        }
      }
    }
  }
  return result;
};

const adviceForAlex = agents => {
  let coor = convertCoordinates(agents);
  let safe = findSafePlaces(coor);

  if (safe.length == 100) {
    return "The whole city is safe for Alex! :-)";
  } else if (safe.length == 0) {
    return "There are no safe locations for Alex! :-(";
  }

  return convertCoordinatesBack(safe);
};

// ------------------------------------------------------------------------------------------------------------

const convertCoordinatesBack = agents => {
  let result = [];
  for (let i = 0; i < agents.length; i++) {
    result.push(String.fromCharCode(65 + agents[i][0]) + (agents[i][1] + 1));
  }
  return result;
};

const checkAgents = agents => {
  let result = [];
  for (let i = 0; i < agents.length; i++) {
    if (
      agents[i][0] >= 0 &&
      agents[i][0] <= 10 &&
      agents[i][1] >= 0 &&
      agents[i][1] <= 10
    )
      result.push(agents[i]);
  }
  return result;
};

const minDistance = (place, locations) => {
  let min = Number.MAX_VALUE;
  for (let i = 0; i < locations.length; i++) {
    let dist = distance(place, locations[i]);
    if (dist < min) {
      min = dist;
    }
  }
  return min;
};

const distance = (coor0, coor1) => {
  let xd = Math.abs(coor0[0] - coor1[0]);
  let yd = Math.abs(coor0[1] - coor1[1]);
  return xd + yd;
};

// ------------------------------------------------------------------------------------------------------------

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
