"""
Contains class that represents an expense.
"""

import uuid


class Expense:
    """
    Expense contains information about spenddings on an item: food, drinks, transportation, etc.
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
        # pylint: disable=too-many-arguments

        self._payer = payer
        self._amount = amount
        self._participants = participants
        self._category = category
        self._description = description
        self._weights = weights
        self._uuid = uuid.uuid4()

    @property
    def payer(self):
        """
        Participant that paid for this expense.
        """
        return self._payer

    # TODO: other properties

    def __hash__(self):
        return hash(self._uuid)
