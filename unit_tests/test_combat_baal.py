import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import combat_baal
from helper_functions.create_entity import make_baal


class TestCombatBaal(TestCase):
    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_baal(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 14,
                     "maxEXP": 2100, "currentEXP": 0, "atk": 100, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_baal(character, make_baal())
        expected = ("The stifling air exerts pressure onto your shoulders...\n"
                    "A figure rises up from the throne. \nThe air trembles in fear.\n"
                    "Baal: HAHAHAHA!!! Finally a worthy opponent!!! Let us celebrate this moment...\n"
                    "WITH A DUEL TO THE DEATH!!!!!!!!!!\n"
                    
                    "\nYou have encountered a wild Baal!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Baal's HP: 2000 / 2000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 1000 damage to Baal!\n"
                    "Baal's HP: 1000 / 2000\n"

                    "\nBaal uses Thunderstorm!\n"
                    "Baal attacked you for 70.\n"
                    "Your HP: 330 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 330 / 400\n"
                    "Baal's HP: 1000 / 2000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 1000 damage to Baal!\n"
                    "Baal's HP: 0 / 2000\n"

                    "\nYou have slain the Baal!\n"
                    "You earned 400 gold! You now have 500 gold.\n"
                    "You earned 2000 XP! You now have 2000/2100 XP.\n\n\n"
        
                    "Baal: Arggh...AGGHHH...AHHHHHHHHHHHH!!! IT CAN'T BE!!! I WAS THE CHOSEN ONE!!!\n"
                    "I WAS SUPPOSED TO BRING BALANCE TO THE WORLD!!! AAAAARRRRGGGGHHHHHH!!!!!!!!!!\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['z', 'x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_baal_try_running(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 14,
                     "maxEXP": 2100, "currentEXP": 0, "atk": 100, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_baal(character, make_baal())
        expected = ("The stifling air exerts pressure onto your shoulders...\n"
                    "A figure rises up from the throne. \nThe air trembles in fear.\n"
                    "Baal: HAHAHAHA!!! Finally a worthy opponent!!! Let us celebrate this moment...\n"
                    "WITH A DUEL TO THE DEATH!!!!!!!!!!\n"

                    "\nYou have encountered a wild Baal!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Baal's HP: 2000 / 2000\n"
                    
                    "\nYou cannot run from a boss fight. Just die in battle.\n"
                    
                    "\nCurrent Status: \n"
                    "Your HP: 400 / 400\n"
                    "Baal's HP: 2000 / 2000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 1000 damage to Baal!\n"
                    "Baal's HP: 1000 / 2000\n"

                    "\nBaal uses Thunderstorm!\n"
                    "Baal attacked you for 70.\n"
                    "Your HP: 330 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 330 / 400\n"
                    "Baal's HP: 1000 / 2000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 1000 damage to Baal!\n"
                    "Baal's HP: 0 / 2000\n"

                    "\nYou have slain the Baal!\n"
                    "You earned 400 gold! You now have 500 gold.\n"
                    "You earned 2000 XP! You now have 2000/2100 XP.\n\n\n"

                    "Baal: Arggh...AGGHHH...AHHHHHHHHHHHH!!! IT CAN'T BE!!! I WAS THE CHOSEN ONE!!!\n"
                    "I WAS SUPPOSED TO BRING BALANCE TO THE WORLD!!! AAAAARRRRGGGGHHHHHH!!!!!!!!!!\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[10])
    @patch('builtins.input', side_effect=['x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_baal_death(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 70, "gold": 100, "level": 14,
                     "maxEXP": 2100, "currentEXP": 0, "atk": 100, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_baal(character, make_baal())
        expected = ("The stifling air exerts pressure onto your shoulders...\n"
                    "A figure rises up from the throne. \nThe air trembles in fear.\n"
                    "Baal: HAHAHAHA!!! Finally a worthy opponent!!! Let us celebrate this moment...\n"
                    "WITH A DUEL TO THE DEATH!!!!!!!!!!\n"

                    "\nYou have encountered a wild Baal!!\n"
                    "Current Status: \n"
                    "Your HP: 70 / 400\n"
                    "Baal's HP: 2000 / 2000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 1000 damage to Baal!\n"
                    "Baal's HP: 1000 / 2000\n"

                    "\nBaal uses Thunderstorm!\n"
                    "Baal attacked you for 70.\n"
                    "Your HP: 0 / 400\n"
                    "\nAlthough I waited for a blood-heating battle for eons... I assume this is the limits of "
                    "your inferior race...Farewell, weakling.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        