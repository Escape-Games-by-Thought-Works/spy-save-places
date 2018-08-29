import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

import java.util.*;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

public class SafeSpacesTest {
    final Comparator<int[]> arrayComparator = (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0];

    SafeSpaces objectUnderTest;

    @Before
    public void setup(){
        objectUnderTest = new SafeSpaces();
    }

    //Level -1 convert coordinates
    /**
     * Test that the method handles an empty list of coordinates correctly
     */
    @Test
    @Ignore
    public void testEmptyCoordinates(){
        String[] agents = {};
        int[][] coordinates = objectUnderTest.convertCoordinates(agents);
        assertArrayEquals("Empty alphanumeric coordinates should lead to empty numeric coordinates",
                new int[][]{},
                coordinates);
    }

    /**
     * Test for correct conversion of a single coordinate
     */
    @Test
    @Ignore
    public void testSingleCoordinate(){
        String[] agents = {"F3"};
        int[][] coordinates = objectUnderTest.convertCoordinates(agents);
        int[][] expected = {{5, 2}};
        Arrays.sort(coordinates, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,coordinates);
    }

    /**
     * Test for correct conversion from a list of coordinates to multi-dimensional, zero-based array
     */
    @Test
    @Ignore
    public void testMultipleCoordinates(){
        String[] agents = {"B6","C2","J7"};
        int[][] coordinates = objectUnderTest.convertCoordinates(agents);
        int[][] expected = {{1, 5}, {2, 1}, {9, 6}};
        Arrays.sort(coordinates, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,coordinates);
    }

    /**
     * Test that alphanumeric coordinates with a double digit number are handled correctly
     */
    @Test
    @Ignore
    public void testDoubleDigits(){
        String[] agents = {"J10"};
        int[][] coordinates = objectUnderTest.convertCoordinates(agents);
        int[][] expected = {{9, 9}};
        Arrays.sort(coordinates, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,coordinates);
    }

    //End Level-1 convert coordinates

    //Level-2 Find safe spaces in the city based on agent locations

    /**
     * Test for six agents at specified locations
     */
    @Test
    @Ignore
    public void testSafeSpacesRound1(){
        int[][] agents = {{1,1},{3,5},{4,8},{7,3},{7,8},{9,1}};
        int[][] safeSpaces = objectUnderTest.findSafeSpaces(agents);
        int[][] expected = {{0, 9}, {0, 7}, {5, 0}};
        Arrays.sort(safeSpaces, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,safeSpaces);
    }

    /**
     * Test for six agents at different specified locations
     */
    @Test
    @Ignore
    public void testSafeSpacesRound2(){
        int[][] agents = {{0,0},{0,9},{1,5},{5,1},{9,0},{9,9}};
        int[][] safeSpaces = objectUnderTest.findSafeSpaces(agents);
        int[][] expected = {{5, 7}, {6, 6}, {7, 5}};
        Arrays.sort(safeSpaces, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,safeSpaces);
    }

    /**
     * Test for on agent at a specified location
     */
    @Test
    @Ignore
    public void testSafeSpacesRound3(){
        int[][] agents = {{0,0}};
        int[][] safeSpaces = objectUnderTest.findSafeSpaces(agents);
        int[][] expected = {{9, 9}};
        Arrays.sort(safeSpaces, arrayComparator);
        Arrays.sort(expected, arrayComparator);
        assertArrayEquals(expected,safeSpaces);
    }

    //End Level-2 Find safe spaces in the city based on agent locations

    //Level-3 Handle edge cases and offering recommendations

    /**
     * Test for agents everywhere in the city
     */
    @Test
    @Ignore
    public void testAgentsEverywhere(){
        String[] agents = {
                "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
                "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
                "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
                "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10",
                "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10",
                "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10",
                "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
                "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10",
                "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10",
                "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals("There are no safe locations for Alex! :-(",
                searchResult.toString());
    }

    /**
     * Test for six agents at specified locations
     */
    @Test
    @Ignore
    public void testAdviceRound1(){
        String[] agents = {"B2", "D6", "E9", "H4", "H9", "J2"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals(Arrays.toString(new String[]{"A10", "A8", "F1"}),
                searchResult.toString());
    }

    /**
     * Test for seven agents at specified locations
     */
    @Test
    @Ignore
    public void testAdviceRound2(){
        String[] agents = {"B4", "C4", "C8", "E2", "F10", "H1", "J6"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals(Arrays.toString(new String[]{"A1", "A10", "E6", "F5", "F6", "G4", "G5","G7", "H8", "I9", "J10"}),
                searchResult.toString());
    }

    /**
     * Test for six agents at different specified locations
     */
    @Test
    @Ignore
    public void testAdviceRound3(){
        String[] agents = {"A1", "A10", "B6", "F2", "J1", "J10"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals(Arrays.toString(new String[]{"F8", "G7", "H6"}),
                searchResult.toString());
    }

    /**
     * Test for only one agent
     */
    @Test
    @Ignore
    public void testAdviceRound4(){
        String[] agents = {"A1"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals(Arrays.toString(new String[]{"J10"}),
                searchResult.toString());
    }

    /**
     * Test for agent outside the map (no agent in the city)
     */
    @Test
    @Ignore
    public void testAgentOutsideMap(){
        String[] agents = {"A12"};
        SafeSpaces.SearchResult searchResult = objectUnderTest.adviceForAlex(agents);
        assertEquals("The whole city is safe for Alex! :-)",
                searchResult.toString());
    }

}
