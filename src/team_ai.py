from __future__ import annotations
from apiwrapper.models import Command, ActionType, MoveActionData, GameState, ClientContext

from logging import getLogger
from typing import TYPE_CHECKING
from helpers import get_config, get_coordinate_difference, _get_vector_angle_degrees, get_entity_coordinates, get_partial_turn, get_own_ship_id

if TYPE_CHECKING:
    from apiwrapper.websocket_wrapper import ClientContext
from apiwrapper.models import GameState, Command


ai_logger = getLogger("team_ai")
"""You can use this logger to track the behaviour of your bot. 

This is preferred to calling print("msg") as it offers 
better configuration (see README.md in root)

Examples:
    >>> ai_logger.debug("A message that is not important but helps with understanding the code during problem solving.")
    >>> ai_logger.info("A message that you want to see to know the state of the bot during normal operation.")
    >>> ai_logger.warning("A message that demands attention, but is not yet causing problems.")
    >>> ai_logger.error("A message about the bot reaching an erroneous state")
    >>> ai_logger.exception("A message that is same as error, but can be only called in Except blocks. " +
    >>>                     "Includes exception info in the log")
    >>> ai_logger.critical("A message about a critical exception, usually causing a premature shutdown")
"""


def process_tick(context: ClientContext, game_state: GameState) -> Command | None:

    ai_logger.info("processing tick")

    # Get information about your ship
    my_ship = None
    my_ship_coordinates = None
    for row in game_state.game_map:
        for cell in row:
            if cell.cell_type == "Ship":
                my_ship = cell.data
                my_ship_coordinates 
                break

    if my_ship is not None:
        # Move forward by 1 cell
        move_command = Command(action_type=ActionType.Move, payload=MoveActionData(distance=1))
    return move_command
