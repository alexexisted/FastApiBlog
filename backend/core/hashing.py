from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


# print(Hasher.get_password_hash("supersecret1234"))
# print(Hasher.verify_password("supersecret1234","$2b$12$hZOm1kcq2yuiiqYp9s0W1.c1sjEOt//kaD1yD8vdv3B2Ypm5mkJ4G"))
