#!/usr/bin/php
<?php
declare(strict_types = 1);

/**
 */
namespace HelpAlex;

require_once __DIR__ . '/../vendor/autoload.php';

use HelpAlex\Exception\InvalidInput;
use HelpAlex\Game\StringIntegerCoordinate;
use HelpAlex\Game\Grid;
use Exception;

/**
 *
 * @author peter
 *        
 */
class Script
{

    /**
     * Holds the dimensions (width and height) of the grid.
     *
     * @var integer
     */
    const GRID_WIDTH = 10;
    const GRID_HEIGHT = 10;

    private $allowedColumns = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J'
    ];

    private $allowedRows = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10'
    ];

    /**
     *
     * @param array $argv
     * @throws InvalidInput
     */
    public function validate(array $argvs)
    {
        foreach ($argvs as $argv) {
            $column = mb_substr($argv, 0, 1);
            $row = mb_substr($argv, 1);
            if (!(in_array($column, $this->allowedColumns) && in_array($row, $this->allowedRows))) {
            throw new InvalidInput(sprintf('Invalid Input %s%s', $column, $row));
            }
        }
    }

    /**
     *
     * @param array $argvs
     * @return StringIntegerCoordinate[]
     */
    public function getCoordinates(array $argvs)
    {
        $coordinates = [];
        foreach ($argvs as $argv) {
            $coordinates[] = new StringIntegerCoordinate(mb_substr($argv, 0, 1), mb_substr($argv, 1));
        }
        
        return $coordinates;
    }
}

try {
    $argvs = $_SERVER['argv'];
    array_shift($argvs);
    
    $script = new Script();
    $script->validate($argvs);
    
    $grid = new Grid(Script::GRID_WIDTH, Script::GRID_HEIGHT);
    $grid->setAgentsLocations($script->getCoordinates($argvs));
    $saveLocations = $grid->getSafeLocations();
    
    echo implode(' ', $saveLocations);
} catch (Exception $e) {
    echo $e->getMessage();
    exit(1);
}

