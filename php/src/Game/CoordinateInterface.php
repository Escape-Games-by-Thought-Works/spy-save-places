<?php
declare(strict_types = 1);
namespace HelpAlex\Game;

interface CoordinateInterface
{

    /**
     * Holds the offset of ASCII "0" to ASCII "A".
     *
     * @var integer
     */
    const BYTEVALUE_OFFSET_TO_A = 64;

    /**
     * 
     * @param string|int $column
     * @param string|int $row
     */
    public function __construct($column, $row);
    
    /**
     *
     * @return int
     */
    public function getColumnAsInteger(): int;
    
    /**
     *
     * @return string
     */
    public function getColumnAsString(): string;
    
        /**
     * 
     * @return int
     */
    public function getRowAsInteger(): int;
    
    /**
     * 
     * @return string
     */
    public function getRowAsString(): string;
    
}
