import enum

class BlockStatus(enum.Enum):
    VALID = 0,
    INVALID = 1,
    CONFLICT = 2