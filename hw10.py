import os
import pickle
filename = 'data/score.bin'

def input_scores():
    s = []
    i = 1
    while (True) :
        n = int(input((f'#{i}? ')))
        if n < 0 :
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save(scores, average, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(average, file)

def load(filepath):
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
        average = pickle.load(file)

    return scores, average

if os.path.exists(filename):
    print('[파일 읽기]')
    s, a = load(filename)
    print(f'\n[점수 출력]\n개인점수: {s}\n평균: {a}')
else:
    print('[점수 입력]')
    scores = input_scores()
    print('\n[점수 출력]\n개인점수: ', end='')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg: .1f}')
    save(scores, avg, filename)