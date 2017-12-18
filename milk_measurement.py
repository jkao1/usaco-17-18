def count_adjustments(s):
    s = s.split('\n')
    days = int(s[0])
    logs = {}
    cows = {}
    ans = 0
    for line in s[1:1 + days]:
        logs[int(line.split(' ')[0])] = line
    best_cows = []
    for day in sorted(logs.iterkeys()):
        print(cows)
        _, cow, delta = logs[day].split(' ')
        try:
            _ = cows[cow]
        except KeyError:
            cows[cow] = 7

        if delta[0] == '+':
            cows[cow] += int(delta[1:])
        elif delta[0] == '-':
            cows[cow] -= int(delta[1:])
        else:
            cows[cow] += int(delta)
        new_best_cows = calculate_best_cows(cows)
        if set(best_cows) == set(new_best_cows):
            continue
        else:
            ans += 1
            best_cows = new_best_cows[:]
    print(cows)
    return str(ans)

def calculate_best_cows(cows):
    best_cows = []
    max_milks = cows.items()[0][1]
    for cow, milks in cows.items():
        if milks > max_milks:
            best_cows = [cow]
            max_milks = milks
        elif milks == max_milks:
            best_cows.append(cow)
    return best_cows

if __name__ == '__main__':
    fin = open('measurement.in', 'r')
    fout = open('measurement.out', 'w')
    fout.write(count_adjustments(fin.read()))
    fin.close()
    fout.close()