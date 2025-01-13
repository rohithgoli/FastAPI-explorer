from passlib.context import CryptContext

pwd_cxt = CryptContext(schemas=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)