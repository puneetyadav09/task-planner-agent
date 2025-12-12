from typing import TypedDict, Optional, List

class TaskPlannerState(TypedDict):
    input: str
    tasks: Optional[List[str]]
    metadata: Optional[dict]
