import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import shop_event
from helper_functions.create_entity import make_shop


class TestShopEvent(TestCase):

    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_pill(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"
                    
                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"
                    
                    "\nYou currently have 100 gold.\n"
                    
                    "\nYou have purchased the Pill of Vitality.\n"
                    "Your HP is now 110 / 110.\n"
                    "You now have 50 gold.\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["currentHP"], 110)
        self.assertEqual(character["maxHP"], 110)
        self.assertEqual(character["gold"], 50)

    @patch('builtins.input', side_effect=['2', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_elixir(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"

                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"

                    "\nYou currently have 100 gold.\n"

                    "\nYou have purchased the Elixir of Vigor.\n"
                    "Your ATK is now 8.\n"
                    "You now attack with Arcane Barrage.\n"
                    "You now have 35 gold.\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["atk"], 8)
        self.assertEqual(character["gold"], 35)

    @patch('builtins.input', side_effect=['3', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_powder(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"

                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"

                    "\nYou currently have 100 gold.\n"

                    "\nYou have purchased the Forbidden White Powder.\n\n"
                    "You have leveled up! You are now level 2. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 110 / 110 --- ATK: 6 --- EXP: 50 / 55\n\n"
                    "You now have 0 gold.\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["currentEXP"], 50)
        self.assertEqual(character["maxEXP"], 55)
        self.assertEqual(character["atk"], 6)
        self.assertEqual(character["gold"], 0)

    @patch('builtins.input', side_effect=['1', '2', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_multiple_items(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 200, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"

                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"

                    "\nYou currently have 200 gold.\n"

                    "\nYou have purchased the Pill of Vitality.\n"
                    "Your HP is now 110 / 110.\n"
                    "You now have 150 gold.\n"
                    
                    "You have purchased the Elixir of Vigor.\n"
                    "Your ATK is now 8.\n"
                    "You now attack with Arcane Barrage.\n"
                    "You now have 85 gold.\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["currentHP"], 110)
        self.assertEqual(character["maxHP"], 110)
        self.assertEqual(character["atk"], 8)
        self.assertEqual(character["gold"], 85)

    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_enough_gold(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 0, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"

                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"

                    "\nYou currently have 0 gold.\n"

                    "\nCome back with enough gold you swine!!! Nothing is free in my town!!!\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["gold"], 0)

    @patch('builtins.input', side_effect=['1', '1', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_out_of_stock(self, mock_output, _):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        shop_event(character, make_shop())
        expected = ("Welcome, hero. I have travelled thousands of miles to be of assistance.\n"
                    "Here are the items that I have managed to bring for you.\n"
                    "But they aren't free. I still have to feed my family you know?\n\n"
                    
                    "1. Item name: Pill of Vitality, Price: 50 gold, Quantity: 1, Increases maxHP by 10 points\n"
                    "2. Item name: Elixir of Vigor, Price: 65 gold, Quantity: 1, Increases ATK by 3 points\n"
                    "3. Item name: Forbidden White Powder, Price: 100 gold, "
                    "Quantity: 50, Increases currentEXP by 100 points\n"
                    
                    "\nYou currently have 100 gold.\n"
                    
                    "\nYou have purchased the Pill of Vitality.\n"
                    "Your HP is now 110 / 110.\n"
                    "You now have 50 gold.\n"
                    "Sorry, you already bought out those items.\n"
                    "Thank you for your patronage.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character["currentHP"], 110)
        self.assertEqual(character["maxHP"], 110)
        self.assertEqual(character["gold"], 50)
