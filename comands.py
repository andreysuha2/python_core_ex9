from dictionary.main import dictionary

def input_error(handler):
    def inner(args):
        try:
            result = handler(*args)
            return result
        except KeyError:
            return f"Contact {args[0]} doesn't exist!"
        except ValueError:
            return "You are trying to set invalid value"
        except IndexError:
            return "Something went wrong, try again"
    return inner

@input_error
def add(name, phone):
    if name in dictionary:
        return f'Contact with name {name} already exists.'
    dictionary[name] = phone
    return f'"{name}" added to conctacts with phone "{phone}".'

@input_error
def change(name, phone):
    if name in dictionary:
        dictionary[name] = phone
        return f'For contact "{name}" phone chaged to {phone}'
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def phone(name):
    if name in dictionary:
        return f"{name}: {dictionary[name]}"
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def remove(name):
    if name in dictionary:
        dictionary.pop(name)
        return f'Contact "{name}" was removed from contacts!'
    return f'Contact "{name}" doesn\'t exist.'

@input_error
def show_all():
    output = "---CONTACTS---\n"
    if len(dictionary):
        for key, value in dictionary.items():
            output += f"{key} : {value}\n"
        return output[:-1]
    else:
        output += "Contacts are empty"
        return output

CLOSE_COMANDS = ("good bye", "close", "exit")
HANDLERS = {
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all
}