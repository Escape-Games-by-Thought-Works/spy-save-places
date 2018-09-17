import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * A class to help us find safe locations for Alex
 */
class SafeSpaces {

    static final int xDim = 10;
    static final int yDim = 10;

    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     *
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param alphanumericCoordinates An alphanumeric representation of coordinates e.g. ["A1","D1"]
     * @return two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]]
     */
    int[][] convertCoordinates(String[] alphanumericCoordinates){
        ArrayList<int[]> coordinates = new ArrayList<>();

        for (int n = 0; n < alphanumericCoordinates.length; n++) {
            char[] characters = alphanumericCoordinates[n].toCharArray();

            //check if x coordinate is between 'A' and 'J'
            if (characters[0] >= 'A' && characters[0] <= 'J') {
                //get integer value from index 1 to end from characters array
                int y = Integer.parseInt(
                        String.valueOf(Arrays.copyOfRange(characters, 1, characters.length)));

                //check if y coordinate is smaller or equal 10
                if (y <= yDim) {
                    int[] xy = new int[2];
                    //ASCII decimal value of char 'A' is 65 (consecutive to char 'J' = 74)
                    xy[0] = characters[0] - 65;
                    xy[1] = y - 1;

                    coordinates.add(xy);
                }
            }
        }

        return coordinates.toArray(new int[coordinates.size()][]);
    }

    /**
     * This method converts the two-dimensional, zero-based representation of the coordinates back to an
     * one dimensional Array with alphanumeric coordinates
     *
     * @param coordinates the two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]]
     * @return alphanumeric representation of coordinates e.g. ["A1","D1"]
     */
    String[] convertToAlphanumericCoordinates(int[][] coordinates){
        //String[] alphanumericCoordinates = new String[coordinates.length];
        ArrayList<String> alphanumericCoordinates = new ArrayList<>();

        for (int n = 0; n < coordinates.length; n++){
            int[] xy = coordinates[n];

            if (xy[0] < xDim) {
                //convert x coordinate
                String ab = Character.toString((char) (xy[0] + 65));
                if (xy[1] < yDim){
                    //concatenate y coordinate
                    ab += Integer.toString(xy[1] + 1);

                    alphanumericCoordinates.add(ab);
                }
            }
        }

        return alphanumericCoordinates.toArray(new String[alphanumericCoordinates.size()]);
    }

    /**
     * This method should take a two-dimensional, zero-based representation of coordinates for the agents locations and
     * find the safest places for Alex in a two-dimensional, zero-based representation of coordinates
     *
     * @see SafeSpaces#convertCoordinates(String[]) for the two-dimensional, zero-based representation of coordinates
     * @param agentCoordinates a two-dimensional, zero-based representation of coordinates for the agents locations
     * @return a two-dimensional, zero-based representation of coordinates for the safest places for alex
     */
    int[][] findSafeSpaces(int[][] agentCoordinates){
        int[][] map = new int[xDim][yDim];
        //fill map with max values
        for (int[] row : map){
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        //update distance of each field with smallest distance to an agent
        for (int[] agent : agentCoordinates){
            for (int x = 0; x < xDim; x++){
                for (int y = 0; y < yDim; y++){
                    //manhattan metric
                    int distance = Math.abs(x - agent[0]) + Math.abs(y - agent[1]);
                    map[x][y] = Math.min(distance, map[x][y]);
                }
            }
        }

        //find greatest distance of all fields to an agent
        int maxDistance = 0;
        for (int x = 0; x < xDim; x++){
            for (int y = 0; y < yDim; y++){
                maxDistance = Math.max(maxDistance, map[x][y]);
            }
        }

        //if the maxDistance is still 0, there were no safe places for Alex
        if (maxDistance == 0){
            return new int[][]{};
        }

        //get all fields with maxDistance and save them in a list
        ArrayList<int[]> safePlaces = new ArrayList<>();
        for (int x = 0; x < xDim; x++){
            for (int y = 0; y < yDim; y++){
                if (map[x][y] == maxDistance){
                    safePlaces.add(new int[]{x, y});
                }
            }
        }

        return safePlaces.toArray(new int[safePlaces.size()][]);
    }

    /**
     * This method should take an array of alphanumeric agent locations and offer advice to Alex for where she
     * should hide out in the city, with special advice for edge cases
     * @param alphanumericCoordinates (e.g. ["A5", "B1"])
     * @return SearchResult with the proper information for Alex
     */
    SearchResult adviceForAlex(String[] alphanumericCoordinates){
        //get coordinates of agents
        int[][] coordinates = this.convertCoordinates(alphanumericCoordinates);
        //find safe places for Alex according to agent coordinates
        int[][] safePlaces = this.findSafeSpaces(coordinates);

        //check corner cases
        if (safePlaces.length == 0){
            return new SearchResult("There are no safe locations for Alex! :-(");
        } else if (safePlaces.length == xDim * yDim){
            return new SearchResult("The whole city is safe for Alex! :-)");
        }

        return new SearchResult(this.convertToAlphanumericCoordinates(safePlaces));
    }

    /**
     * Class that contains advice for Alex
     * In general the safeLocations array should be filled
     * However there edgecases to be taken into account (e.g. no safe locations or only safe locations) which would
     * only require a message
     */
    class SearchResult {
        private String message;
        private String[] safeLocations;

        public SearchResult(String message) {
            this.message = message;
        }

        public SearchResult(String[] safeLocations) {
            Arrays.sort(safeLocations);
            this.safeLocations = safeLocations;
        }

        @Override
        public String toString() {
            return message != null ? message : Arrays.toString(safeLocations);
        }
    }
}
