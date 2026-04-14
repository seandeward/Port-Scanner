
def group_tasks_by_owner(tasks):
  result_dict = {}
  for task in tasks:
    owner = task['owner']
    title = task['title']
    if owner not in result_dict:
      result_dict[owner] = []
    result_dict[owner].append(title)
  return result_dict

if __name__ == "__main__":
  dict1 = {'owner': 'loki', 'title': '24'}
  dict2 = {'owner': 'loki', 'title': '94'}
  dict3 = {'owner': 'loki', 'title': '94'}

  dict4 = {'owner': 'ronan', 'title': '14'}
  dict5 = {'owner': 'ronan', 'title': '174'}

  dict6 = {'owner': 'groot', 'title': '1446'}

  all_dicts = [dict1, dict2, dict3, dict4, dict5, dict6]

  print(all_dicts)

  results = dict[str, str](group_tasks_by_owner(all_dicts))

  print(f"[+] RESULTS = {results}")

  print("") # for terminal space

  for name, value_list in results.items():
    print(f"[-] OPEN PORTS ON {name}")
    print(f"   -> {value_list}")
    print("") # for terminal space
