
from login import SankhyaLogin

if __name__ == "__main__":
    sankhyaLogin = SankhyaLogin()
    bearer_token = sankhyaLogin.get_bearer_token()
    print(bearer_token)