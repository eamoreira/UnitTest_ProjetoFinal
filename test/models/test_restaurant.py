import pytest

from src.models.restaurant import Restaurant

class TestRestaurant:

    @pytest.fixture
    def restaurant(self):
        return Restaurant('Meu Restaurante', 'Comida Brasileira')

    def test_describe_restaurant(self, restaurant, capsys):
        # Setup
        expected_output = (
            "Esse restaurante chama Meu Restaurante e serve Comida Brasileira.\n"
            "Esse restaurante está servindo 0 consumidores desde que está aberto.\n"
        )

        # Chamada
        restaurant.describe_restaurant()
        captured = capsys.readouterr()
        output = captured.out

        # Avaliação
        assert output == expected_output

    @pytest.mark.parametrize('isOpened, result', [
        (True, ' aberto!\n'),
        (False, ' abrindo!\n')
    ])
    def test_open_restaurant(self, isOpened, restaurant, capsys, result):
        # Setup
        resultado_esperado = result
        restaurant.open = isOpened

        # Chamada
        restaurant.open_restaurant()
        captured = capsys.readouterr()
        output = captured.out

        # Avaliação
        assert output == f'{restaurant.restaurant_name}' + resultado_esperado

    @pytest.mark.parametrize('isOpen, result', [
        (False, ' fechado!\n'),
        (True, ' fechando!\n')
    ])
    def test_close_restaurant(self, isOpen, restaurant, capsys, result):
        # Setup
        expected_output = result
        restaurant.open = isOpen

        # Chamada
        restaurant.close_restaurant()  # Em seguida, fecha o restaurante
        captured = capsys.readouterr()
        output = captured.out

        # Avaliação
        assert output == f'{restaurant.restaurant_name}' + expected_output

    def test_set_number_served(self, restaurant, capsys):
        # Setup
        expected_output = "Meu Restaurante está fechado!\n"

        # Chamada
        restaurant.set_number_served(50)  # Tenta definir o número de clientes quando o restaurante está fechado
        captured = capsys.readouterr()
        output = captured.out

        # Avaliação
        assert output == expected_output

    def test_increment_number_served(self, restaurant, capsys):
        # Setup
        expected_output = "Meu Restaurante está fechado!\n"

        # Chamada
        restaurant.increment_number_served(10)  # Tenta incrementar o número de clientes quando o restaurante está fechado
        captured = capsys.readouterr()
        output = captured.out

        # Avaliação
        assert output == expected_output
