import json
import os
import re

from django.contrib.auth import authenticate, login
from territory_project.models import *

def handle_auth(request, name, password):
    assert isinstance(name, str)
    assert isinstance(password, str)
    user = authenticate(username=name, password=password)
    if user is None:
        raise Exception('Email o contraseña incorrectos.')
    else:
        login(request, user)
    return user
