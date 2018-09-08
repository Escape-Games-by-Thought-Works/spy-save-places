package main;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


//Created by Oliver Bordas
//Email: zedasgm@gmail.com
//Location: Budapest, Hungary
//@20180908

public class SafePlaceFInderImplemented {
	
	private int actualMaximumLength =1;
	private int cologneCityGridSize = 100;

	private Integer[][] cologneCityGrid = new Integer[10][10];
	private final Map<String, BigDecimal> tableMap = new HashMap<>();
	private final Map<BigDecimal, String> tableMapREVERSE = new HashMap<>();
	
	private List<String> agentLocations = new ArrayList<String>();
	private List<BigDecimal> translatedAgentLocations = new ArrayList<BigDecimal>();
	
	private List<String> safeLocations = new ArrayList<String>();
	
	
	
	public SafePlaceFInderImplemented() {
		super();
		
		setupTableMap();
		setuptableMapREVERSE();
	}



	public List<String> agentLocationProcessorAndInit(List<String> agentInput) {
		agentLocations = agentInput;
		
		for (String agent : agentLocations) {		
			if(tableMap.get(agent)==null) {
				continue;
			}
			translatedAgentLocations.add(bigDecimalScaleErrorCorrecter(tableMap.get(agent)));			
		}
		
		if(translatedAgentLocations.isEmpty()) {
			safeLocations.add("The whole city is safe for Alex! :-)");
			System.out.println("The whole city is safe for Alex! :-)");
			return safeLocations;
		} else if (translatedAgentLocations.size()==100) {
			safeLocations.add("There are no safe locations for Alex! :-(");
			System.out.println("There are no safe locations for Alex! :-(");
			return safeLocations;
		}
		
		cologneCityGridSize=cologneCityGridSize-translatedAgentLocations.size();
		
		safePlaceFinder(translatedAgentLocations);
		
		return safeLocations;
		
	}
	
	
	
	private List<String> safePlaceFinder(List<BigDecimal> locations) {
		
		List<BigDecimal> stepsList = new ArrayList<BigDecimal>();
		List<BigDecimal> validStepsList = new ArrayList<BigDecimal>();
		
		for(BigDecimal location : locations) {
			stepsList.addAll(oneStepCalculator(location));			
		}
		
		validStepsList=validStepsChecker(stepsList);
		
		validStepsSetter(validStepsList);
		
		cologneCityGridSize = cologneCityGridSize-validStepsList.size();
		
		
		if(cologneCityGridSize==0) {
			
			for(BigDecimal safeLocation : validStepsList) {		

				safeLocations.add(tableMapREVERSE.get(bigDecimalScaleErrorCorrecter(safeLocation)));
			}
			System.out.println(safeLocations);
			return safeLocations;
		}
		
		actualMaximumLength++;
		safePlaceFinder(validStepsList);
		
		return safeLocations;
		
	}
	
	private void validStepsSetter(List<BigDecimal> validStepsList) {
	
	for(BigDecimal step : validStepsList) {
		BigDecimal valueX =	step.subtract(step.remainder(BigDecimal.ONE));
		BigDecimal valueY =	step.remainder(BigDecimal.ONE).multiply(BigDecimal.TEN);
		
		cologneCityGrid[valueX.intValue()][valueY.intValue()] = actualMaximumLength;		
	}
	
	}
	
	
	private List<BigDecimal> validStepsChecker(List<BigDecimal> stepsList) {
		List<BigDecimal> validStepsList = new ArrayList<BigDecimal>();
		
		for(BigDecimal step : stepsList) {
		step=bigDecimalScaleErrorCorrecter(step);
		BigDecimal valueX =	step.subtract(step.remainder(BigDecimal.ONE));
		BigDecimal valueY =	step.remainder(BigDecimal.ONE).multiply(BigDecimal.TEN);
		Integer locationInCologne = cologneCityGrid[valueX.intValue()][valueY.intValue()];
		
		if(validStepsList.contains(step) || translatedAgentLocations.contains(step) || (locationInCologne != null && locationInCologne<=actualMaximumLength) ) {
			continue;
		}
		
		validStepsList.add(step);		
		}
		
		return validStepsList;		
	}
	
	
	
	private List<BigDecimal> oneStepCalculator(BigDecimal location) {
		List<BigDecimal> valueList = new ArrayList<BigDecimal>();
		BigDecimal valueX =	location.subtract(location.remainder(BigDecimal.ONE));
		BigDecimal valueY =	location.remainder(BigDecimal.ONE).multiply(BigDecimal.TEN);
	
		//it also checks for invalid locations such as <0 or 9<
		//the steps are  x-1, y-1, y+1, x+1		
		if(valueX.subtract(BigDecimal.ONE).compareTo(BigDecimal.ZERO)!=-1) {
			BigDecimal firstStep = valueX.subtract(BigDecimal.ONE).add(valueY.divide(BigDecimal.TEN));
			
			valueList.add(firstStep);
		}
		
		if(valueY.subtract(BigDecimal.ONE).compareTo(BigDecimal.ZERO)!=-1) {			
			BigDecimal secondStep = valueX.add(valueY.subtract(BigDecimal.ONE).divide(BigDecimal.TEN));
			
			valueList.add(secondStep);
		}
		
		if(valueY.add(BigDecimal.ONE).compareTo(BigDecimal.TEN)==-1) {			
			BigDecimal thirdStep = valueX.add(valueY.add(BigDecimal.ONE).divide(BigDecimal.TEN));
			
			valueList.add(thirdStep);
		}
		
		if(valueX.add(BigDecimal.ONE).compareTo(BigDecimal.TEN)==-1) {			
			BigDecimal fourthStep = valueX.add(BigDecimal.ONE).add(valueY.divide(BigDecimal.TEN));
			
			valueList.add(fourthStep);
		}	
		
		return valueList;
	}
	
	
	
	
	private void setuptableMapREVERSE() {
		for (String key : tableMap.keySet()){
			tableMapREVERSE.put(tableMap.get(key), key);
		}
	}


	private void setupTableMap() {
		BigDecimal tableValue = new BigDecimal(0.0);
		
		for (char c = 'A'; c <= 'J'; c++) {		
			
			tableValue = tableValue.remainder(BigDecimal.ONE);
			
			for(int i = 1; i <= 10; i++) {
			String t1 =	String.valueOf(c);
			String t2 =	String.valueOf(i);
			String t3 =	String.valueOf(t1+t2);
			tableMap.put(t3, tableValue);
			
			if(tableValue.compareTo(BigDecimal.TEN)==0 || tableValue.compareTo(BigDecimal.TEN)==1){			
			tableValue=tableValue.subtract(BigDecimal.ONE);
			break;
			}
			tableValue=tableValue.add(BigDecimal.ONE);
			}			
			tableValue=tableValue.add(new BigDecimal(0.1).setScale(1, RoundingMode.DOWN));
		//get just the fractional BigDecimal.remainder( BigDecimal.ONE );	
		}
	}
	
	public BigDecimal bigDecimalScaleErrorCorrecter(BigDecimal value) {
	
	if(value.remainder(BigDecimal.ONE).compareTo(BigDecimal.ZERO) == 0) {
		value = value.setScale(0);		
	}
	
	return value;
	}



	public Map<String, BigDecimal> getTableMap() {
		return tableMap;
	}



	public Map<BigDecimal, String> getTableMapREVERSE() {
		return tableMapREVERSE;
	}
	
	
	
	
}
