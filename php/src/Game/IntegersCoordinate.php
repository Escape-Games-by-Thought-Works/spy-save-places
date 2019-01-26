<?php
declare(strict_types = 1);
namespace HelpAlex\Game;

class IntegersCoordinate extends AbstractCoordinate
{
    /**
     *
     * @return string
     */
    public function getColumnAsString(): string
    {
        return $this->toString($this->column);
    }
    
}
