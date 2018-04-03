from blackbox.core.helpers.enums import ChoiceEnum

__author__ = 'Ashraful'


class MenuAccessTypeEnum(ChoiceEnum):
    All = 0
    View = 1
    Edit = 2
    Create = 3
    NoAccess = 4
