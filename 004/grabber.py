FILENAME = 'data.txt'
PERSON_DELIMITER = '-'


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
