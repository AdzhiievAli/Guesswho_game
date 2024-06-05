import pytest
import pygame
from unittest.mock import Mock, patch
from main_logic import GuessWhoGame
import os

@pytest.fixture
def setup_game():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pack = 'fruits_pack'
    game = GuessWhoGame(screen, pack)
    yield game
    pygame.quit()

@pytest.fixture
def setup_mock_game():
    with patch('main_logic.GuessWhoGame.__init__', lambda x, y, z: None):
        game = GuessWhoGame(None, None)
        game.screen = pygame.display.set_mode((1920, 1080))
        game.current_player = 1
        game.secret_card1 = Mock()
        game.secret_card2 = Mock()
        game.board1 = Mock()
        game.board2 = Mock()
        game.final_guess_button = pygame.Rect(800, 900, 200, 50)
        game.question_button1 = Mock()
        game.question_button2 = Mock()
        yield game
    pygame.quit()

@pytest.mark.parametrize("initial_player, expected_player", [
    (1, 2),
    (2, 1)
])
def test_switch_player(setup_game, initial_player, expected_player):
    game = setup_game
    game.current_player = initial_player
    game.switch_player()
    assert game.current_player == expected_player

def test_load_pack(setup_game):
    game = setup_game
    assert os.path.exists(game.pack_path)
    names_file_path = os.path.join(game.pack_path, 'names.txt')
    questions_file_path = os.path.join(game.pack_path, 'questions.txt')
    assert os.path.exists(names_file_path)
    assert os.path.exists(questions_file_path)
    card_images = [os.path.join(game.pack_path, f'{i}.png') for i in range(1, 13)]
    for image in card_images:
        assert os.path.exists(image)

def test_final_guess_correct_guess(setup_mock_game):
    game = setup_mock_game
    game.secret_card2.name = "TestName"
    game.current_player = 1

    with patch('builtins.input', return_value="TestName"):
        result = game.final_guess_button.collidepoint((850, 925))  
        assert result

if __name__ == '__main__':
    pytest.main()
