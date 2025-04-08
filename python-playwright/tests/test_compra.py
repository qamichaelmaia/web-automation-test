import sys
import os
import time
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_page import MenuPage



@pytest.mark.feature("Fluxo de compra")
def test_fluxo_de_compra():
    """
    Teste automatizado que valida o fluxo de compra completo com sucesso no sistema.
    - Login
    - Adição de produtos
    - Remoção de item
    - Checkout
    - Logout
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()

        try:
            login_page = LoginPage(page)
            inventory = InventoryPage(page)
            cart = CartPage(page)
            checkout = CheckoutPage(page)
            menu = MenuPage(page)

            print("Login no sistema")
            login_page.acessar()
            login_page.preencher_dados()
            login_page.logar()

            print("Adicionar produtos e acessar o carrinho")
            inventory.adicionar_todos_produtos()
            inventory.acessar_carrinho()

            print("Remover item e iniciar checkout")
            cart.remover_um_item()
            cart.iniciar_checkout()

            print("Preencher dados e finalizar compra")
            checkout.preencher_info()
            checkout.continuar_e_finalizar()

            print("Logout do sistema")
            menu.logout()

        except Exception as e:
            screenshot_path = f"reports/screenshots/test_fluxo_de_compra_error.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            page.screenshot(path=screenshot_path, full_page=True)
            pytest.fail(f"Teste falhou com exceção: {e}")

        finally:
            print("Encerrando navegador...")
            time.sleep(2)
            browser.close()
