class HoneyLemonadeConnect:
    def init(self):
        self.board = [[' '] * 7 for _ in range(6)]  # Our 6x7 Connect 4 board
        self.current_player = '🍋'  # Lemon player starts (because why not?)

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                break

    def check_winner(self):
        # Check for a winning sequence (4 in a row)
        for row in range(6):
            for col in range(4):
                if (self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != ' '):
                    return True  # Horizontal win

        for row in range(3):
            for col in range(7):
                if (self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != ' '):
                    return True  # Vertical win

        for row in range(3):
            for col in range(4):
                if (self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != ' '):
                    return True  # Diagonal (from top-left to bottom-right) win

                if (self.board[row][col + 3] == self.board[row + 1][col + 2] == self.board[row + 2][col + 1] == self.board[row + 3][col] != ' '):
                    return True  # Diagonal (from top-right to bottom-left) win

        return False  # No winner yet

    def play(self):
        while True:
            self.display_board()
            column =
int(input(f"{self.currentplayer}, it's your move! Enter a column (0-6): "))
            self.makemove(column)
            if self.checkwinner():
                print(f"{self.currentplayer} wins! 🏆")
                break
            self.current_player = '🍯' if self.current_player == '🍋' else '🍋'  # Switch players

if __name == "__main":
    game = HoneyLemonadeConnect()
    game.play()
