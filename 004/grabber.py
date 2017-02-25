import json


FILENAME = 'data.txt'
PERSON_DELIMITER = '-'


def to_json(func):
    def wrapper():
        func_output = func()
        encoded = []
        person_info = {}

        for person in func_output:
            for info in person:
                person_info.update({info[1]: info[0]})

            encoded.append(person_info)
            person_info = {}

        return json.dumps(encoded, sort_keys=True, indent=4)

    return wrapper


@to_json
def retrieve_data():

    persons = []
    tmp = ()

    with open(FILENAME) as opened:
        for line in opened:
            line = line.strip()

            if line == PERSON_DELIMITER:
                persons.append(tmp)
                tmp = ()
            else:
                key, value = line.split(':')
                tmp = tmp + ((value, key),)

        if tmp:
            persons.append(tmp)

    return persons


if __name__ == '__main__':
    print(retrieve_data())
