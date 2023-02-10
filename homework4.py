############################################################
# CIS 5210: Homework 4
############################################################
# Include your imports here, if any are used.
import collections
import copy
import itertools
import random
import math
import sys
student_name = "Jingjing Bai"
############################################################
# Section 1: Dominoes Game
############################################################
def create_dominoes_game(rows, cols):
    pass
class DominoesGame(object):
    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.moveout = None
        self.leaf_count = 0

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for tmp in range(self.rows)] for _ in range(self.cols)]

    def is_legal_move(self, row, col, vertical):
        if vertical:
            if 0 <= row < self.rows - 1 and 0 <= col < self.cols:
                return not self.board[row][col] and not self.board[row + 1][col]
            return False
        else:
            if 0 <= row < self.rows and 0 <= col < self.cols - 1:
                return not self.board[row][col] and not self.board[row][col + 1]
            return False

    def legal_moves(self, vertical):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.is_legal_move(r, c, vertical):
                    yield (r, c)

    def perform_move(self, row, col, vertical):
        if vertical:
            self.board[row][col] = True
            self.board[row + 1][col] = True
        else:
            self.board[row][col] = True
            self.board[row][col + 1] = True

    def game_over(self, vertical):
        try:
            next(self.legal_moves(vertical))
            return False
        except:
            return True

    def copy(self):
        return DominoesGame([[elem for elem in row] for row in self.board])

    def successors(self, vertical):
        for move in self.legal_moves(vertical):
            copy = self.copy()
            copy.perform_move(move[0], move[1], vertical)
            yield (move, copy)

    def get_random_move(self, vertical):
        return random.choice(list(self.legal_moves(vertical)))

    # Required
    def get_best_move(self, vertical, limit):
        v = self.get_max_value(self, vertical, vertical, limit, -sys.maxsize, sys.maxsize)
        return (self.moveout, v, self.leaf_count)

    def get_value(self, vertical):
        return sum(1 for _ in self.legal_moves(vertical)) - sum(1 for _ in self.legal_moves(not vertical))

    def get_max_value(self, root, root_vertical, vertical, limit, alpha, beta):
        if self.game_over(vertical) or limit == 0:
            root.leaf_count += 1
            return self.get_value(root_vertical)

        v = -sys.maxsize
        for move, game in self.successors(vertical):
            g = game.get_min_value(root, root_vertical, not vertical, limit-1, alpha, beta)
            if v < g:
                self.moveout = move
                v = g
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def get_min_value(self, root, root_vertical, vertical, limit, alpha, beta):
        if self.game_over(vertical) or limit == 0:
            root.leaf_count += 1
            return self.get_value(root_vertical)

        v = sys.maxsize
        for move, game in self.successors(vertical):
            g = game.get_max_value(root, root_vertical, not vertical, limit-1, alpha, beta)
            if v > g:
                self.moveout = move
                v = g

            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

############################################################
# Section 2: Feedback
############################################################
feedback_question_1 = """
12
"""
feedback_question_2 = """
How to design a iterative way to cal the max or min of a node. This could be a hint.
"""
feedback_question_3 = """
This game is a really good design to understand the algorithm in course.
"""
