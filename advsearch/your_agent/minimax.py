import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    alpha = -10**9
    beta = 10**9

    (value, move) =  maxr(state, alpha, beta, max_depth, 0, eval_func, state.player,None)
    return move
    
    raise NotImplementedError()

def maxr(state,alpha:float, beta:float, max_depth, depth, eval_func, player,lastMove):
    #print(state.board)
    if (((depth >= max_depth) and (max_depth != -1)) or state.is_terminal()):
        return(eval_func(state, player), lastMove)
    else:
        bestValue = -10**9
        bestMove = None
        for move in state.legal_moves():
            (value, nextMove) = minr(state.next_state(move), alpha, beta, max_depth, depth+1, eval_func, player, move)
            if (value > bestValue):
                bestValue = value
                bestMove = nextMove
            alpha = max(value,alpha)
            if (alpha >= beta):
                break
    return (bestValue, bestMove)

def minr(state,alpha:float, beta:float, max_depth, depth, eval_func, player,lastMove):
    #print(state.board)
    if (((depth >= max_depth) and (max_depth != -1)) or state.is_terminal()):
        return(eval_func(state, player), lastMove)
    else:
        worstValue = 10**9
        worstMove = None
        for move in state.legal_moves():
            (value, nextMove) = maxr(state.next_state(move), alpha, beta, max_depth, depth+1, eval_func, player, move)
            if (value < worstValue):
                worstValue = value
                worstMove = nextMove
            
            beta = min(value,beta)
            if (alpha >= beta):
                break
    return (worstValue, worstMove)

