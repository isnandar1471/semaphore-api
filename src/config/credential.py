import typing


import uuid
import pydantic


class PayloadStructure(pydantic.BaseModel):
    """
    # References:
    [registered-claim-names](https://pyjwt.readthedocs.io/en/stable/usage.html#registered-claim-names)
    """

    username: str

    type: typing.Literal[1, 2]
    """

    `1` : token biasa

    `2` : refresh token
    """

    exp: int
    """
    exp (Expiration Time) Claim
    """

    iat: int
    """
    iat (Issued At) Claim
    """

    nbf: typing.Union[int, None] = None
    """
    nbf (Not Before Time) Claim
    """

    iss: typing.Union[int, None] = None
    """
    iss (Issuer) Claim
    """

    aud: typing.Union[int, None] = None
    """
    aud (Audience) Claim
    """

    # def __init__(
    #     self,
    #     username: str,
    #     type: typing.Literal[1, 2],
    #     exp: int,
    #     iat: typing.Union[int, None] = None,
    #     nbf: typing.Union[int, None] = None,
    #     iss: typing.Union[int, None] = None,
    #     aud: typing.Union[int, None] = None,
    # ) -> None:
    #     """
    #     # Parameters
    #     iat:
    #       `None` for current unix
    #     """

    #     self.username = username
    #     self.type = type
    #     self.exp = exp
    #     self.iat = iat
    #     self.iat = iat if iat is not None else int(time.time())
    #     self.nbf = nbf
    #     self.iss = iss
    #     self.aud = aud


class EmailVerificationKey(pydantic.BaseModel):
    """
    References:
    """

    uuid4: typing.Union[uuid.UUID, str]

    version: int

    generated_at: float

    # def __init__(
    #     self,
    #     uuid4: typing.Optional[uuid.UUID] = None,
    #     version: typing.Optional[int] = None,
    #     generated_at: typing.Optional[float] = None,
    # ) -> None:
    #     self.uuid4 = str(uuid4 if uuid4 is not None else uuid.uuid4())
    #     self.version = version if version is not None else 1
    #     self.generated_at = generated_at if generated_at is not None else time.time()
