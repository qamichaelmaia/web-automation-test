from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Torna visível
    #iphone = p.devices['iPhone 15']  # Define o dispositivo para simular

    context = browser.new_context(
        color_scheme='light',  # Define o tema escuro
        #record_video_dir='.', # Diretório para salvar os vídeos
        viewport={'width': 1280, 'height': 720},  # Define a largura e altura da janela
        #**iphone,  # Define o dispositivo para simular
    )

    page = context.new_page()

    page.goto('https://admin-demo.nopcommerce.com/login')
    sleep(3)

    print(page.title())

    #breakpoint = page.pause()  # Pausa a execução do script para depuração
    browser.close()
