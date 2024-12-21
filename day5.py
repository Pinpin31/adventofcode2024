rules = []
pages = []

def order_rules(rules):
    order_dict = {}
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if before not in order_dict:
            order_dict[before] = set()
        order_dict[before].add(after)
    return order_dict

def is_ordered(pages, order_dict):
    pages_index = {page: idx for idx, page in enumerate(pages)}
    for before, afters in order_dict.items():
        if before in pages:
            for after in afters:
                if after in pages_index and pages_index[before] > pages_index[after]:
                    return False
    return True


with open('day5.input1', 'r') as f:
    rules = [line.strip() for line in f.readlines()]

with open('day5.input2', 'r') as f:
    pages_list = [line.strip() for line in f.readlines()]

order_dict = order_rules(rules)
pages_sum = 0

for pages in pages_list:
    array_pages = list(map(int,pages.split(',')))
    if is_ordered(array_pages, order_dict):
        count = len(array_pages)
        middle = count // 2
        print(array_pages)
        pages_sum += int(array_pages[middle])

print(pages_sum)
