import random

# Models
from core.models import GenCode


# We have to take some logs, on whos generating a sqlcode
def randnum():
    return random.randint(1000, 9999)


def generatesqlcode(token, name):
    number = randnum()

    try:
        GenCode.objects.create(
            code=number,
            generatedby=name,
        )

        return number
    except Exception as e:
        print("Error " + str(e))
