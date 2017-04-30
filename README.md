# GEODJANGO BOILERPLATE

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com **Python 3.5.0**
3. Ative o virtualenv.
4. Instale as dependências.
5. Crie um banco de dados espaciais com o **PostgreSQL/PostGIS**
6. Configure a instância com o .env

```console
git clone git@github.com:marcellobenigno/geodjango_boilerplate.git geodjango_boilerplate_src
cd geodjango_boilerplate
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
createdb geodjango_boilerplate -T postgis
cp contrib/env-sample .env
```