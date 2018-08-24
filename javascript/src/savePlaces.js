// This is where you implement your solution 
const convertCoordinates = (alphaNumericAgents) => {
  return alphaNumericAgents
    .map(convertAlphaNumericToIndexedCoordinate)
}

const findSafePlaces = (indexedAgents) => {
  const allPlaces = createAllPlaces();
  return allPlaces
    .map( place => addDistanceToNearestAgent(place, indexedAgents) )
    .filter(onlyPlacesWithMaxDistance)
    .map(place => place.coordinates)
}

const adviceForAlex = (alphaNumericAgents) => {
  const allowedAgents = alphaNumericAgents
    .filter(onlyAllowedCoordinatesInsideTheCity)

  const indexedAgents = convertCoordinates(allowedAgents)

  if (indexedAgents.length === 0) {
    return "The whole city is safe for Alex! :-)"
  }

  const safePlaces = findSafePlaces(indexedAgents)

  if (safePlaces.length === 0) return "There are no safe locations for Alex! :-("

  return safePlaces.map(convertIndexedToAlphaNumericCoordinate)
}

// private methods

onlyAllowedCoordinatesInsideTheCity = (coordinate) => {
  const row = coordinate.slice(0, 1)
  const col = coordinate.slice(1)
  return row.match(/^[A-J]$/) && col >= 1 && col <= 10
}

const convertAlphaNumericToIndexedCoordinate = (alphaNumericCoordinate) => {
  const row = alphaNumericCoordinate.charCodeAt(0) - 65
  const column = alphaNumericCoordinate.slice(1) - 1
  return [row, column]
}

const convertIndexedToAlphaNumericCoordinate = (indexedCoordinate) => {
  const row = String.fromCharCode(indexedCoordinate[0] + 65)
  const column = indexedCoordinate[1] + 1
  return  row + column
}

const addDistanceToNearestAgent = (place, agentCoordinates) => {
  place.distanceToNearestAgent = calculateDistanceToNearestAgent(agentCoordinates, place)
  return place
}

const calculateDistanceToNearestAgent = (agents, coordinate) => {
  return agents
    .map(agent => calculateDistance(agent, coordinate))
    .reduce(keepSmallestDistance)
}

const calculateDistance = (agent, place) => {
  return Math.abs(place.coordinates[0] - agent[0]) +
    Math.abs(place.coordinates[1] - agent[1])
}

const keepSmallestDistance = (min, distance) => {
  return distance < min ? distance : min
}

const createAllPlaces = () => {
  let allPlaces = []
  for(let i = 0; i < 10; i++) {
    for(let j = 0; j < 10; j++) {
      allPlaces.push(
        {
          'coordinates': [i, j]
        }
      )
    }
  }
  return allPlaces
}

const onlyPlacesWithMaxDistance = (place, dummy, allPlaces) => {
  const maxDistance = allPlaces
    .reduce( keepMaxDistance, 0 )
  if ( maxDistance === 0 ) return false
  return place.distanceToNearestAgent === maxDistance;
}

const keepMaxDistance = (max, place) => {
  return place.distanceToNearestAgent > max ? place.distanceToNearestAgent : max
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAlex
}
