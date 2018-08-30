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
