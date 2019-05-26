const NO_AGENTS_IN_CITY = "The whole city is safe for Alex! :-)";
const NO_SAFE_LOCATIONS = "There are no safe locations for Alex! :-(";

// This is where you implement your solution
const convertCoordinates = agents => {
  const agentMapped = agents.map(agent => {
    return [
      agent.substring(0).charCodeAt(0) - 65,
      parseInt(agent.substring(1), 10) - 1
    ];
  });
  return agentMapped;
};

const findSafePlaces = agents => {
  return "findSafePlaces";
};

const adviceForAlex = agents => {
  //1. convert agents to coordinates
  const agentCoordinates = convertCoordinates(agents);
  return "adviceForAlex";
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
