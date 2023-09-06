import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    sem_estoque = []
    com_estoque = ['chocolate', 'morango', 'creme']

    @pytest.fixture
    def setup_ice_cream_stand(self, estoque):
        return IceCreamStand('Kibon', 'sorvetes', estoque)

    @pytest.fixture
    def setup_ice_cream_stand_no_estoque(self):
        return IceCreamStand('Kibon', 'sorvetes', [])

    @pytest.mark.parametrize('estoque, expected_result',
                             [(com_estoque, '\nNo momento temos os seguintes sabores de sorvete disponíveis:'
                              '\n\t-chocolate\n\t-morango\n\t-creme\n'),
                              (sem_estoque, 'Estamos sem estoque atualmente!\n')])
    def test_flavors_available(self, setup_ice_cream_stand, estoque, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('estoque, flavor, expected_result',
                             [(com_estoque, 'chocolate', 'Temos no momento chocolate!\n'),
                              (com_estoque, '', 'Por favor, informe um sabor válido.\n'),
                              (com_estoque, 'menta', 'Não temos no momento menta!\n'),
                              (sem_estoque, 'chocolate', 'Estamos sem estoque atualmente!\n'),
                              (sem_estoque, '', 'Estamos sem estoque atualmente!\n'),
                              (sem_estoque, 'menta', 'Estamos sem estoque atualmente!\n')])
    def test_find_flavor(self, setup_ice_cream_stand, flavor, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('estoque, flavor, expected_result',
                             [(com_estoque, 'menta', 'menta adicionado ao estoque!\n'),
                              (com_estoque, 'morango', 'morango já disponível!\n'),
                              (com_estoque, '', 'Por favor, informe um sabor válido.\n'),
                              (sem_estoque, 'menta', 'menta adicionado ao estoque!\n'),
                              (sem_estoque, '', 'Por favor, informe um sabor válido.\n')])
    def test_add_flavor(self, setup_ice_cream_stand, flavor, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result