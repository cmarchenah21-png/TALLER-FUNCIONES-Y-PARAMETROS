def conectar_api(url, timeout=30, retries=3, use_ssl=True):
    return f"Conectando a {url} | timeout={timeout}s | retries={retries} | use_ssl={use_ssl}"


print(conectar_api("https://api.ejemplo.com"))

print(conectar_api("https://api.ejemplo.com", timeout=60, retries=5, use_ssl=False))