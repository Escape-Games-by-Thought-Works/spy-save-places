<?php
declare(strict_types = 1);
namespace HelpAlex\Game;

class StringIntegerCoordinate extends AbstractCoordinate
{
    /**
     *
     * @return int
     */
    public function getColumnAsInteger(): int
    {
        return (int) $this->toInteger($this->column);
    }

}
