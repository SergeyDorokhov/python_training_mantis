import random
import re
import string

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 20
    rand_string = (prefix + " ".join([random.choice(symbols) for x in range(random.randrange(maxlen))]))
    return re.sub(r'\s+', ' ', rand_string)


testdata = [Project(name=random_string("name", 10).rstrip(),
                    description=random_string("header", 15), ) for i in range(1)]
