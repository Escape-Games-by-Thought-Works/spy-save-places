import java.util.Arrays;

/**
 * A class to help us find safe locations for Alex
 */
public class SafeSpaces {

    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     *
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param alphanumericCoordinates An alphanumeric representation of coordinates e.g. ["A1","D1"]
     * @return two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]]
     */


    /**
     * This method should take a two-dimensional, zero-based representation of coordinates for the agents locations and
     * find the safest places for Alex in a two-dimensional, zero-based representation of coordinates
     *
     * @param //agentCoordinates a two-dimensional, zero-based representation of coordinates for the agents locations
     * @return a two-dimensional, zero-based representation of coordinates for the safest places for alex
     * @see SafeSpaces#convertCoordinates(String[]) for the two-dimensional, zero-based representation of coordinates
     */

    public int[][] convertCoordinates(String[] alphanumericCoordinates) {

        int x = 0;
        int y = 0;
        int xValue = 0;
        int yValue = 0;
        int agentCounter = 0;

        for (String item : alphanumericCoordinates) {

            switch (item.charAt(0)) {
                case 'A':
                    xValue = 0;
                    break;
                case 'B':
                    xValue = 1;
                    break;
                case 'C':
                    xValue = 2;
                    break;
                case 'D':
                    xValue = 3;
                    break;
                case 'E':
                    xValue = 4;
                    break;
                case 'F':
                    xValue = 5;
                    break;
                case 'G':
                    xValue = 6;
                    break;
                case 'H':
                    xValue = 7;
                    break;
                case 'I':
                    xValue = 8;
                    break;
                case 'J':
                    xValue = 9;
                    break;
                default:
                    continue;
            }

            if (item.length() == 2) {
                agentCounter++;
            } else if (item.length() == 3) {
                if (Character.getNumericValue(item.charAt(1) + item.charAt(2)) < 11) {
                    agentCounter++;
                }
            }
        }


        if (agentCounter == 0) {

            int[][] noAgents = new int[0][0];
            return noAgents;
        }

        int[][] output = new int[agentCounter][2];

        for (String item : alphanumericCoordinates) {
            y = 0;
            switch (item.charAt(0)) {
                case 'A':
                    xValue = 0;
                    break;
                case 'B':
                    xValue = 1;
                    break;
                case 'C':
                    xValue = 2;
                    break;
                case 'D':
                    xValue = 3;
                    break;
                case 'E':
                    xValue = 4;
                    break;
                case 'F':
                    xValue = 5;
                    break;
                case 'G':
                    xValue = 6;
                    break;
                case 'H':
                    xValue = 7;
                    break;
                case 'I':
                    xValue = 8;
                    break;
                case 'J':
                    xValue = 9;
                    break;
                default:
                    continue;
            }

            if (item.length() == 2) {
                yValue = Character.getNumericValue(item.charAt(1)) - 1;
            } else if (item.length() == 3) {
                if (Character.getNumericValue(item.charAt(1) + item.charAt(2)) < 11) {
                    yValue = Character.getNumericValue(item.charAt(1) + item.charAt(2)) - 1;
                } else {
                    continue;
                }
            } else {
                continue;
            }

            output[x][y] = xValue;
            y++;
            output[x][y] = yValue;

            x++;

        }
        return output;
    }

    public int[][] findSafeSpaces(int[][] agentCoordinates) {
        int x = 0;
        int y = 0;
        boolean agent;
        int highestValue = 0;
        int[][] result = new int[10][10];
        for (x = 0; x < 10; x++) {
            for (y = 0; y < 10; y++) {
                agent = false;
                for (int a = 0; a < agentCoordinates.length; a++) {
                    if ((agentCoordinates[a][0] == x) && (agentCoordinates[a][1] == y)) {
                        agent = true;
                    }
                }
                if (!agent) {
                    for (int a = 0; a < agentCoordinates.length; a++) {
                        if (result[x][y] == 0 || Math.abs((agentCoordinates[a][0] - x)) + Math.abs((agentCoordinates[a][1] - y)) < result[x][y]) {
                            result[x][y] = Math.abs((agentCoordinates[a][0] - x)) + Math.abs((agentCoordinates[a][1] - y));
                        }
                    }
                }
            }
        }


        for (x = 0; x < 10; x++) {
            for (y = 0; y < 10; y++) {

                if (result[x][y] > highestValue) {
                    highestValue = result[x][y];
                }
            }
        }

        int count = 0;
        if (highestValue != 0 || agentCoordinates.length == 0) {
            for (x = 0; x < 10; x++) {
                for (y = 0; y < 10; y++) {

                    if (result[x][y] == highestValue) {
                        count++;
                    }
                }
            }

            int[][] places = new int[count][2];
            int a = 0;
            for (x = 0; x < 10; x++) {
                for (y = 0; y < 10; y++) {

                    if (result[x][y] == highestValue) {
                        places[a][0] = x;
                        places[a][1] = y;
                        a++;
                    }
                }
            }
            return places;
        } else {
            int[][] emptyPlaces = new int[0][0];
            return emptyPlaces;
        }


    }

    /**
     * This method should take an array of alphanumeric agent locations and offer advice to Alex for where she
     * should hide out in the city, with special advice for edge cases
     *
     * @param alphanumericCoordinates (e.g. ["A5", "B1"])
     * @return SearchResult with the proper information for Alex
     */


    public SearchResult adviceForAlex(String[] alphanumericCoordinates) {

        String noSafe = "There are no safelocations  for Alex! :-(";
        String allSafe = "The whole city is safe for Alex! :-)";


        int[][] resultConvert = convertCoordinates(alphanumericCoordinates);
        int[][] safeSpaces = findSafeSpaces(resultConvert);

        String xValue = "";
        String yValue = "";

        if (safeSpaces.length == 0) {
            SearchResult searchResult = new SearchResult(noSafe);
            return searchResult;
        }
        if (safeSpaces.length == 100) {
            SearchResult searchResult2 = new SearchResult(allSafe);
            return searchResult2;
        }

        String[] safeLocations = new String[safeSpaces.length];

        for (int i = 0; i < safeSpaces.length; i++) {

            switch (safeSpaces[i][0]) {
                case 0:
                    xValue = "A";
                    break;
                case 1:
                    xValue = "B";
                    break;
                case 2:
                    xValue = "C";
                    break;
                case 3:
                    xValue = "D";
                    break;
                case 4:
                    xValue = "E";
                    break;
                case 5:
                    xValue = "F";
                    break;
                case 6:
                    xValue = "G";
                    break;
                case 7:
                    xValue = "H";
                    break;
                case 8:
                    xValue = "I";
                    break;
                case 9:
                    xValue = "J";
                    break;
                default:
                    continue;
            }

            int yPlace = safeSpaces[i][1] + 1;
            yValue = Integer.toString(yPlace);

            safeLocations[i] = xValue + yValue;
        }

        SearchResult searchResult3 = new SearchResult(safeLocations);


        return searchResult3;
    }

    /**
     * Class that contains advice for Alex
     * In general the safeLocations array should be filled
     * However there edgecases to be taken into account (e.g. no safe locations or only safe locations) which would
     * only require a message
     */
    public class SearchResult {
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
