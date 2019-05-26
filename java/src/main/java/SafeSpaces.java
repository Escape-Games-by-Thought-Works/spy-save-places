import java.util.Arrays;

/**
 * A class to help us find safe locations for Alex
 */
class SafeSpaces {

    private boolean isAgentOutside;

    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     * <p>
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param alphanumericCoordinates An alphanumeric representation of coordinates e.g. ["A1","D1"]
     * @return two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]]
     */
    int[][] convertCoordinates(String[] alphanumericCoordinates) {
        int[][] returnArray = new int[alphanumericCoordinates.length][2];
        for (int i = 0; i < alphanumericCoordinates.length; i++) {
            String code = alphanumericCoordinates[i];
            int[] result = new int[2];
            int x = code.charAt(0) - 65;
            int y = Integer.parseInt(code.substring(1)) - 1;
            result[0] = x;
            result[1] = y;
            returnArray[i] = result;
            if(x>=10 || y>= 10){
                this.isAgentOutside=true;
            }
        }
        return returnArray;
    }


    /**
     * This method should take a two-dimensional, zero-based representation of coordinates for the agents locations and
     * find the safest places for Alex in a two-dimensional, zero-based representation of coordinates
     *
     * @param agentCoordinates a two-dimensional, zero-based representation of coordinates for the agents locations
     * @return a two-dimensional, zero-based representation of coordinates for the safest places for alex
     * @see SafeSpaces#convertCoordinates(String[]) for the two-dimensional, zero-based representation of coordinates
     */
    int[][] findSafeSpaces(int[][] agentCoordinates) {
        int maxX = 10;
        int maxY = 10;
        int[][] coordinatesWithSafeDistance = new int[maxX][maxY];

        for (int i = 0; i < maxX; i++) {
            for (int j = 0; j < maxY; j++) {
                int[] distances = new int[agentCoordinates.length];
                for (int k = 0; k < agentCoordinates.length; k++) {
                    int[] currentPoint = new int[2];
                    currentPoint[0] = i;
                    currentPoint[1] = j;
                    int distance = calculateDistance(currentPoint, agentCoordinates[k]);
                    distances[k] = distance;
                }
                coordinatesWithSafeDistance[i][j] = minValue(distances);
            }
        }


        return calculateSafePoints(coordinatesWithSafeDistance);
    }

    /**
     * This method should take an array of alphanumeric agent locations and offer advice to Alex for where she
     * should hide out in the city, with special advice for edge cases
     *
     * @param alphanumericCoordinates (e.g. ["A5", "B1"])
     * @return SearchResult with the proper information for Alex
     */
    SearchResult adviceForAlex(String[] alphanumericCoordinates) {
        SearchResult returnValue;
        int[][] safePlaces = findSafeSpaces(convertCoordinates(alphanumericCoordinates));
        System.out.println("LEN"+safePlaces.length);
        if (safePlaces.length == 0) {
            returnValue = new SearchResult("There are no safe locations for Alex! :-(");
        } else if (isAgentOutside) {
            returnValue = new SearchResult("The whole city is safe for Alex! :-)");
        } else {
            return new SearchResult(convertCoordinates(safePlaces));
        }
        return returnValue;
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

    private int calculateDistance(int[] firstPoint, int[] secondPoint) {
        return Math.abs(firstPoint[0] - secondPoint[0])
                + Math.abs(firstPoint[1] - secondPoint[1]);
    }

    private int minValue(int[] distances) {
        return Arrays.stream(distances).min().getAsInt();
    }

    private int maxValue(int[] distances) {
        return Arrays.stream(distances).max().getAsInt();
    }


    private int[][] calculateSafePoints(int[][] coordinatesWithSafeDistance) {

        int[][] safePoints = new int[100][2];

        int[] distances = new int[100];


        int count = 0;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                distances[count] = coordinatesWithSafeDistance[i][j];
                count++;
            }
        }

        int maxSafeDistance = maxValue(distances);
        if (maxSafeDistance == 0) {
            return new int[0][0];
        }

        int finalCount = 0;


        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (coordinatesWithSafeDistance[i][j] == maxSafeDistance) {
                    int[] data = new int[2];
                    data[0] = i;
                    data[1] = j;
                    safePoints[finalCount] = data;
                    finalCount++;
                }

            }
        }

        int[][] finalReturnArray = new int[finalCount][2];

        for (int i = 0; i < finalCount; i++) {
            finalReturnArray[i] = safePoints[i];
        }
        return finalReturnArray;
    }

    private String[] convertCoordinates(int[][] coordinates){
        String[] returnArray=new String[coordinates.length];
        for (int i=0; i< coordinates.length;i++){
            String first =  String.valueOf((char)(coordinates[i][0] + 65));
            int second = coordinates[i][1]+1;
            returnArray[i]=first+second;
        }
        return returnArray;
    }

}
