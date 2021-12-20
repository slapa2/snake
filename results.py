import json
from datetime import datetime
from printer import Printer


def get_results(n=None):
    with open('var/results.json', 'r') as f:
        results = json.load(f)
    if n is None:
        return results
    ret = results if len(results) < n else results[:n]
    return list(ret)


def print_results(n):
    printer = Printer()
    print(printer.best_scores)
    print('\t POS.\t SCORE\t DATE')
    for i, result in enumerate(get_results(n), start=1):
        print(f'\t {i}.\t {result["score"]}\t {result["date"]}')
    print('\n')


def save_result(points):
    results = get_results()
    result = {
        'score': points,
        'date': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M'),
    }
    results.append(result)

    results.sort(key=lambda item: item.get('score'), reverse=True)

    with open('var/results.json', 'w') as f:
        json.dump(results, f)
