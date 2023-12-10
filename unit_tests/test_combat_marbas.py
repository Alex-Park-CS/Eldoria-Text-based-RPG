import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import combat_marbas
from helper_functions.create_entity import make_marbas


class TestCombatMarbas(TestCase):
    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_marbas(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 14,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_marbas(character, make_marbas())
        expected = ("Visible mist forms when you start breathing...\n"
                    "A hideous lich rises from the ground...!\n"
                    "\nYou have encountered a wild Marbas!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Marbas' HP: 800 / 800\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Marbas!\n"
                    "Marbas' HP: 300 / 800\n"

                    "\nMarbas uses Tainting Hands!\n"
                    "Marbas attacked you for 65.\n"
                    "Your HP: 335 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 335 / 400\n"
                    "Marbas' HP: 300 / 800\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Marbas!\n"
                    "Marbas' HP: -200 / 800\n"

                    "\nYou have slain the Marbas!\n"
                    "You earned 300 gold! You now have 400 gold.\n"
                    "You earned 1000 XP! You now have 1000/800 XP.\n\n\n"
                    "\nYou have leveled up! You are now level 15. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 368 / 440 --- ATK: 56 --- EXP: 200 / 880\n\n"
                    "You gained a blue orb, containing Marbas' soul. You have no idea what to do with it.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 368)
        self.assertEqual(character['maxHP'], 440)
        self.assertEqual(character['atk'], 56)
        self.assertEqual(character['currentEXP'], 200)
        self.assertEqual(character['maxEXP'], 880)
        self.assertEqual(character['gold'], 400)
        self.assertEqual(character['orb'], 1)

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['z', 'x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_marbas_try_running(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 400, "gold": 100, "level": 14,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_marbas(character, make_marbas())
        expected = ("Visible mist forms when you start breathing...\n"
                    "A hideous lich rises from the ground...!\n"
                    "\nYou have encountered a wild Marbas!!\n"
                    "Current Status: \n"
                    "Your HP: 400 / 400\n"
                    "Marbas' HP: 800 / 800\n"
                    
                    "\nYou cannot run from a boss fight. Just die in battle.\n"
                    
                    "\nCurrent Status: \n"
                    "Your HP: 400 / 400\n"
                    "Marbas' HP: 800 / 800\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Marbas!\n"
                    "Marbas' HP: 300 / 800\n"

                    "\nMarbas uses Tainting Hands!\n"
                    "Marbas attacked you for 65.\n"
                    "Your HP: 335 / 400\n"

                    "\nCurrent Status: \n"
                    "Your HP: 335 / 400\n"
                    "Marbas' HP: 300 / 800\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Marbas!\n"
                    "Marbas' HP: -200 / 800\n"

                    "\nYou have slain the Marbas!\n"
                    "You earned 300 gold! You now have 400 gold.\n"
                    "You earned 1000 XP! You now have 1000/800 XP.\n\n\n"
                    "\nYou have leveled up! You are now level 15. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 368 / 440 --- ATK: 56 --- EXP: 200 / 880\n\n"
                    "You gained a blue orb, containing Marbas' soul. You have no idea what to do with it.\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 368)
        self.assertEqual(character['maxHP'], 440)
        self.assertEqual(character['atk'], 56)
        self.assertEqual(character['currentEXP'], 200)
        self.assertEqual(character['maxEXP'], 880)
        self.assertEqual(character['gold'], 400)
        self.assertEqual(character['orb'], 1)

    @patch('random.randint', side_effect=[10])
    @patch('builtins.input', side_effect=['x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_marbas_death(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 400, "currentHP": 65, "gold": 100, "level": 14,
                     "maxEXP": 800, "currentEXP": 0, "atk": 50, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        combat_marbas(character, make_marbas())
        expected = ("Visible mist forms when you start breathing...\n"
                    "A hideous lich rises from the ground...!\n"
                    "\nYou have encountered a wild Marbas!!\n"
                    "Current Status: \n"
                    "Your HP: 65 / 400\n"
                    "Marbas' HP: 800 / 800\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 500 damage to Marbas!\n"
                    "Marbas' HP: 300 / 800\n"

                    "\nMarbas uses Tainting Hands!\n"
                    "Marbas attacked you for 65.\n"
                    "Your HP: 0 / 400\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 0)
