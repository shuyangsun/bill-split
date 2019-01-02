"""
Tool to help split bill.

Input format:
Expenses are separated into lines, represented in the following format:
participants: a, b, c, ...
payer, amount, description: participants (separated by comma)

Note: use "all, -a, -b" to represent everyone but a and b in an expense.

Sample input:
participants: a, b, c, d
a, 100: a, b, c, d
d, 200, food: a, b
"""

import uuid
import sys
import math

from collections import defaultdict
from collections import namedtuple


class Expense:
    def __init__(self, payer, amount, participants, description=None):
        self.payer = payer
        self.amount = amount
        self.description = description
        self.participants = participants
        self._uuid = uuid.uuid4()

    def __hash__(self):
        return hash(self._uuid)


def parse_participants(content, all_participants):
    participants = set([ele.strip() for ele in content.split(',')])
    has_all = 'all' in participants
    res = set(all_participants) if has_all else participants
    if has_all:
        for ele in participants:
            if ele.startswith('-'):
                res.remove(ele[1:])
    return res


def parsed_input(content):
    content = content.strip()
    lines = content.split('\n')
    lines = [ele.split(':') for ele in lines]

    all_participants = {}
    idx_to_remove = None
    for idx, line in enumerate(lines):
        if line[0].strip().startswith('participants'):
            all_participants = set([ele.strip() for ele in line[1].split(',')])
            idx_to_remove = idx
            break
    del lines[idx_to_remove]

    res = set()

    for line in lines:
        expense_content, participants_content = line[0], line[1]
        expense_content = [ele.strip() for ele in expense_content.split(',')]
        participants = parse_participants(participants_content, all_participants)
        expense = Expense(
            expense_content[0],
            float(expense_content[1]),
            participants,
            expense_content[2] if len(expense_content) >= 3 else None
        )
        res.add(expense)

    return res


def calculate_net_transactions(expense_dict):
    res = defaultdict(float)
    for expense in expense_dict:
        amount = expense.amount
        res[expense.payer] += amount
        amount_each = amount / len(expense.participants)
        for participant in expense.participants:
            res[participant] -= amount_each
    return res


def calculate_peer_transactions(net_transactions):
    recipients = dict()
    senders = dict()
    
    for participant, amount in net_transactions.items():
        if amount > 0:
            recipients[participant] = abs(amount)
        else:
            senders[participant] = abs(amount)

    res = set()
    while recipients and senders:
        cur_res = namedtuple('transaction', ('sender', 'recipient', 'amount'))
        rname, sname= next(iter(recipients.keys())), next(iter(senders.keys()))
        ramount, samount = recipients[rname], senders[sname]
        cur_res.sender, cur_res.recipient = sname, rname
        if ramount > samount:
            cur_res.amount = samount
            recipients[rname] -= samount
            senders.pop(sname)
        elif ramount < samount:
            cur_res.amount = ramount
            recipients.pop(rname)
            senders[sname] -= ramount
        else:
            cur_res.amount = ramount
            senders.pop(sname)
            recipients.pop(rname)
        res.add(cur_res)

    return res


if __name__=='__main__':
    content = ''
    for line in sys.stdin:
        content += line
    expense_dict = parsed_input(content)
    net_transactions = calculate_net_transactions(expense_dict)
    result = list(calculate_peer_transactions(net_transactions))
    result_sorted = sorted(result, key=lambda x: x.sender)
    for ele in result_sorted:
        print('{0} --> {1}: {2:.2f}'.format(ele.sender, ele.recipient, ele.amount))
