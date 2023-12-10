import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import combat_andromalius
from helper_functions.create_entity import make_andromalius


class TestCombatAndromalius(TestCase):

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_Andromalius(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 14,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 1}
        combat_andromalius(character, make_andromalius())
        expected = ("Each breath you take seems to pierce your lungs...\n"
                    "A demon in the figure of a man holding a serpent staff walks out of thin air...!\n"
                    "\nYou have encountered a wild Andromalius!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Andromalius' HP: 1000 / 1000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Andromalius!\n"
                    "Andromalius' HP: 500 / 1000\n"

                    "\nAndromalius uses Serpent's Fang!\n"
                    "Andromalius attacked you for 55.\n"
                    "Your HP: 345 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 345 / 400\n"
                    "Andromalius' HP: 500 / 1000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Andromalius!\n"
                    "Andromalius' HP: 0 / 1000\n"

                    "\nYou have slain the Andromalius!\n"
                    "You earned 350 gold! You now have 450 gold.\n"
                    "You earned 1100 XP! You now have 1100/800 XP.\n\n\n"
                    "\nYou have leveled up! You are now level 15. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 379 / 440 --- ATK: 56 --- EXP: 300 / 880\n\n"
                    "You gained a red orb, containing Andromalius' soul. You have no idea what to do with it.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 379)
        self.assertEqual(character['maxHP'], 440)
        self.assertEqual(character['atk'], 56)
        self.assertEqual(character['currentEXP'], 300)
        self.assertEqual(character['maxEXP'], 880)
        self.assertEqual(character['gold'], 450)
        self.assertEqual(character['orb'], 2)

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['z', 'x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_andromalius_try_running(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 15,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 1}
        combat_andromalius(character, make_andromalius())
        expected = ("Each breath you take seems to pierce your lungs...\n"
                    "A demon in the figure of a man holding a serpent staff walks out of thin air...!\n"
                    "\nYou have encountered a wild Andromalius!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Andromalius' HP: 1000 / 1000\n"
                    
                    "\nYou cannot run from a boss fight. Just die in battle.\n"
                    
                    "\nCurrent Status: \n"
                    "Your HP: 400 / 400\n"
                    "Andromalius' HP: 1000 / 1000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Andromalius!\n"
                    "Andromalius' HP: 500 / 1000\n"

                    "\nAndromalius uses Serpent's Fang!\n"
                    "Andromalius attacked you for 55.\n"
                    "Your HP: 345 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 345 / 400\n"
                    "Andromalius' HP: 500 / 1000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Andromalius!\n"
                    "Andromalius' HP: 0 / 1000\n"

                    "\nYou have slain the Andromalius!\n"
                    "You earned 350 gold! You now have 450 gold.\n"
                    "You earned 1100 XP! You now have 1100/800 XP.\n\n\n"
                    "\nYou have leveled up! You are now level 16. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 379 / 440 --- ATK: 56 --- EXP: 300 / 880\n\n"
                    "You gained a red orb, containing Andromalius' soul. You have no idea what to do with it.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 379)
        self.assertEqual(character['maxHP'], 440)
        self.assertEqual(character['atk'], 56)
        self.assertEqual(character['currentEXP'], 300)
        self.assertEqual(character['maxEXP'], 880)
        self.assertEqual(character['gold'], 450)
        self.assertEqual(character['orb'], 2)

    @patch('random.randint', side_effect=[10])
    @patch('builtins.input', side_effect=['x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_andromalius_death(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 55, "gold": 100, "level": 15,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 1}
        combat_andromalius(character, make_andromalius())
        expected = ("Each breath you take seems to pierce your lungs...\n"
                    "A demon in the figure of a man holding a serpent staff walks out of thin air...!\n"
                    "\nYou have encountered a wild Andromalius!!\n"
                    "Current Status: \n"
                    "Your HP: 55 / 400\n"
                    "Andromalius' HP: 1000 / 1000\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Andromalius!\n"
                    "Andromalius' HP: 500 / 1000\n"

                    "\nAndromalius uses Serpent's Fang!\n"
                    "Andromalius attacked you for 55.\n"
                    "Your HP: 0 / 400\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 0)
