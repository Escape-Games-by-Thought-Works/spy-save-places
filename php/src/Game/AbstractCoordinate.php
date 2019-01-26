<?php
declare(strict_types = 1);
namespace HelpAlex\Game;

abstract class AbstractCoordinate implements CoordinateInterface
{

    /**
     * Holds the column of the coordinate.
     *
     * @var string
     */
    protected $column = '';

    /**
     * Holds the row of the coordinate.
     *
     * @var int
     */
    protected $row = 0;

    /**
     * 
     * @param string|int $column
     * @param string|int $row
     */
    public function __construct($column, $row)
    {
        $this->column = $column;
        $this->row = $row;
    }

    /**
     *
     * @return int
     */
    public function getColumnAsInteger(): int
    {
        return (int) $this->column;
    }
    
    /**
     *
     * @return string
     */
    public function getColumnAsString(): string
    {
        return (string) $this->column;
    }
    
        /**
     * 
     * @return int
     */
    public function getRowAsInteger(): int
    {
        return (int) $this->row;
    }
    
    /**
     * 
     * @return string
     */
    public function getRowAsString(): string
    {
        return (string) $this->toString($this->row);
    }
    
    /**
     *
     * @param string $value
     * @return number
     */
    protected function toInteger($value = '')
    {
        return ord($value) - self::BYTEVALUE_OFFSET_TO_A;
    }

    /**
     *
     * @param number $value
     * @return string
     */
    protected function toString($value = 0)
    {
        return chr($value + self::BYTEVALUE_OFFSET_TO_A);
    }
}
