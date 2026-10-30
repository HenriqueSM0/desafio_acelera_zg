import requests

def executar_passo_3(cpf: str):
    """
    Realiza a requisição POST para o Passo 3 do desafio Hashcode.
    Envia o CPF e a resposta calculada da questão de pseudocódigo.
    """

    url = "https://desafio-endpoint-hashcode-n2.onrender.com/passo3"
    
    resposta_questao = "11"
    
    payload = {
        "cpf": cpf,
        "respostaQuestaoObjetiva": resposta_questao
    }
    
    print(f"Iniciando Passo 3...")
    print(f"Resposta calculada da questão: {resposta_questao}")
    print(f"Enviando POST para: {url}\n")
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        print("Requisição realizada com sucesso!")
        print("Resposta do Servidor (Passo 3):")
        print(response.json())
        
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        print(f"Erro_info: {response.text}")
    except Exception as err:
        print(f"Ocorreu um erro inesperado: {err}")

if __name__ == "__main__":
    MEU_CPF = "xxx.xxx.xxx-xx" 
    
    executar_passo_3(MEU_CPF)