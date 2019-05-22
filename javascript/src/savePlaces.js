// This is where you implement your solution 
const convertCoordinates = (agents) => {
    return agents
        .map(agent => ([
            agent.charCodeAt(0) - 65,
            parseInt(agent.substr(1), 10) - 1,
        ]));
}

const findSafePlaces = (agents) => {

    // utility function to calculate the distance to the closest agent
    // by providing coordinates
    const calcDistanceToClosest = (x, y) => {
        return agents
            // remove agents outside the city
            .filter(([agentX, agentY]) => (
                agentX > -1 && agentX < 10 && agentY > -1 && agentY < 10
            ))
            .reduce((toClosest, [aX, aY]) => {
                const distance = Math.abs(x - aX) + Math.abs(y - aY);
                return toClosest > distance ? distance : toClosest;
            }, 20); // 20 as an initial value (bigger than the max possible distance)
    };

    // create a one dimensional array
    // and fill it with the corresponding distance to closest agents
    const distances = new Array(100)
        .fill(0)
        .map((v, i) => calcDistanceToClosest(i % 10, Math.floor(i / 10)));

    // safest distance
    const safestDistance = Math.max(...distances);

    return safestDistance
        // extract coordinates that have the safest distance
        ? distances.reduce((safePlaces, distance, i) => (
            distance === safestDistance
                ? [...safePlaces, [i % 10, Math.floor(i / 10)]]
                : safePlaces
        ), [])
        // edge case, no safe places
        : [];

}

const adviceForAlex = (agents) => {
    const safestPlaces = findSafePlaces(convertCoordinates(agents));
    switch (safestPlaces.length) {
        case 0:
            return 'There are no safe locations for Alex! :-(';
        case 100:
            return 'The whole city is safe for Alex! :-)';
        default:
            return safestPlaces
                .map(p => (
                    [String.fromCharCode(p[0] + 65), p[1] + 1].join('')
                ));
    }
}

module.exports = {
    convertCoordinates,
    findSafePlaces,
    adviceForAlex
}
