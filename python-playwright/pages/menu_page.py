class MenuPage:
    def __init__(self, page):
        self.page = page
        self.botao_menu = 'button[id="react-burger-menu-btn"]'
        self.link_logout = 'a#logout_sidebar_link'

    def logout(self):
        print("Realizando logout...")
        self.page.click(self.botao_menu)
        self.page.wait_for_selector(self.link_logout)
        self.page.click(self.link_logout)
        self.page.wait_for_selector('input[data-test="login-button"]')
        print("Logout concluído!")
