#  Web Automation Test com Python + Playwright + Pytest

Este repositório contém uma suíte de testes automatizados desenvolvida com **Playwright (modo síncrono)** e **Pytest**, simulando o fluxo completo de compra em uma aplicação web. O projeto inclui cenários funcionais, captura de evidências (screenshots), geração de relatórios em HTML e estrutura modular baseada em Page Objects.

---

##  Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Playwright Python](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [pytest-html](https://pypi.org/project/pytest-html/)
- Estrutura Page Object Model (POM)

---

##  Cenários de Teste

- ✅ Login no sistema
- ✅ Adição de todos os produtos ao carrinho
- ✅ Remoção de um item
- ✅ Preenchimento dos dados de checkout
- ✅ Finalização da compra
- ✅ Logout do sistema
- ⚠️ Captura de screenshot automática em caso de falha

---

##  Instalação e Execução
### 1 - Crie um ambiente virtual

``` bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 2 - Instale as dependências

``` bash
pip install -r requirements.txt
```
### 3 - Instale o browser do playwright

``` bash
playwright install
```
### 4 - Rode os testes com relatório HTML

``` bash
pytest tests/ --html=reports/report.html --self-contained-html
```