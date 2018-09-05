const init = 99;

//    1 2 3 4 ... 10
// A
// B
// C
// D
// ...
const createGrid = () => {
  const xs = {
    "1": init,
    "2": init,
    "3": init,
    "4": init,
    "5": init,
    "6": init,
    "7": init,
    "8": init,
    "9": init,
    "10": init
  };
  const ys = {
    A: { ...xs },
    B: { ...xs },
    C: { ...xs },
    D: { ...xs },
    E: { ...xs },
    F: { ...xs },
    G: { ...xs },
    H: { ...xs },
    I: { ...xs },
    J: { ...xs }
  };
  return ys;
};

const convertCoordinates = agents => {
  const ys = createGrid();
  const coordinates = [];

  agents.forEach(agent => {
    const agentXKey = agent.substring(1);
    const agentYKey = agent.substring(0, 1);

    if (!ys[agentYKey] || !ys[agentYKey][agentXKey]) {
      // console.log("ignore agent", agent);
      return;
    }

    coordinates.push([
      Object.keys(ys).indexOf(agentYKey),
      Object.keys(ys[agentYKey]).indexOf(agentXKey)
    ]);
  });

  return coordinates;
};

const findSafePlaces = agents => {
  const ys = createGrid();

  agents.forEach(agent => {
    const agentYKey = Object.keys(ys)[agent[0]];
    const agentXKey = Object.keys(ys[agentYKey])[agent[1]];

    if (!ys[agentYKey] || !ys[agentYKey][agentXKey]) {
      // console.log("ignore agent", agent, agentYKey, agentXKey);
      return;
    }

    for (const yKey in ys) {
      for (const xKey in ys[yKey]) {
        const xDistance = parseInt(agentXKey) - parseInt(xKey);
        const yDistance = agentYKey.charCodeAt(0) - yKey.charCodeAt(0);
        const distance = Math.abs(xDistance) + Math.abs(yDistance);
        ys[yKey][xKey] = Math.min(distance, ys[yKey][xKey]);
      }
    }
  });

  let maxDistance = 0;

  for (const yKey in ys) {
    for (const xKey in ys[yKey]) {
      maxDistance = Math.max(maxDistance, ys[yKey][xKey]);
    }
  }

  const safe = [];
  for (const yKey in ys) {
    for (const xKey in ys[yKey]) {
      if (ys[yKey][xKey] === maxDistance) {
        safe.push([
          Object.keys(ys).indexOf(yKey),
          Object.keys(ys[yKey]).indexOf(xKey)
        ]);
      }
    }
  }

  return safe;
};

const adviceForAlex = agents => {
  const ys = createGrid();

  agents.forEach(agent => {
    const agentXKey = agent.substring(1);
    const agentYKey = agent.substring(0, 1);

    if (!ys[agentYKey] || !ys[agentYKey][agentXKey]) {
      // console.log("ignore agent", agent);
      return;
    }

    for (const yKey in ys) {
      for (const xKey in ys[yKey]) {
        const xDistance = parseInt(agentXKey) - parseInt(xKey);
        const yDistance = agentYKey.charCodeAt(0) - yKey.charCodeAt(0);
        const distance = Math.abs(xDistance) + Math.abs(yDistance);
        ys[yKey][xKey] = Math.min(distance, ys[yKey][xKey]);
      }
    }
  });

  let maxDistance = 0;

  for (const yKey in ys) {
    for (const xKey in ys[yKey]) {
      maxDistance = Math.max(maxDistance, ys[yKey][xKey]);
    }
  }

  const safe = [];
  for (const yKey in ys) {
    for (const xKey in ys[yKey]) {
      if (ys[yKey][xKey] === maxDistance) {
        safe.push(yKey + xKey);
      }
    }
  }

  if (maxDistance === 0) {
    return "There are no safe locations for Alex! :-(";
  } else if (maxDistance === init) {
    return "The whole city is safe for Alex! :-)";
  }

  return safe;
};

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
};
