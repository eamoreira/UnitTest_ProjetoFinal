import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def setup_ice_cream_stand(self):
        return IceCreamStand('Kibon', 'sorvetes', ['chocolate', 'morango', 'creme'])

    def test_flavors_available(self, setup_ice_cream_stand, capsys):
        # Setup
        resultado_esperado = (
            "\nNo momento temos os seguintes sabores de sorvete disponíveis:"
            "\n\t-chocolate"
            "\n\t-morango"
            "\n\t-creme\n"
        )

        # Chamada
        setup_ice_cream_stand.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado


    def test_flavors_no_estoque(self, setup_ice_cream_stand, capsys):
        # Setup
        resultado_esperado = "Estamos sem estoque atualmente!\n"
        setup_ice_cream_stand.flavors = []

        # Chamada
        setup_ice_cream_stand.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [
        ('chocolate', 'Temos no momento chocolate!\n'),
        ('morango', 'Temos no momento morango!\n'),
        ('', 'Sabor indisponível!\n'),
        ('menta', 'Sabor indisponível!\n')
    ])
    def test_find_flavor_success(self, flavor, setup_ice_cream_stand, capsys, result):
        # Setup
        resultado_esperado = result

        # Chamada
        setup_ice_cream_stand.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [
        ('menta', 'menta adicionado ao estoque!\n'),
        ('morango', 'morango já disponível!\n'),
        ('chocolate', 'chocolate já disponível!\n'),
        ('', 'Sabor inválido!\n')
    ])
    def test_add_flavor_success(self, flavor, setup_ice_cream_stand, capsys, result):
        # Setup
        resultado_esperado = result

        # Chamada
        setup_ice_cream_stand.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado
