import sys
from random import shuffle

class Player():
    def __init__(self, player_deck):
        self.player_deck = player_deck
        self.lifepoints = 1000
        self.name = None
        self.hand = None
        self.current_card = None


    def get_user_name(self):
        self.name = input("Player, what is your name? ")


    def deck_draw(self):
        shuffle(self.player_deck)
        drawn_cards = self.player_deck[0:2]
        self.hand = drawn_cards
        del self.player_deck[0:2]


    # make this work for both players and drawing a new card
    def single_card_draw(self):
        draw_single_card = self.player_deck[0]
        self.hand.append(draw_single_card)
        del self.player_deck[0]


    # remove current card from cards in hand
    def delete_card_in_hand(self):
        for x in range(len(self.hand)):
            if self.hand[x][0] == self.current_card[0]:
                self.hand.pop(x)
                break


    # for testing opponent's cards only
    def opponent_draw(self):
        cpu_deck = self.player_deck
        shuffle(cpu_deck)
        draw_single_card = cpu_deck[0]
        self.hand = draw_single_card


    # function for the actual battle sequence and life point damage calculation
    def damage_calculation(self, player2):
        # check for which attack stat is greater
        # perform calculation for how many life points need to be subtracted and from which player
        # adjust life points based on battle result
        if self.current_card[1] > player2.hand[1]:
            player2.lifepoints -= (self.current_card[1] - player2.hand[1])
            print(f"Opponent's lifepoints are now: {player2.lifepoints}\n")

        if self.current_card[1] < player2.hand[1]:
            self.lifepoints -= (player2.hand[1] - self.current_card[1])
            print(f"{self.name}, your lifepoints are now: {self.lifepoints}\n")


    def fight(self, player2):
        print("Time to battle!\n")
        self.get_user_name()
        print("Now drawing cards...\n")
        self.deck_draw()
        while (self.lifepoints > 0) and (player2.lifepoints > 0):
            self.single_card_draw()
            player2.opponent_draw()
            print(f"Oppenent's monster is: {player2.hand[0]}, Attack: {player2.hand[1]}\n")
            print("Here are the cards in your hand: \n")

            for i in range(len(self.hand)):
                print(f"{self.hand[i][0]}, Attack: {self.hand[i][1]}")

            print("\n")

            hand_name_check_list = [x[0] for x in self.hand]
            chosen_card = input(f"{self.name}, please select your card: ")
            print("\n")

            # starts asking and checking for actual card if not found on first ask
            if chosen_card in hand_name_check_list: 
                self.current_card = chosen_card

            if chosen_card not in hand_name_check_list:
                for i in range(2):
                    chosen_card = input(f"{self.name}, please select a valid card: ")
                    print("\n")
                    if chosen_card in hand_name_check_list:
                        self.current_card = chosen_card
                        break

            if chosen_card not in hand_name_check_list:
                print("Sorry, you have forfeitted the game by not selecting a valid card. Game Over.")
                sys.exit()

            for i in range(len(self.hand)):
                if self.hand[i][0] == self.current_card:
                    self.current_card = self.hand[i]
                     
            self.delete_card_in_hand()

            print("Now time for the battle sequence.\n")
            print(f"{chosen_card} is now battling {player2.hand[0]}\n")

            # this can be put into the battle_sequence function or battle_calculation function
            self.damage_calculation(player2)

            print("------------------------------------------------\n")

        if self.lifepoints <= 0:
            print(f"Sorry, {self.name} your lifepoints have reached 0 and you have lost.")

        else:
            print(f"Congrats, {self.name}! You have deafeated your opponent!")


if __name__ == '__main__':
    # ask player to input their own name to be used as Player class instance??
    # use input here and then assign that in place of first_player
    deck = [['zeus', 800], ['demeter', 1200], ['hephaestus', 1000], ['apollo', 900], ['ares', 1250], ['hermes', 1300], ['aphrodite', 1400], ['poseodon', 1600], ['artemis', 1550]]
    player1 = Player(deck)
    opponent = Player(deck)
    player1.fight(opponent)