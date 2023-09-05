import pytest

from src.models.restaurant import Restaurant


class TestRestaurant:

    @pytest.fixture
    def restaurant_setup(self):
        # Criar uma instância do restaurante e retorná-la
        return Restaurant("Sorveteria", "Sorvetes")

    @pytest.mark.parametrize('result',
                             [
                                 'Esse restaturante chama Sorveteria e serve Sorvetes.\n'
 'Esse restaturante está servindo 0 consumidores desde que está aberto.\n'
                             ])
    def test_describe_restaurant(self, restaurant_setup, result, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result

        # Chamada
        restaurante.describe_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 'Sorveteria agora está aberto!\n',
                                 'Sorveteria já está aberto!\n'
                             ])
    def test_open_restaurant(self, restaurant_setup, result, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result

        # Chamada
        restaurante.open_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 'Sorveteria agora está fechado!\n',
                                 'Sorveteria já está fechado!\n'
                             ])
    def test_close_restaurant(self, restaurant_setup, result, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result

        # Chamada
        restaurante.close_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 '10\n',
                                 'Sorveteria está fechado!\n'
                             ])
    def test_set_number_served(self, restaurant_setup, result, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result

        # Chamada
        restaurante.set_number_served(10)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 '22\n',
                                 'Sorveteria está fechado!\n'
                             ])
    def test_increment_number_served(self, restaurant_setup, result, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result
        restaurante.set_number_served(10)

        # Chamada
        restaurante.increment_number_served(12)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    '''
        # Cenário de teste com sucesso, somando o numero de clientes já servidos
        def test_increment_number_served_com_sucesso(self, restaurant_setup, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result
        restaurante.set_number_served(10)

        # Chamada
        restaurante.increment_number_served(12)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado
        
        # Cenário de teste alternativo, tentando somar no numero de clientes já servidos em um restaurante já fechado
        def test_increment_number_served_fechado(self, restaurant_setup, capsys):
        # Setup
        restaurante = restaurant_setup
        resultado_esperado = result
        restaurante.set_number_served(10)

        # Chamada
        restaurante.increment_number_served(12)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado
    '''