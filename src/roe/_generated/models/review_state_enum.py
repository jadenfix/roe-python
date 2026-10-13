from enum import Enum

class ReviewStateEnum(str, Enum):
    AGREED = "agreed"
    DISAGREED = "disagreed"
    UNREVIEWED = "unreviewed"

    def __str__(self) -> str:
        return str(self.value)
