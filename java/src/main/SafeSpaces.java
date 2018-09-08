package main;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * A class to help us find safe locations for Alex
 */
public class SafeSpaces {
	
	private SafePlaceFInderImplemented safePlaceFinder = new SafePlaceFInderImplemented();

    /**
     * This method should convert an one dimensional Array with alphanumeric coordinates (e.g. ["A1"]) to a
     * two-dimensional, zero-based representation of the coordinates
     *
     * For example the input of ["A6"] should lead to [[0,5]]
     *
     * @param alphanumericCoordinates An alphanumeric representation of coordinates e.g. ["A1","D1"]
     * @return two-dimensional, zero-based representation of the coordinates (e.g. [[0,0],[3,0]]
     */
	public   int[][] convertCoordinates(String[] alphanumericCoordinates){
		
		int[][] output = new int[alphanumericCoordinates.length][2];
		
		for (int i = 0; i<alphanumericCoordinates.length; i++) {
			BigDecimal value = safePlaceFinder.getTableMap().get(alphanumericCoordinates[i]);
			BigDecimal valueX =	value.subtract(value.remainder(BigDecimal.ONE));
			BigDecimal valueY =	value.remainder(BigDecimal.ONE).multiply(BigDecimal.TEN);
			output[i]=new int[] {valueY.intValue(), valueX.intValue()};
		}
		
       return output;
    }

    /**
     * This method should take a two-dimensional, zero-based representation of coordinates for the agents locations and
     * find the safest places for Alex in a two-dimensional, zero-based representation of coordinates
     *
     * @see SafeSpaces#convertCoordinates(String[]) for the two-dimensional, zero-based representation of coordinates
     * @param agentCoordinates a two-dimensional, zero-based representation of coordinates for the agents locations
     * @return a two-dimensional, zero-based representation of coordinates for the safest places for alex
     */
	public   int[][] findSafeSpaces(int[][] agentCoordinates){
		
		List<String> agentLocations = new ArrayList<String>();
		List<String> myOutput = new ArrayList<String>();		
		
		for (int[] agent : agentCoordinates) {
			BigDecimal valueX = new BigDecimal(agent[1]);
			BigDecimal valueY = new BigDecimal(agent[0]);
			BigDecimal value = valueX.add(valueY.divide(BigDecimal.TEN));
			
			agentLocations.add(safePlaceFinder.getTableMapREVERSE().get(safePlaceFinder.bigDecimalScaleErrorCorrecter(value)));
		}
		
		myOutput = safePlaceFinder.agentLocationProcessorAndInit(agentLocations);
		
		int[][] programOutputJustForTHISTest = new int[myOutput.size()][2];
		
		for (int i = 0; i<programOutputJustForTHISTest.length; i++) {
			BigDecimal value = safePlaceFinder.getTableMap().get(myOutput.get(i));
			BigDecimal valueX =	value.subtract(value.remainder(BigDecimal.ONE));
			BigDecimal valueY =	value.remainder(BigDecimal.ONE).multiply(BigDecimal.TEN);
			programOutputJustForTHISTest[i]=new int[] {valueY.intValue(), valueX.intValue()};
		}
		
        return programOutputJustForTHISTest;
    }

    /**
     * This method should take an array of alphanumeric agent locations and offer advice to Alex for where she
     * should hide out in the city, with special advice for edge cases
     * @param alphanumericCoordinates (e.g. ["A5", "B1"])
     * @return SearchResult with the proper information for Alex
     */
	public  SearchResult adviceForAlex(String[] alphanumericCoordinates){
		
		String itsSoSafe = "The whole city is safe for Alex! :-)";
		String itsNOTSoSafe = "There are no safe locations for Alex! :-(";
		
		List<String> agentLocations = new ArrayList<String>();
		List<String> myOutput = new ArrayList<String>();		
		
		agentLocations = Arrays.asList(alphanumericCoordinates);
		
		myOutput = safePlaceFinder.agentLocationProcessorAndInit(agentLocations);
		
		if(myOutput.size() == 1 && myOutput.get(0).equals(itsSoSafe) )
		{
			 return new SearchResult(itsSoSafe);
		} else if (myOutput.size() == 1 && myOutput.get(0).equals(itsNOTSoSafe)) {
			
			 return new SearchResult(itsNOTSoSafe);
		}
		
		
        return new SearchResult(myOutput.toArray(new String[0]));
    }

    /**
     * Class that contains advice for Alex
     * In general the safeLocations array should be filled
     * However there edgecases to be taken into account (e.g. no safe locations or only safe locations) which would
     * only require a message
     */
	public  class SearchResult {
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
