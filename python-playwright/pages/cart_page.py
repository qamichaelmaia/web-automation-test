class CartPage:
    def __init__(self, page):
        self.page = page
        self.botao_remover = 'button[data-test^="remove"]'
        self.botao_checkout = 'button[data-test="checkout"]'

    def remover_um_item(self):
        print("Removendo um produto do carrinho...")
        self.page.wait_for_selector('.cart_item')
        self.page.click(self.botao_remover)
        print("Produto removido!")

    def iniciar_checkout(self):
        print("Iniciando o processo de checkout...")
        self.page.click(self.botao_checkout)
        self.page.wait_for_selector('input[data-test="firstName"]')
