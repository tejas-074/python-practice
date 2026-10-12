def get_age(user, key):
    try:
        age = int(user[key])
        print(f"Age is {age}")
    except KeyError:
        print(f"Key '{key}' is missing")
    except ValueError:
        print(f"Value for '{key}' is not a number")
    except Exception as error:
        print(f"Something else went wrong: {error}")

user = {"name": "Tejas", "age": "22", "city": "Surat"}

get_age(user, "age")
get_age(user, "email")
get_age(user, "city")
get_age(None, "age")