import requests

def executar_passo_2(cpf: str):
    """
    Realiza a requisição POST para o Passo 2 do desafio Hashcode.
    """

    url = "https://desafio-endpoint-hashcode-n2.onrender.com/passo2"
    
    payload = {
        "cpf": cpf
    }
    
    print(f"Iniciando Passo 2...")
    print(f"Enviando POST para: {url}\n")
    
    try:

        response = requests.post(url, json=payload)
        
        response.raise_for_status()
        
        print("Requisição realizada com sucesso!")
        print("Resposta do Servidor:")
        
        print(response.json())
        
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        print(f"Erro_info: {response.text}")
    except Exception as err:
        print(f"Ocorreu um erro inesperado: {err}")

if __name__ == "__main__":
    MEU_CPF = "xxx.xxx.xxx-xx"
    
    executar_passo_2(MEU_CPF)