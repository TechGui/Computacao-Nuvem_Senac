## Automação de Acesso ao Blackboard
### Descrição
Este script Python automatiza o processo de login e navegação na plataforma Blackboard, agilizando o acesso às suas atividades.

### Pré-requisitos
**Python:** Instale a versão mais recente do Python (https://www.python.org/).
**Selenium:** Instale a biblioteca Selenium utilizando o gerenciador de pacotes pip:

```pip install selenium```

**WebDriver:** Instale a biblioteca WebDriver correspondente ao seu navegador (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

```pip install webdriver_manager```

Instalação
**Clone o repositório:**

```git clone https://seu-repositorio.git```

**Crie um arquivo .env:** Crie um arquivo chamado .env na raiz do projeto e adicione as seguintes linhas, substituindo os valores pelas suas credenciais:

```BLACKBOARD_CPF = seu_cpf```
```BLACKBOARD_SENHA = sua_senha```

### Uso
**Execute o script:**

```python login_blackboard.py```

**Selecione a opção desejada:** Siga as instruções no terminal para escolher a sala de aula que deseja acessar.

### Configurações
**Navegador:** O script utiliza o navegador Firefox por padrão. Para alterar o navegador, modifique a linha onde o WebDriver é inicializado.
**Credenciais:** As credenciais de acesso ao Blackboard são armazenadas no arquivo .env para garantir a segurança.
**Seletores CSS:** Os seletores CSS utilizados para localizar os elementos na página do Blackboard podem precisar ser ajustados caso a interface da plataforma seja alterada.

### 🤝 Contribuídores

<a href="https://github.com/Gerson-Clara"><img src="https://github.com/Gerson-Clara.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/TechGui"><img src="https://github.com/TechGui.png" width="45" height="45"></a> &nbsp;