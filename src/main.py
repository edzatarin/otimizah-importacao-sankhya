
from login import SankhyaLogin
from parceiro import SankhyaParceiro

if __name__ == "__main__":
    #sankhyaLogin = SankhyaLogin()
    #bearer_token = sankhyaLogin.get_bearer_token()
    #print(bearer_token)
    sankhyaParc = SankhyaParceiro()
    parc = sankhyaParc.get_parceiro()