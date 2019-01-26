<?php
declare(strict_types = 1);

use PHPUnit\Framework\TestCase;

use HelpAlex\Game\Grid;
use HelpAlex\Game\StringIntegerCoordinate;

final class GridTest extends TestCase
{

    const BYTEVALUE_OFFSET_TO_A = 64;
    
    /**
     *
     * @var Grid
     */
    private $grid;

    /**
     */
    protected function setUp()/* The :void return type declaration that should be here would cause a BC issue */
    {
        $this->grid = new Grid(10, 10);
    }

    /**
     */
    public function testGetSafeLocations_ThereIsNoAgent_ReturnCityIsSafe(): void
    {
        // prepare
        $agentsLocations = [];
        $this->grid->setAgentsLocations($agentsLocations);
        
        // invoke
        $actual = $this->grid->getSafeLocations();
        
        // assert
        $this->assertEquals([
            Grid::MESSAGE_CITY_IS_SAVE
        ], $actual);
    }

    /**
     */
    public function testGetSafeLocations_ThereAreAgentsEverywhere_ReturnCityIsUnSafe(): void
    {
        // prepare
        $input = [];
        for ($i = 1; $i <= 10; $i ++) {
            for ($j = 1; $j <= 10; $j ++) {
                $input[] = [
                    chr($i + self::BYTEVALUE_OFFSET_TO_A),
                    (string) $j
                ];
            }
        }
        
        $agentsLocations = $this->prepareAgentsLocations($input);
        $this->grid->setAgentsLocations($agentsLocations);
        
        // invoke
        $actual = $this->grid->getSafeLocations();
        
        // assert
        $this->assertEquals([
            Grid::MESSAGE_CITY_IS_UNSAVE
        ], $actual);
    }

    /**
     */
    public function testGetSafeLocations_ThereIsAnAgentButOutsideOfGrid_ReturnCityIsSafe(): void
    {
        // prepare
        $input = [
            [
                'X',
                '88'
            ]
        ];
        
        $agentsLocations = $this->prepareAgentsLocations($input);
        $this->grid->setAgentsLocations($agentsLocations);
        
        // invoke
        $actual = $this->grid->getSafeLocations();
        
        // assert
        $this->assertEquals([
            Grid::MESSAGE_CITY_IS_SAVE
        ], $actual);
    }

    /**
     */
    public function testGetSafeLocations_ThereAreSomeAgents_ReturnThereLocations(): void
    {
        // prepare
        $input = [
            [
                'A',
                '1'
            ],
            [
                'D',
                '2'
            ]
        ];
        
        $agentsLocations = $this->prepareAgentsLocations($input);
        $this->grid->setAgentsLocations($agentsLocations);
        
        // invoke
        $actual = $this->grid->getSafeLocations();
        
        // assert
        $this->assertEquals([
            'J10'
        ], $actual);
    }

    /**
     *
     * @param array $input
     * @return StringIntegerCoordinate[]
     */
    private function prepareAgentsLocations(array $input)
    {
        $agentsLocations = [];
        foreach ($input as $coordinate) {
            $agentsLocations[] = new StringIntegerCoordinate($coordinate[0], $coordinate[1]);
        }
        
        return $agentsLocations;
    }
}
