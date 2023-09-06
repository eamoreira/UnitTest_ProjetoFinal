import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def setup_ice_cream_stand(self):
        return IceCreamStand('Kibon', 'sorvetes', ['chocolate', 'morango', 'creme'])

    @pytest.mark.parametrize('result', ['\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t-chocolate\n\t-morango\n\t-creme\n'])
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

    @pytest.mark.parametrize('result', ['Estamos sem estoque atualmente!\n'])
    def test_flavors_no_estoque(self, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result
        sorveteria.flavors = []

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('chocolate', 'Temos no momento chocolate!\n'),
                                                ('morango', 'Temos no momento morango!\n'),
                                                ('', 'Sabor indisponível!\n'),
                                                ('menta', 'Sabor indisponível!\n')])
    def test_find_flavor_success(self, flavor, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('menta', 'menta adicionado ao estoque!\n'),
                                                ('morango', 'morango já disponível!\n'),
                                                ('chocolate', 'chocolate já disponível!\n'),
                                                ('', 'Sabor inválido!\n')])
    def test_add_flavor_success(self, flavor, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    # @pytest.mark.parametrize('result',
    #                          [
    #                              'Temos no momento \n',
    #                              'Não temos no momento \n',
    #                              'Estamos sem estoque atualmente!'
    #                          ])
    # def test_find_flavor(self, setup_ice_cream_stand, result, capsys):
    #     # Setup
    #     sorveteria = setup_ice_cream_stand
    #     resultado_esperado = result
    #
    #     # Chamada
    #     sorveteria.describe_restaurant()
    #     captured = capsys.readouterr()
    #     resultado = captured.out
    #
    #     # Avaliação
    #     assert resultado == resultado_esperado

    # @pytest.mark.parametrize('result',
    #                          [
    #                              'Sabor já disponivel!\n',
    #                              'adicionado ao estoque!\n',
    #                              'Estamos sem estoque atualmente!'
    #                          ])
    # def test_add_flavor(self, setup_ice_cream_stand, result, capsys):
    #     # Setup
    #     sorveteria = setup_ice_cream_stand
    #     resultado_esperado = result
    #
    #     # Chamada
    #     sorveteria.describe_restaurant()
    #     captured = capsys.readouterr()
    #     resultado = captured.out
    #
    #     # Avaliação
    #     assert resultado == resultado_esperado
