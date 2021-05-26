import tinydb

from easel import component
from easel import course

ASSIGN_GROUPS_PATH=course.COURSE_PATH+"/assignment_groups"
ASSIGN_GROUP_PATH=ASSIGN_GROUPS_PATH+"/{}"

class AssignmentGroup(component.Component):

    def __init__(self, name="", position=-1, group_weight=-1):
        super().__init__(ASSIGN_GROUPS_PATH, ASSIGN_GROUP_PATH)
        self.canvas_ids = {}
        self.name = name
        self.position = position
        self.group_weight = group_weight

    def __repr__(self):
        return (f"AssignmentGroup(name={self.name}, position={self.position},"
                f" weight={self.group_weight})")

    def gen_query(self):
        return tinydb.Query().name == self.name

# Needed for custom yaml tag
def constructor(loader, node):
    return AssignmentGroup(**loader.construct_mapping(node))
