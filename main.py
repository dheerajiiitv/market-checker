from typing import List

from fastapi import FastAPI, HTTPException, Depends
from services.scrape import fetch_webpage_content
from services.core import CompliantChecker
from models.types import ComplianceResult, URLInput

app = FastAPI()

def get_compliance_results():
    return CompliantChecker()

@app.get("/")
async def root():
    return {"message": "Status: OK"}


@app.post("/check-compliance/", response_model=List[str])
async def check_compliance(urls: URLInput, compliance_checker=Depends(get_compliance_results)) -> List[str]:
    try:
        policy_content = fetch_webpage_content(urls.policy_url)
        target_content = fetch_webpage_content(urls.target_url)
        findings = compliance_checker.analyze_compliance(policy_content, target_content)
        return findings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

