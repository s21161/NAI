from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

"""https://pl.wikipedia.org/wiki/Nim
Gra NIM w wariancji 'Taktix' z kolumną - Taktix: 16 pionków ustawiamy w kwadrat 4x4. wolno zbierać dowolną ilość kamieni byle z tylko jednej kolumny

Jak przygotwac srodowisko do gry:
     - Zainstalowac easyAI - pip install easyai

    Autorzy:
     - Jakub Gwiazda(s20497)
     - Artur Jankowski(s21161)
     """


class Nim(TwoPlayerGame):

    def __init__(self, players, piles=None):
        """Inicjalizacja gracza oraz kolumn z pionkami
        Parameters:
            players: zmienna będąca listą dwóch graczy z TwoPlayerGame od easyAI
            piles: kolumny z pionkami
        Returns:
            self.piles = piles if (piles != None) else [4, 4, 4, 4]: stworzenie 4 kolumn z 4 pionkami zgodnie z zasadami wariantu gry
            self.players = players: wybór rodzai graczy, którzy będą grali, w linijce 67 mamy aktualnie jednego gracza ludzkiego i jednego gracza AI
            self.current_player = 1: aktualny gracz 1 to użytkownik, czyli ludzki gracz"""
        self.players = players
        self.piles = piles if (piles != None) else [4, 4, 4, 4]
        self.current_player = 1

    def possible_moves(self):
        """Możliwe ruchy gracza w aktualnym momencie gry"""
        return ["%d,%d" % (i + 1, j) for i in range(len(self.piles))
                for j in range(1, self.piles[i] + 1)]

    def make_move(self, move):
        """Funkcja umożliwiająca wykonanie ruchu, podajemy najpierw indeks kolumny a potem ilość pionków jaką chcemy zabrać w formacie '1,1',
        następnie usuwa z podanej kolumny podaną ilość pionków - o ile jest to wykonalne

        Parameters:
            move: lista dostępnych ruchów
        Returns:
            self.piles: aktualizacja"""
        move = list(map(int, move.split(',')))
        self.piles[move[0] - 1] -= move[1]

    def show(self):
        """Pokazywanie na ekranie konsoli dostępnych ruchów z funkcji possible_moves"""
        print(" ".join(map(str, self.piles)))
        for e in self.possible_moves():
            print(e + '   ', end='')
        print("")

    def win(self):
        """Wygranie gdy największy nie ma już pionków, czyli był ostatni ruch"""
        return max(self.piles) == 0

    def is_over(self):
        """Zakończenie gry gdy win zwróci true"""
        return self.win()

    def scoring(self):
        """Śledzenie aktualnego wyniku"""
        return 100 if self.win() else 0

ai = Negamax(2)
"""Ile ruchów naprzód AI ma planować"""
game = Nim([Human_Player(), AI_Player(ai)])
"""tworzenie gry z 2 graczami, gdzie drugi jest sztuczną inteligencją z negamax podanym w argumencie AI_Player"""
game.play()
"""Start gry"""
print("player %d wins" % game.current_player)
"""Wypisanie na ekranie konsoli który gracz wygrał"""