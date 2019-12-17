def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    for line in lines:
        if line == 'Allen':
            person = line
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line)
    print(new)


def main():
    lines = read_file('input.txt')
    new = convert(lines)


main()
