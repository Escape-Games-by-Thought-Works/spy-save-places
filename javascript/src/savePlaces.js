const cordX = ["1","2","3","4","5","6","7","8","9","10"];
const cordY = ["A","B","C","D","E","F","G","H","I","J"];
// This is where you implement your solution 
const convertCoordinates = (agents) => {
  coordinates = [];
  agents.forEach(agent => {
    agentY = agent.substring(0,1);
    agentX = agent.substring(1);
    coordinates.push([cordY.indexOf(agentY),cordX.indexOf(agentX)])  
  });
  
  return coordinates;
}

const findSafePlaces = (agents) => { 
  let gridWithDistances = [];
  let safePlaces = [];
  let maxDistance = 0;

  for (let iY = 0; iY < cordY.length; iY++) {
    gridWithDistances.push([]);
    
    for (let iX = 0; iX < cordX.length; iX++) {
      gridWithDistances[iY].push([]);  
      gridWithDistances[iY][iX] = Number.MAX_SAFE_INTEGER;  
      agents.forEach(agent => {
        if (!((agent[0] == -1) || (agent[1] == -1))) // If there a point outside of the grid the convertCoordinates function will return -1
        {
          let currentDistance = Math.abs(iY-agent[0]) + Math.abs(iX-agent[1]);
          gridWithDistances[iY][iX] = Math.min(gridWithDistances[iY][iX],currentDistance);
        }
     }); 

     maxDistance = Math.max(maxDistance,gridWithDistances[iY][iX]);

    }
  }
  if (maxDistance > 0) {
    for (let iY = 0; iY < cordY.length; iY++) {
      for (let iX = 0; iX < cordX.length; iX++) {
        if (maxDistance === gridWithDistances[iY][iX] )
        safePlaces.push([iY,iX])
      }
    }
  }


  return safePlaces;
}

const adviceForAlex = (agents) => {
  let output = undefined; // to have only one return ....
  const mappedCoordinates = convertCoordinates(agents);
  const safePlaces = findSafePlaces(mappedCoordinates);

  if (safePlaces.length == 0)
    output = 'There are no safe locations for Alex! :-(';
  else if (safePlaces.length == cordY.length * cordX.length )
    output= 'The whole city is safe for Alex! :-)';
  else if (safePlaces.length > 0)
  {
    // Map array format to output format
    output = [];
    safePlaces.forEach(safePlace => {
      output.push(cordY[safePlace[0]].concat(cordX[safePlace[1]]));
    });
  }
  return output;
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
