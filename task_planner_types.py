from typing import TypedDict, List, Optional

class TaskPlannerState(TypedDict):
    user_input: str
    tasks: Optional[List[str]]
    plan: Optional[str]
