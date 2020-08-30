from abc import ABC
from typing import List
from collections import Counter


class VotingStrategy(ABC):
    def vote(self, labels: List[str]) -> (str, int):
        pass


class FirstOccurrenceMajorityVoting(VotingStrategy):
    """
    This voting strategy uses a counter to identify who has the most votes and it breaks a tie by picking the winner
    that showed up first in the list.
    """

    def vote(self, labels: List[str]) -> (str, int):
        votes: Counter = Counter(labels)
        winner, vote_count = votes.most_common(1)[0]

        return winner, vote_count


class KReductionBasedMajorityVoting(VotingStrategy):
    """
    This voting strategy uses a counter to identify who has the most votes and it breaks a tie by reducing K until
    a unique winner is found.
    """

    def vote(self, labels: List[str]) -> (str, int):
        vote_counts: Counter = Counter(labels)
        winner, vote_count = vote_counts.most_common(1)[0]
        num_winners = len([count
                           for count in vote_counts.values()
                           if count == vote_count])

        if num_winners == 1:
            return winner, vote_count  # unique winner, so return it
        else:
            return self.vote(labels[:-1])  # try again without the farthest
