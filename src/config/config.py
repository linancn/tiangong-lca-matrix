import toml

config = toml.load(".secrets/secrets.toml")

FASTAPI_AUTH = config["FASTAPI"]["FASTAPI_AUTH"]
FASTAPI_BEARER_TOKEN = config["FASTAPI"]["BEARER_TOKEN"]
