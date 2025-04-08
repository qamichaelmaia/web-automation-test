from utils.config import URL, USUARIO, SENHA

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = URL
        self.usuario_input = 'input[data-test="username"]'
        self.senha_input = 'input[data-test="password"]'
        self.botao_login = 'input[data-test="login-button"]'

    def acessar(self):
        print("Acessando a página de login...")
        self.page.goto(self.url)
        self.page.wait_for_selector(self.usuario_input)

    def preencher_dados(self, usuario=USUARIO, senha=SENHA):
        print("Preenchendo dados de login...")
        self.page.fill(self.usuario_input, usuario)
        self.page.fill(self.senha_input, senha)

    def logar(self):
        print("Efetuando login...")
        self.page.click(self.botao_login)
        self.page.wait_for_selector('.inventory_list')
        print("Login realizado com sucesso!")
