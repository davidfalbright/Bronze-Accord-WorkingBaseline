from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI()

class BBXPComponent(BaseModel):
    belief: Optional[str]
    intent: Optional[str]
    conviction_link: Optional[str]
    safeguard_link: Optional[str]
    exceptions: Optional[str]
    mitigations: Optional[str]

class BBXPMetadata(BaseModel):
    interpretation_hint: Optional[str]
    language: str
    confidence_rating: Optional[float]
    alignment_scope: Optional[List[str]]
    export_permission: Optional[str]
    anti_capture: Optional[bool]

class BBXPBundle(BaseModel):
    type: str
    protocol: str
    source_framework: str
    bundle_id: str
    timestamp: str
    components: BBXPComponent
    meta: BBXPMetadata

bbxp_log = []

@app.post("/submit_bbxp_bundle")
async def submit_bbxp_bundle(bundle: BBXPBundle, request: Request):
    if bundle.protocol != "bbxp_v1":
        raise HTTPException(status_code=400, detail="Unsupported BBXP protocol version.")

    client_ip = request.client.host
    is_bronze_aligned = "bronze_accord" in bundle.source_framework.lower()

    record = {
        "id": bundle.bundle_id,
        "timestamp": bundle.timestamp,
        "client_ip": client_ip,
        "source_framework": bundle.source_framework,
        "bronze_aligned": is_bronze_aligned,
        "components": bundle.components.dict(),
        "meta": bundle.meta.dict()
    }

    bbxp_log.append(record)
    return {
        "status": "accepted",
        "bronze_aligned": is_bronze_aligned,
        "record_id": record["id"],
        "client_ip": client_ip
    }
