from re import search, S, M

def print_totals(filename, signals=(2, 3), output='output.log'):
    with open(filename, 'r') as f_in:
        file_body = f_in.read()

    with open(output, 'w') as f_out:
        for num in signals:
            total = get_totals(num=num, file=file_body)
            print(total, file=f_out)

def get_totals(num, file):
    aux = search(fr'Signal {num}.*^Totals.*?^((?:\+|-)?\d*\.?\d+(?:e|E)?(?:\+|-)?\d+)$.*$.*Signal', file, flags=M | S)

    if aux:
        return aux.group(1)
    else:
        return 0.

if __name__ == '__main__':
    filenames = ('./BES-BC-113-IR01446-REMEASURED_2022-07-14_09-16-19_H06.txt',)

    for filename in filenames:
        print_totals(filename)
