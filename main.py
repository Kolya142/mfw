def pars(tr, data):
    out = ""
    for i in data:
        if not i in tr:
            out += i
            continue
        out += tr[i]
    return out
if __name__ == '__main__':
    import math
    form = input("formula:")
    translate = {"^": "pow", "{": "(", "}": ")", "=": "==", "#": "sqrt", "e": f'{math.e}', "p": f'{math.pi}'}
    data = pars(translate, form)
    print(data)
