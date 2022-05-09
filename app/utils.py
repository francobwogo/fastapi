from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"], deprecated="auto")

def hash(password: str):
    hashed_password = pwd_context.hash(password)

    return hashed_password

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)