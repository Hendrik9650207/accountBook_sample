class Receipt:
    def __init__(self, tag, cost):
        self.tag = tag
        self.cost = cost


receipt_list = []
chosen_receipt_list = []


def action_add_receipt():
    tag = input('請輸入 tag: ')
    cost = input('請輸入花費:')
    receipt_list.append(Receipt(tag, cost))


def action_print_receipt_list():
    for i, r in enumerate(receipt_list):
        print(f'{i} {r.tag} {r.cost}')


def action_print_chosen_receipt_list():
    for i, r in enumerate(chosen_receipt_list):
        print(f'{i} {r.tag} {r.cost}')


def action_search_ID():
    id = input('請輸入ID:')
    if int(id) < len(receipt_list):
        chosen_receipt_list.clear()
        chosen_receipt_list.append(receipt_list[int(id)])


def action_search_cost():
    cost_min = int(input('請輸入最小值:'))
    cost_max = int(input('請輸入最大值:'))
    chosen_receipt_list.clear()
    for r in receipt_list:
        if cost_max >= r.cost >= cost_min:
            chosen_receipt_list.append(r)


def action_search_tag():
    tag = str(input('請輸入tag:'))
    chosen_receipt_list.clear()
    for r in receipt_list:
        if r.tag == tag:
            chosen_receipt_list.append(r)


def clear_chosen_receipt_list():
    chosen_receipt_list.clear()


def action_remove_chosen_receipt():
    for r in chosen_receipt_list:
        receipt_list.remove(r)
    chosen_receipt_list.clear()
    save_data()


def save_data():
    file = open('data.txt', 'w', encoding='utf-8')
    for r in receipt_list:
        file.write(r.tag + ',' + r.cost)
    file.close()


try:
    file = open('data.txt', 'r', encoding='utf-8')
    r_list = file.readlines()
    for rd in r_list:
        words = rd.split(',')
        receipt_list.append(Receipt(words[0], int(words[1])))
except FileNotFoundError:
    print('No Record!')


while True:
    user_input = input('請輸入動作:\n'
                       '1: 新增帳目\n'
                       '2: 查詢帳目(ID)\n'
                       '3: 查詢帳目(cost)\n'
                       '4: 查詢帳目(Tag)\n'
                       '5: 刪除帳目(選擇)\n'
                       '6: 清空選擇\n'
                       '7: 印出目前選擇帳目\n'
                       '8: 印出所有帳目\n')
    if user_input == '1':
        action_add_receipt()
    elif user_input == '2':
        action_search_ID()
    elif user_input == '3':
        action_search_cost()
    elif user_input == '4':
        action_search_tag()
    elif user_input == '5':
        action_remove_chosen_receipt()
    elif user_input == '6':
        clear_chosen_receipt_list()
    elif user_input == '7':
        action_print_chosen_receipt_list()
    elif user_input == '8':
        action_print_receipt_list()
    else:
        print('Not found')



