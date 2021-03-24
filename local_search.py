import nqueens
import random
import math

def scheduling(T, decay_rate):
    T = T * decay_rate
    return T


def simulated_annealing(decay_rate, Board, min_threshold_value):
    T = 100
    current = Board
    current.h = nqueens.numAttackingQueens(current)
    while True:
        T = scheduling(T, decay_rate)
        if (T < min_threshold_value or current.h == 0):
            return current
                    
        neighbor_states = nqueens.getSuccessorStates(current)
        next_state = random.choice(neighbor_states)
        next_state.h = nqueens.numAttackingQueens(next_state)

        delta_e = current.h - next_state.h

        if (delta_e > 0 ):
            current = next_state
        else:
            rand_number = random.random()
            if (rand_number < math.e**(delta_e/T)):
                current = next_state

    


def main():
    
    board_sizes = [4, 8, 16]
    thresh_values = [.000001, .0000001, .00000001]
    decay_rate = [0.9, 0.75, 0.5]
   
    for x in board_sizes:
        print("**********************************")
        print("Board Size: ", x)
        print("**********************************")
        for j in range(len(decay_rate)):
            print("decayRate: %s ThresHold: %e" % (decay_rate[j], thresh_values[j]))
            print("######################################")
            count_h_value = 0
            for i in range(10):
                print('Run', i)
                print('Initial: ')
                board = nqueens.Board(x)
                board.rand()
                board.printBoard()
                print("h-value: ", nqueens.numAttackingQueens(board))
                answer = simulated_annealing(decay_rate[j], board, thresh_values[j])
                print("Final h_value: ", answer.h)
                answer.printBoard()
                count_h_value += answer.h
            print("--------------------------------------")
            print("Average h value: ", count_h_value/10)
            print("--------------------------------------")
        

main()     
           





