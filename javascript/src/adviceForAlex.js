const { convertCoordinates, serializeCoordinates } = require('./convertCoordinates.js');
const { findSafePlaces, cityArea } = require('./findSafePlaces.js');

// Third Level
const adviceForAlex = (agents) => {
  const safePlaces = findSafePlaces(convertCoordinates(agents));

  if (safePlaces.length === 0) return "There are no safe locations for Alex! :-(";
  if (safePlaces.length === cityArea) return "The whole city is safe for Alex! :-)";

  return safePlaces.map(serializeCoordinates);
}

module.exports = { adviceForAlex };

