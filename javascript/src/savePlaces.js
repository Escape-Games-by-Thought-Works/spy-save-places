// This is where you implement your solution
const SIZE = 10;

const convertCoordinates = (agents) => {
  coords = [];
  agents.forEach(agent => {
    x = agent.charCodeAt() - 'A'.charCodeAt();
    if (x < 0 || x >= SIZE) return;
    y = Number(agent.slice(1)) - 1;
    if (y < 0 || y >= SIZE) return;
    coords.push([x, y]);
  });
  return coords;
};

const findSafePlaces = (agents) => safeSpaces(distanceMap(agents));

const adviceForAlex = (agents) => {
  const spaces = findSafePlaces(convertCoordinates(agents));
  if (spaces.length == 0) return 'There are no safe locations for Alex! :-(';
  if (spaces.length == SIZE * SIZE) return 'The whole city is safe for Alex! :-)';
  return spaces.map(xy => `${String.fromCharCode(xy[0] + 'A'.charCodeAt())}${xy[1] + 1}`);
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};

const MAX_DIST = (2 * SIZE);

const distanceMap = (agents) => {
  const d = Array.from(Array(SIZE), () => Array.from(Array(SIZE), () => MAX_DIST));
  if (agents.length == 0) return d;
  for (let x = 0; x < SIZE; x++) {
    for (let y = 0; y < SIZE; y++) {
      distances = agents.map(agent => taxiCabDistance(agent, x, y));
      d[x][y] = Math.min(d[x][y], ...distances);
    }
  }
  return d;
};

const taxiCabDistance = (agent, x, y) => Math.abs(agent[0] - x) + Math.abs(agent[1] - y);

const safeSpaces = (distanceMap) => {
  let maxDist = Math.max(...distanceMap.map(row => Math.max(...row)));
  if (maxDist <= 0) return [];
  spaces = [];
  for (let x = 0; x < SIZE; x++) {
    for (let y = 0; y < SIZE; y++) {
      if (distanceMap[x][y] == maxDist) spaces.push([x, y]);
    }
  }
  return spaces;
};
