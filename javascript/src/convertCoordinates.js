const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

// First Level
const parseCoordinates = (coordinates) => {
    const [ x, ...y ] = coordinates.split('');
    return [ alphabet.indexOf(x), parseInt(y.join(''), 10) - 1 ];
};
const serializeCoordinates = ([ x, y ]) => `${ alphabet[x] }${ y + 1 }`;

const convertCoordinates = (agents) => agents.map(parseCoordinates);

module.exports = {
  convertCoordinates,
  serializeCoordinates
};

