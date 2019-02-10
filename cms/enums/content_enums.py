import enum

__author__ = 'Ashraful'


class ContentTypeEnum(enum.Enum):
    Plain = 0
    Table = 1
    Card = 2
    Graph = 3
    Chart = 4
    Custom = 5
    Tab = 6


class ContentStatusEnum(enum.Enum):
    Draft = 0
    Publish = 1
    Archive = 2
