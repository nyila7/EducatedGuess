import argon2
import conf
ph = argon2.PasswordHasher()


def hash_password(password):
    return ph.hash(password)


def verify_password(hashed_password, password):
    try:
        ph.verify(hashed_password, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False


def get_hashed_password(username) -> str:
    with open(conf.path("users.txt"), mode="r", encoding="utf-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            if ":" in sor:
                if sor.split(":")[0] == username:
                    return sor.split(":")[1].strip()
    return None


def add_user(username, password) -> bool:
    if get_hashed_password(username) is not None:
        return False
    with open(conf.path("users.txt"), mode="a", encoding="utf-8") as f:
        f.write(f"{username}:{hash_password(password)}\n")
        return True
