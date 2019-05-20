import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * A class to help us find safe locations for Alex
 */
class SafeSpaces {

    // General constants
    private static final String EMPTY_STRING = "";

    // Map related constants
    private static final int NUMBER_OF_COORDINATES_X = 10;
    private static final int NUMBER_OF_COORDINATES_Y = 10;
    private static final char FIRST_FIELD_X = 'A';


    // Special constants for advices
    private static final String NO_SAFE_LOCATIONS = "There are no safe locations for Alex! :-(";
    private static final String SAFE_CITY = "The whole city is safe for Alex! :-)";


    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     *
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param alphanumericCoordinates An alphanumeric representation of coordinates (e.g. ["A1","D1"])
     * @return two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]])
     */
    int[][] convertCoordinates(String[] alphanumericCoordinates){
        int [][] result = new int[alphanumericCoordinates.length][2];

        for (int i = 0; i < alphanumericCoordinates.length; i++){
            result[i][0] = convertToZeroBasedCoordinateX(alphanumericCoordinates[i]);
            result[i][1] = convertToZeroBasedCoordinateY(alphanumericCoordinates[i]);
        }

       return result;
    }

    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     *
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param zeroBasedCoordinates A two-dimensional, zero-based representation of coordinates (e.g. [[0,0],[3,0]])
     * @return An alphanumeric representation of the coordinates (e.g. ["A1","D1"])
     */
    private String[] convertCoordinates(int[][] zeroBasedCoordinates){
        String [] result = new String[zeroBasedCoordinates.length];

        for (int i = 0; i < zeroBasedCoordinates.length; i++){
             int [] coordinate = zeroBasedCoordinates[i];
            result[i] = String.join("",
                     convertToAlphanumericCoordinateX(coordinate[0]),
                     convertToAlphanumericCoordinateY(coordinate[1]));
        }

        return result;
    }

    private int convertToZeroBasedCoordinateX(String alphanumericCoordinateX){
        return alphanumericCoordinateX.charAt(0) - FIRST_FIELD_X ;
    }

    private int convertToZeroBasedCoordinateY(String alphanumericCoordinateY){
        return Integer.parseInt(alphanumericCoordinateY.replaceAll("[A-Z]", EMPTY_STRING)) - 1;
    }

    private String convertToAlphanumericCoordinateX(int zeroBasedCoordinateX){
        return String.valueOf ((char)(FIRST_FIELD_X + zeroBasedCoordinateX));
    }

    private String convertToAlphanumericCoordinateY(int zeroBasedCoordinateY){
        return String.valueOf (zeroBasedCoordinateY + 1);
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
        List<int[]> safestLocations = new ArrayList<>();
        int minDistanceOverall = 1;
        for (int positionX = 0; positionX < NUMBER_OF_COORDINATES_X; positionX++) {
            for (int positionY = 0; positionY < NUMBER_OF_COORDINATES_Y; positionY++) {
                int minDistance = determineMinimumDistance(agentCoordinates, positionX, positionY);

                // The newly found distance is greater than the prior one and thus better
                if (minDistance > minDistanceOverall){
                    minDistanceOverall = minDistance;
                    safestLocations.clear();
                    int[] element = new int[2];
                    element[0] = positionX;
                    element[1] = positionY;
                    safestLocations.add(element);

                // The distance is as good as the actual best one
                }else if(minDistance == minDistanceOverall){
                    int[] element = new int[2];
                    element[0] = positionX;
                    element[1] = positionY;
                    safestLocations.add(element);
                }

            }
        }

        int size = safestLocations.size();
        final int[][] result = new int[size][2];
        IntStream.range(0, size).forEach(pos -> result[pos] = safestLocations.get(pos));

        return result;
    }

    /**
     * This method should take all agent coordinates and a given two-dimensional location to determine the minimum distance between all agents and the location.
     * @param agentCoordinates coordinates of all agents (zero-based)
     * @param positionX x position of the two-dimensional location
     * @param positionY y position of the two-dimensional location
     * @return the minimum distance (Manhattan distance) between all agent coordinates and a given two-dimensional location
     */
    private int determineMinimumDistance(int[][] agentCoordinates, int positionX, int positionY) {
        int [] manhattanDistances = new int[agentCoordinates.length];
        for (int i = 0; i < agentCoordinates.length; i++){
            int[] agentCoordinate = agentCoordinates[i];
            manhattanDistances[i] = Math.abs(agentCoordinate[0] - positionX) + Math.abs(agentCoordinate[1] - positionY);
        }
        return IntStream.of(manhattanDistances).min().orElse(0);
    }

    /**
     * This method should take an array of alphanumeric agent locations and offer advice to Alex for where she
     * should hide out in the city, with special advice for edge cases
     * @param alphanumericCoordinates (e.g. ["A5", "B1"])
     * @return SearchResult with the proper information for Alex
     */
    SearchResult adviceForAlex(String[] alphanumericCoordinates){
        SearchResult result;

        if (alphanumericCoordinates.length == 0 || agentsOutsideMap(alphanumericCoordinates)){
            result = new SearchResult(SAFE_CITY);
        }else{
            int[][] safeLocations = findSafeSpaces(convertCoordinates(alphanumericCoordinates));

            if (safeLocations.length == 0){
                result = new SearchResult(NO_SAFE_LOCATIONS);
            }else{
                result = new SearchResult(convertCoordinates(safeLocations));
            }
        }

        return result;
    }

    /**
     * This method should check if all agents are outside the map/city.
     * @param alphanumericCoordinates An alphanumeric representation of coordinates e.g. ["A1","D1"]
     * @return true in case that all agents are outside the city, otherwise false.
     */
    private boolean agentsOutsideMap(String[] alphanumericCoordinates) {
        Predicate<int[]> filter = (val) ->
                (val[0] < 0 || val[0] > NUMBER_OF_COORDINATES_X) || (val[1] < 0 || val[1] > NUMBER_OF_COORDINATES_X);

        return Stream.of(convertCoordinates(alphanumericCoordinates)).allMatch(filter);
    }

    /**
     * Class that contains advice for Alex
     * In general the safeLocations array should be filled
     * However there edge cases to be taken into account (e.g. no safe locations or only safe locations) which would
     * only require a message
     */
    class SearchResult {
        private String message;
        private String[] safeLocations;

        SearchResult(String message) {
            this.message = message;
        }

        SearchResult(String[] safeLocations) {
            Arrays.sort(safeLocations);
            this.safeLocations = safeLocations;
        }

        @Override
        public String toString() {
            return message != null ? message : Arrays.toString(safeLocations);
        }
    }
}
