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
