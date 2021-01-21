from src import InstaGet

from os import environ
import subprocess
import sys

if __name__ == "__main__":
    
    try:
        username = str(input("username: "))
    except Exception as e:
        raise Exception(e)
    instaget = InstaGet(username=username)
    profile = instaget.get_profile()
    print(profile)
