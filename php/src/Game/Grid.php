<?php
declare(strict_types = 1);
namespace HelpAlex\Game;

class Grid
{

    /**
     * Holds static messages.
     *
     * @var string
     */
    const MESSAGE_CITY_IS_SAVE = 'The whole city is safe for Alex! :-)';
    const MESSAGE_CITY_IS_UNSAVE = 'There are no safe locations for Alex! :-(';

    /**
     * Holds all distances in an array (columns) of arrays (rows).
     *
     * @var array
     */
    private $distances;

    /**
     *
     * @var array
     */
    private $agentsLocations = [];

    /**
     * Holds the max of distances of all grid cells.
     *
     * @var int
     */
    private $maxDistance = 0;

    /**
     * Holds the width of the grid.
     *
     * @var int
     */
    private $gridWidth = 10;

    /**
     * Holds the height of the grid.
     *
     * @var int
     */
    private $gridHeight = 10;

    /**
     * Holds the the max possible distance within the grid as max grid dimension.
     *
     * @var int
     */
    private $maxGridDimension = 19;

    /**
     *
     * @param number $gridWidth
     * @param number $gridHeight
     */
    public function __construct($gridWidth = 10, $gridHeight = 10)
    {
        $this->gridWidth = $gridWidth;
        $this->gridHeight = $gridHeight;
        $this->maxGridDimension = $this->gridWidth + $this->gridHeight - 1;
        
        $this->initGrid();
    }

    /**
     * Set all <var>$agentsLocations</var> as array of coordinates.
     *
     * @param StringIntegerCoordinate[] $agentsLocations
     *
     * @codeCoverageIgnore No business logic
     */
    public function setAgentsLocations(array $agentsLocations)
    {
        $this->agentsLocations = $agentsLocations;
    }

    /**
     * Retrieves an array containing all save locations or a message, if there are no save or only save locations.
     *
     * @return string[]|array
     */
    public function getSafeLocations()
    {
        $this->calcDistancesToNeighbors();
        $this->maxDistance = max(array_map('max', $this->distances));
        
        if ($this->maxDistance === 0) {
            return [
                self::MESSAGE_CITY_IS_UNSAVE
            ];
        } elseif ($this->maxDistance === $this->maxGridDimension) {
            return [
                self::MESSAGE_CITY_IS_SAVE
            ];
        }
        
        $safeLocations = [];
        foreach ($this->distances as $column => $columns) {
            foreach ($columns as $row => $distance) {
                if ($distance === $this->maxDistance) {
                    $coordinate = new IntegersCoordinate($column, $row);
                    $safeLocations[] = $coordinate->getColumnAsString() . $coordinate->getRowAsInteger();
                }
            }
        }
        
        return $safeLocations;
    }

    /**
     * Initializes the grid (i.e.
     * set all distances to the grid's max dimension.
     *
     * @codeCoverageIgnore No business logic
     */
    private function initGrid()
    {
        for ($column = 1; $column <= $this->gridWidth; $column ++) {
            for ($row = 1; $row <= $this->gridHeight; $row ++) {
                $this->distances[$column][$row] = $this->maxGridDimension;
            }
        }
    }

    /**
     * Calc the distances of a <var>$agentsLocation</var> to its neightbors.
     *
     * @codeCoverageIgnore No business logic
     *
     */
    private function calcDistancesToNeighbors()
    {
        foreach ($this->agentsLocations as $agentsLocation) {
            for ($column = 1; $column <= $this->gridWidth; $column ++) {
                for ($row = 1; $row <= $this->gridHeight; $row ++) {
                    $distance = abs($agentsLocation->getRowAsInteger() - $row) + abs($agentsLocation->getColumnAsInteger() - $column);
                    $this->distances[$column][$row] = min($this->distances[$column][$row], $distance);
                }
            }
        }
    }

}
