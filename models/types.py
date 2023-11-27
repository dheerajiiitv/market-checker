from pydantic import BaseModel
from typing import Optional, List


class URLInput(BaseModel):
    policy_url: str
    target_url: str


class ComplianceFinding(BaseModel):
    compliant: bool
    reason: Optional[str] = None
    recommended_changes: Optional[str] = None


class ComplianceResult(BaseModel):
    findings: List[ComplianceFinding]
