import io
from unittest import TestCase
from unittest.mock import patch
from helper_functions.special_events import combat


class TestCombat(TestCase):
    @patch('random.randint', side_effect=[5, 6])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_boar(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 20, "orb": 0}
        mutant_boar = {"name": "Mutant Boar", "currentHP": 50, "maxHP": 50, "move": "Headbutt",
                       "atk": 5, "EXP": 10, "gold": 5, "runnable": True}
        combat(character, mutant_boar)
        expected = ("\nYou have encountered a wild Mutant Boar!!\n"
                    "Current Status: \n"
                    "Your HP: 100 / 100\n"
                    "Mutant Boar's HP: 50 / 50\n"

                    "\nYou rolled the die of fate... to roll 5!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 25 damage to Mutant Boar!\n"
                    "Mutant Boar's HP: 25 / 50\n"

                    "\nMutant Boar uses Headbutt!\n"
                    "Mutant Boar attacked you for 5.\n"
                    "Your HP: 95 / 100\n"

                    "\nCurrent Status: \n"
                    "Your HP: 95 / 100\n"
                    "Mutant Boar's HP: 25 / 50\n"

                    "\nYou rolled the die of fate... to roll 6!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 30 damage to Mutant Boar!\n"
                    "Mutant Boar's HP: -5 / 50\n"

                    "\nYou have slain the Mutant Boar!\n"
                    "You earned 5 gold! You now have 105 gold.\n"
                    "You earned 10 XP! You now have 10/50 XP.\n\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 95)
        self.assertEqual(character['gold'], 105)
        self.assertEqual(character['currentEXP'], 10)

    @patch('random.randint', side_effect=[12, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_soldier(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 100, "currentHP": 100, "gold": 100, "level": 1,
                     "maxEXP": 50, "currentEXP": 0, "atk": 5, "move": "Magic Missile",
                     "x-position": 10, "y-position": 10, "orb": 0}
        soldier = {"name": "Legion Soldier", "currentHP": 100, "maxHP": 100, "move": "Spear Thrust",
                   "atk": 10, "EXP": 25, "gold": 20, "runnable": True}
        combat(character, soldier)
        expected = ("\nYou have encountered a wild Legion Soldier!!\n"
                    "Current Status: \n"
                    "Your HP: 100 / 100\n"
                    "Legion Soldier's HP: 100 / 100\n"

                    "\nYou rolled the die of fate... to roll 12!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 60 damage to Legion Soldier!\n"
                    "Legion Soldier's HP: 40 / 100\n"

                    "\nLegion Soldier uses Spear Thrust!\n"
                    "Legion Soldier attacked you for 10.\n"
                    "Your HP: 90 / 100\n"

                    "\nCurrent Status: \n"
                    "Your HP: 90 / 100\n"
                    "Legion Soldier's HP: 40 / 100\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 50 damage to Legion Soldier!\n"
                    "Legion Soldier's HP: -10 / 100\n"

                    "\nYou have slain the Legion Soldier!\n"
                    "You earned 20 gold! You now have 120 gold.\n"
                    "You earned 25 XP! You now have 25/50 XP.\n\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 90)
        self.assertEqual(character['gold'], 120)
        self.assertEqual(character['currentEXP'], 25)

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_imp(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 300, "currentHP": 300, "gold": 100, "level": 10,
                     "maxEXP": 50, "currentEXP": 0, "atk": 20, "move": "Magic Missile",
                     "x-position": 10, "y-position": 19, "orb": 0}
        imp = {"name": "Imp", "currentHP": 300, "maxHP": 300, "atk": 20, "EXP": 35,
               "move": "Tail Whip", "gold": 20, "runnable": True}
        combat(character, imp)
        expected = ("\nYou have encountered a wild Imp!!\n"
                    "Current Status: \n"
                    "Your HP: 300 / 300\n"
                    "Imp's HP: 300 / 300\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Imp!\n"
                    "Imp's HP: 100 / 300\n"

                    "\nImp uses Tail Whip!\n"
                    "Imp attacked you for 20.\n"
                    "Your HP: 280 / 300\n"

                    "\nCurrent Status: \n"
                    "Your HP: 280 / 300\n"
                    "Imp's HP: 100 / 300\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Imp!\n"
                    "Imp's HP: -100 / 300\n"

                    "\nYou have slain the Imp!\n"
                    "You earned 20 gold! You now have 120 gold.\n"
                    "You earned 35 XP! You now have 35/50 XP.\n\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 280)
        self.assertEqual(character['gold'], 120)
        self.assertEqual(character['currentEXP'], 35)

    @patch('random.randint', side_effect=[10, 10])
    @patch('builtins.input', side_effect=['x', 'x'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_commander_level_up_in_combat(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 300, "currentHP": 300, "gold": 100, "level": 10,
                     "maxEXP": 50, "currentEXP": 0, "atk": 20, "move": "Magic Missile",
                     "x-position": 10, "y-position": 18, "orb": 0}
        commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400,
                     "move": "Sword Slash", "atk": 40, "EXP": 60, "gold": 75, "runnable": True}
        combat(character, commander)
        expected = ("\nYou have encountered a wild Legion Commander!!\n"
                    "Current Status: \n"
                    "Your HP: 300 / 300\n"
                    "Legion Commander's HP: 400 / 400\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Legion Commander!\n"
                    "Legion Commander's HP: 200 / 400\n"

                    "\nLegion Commander uses Sword Slash!\n"
                    "Legion Commander attacked you for 40.\n"
                    "Your HP: 260 / 300\n"

                    "\nCurrent Status: \n"
                    "Your HP: 260 / 300\n"
                    "Legion Commander's HP: 200 / 400\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Legion Commander!\n"
                    "Legion Commander's HP: 0 / 400\n"

                    "\nYou have slain the Legion Commander!\n"
                    "You earned 75 gold! You now have 175 gold.\n"
                    "You earned 60 XP! You now have 60/50 XP.\n\n\n"
                    "\nYou have leveled up! You are now level 11. You feel stronger, "
                    "as the aura around you settles down.\n"
                    "Your new stats --- HP: 286 / 330 --- ATK: 22 --- EXP: 10 / 55\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 286)
        self.assertEqual(character['atk'], 22)
        self.assertEqual(character['gold'], 175)
        self.assertEqual(character['currentEXP'], 10)

    @patch('random.randint', side_effect=[10])
    @patch('builtins.input', side_effect=['x', 'z'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_commander_hit_and_run(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 300, "currentHP": 300, "gold": 100, "level": 10,
                     "maxEXP": 50, "currentEXP": 0, "atk": 20, "move": "Magic Missile",
                     "x-position": 11, "y-position": 18, "orb": 0}
        commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400,
                     "move": "Sword Slash", "atk": 40, "EXP": 60, "gold": 75, "runnable": True}
        combat(character, commander)
        expected = ("\nYou have encountered a wild Legion Commander!!\n"
                    "Current Status: \n"
                    "Your HP: 300 / 300\n"
                    "Legion Commander's HP: 400 / 400\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Legion Commander!\n"
                    "Legion Commander's HP: 200 / 400\n"

                    "\nLegion Commander uses Sword Slash!\n"
                    "Legion Commander attacked you for 40.\n"
                    "Your HP: 260 / 300\n"

                    "\nCurrent Status: \n"
                    "Your HP: 260 / 300\n"
                    "Legion Commander's HP: 200 / 400\n"

                    "\nYou run away, shrieking like a little girl. To think that the fate of "
                    "this world lies on the likes of you...\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 260)
        self.assertEqual(character['gold'], 100)
        self.assertEqual(character['currentEXP'], 0)

    @patch('random.randint', side_effect=[10])
    @patch('builtins.input', side_effect=['x', 'z'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_commander_character_death(self, mock_output, _, __):
        character = {"name": "Ysera", "maxHP": 300, "currentHP": 40, "gold": 100, "level": 10,
                     "maxEXP": 50, "currentEXP": 0, "atk": 20, "move": "Magic Missile",
                     "x-position": 11, "y-position": 18, "orb": 0}
        commander = {"name": "Legion Commander", "currentHP": 400, "maxHP": 400,
                     "move": "Sword Slash", "atk": 40, "EXP": 60, "gold": 75, "runnable": True}
        combat(character, commander)
        expected = ("\nYou have encountered a wild Legion Commander!!\n"
                    "Current Status: \n"
                    "Your HP: 40 / 300\n"
                    "Legion Commander's HP: 400 / 400\n"

                    "\nYou rolled the die of fate... to roll 10!\n"

                    "\nYou used Magic Missile!\n"
                    "You dealt 200 damage to Legion Commander!\n"
                    "Legion Commander's HP: 200 / 400\n"

                    "\nLegion Commander uses Sword Slash!\n"
                    "Legion Commander attacked you for 40.\n"
                    "Your HP: 0 / 300\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
        self.assertEqual(character['currentHP'], 0)
