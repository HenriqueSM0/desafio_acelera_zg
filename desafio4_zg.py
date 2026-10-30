import requests

def executar_passo_4(cpf: str):
    """
    Realiza a requisição GET para o Passo 4 do desafio Hashcode.
    Envia CPF, nome formatado e o token recebido no passo anterior como query parameters.
    """
    url = "https://desafio-endpoint-hashcode-n2.onrender.com/passo4"
    
    token = "843a08efe8a5f5d57d8539619ea4d52b0f563112"
    
    nome_formatado = "Nome_Sobrenome" 
    
    parametros = {
        "cpf": cpf,
        "nome": nome_formatado,
        "token": token
    }
    
    print(f"Iniciando Passo 4...")
    print(f"Enviando GET para: {url} com os parâmetros definidos.\n")
    
    try:
        response = requests.get(url, params=parametros)
        
        response.raise_for_status()
        
        print("Requisição realizada com sucesso!")
        print("Resposta do Servidor (Passo 4):")
        
        print(response.json())
        
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        print(f"Erro_info: {response.text}")
    except Exception as err:
        print(f"Ocorreu um erro inesperado: {err}")

if __name__ == "__main__":
    MEU_CPF = "xxx.xxx.xxx-xx"
    
    executar_passo_4(MEU_CPF)