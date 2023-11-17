def start(rule_list, changed_string):
    result = ""
    _out = [changed_string]
    rules = rule_list.split(";")
    for n in range(0, len(rules)):
        rules[n] = rules[n].split("-")
    while True:
        stop_mark=False
        change_mark = False
        for i in range(0, len(rules)):
            if rules[i][1].find('*')>-1:
                rules[i][1]=rules[i][1].replace('*','')
                stop_mark=True
            if changed_string.find(rules[i][0]) > -1:
                result = changed_string.replace(rules[i][0], rules[i][1], 1)
                change_mark = True
                break
            else:
                continue
        changed_string = result
        if change_mark is True:
            _out.append(changed_string)
            if stop_mark==True:
                break
        else:
            break
    return _out



def check_rules(rule_list,word):
    rules = rule_list.split(";")
    for r in rules:
        if len(r.split("-")) != 2:
            return False      
    if word.find('*')>-1 and word.find('-')>-1 and word.find(';')>-1:
        return False
    return True


