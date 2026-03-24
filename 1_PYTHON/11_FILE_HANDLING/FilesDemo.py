def create_file(file_name):
    with open(file_name, "w") as file_Handle:
        file_Handle.close()


def append_contents(file_name, content):
    with open(file_name, "a") as file_Handle:
        file_Handle.write(content)
        file_Handle.close()


file_name = "mynotes.txt"
content = "namaskara karnataka"

create_file(file_name)
append_contents(file_name, content)