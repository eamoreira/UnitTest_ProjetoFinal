class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # 1- Melhoria: correção para retornar os textos da descrição do restaurante
    # 2- Melhoria: correção na chamada do restaurant_name
    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        print(f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.")
        print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")

    # 3- Melhoria: Alterado o valor do 'self.open' de False para True
    # 4- Melhoria: Alterado o valor do 'number_served' de -2 para 0
    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            print(f"{self.restaurant_name} abrindo!")
        else:
            print(f"{self.restaurant_name} aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} fechando!")
        else:
            print(f"{self.restaurant_name} fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    # 5- Melhoria: Alterado de = para +=
    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers
        else:
            print(f"{self.restaurant_name} está fechado!")
