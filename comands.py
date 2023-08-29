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
            return "You are sending invalid count of parameters. Please use help comand for hint"
    return inner

@input_error
def add(*args):
    name, phone = args[0], args[1]
    if name in dictionary:
        return f'Contact with name {name} already exists.'
    dictionary[name] = phone
    return f'"{name}" added to conctacts with phone "{phone}".'

@input_error
def change(*args):
    name, phone = args[0], args[1]
    if name in dictionary:
        dictionary[name] = phone
        return f'For contact "{name}" phone chaged to {phone}'
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def phone(*args):
    name = args[0]
    if name in dictionary:
        return f"{name}: {dictionary[name]}"
    return f'Contact with name "{name}" doesn\'t exist.'

@input_error
def remove(*args):
    name = args[0]
    if name in dictionary:
        dictionary.pop(name)
        return f'Contact "{name}" was removed from contacts!'
    return f'Contact "{name}" doesn\'t exist.'

@input_error
def show_all(*args):
    if len(args):
        raise IndexError
    output = "---CONTACTS---\n"
    if len(dictionary):
        for key, value in dictionary.items():
            output += f"{key} : {value}\n"
        return output[:-1]
    else:
        output += "Contacts are empty"
        return output
    
@input_error    
def help(*args):
    return """
        --- CONTACTS HELP ---
        syntax: add {name} {phone}
        description: adding number to contacts list 
        example: add ivan +380999999999

        syntax: change {name} {phone}
        description: changing phone number for contact
        example: change ivan +380999999999

        syntax: phone {name}
        description: finding phone number by contact name
        example: phone ivan

        syntax: remove {name}
        description: removing contact from contacts list
        example: remove ivan

        syntax: show all
        description: showing list of contacts
        example: show all
    """

CLOSE_COMANDS = ("good bye", "close", "exit")
HANDLERS = {
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "help": help
}