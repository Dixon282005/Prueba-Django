import requests

def obtener_repos_originales(usuario):
    url = f'https://api.github.com/users/{usuario}/repos'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error en la petición: {e}")
        return []
    
    repos_data = response.json()
    
    return [
        repo['name'] 
        for repo in repos_data 
        if not repo.get('fork', False)
    ]