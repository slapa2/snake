import json


def get_results(n=None):
    with open('var/results.json', 'r') as f:
        results = json.load(f)
    if n is None:
        return results
    return results if len(results) < n else results [:n]


def print_results(n):
    print('-------- BEST SCORES ---------')
    for result in get_results(n):
        print(result)
    print('------------------------------')
    print()


def save_result(result):
    results = get_results()
    results.append(result)
    with open('var/results.json', 'w') as f:
        json.dump(sorted(results, reverse=True), f)
