class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.botoes_adicionar = 'button.btn_inventory'
        self.link_carrinho = 'a.shopping_cart_link'

    def adicionar_todos_produtos(self):
        print("🛒 Adicionando todos os produtos ao carrinho...")
        botoes = self.page.locator(self.botoes_adicionar)
        count = botoes.count()
        for i in range(count):
            botoes.nth(i).click()
        print(f"{count} produto(s) adicionado(s) ao carrinho!")

    def acessar_carrinho(self):
        print("Acessando o carrinho de compras...")
        self.page.click(self.link_carrinho)
        self.page.wait_for_selector('.cart_item')
