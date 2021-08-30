from app.admin.user.models import User
from app.services.errors.exceptions import UnauthorizedError


def validate_token(basic, params):
    try:
        if not basic:
            raise UnauthorizedError("Invalid Basic Negado Header")

        if params["grant_type"] == "password":
            pass

        username = params["username"]
        password = params["password"]
    except:
        raise UnauthorizedError("Alguma coisa deu errado")

    user = User.query.filter(User.deleted_at == None, User.status == 1)

    if basic == "NDRleHByZXNzYWRtaW46NDRleHByZXNzcGFzc3dvcmQ=":
        user = user.filter(User.group_id == 5)
    elif basic == "b2ZlcnRhcGxheXVzZXI6b2ZlcnRhcGxheXBhc3N3b3Jk":
        user = user.filter(User.group_id != 5)
    else:
        raise UnauthorizedError("Invalid Basic Negado")

    if "@" in username:
        user = user.filter(User.email == username)
    else:
        user = user.filter(User.cpf == username)

    user = user.first()

    return user, password
