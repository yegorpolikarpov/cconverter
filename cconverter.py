import json
import requests

CODE1 = input().upper()


def get_rate(code):
    if CODE1 == code:
        return 1
    url = f"http://www.floatrates.com/daily/{CODE1.lower()}.json"
    r = requests.get(url)
    temp = json.loads(r.text)
    return temp[code.lower()]['rate']


with open("cache.json", "w") as cache:
    json.dump({'USD': get_rate('USD'), 'EUR': get_rate('EUR')}, cache, indent=1)
while True:
    code2 = input().upper()
    if not code2:
        exit()
    money1 = float(input())
    print("Checking the cache...")
    with open("cache.json", "r") as cache:
        cached_rates = json.load(cache)
    if code2 in cached_rates:
        print("Oh! It is in the cache!")
        print(f"You received {money1 * cached_rates[code2]:.2f} {code2}.")
    else:
        cached_rates[code2] = get_rate(code2)
        with open("cache.json", "w") as cache:
            json.dump(cached_rates, cache, indent=1)
        print("Sorry, but it is not in the cache!")
        print(f"You received {money1 * cached_rates[code2]:.2f} {code2}.")
