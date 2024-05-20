from pydantic_settings import BaseSettings
from pydantic import SecretStr, BaseModel
from decouple import config



class ServerSettings(BaseModel):
    port: SecretStr = SecretStr(config('port'))
    host: SecretStr = SecretStr(config('host'))

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'



server_settings = ServerSettings()