
## Ferramentas utilizadas:

<ul> 
<li>Terminal de sua escolha</li>
<li>Postman ou equivalente</li>
</ul>


## Instalação da Aplicação

Abra o terminal/Powershell e rode os comandos abaixo:

Clonando o repositório:
```
git clone https://github.com/andre21cavalcante/Api-python-Flask.git
```
Entrando na pasta:
```
cd Api-python-Flask-master

```

Instalando os pacotes:
```
pip install flask
```

```
pip install flask_sqlalchemy
```
Iniciando aplicação 

```
python
from app import db
```

---

## Rotas:

|Método|Rota|Descrição|
| -----| -----| -----------|
|**GET** | */users* | Mostra todos os usuarios|
|**GET** | */user/{numero_id}* | Mostra o usuário de id escolhido|
|**PUT** | */user/{numero_id}*| Atualiza as informações do id selecionado|
|**POST** | */user/* | Cria um novo usuário|
|**DELETE** | */user/{numero_id}* | Deleta o usuário|


---

Projeto desenvolvido por [André Cavalcante](https://github.com/andre21cavalcante)
