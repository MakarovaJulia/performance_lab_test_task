import json


def get_value_by_id(data, name, target_id):
    for item in data[name]:
        if item['id'] == target_id:
            return item['value']
    return None


def add_value_to_tests(tests, values):
    if isinstance(tests, dict):
        data_id = None
        for key, value in tests.items():
            if key == 'id':
                data_id = value
            if key == "value" and value == "":
                tests[key] = get_value_by_id(values, "values", data_id)
            add_value_to_tests(value, values)
    elif isinstance(tests, list):
        for item in tests:
            add_value_to_tests(item, values)
    return tests


if __name__ == '__main__':
    path1 = str(input())
    path2 = str(input())
    with open(path1, "r") as tests_file:
        tests = json.load(tests_file)
    with open(path2, "r") as values_file:
        values = json.load(values_file)
    report = add_value_to_tests(tests, values)
    with open('report.json', 'w', encoding='utf-8') as file:
        json.dump(report, file, indent=1)
