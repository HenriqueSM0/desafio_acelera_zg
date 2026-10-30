# REST API Integration Challenge (Python)

Este repositório contém a solução automatizada em Python para um desafio sequencial de integração com APIs RESTful. O projeto demonstra a comunicação de ponta a ponta com serviços web, englobando autenticação, manipulação de payloads JSON, uso de Query Parameters e validação de regras de negócio.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Requests** (Cliente HTTP)

## 📌 Fluxo da Aplicação

O fluxo é dividido em chamadas encadeadas onde cada resposta fornece instruções/credenciais para o estágio seguinte:

1. **Passo 1 & 2 (`POST`)**: Validação inicial com envio de payload estruturado em JSON.
2. **Passo 3 (`POST`)**: Resolução de problema de lógica/pseudocódigo e envio do resultado no corpo da requisição para geração de token de acesso.
3. **Passo 4 (`GET`)**: Autenticação e consumo de endpoint restrito utilizando o *Token Bearer/Query Parameter* recebido na etapa anterior.

## 🛠️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install requests
   ```

3. Execute o script principal:
   ```bash
   python desafiox_zg.py
   ```

---
> **Nota de Segurança:** Todos os dados sensíveis e chaves de identificação pessoal foram anonimizados no código público seguindo as melhores práticas de privacidade.