import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def setup_ice_cream_stand(self):
        return IceCreamStand('Kibon', 'sorvetes', ['chocolate', 'morango', 'creme'])

    @pytest.mark.parametrize('result',
                             [
                                 'No momento temos os seguintes sabores de sorvete disponíveis:\n'
                                 'Estamos sem estoque atualmente!\n'
                             ])
    def test_flavors_available(self, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 'Temos no momento \n',
                                 'Não temos no momento \n',
                                 'Estamos sem estoque atualmente!'
                             ])
    def test_find_flavor(self, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.describe_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 'Sabor já disponivel!\n',
                                 'adicionado ao estoque!\n',
                                 'Estamos sem estoque atualmente!'
                             ])
    def test_add_flavor(self, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.describe_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado
