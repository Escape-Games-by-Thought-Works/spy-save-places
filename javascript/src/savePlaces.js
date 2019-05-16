// This is where you implement your solution
const convertCoordinates = agents => {
  const xCoordinates = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
  const yCoordinates = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"];
  if (!agents) {
    throw new Error("Not a valid agent!");
  }
  if (agents.length === 0) {
    return [];
  } else {
    return agents.map(agent => {
      const secondCoordinate = agent.substr(1, agent.length - 1);
      return [
        xCoordinates.indexOf(agent[0]),
        yCoordinates.indexOf(secondCoordinate)
      ];
    });
  }
};

const findSafePlaces = agents => {
  return "findSafePlaces";
};

const adviceForAlex = agents => {
  return "adviceForAlex";
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
