class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.input_nome = 'input[data-test="firstName"]'
        self.input_sobrenome = 'input[data-test="lastName"]'
        self.input_cep = 'input[data-test="postalCode"]'
        self.botao_continuar = 'input[data-test="continue"]'
        self.botao_finalizar = 'button[data-test="finish"]'

    def preencher_info(self):
        print("Preenchendo informações do checkout...")
        self.page.fill(self.input_nome, "Michael")
        self.page.fill(self.input_sobrenome, "Maia")
        self.page.fill(self.input_cep, "12345")

    def continuar_e_finalizar(self):
        print("Continuando e finalizando compra...")
        self.page.click(self.botao_continuar)
        self.page.wait_for_selector('.summary_info')
        self.page.click(self.botao_finalizar)
        self.page.wait_for_selector('.complete-header')
        print("Compra finalizada com sucesso!")
