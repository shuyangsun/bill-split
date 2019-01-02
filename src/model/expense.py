"""
Contains class that represents an expense.
"""


import uuid


class Expense:
    """
    Expense contains information about spendings on an item: food, drinks, transportation, etc.
    """

    def __init__(
            self,
            payer,
            amount,
            participants,
            category=None,
            description=None,
            weights=None
        ):
        self._payer = payer
        self._amount = amount
        self._participants = participants
        self._category = category
        self._description = description
        self._weights = weights
        self._uuid = uuid.uuid4()

    @property
    def payer(self):
        return self._payer

    # TODO: other properties

    def __hash__(self):
        return hash(self._uuid)

