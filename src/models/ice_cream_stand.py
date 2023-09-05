from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")
        else:
            print("Estamos sem estoque atualmente!")

    # 6- Melhoria: Correção no retorno do metodo, para que informe o sabor e não a lista de sabores
    # 7- Melhoria: Removido do metodo buscar sabor a condição desnecessaria "if self.flavors:"
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if flavor in self.flavors:
            print(f"Temos no momento {flavor}!")
        else:
            print(f"Não temos no momento {flavor}!")

    # 8- Melhoria: Removido do metodo adicionar sabor o retorno desnecessario "Estamos sem estoque atualmente!"
    # 9- Melhoria: Alterado do metodo adicionar sabor a condição para acrescentar
    # apenas um não existente na lista de sabores
    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"{flavor} adicionado ao estoque!")
        else:
            print(f"{flavor} já disponível!")
