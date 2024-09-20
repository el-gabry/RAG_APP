from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str  # Or the appropriate data type for your file ID
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    do_reset: Optional[int] = 0
