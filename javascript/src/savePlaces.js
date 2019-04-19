// This is where you implement your solution 
const convertCoordinates = (agents  = []) => {
  
  Array.isArray(agents) || (agents = [agents])

  return agents.map((coord, i) => {

    /** @type String */
    const xCoord_unparsed = coord[0]
    /** @type String */
    const yCoord_unparsed = (coord.length == 2) ? coord[1] : '' + coord[1] + coord[2]
    
    let xCoord = xCoord_unparsed.charCodeAt(0) - 65
    let yCoord = parseInt(yCoord_unparsed) - 1

    return [xCoord,yCoord]
  })
}

const findSafePlaces = (agents) => {
  
  /* create a map aka Distance Array (distArray) to store the Distance-to-Agent (distToAgent) Values */
  let distArray = Array(10).fill(0)
  for(let i = 0; i<10; i++) distArray[i] = Array(10).fill(0)

  let distToAgent = 1;
  let spotsToVisit = []
  let nextSpotsToVisit = []
  let safePlaces = []

  const isNotOutOfBounds = ([xCoord, yCoord]) => ( ! ((xCoord < 0) || (xCoord > 9) || (yCoord < 0) || (yCoord > 9)) )
  
  agents = agents.filter(isNotOutOfBounds)
  for (agent of agents){
    let [xCoord, yCoord] = agent
    distArray[xCoord][yCoord] = 'X'
  }

  /* No Agents must return an Array with ervery spot as a safe spot */
  if (agents.length == 0){
    for (let i=0; i<10; i++){
      for (let j=0; j<10; j++){
        safePlaces.push([i,j])
      }
    }

    return safePlaces
  }

  /* 100 Agents must return an empty Array with no safe spot */
  if (agents.length == 100){

    return []
  }

  spotsToVisit = agents

  do{
    for (spot of spotsToVisit){
      let [xCoord, yCoord] = spot

      for (direction of [[1,0],[0,1],[-1,0],[0,-1]]){
        if (isNotOutOfBounds([xCoord + direction[0], yCoord + direction[1]])){
          if (distArray[xCoord + direction[0]][yCoord + direction[1]] == 0){
            distArray[xCoord + direction[0]][yCoord + direction[1]] = distToAgent

            nextSpotsToVisit.push([xCoord + direction[0], yCoord + direction[1]])
          } 
        }
      }
    }

    safePlaces = spotsToVisit
    spotsToVisit = nextSpotsToVisit
    nextSpotsToVisit = []
    distToAgent++

  } while (spotsToVisit.length)

  return safePlaces
}

const adviceForAlex = (agents) => {

  const reConvertCoordinates = (agents  = []) => {
  
    Array.isArray(agents) || (agents = [agents])
  
    return agents.map((coord, i) => {
  
      const xCoord = coord[0]
      const yCoord = coord[1]
      
      let xCoord_alphanum = String.fromCharCode(xCoord + 65)
      let yCoord_alphanum = (yCoord+1).toString()
  
      return xCoord_alphanum + yCoord_alphanum
    })
  }

  agents = convertCoordinates(agents)
  let safePlaces = findSafePlaces(agents)
  safePlaces = reConvertCoordinates(safePlaces)

  return safePlaces.length == 100 ?
         'The whole city is safe for Alex! :-)' :
         safePlaces.length == 0 ?
         'There are no safe locations for Alex! :-(' :
         safePlaces
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
