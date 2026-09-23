"""Garden Services — the home page band plus the standalone services page.

The band's copy and photo live in a single settings document so the admin can
restyle it without touching the service list, while each service is its own
document rendered as a card on /garden-services.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import BaseModel

from app.db.mongodb import get_db
from app.deps import require_admin
from app.models.common import serialize, to_object_id

router = APIRouter(prefix="/garden-services", tags=["garden-services"])

SECTION_ID = "section"


class SectionConfig(BaseModel):
    """Copy shared by the home band and the hero of the services page."""
    title: str = "Garden services by MyGarden"
    body: str = ""
    image: str = ""
    cta_label: str = "View all Garden Service"
    page_title: str = "Garden Services"
    page_subtitle: str = ""
    page_image: str = ""
    contact_note: str = ""
    whatsapp: str = ""
    active: bool = True


class ServiceIn(BaseModel):
    title: str
    summary: str = ""
    description: str = ""
    image: str = ""
    price_from: str = ""
    duration: str = ""
    features: list[str] = []
    order: int = 0
    active: bool = True


class ServiceUpdate(BaseModel):
    title: str | None = None
    summary: str | None = None
    description: str | None = None
    image: str | None = None
    price_from: str | None = None
    duration: str | None = None
    features: list[str] | None = None
    order: int | None = None
    active: bool | None = None


async def _section(db) -> dict:
    doc = await db.garden_service_section.find_one({"_id": SECTION_ID})
    if not doc:
        return SectionConfig().model_dump()
    doc.pop("_id", None)
    return {**SectionConfig().model_dump(), **serialize(doc)}


@router.get("")
async def public_garden_services():
    """The band's copy plus every live service, in admin order."""
    db = get_db()
    docs = await db.garden_services.find({"active": True}).sort("order", 1).to_list(length=200)
    return {"section": await _section(db), "items": [serialize(d) for d in docs]}


@router.get("/admin", dependencies=[Depends(require_admin)])
async def admin_garden_services():
    """Everything, including services switched off."""
    db = get_db()
    docs = await db.garden_services.find({}).sort("order", 1).to_list(length=200)
    return {"section": await _section(db), "items": [serialize(d) for d in docs]}


@router.put("/section", dependencies=[Depends(require_admin)])
async def save_section(body: SectionConfig):
    db = get_db()
    patch = body.model_dump()
    patch["updated_at"] = datetime.now(timezone.utc)
    await db.garden_service_section.update_one({"_id": SECTION_ID}, {"$set": patch}, upsert=True)
    return await _section(db)


@router.post("", dependencies=[Depends(require_admin)])
async def create_service(body: ServiceIn):
    db = get_db()
    doc = body.model_dump()
    if not doc["title"].strip():
        raise HTTPException(status_code=400, detail="Title required")
    if not doc.get("order"):
        last = await db.garden_services.find({}).sort("order", -1).to_list(length=1)
        doc["order"] = (last[0].get("order", 0) + 1) if last else 0
    doc["created_at"] = datetime.now(timezone.utc)
    res = await db.garden_services.insert_one(doc)
    doc["_id"] = res.inserted_id
    return serialize(doc)


@router.patch("/{service_id}", dependencies=[Depends(require_admin)])
async def update_service(service_id: str, body: ServiceUpdate):
    db = get_db()
    patch = body.model_dump(exclude_none=True)
    if not patch:
        raise HTTPException(status_code=400, detail="Nothing to update")
    res = await db.garden_services.find_one_and_update(
        {"_id": to_object_id(service_id)}, {"$set": patch}, return_document=True
    )
    if not res:
        raise HTTPException(status_code=404, detail="Service not found")
    return serialize(res)


@router.put("/order", dependencies=[Depends(require_admin)])
async def reorder_services(ids: list[str] = Body(..., embed=True)):
    """Persist a reorder: the array position becomes `order`."""
    db = get_db()
    for i, sid in enumerate(ids):
        await db.garden_services.update_one({"_id": to_object_id(sid)}, {"$set": {"order": i}})
    return {"ok": True, "count": len(ids)}


@router.delete("/{service_id}", dependencies=[Depends(require_admin)])
async def delete_service(service_id: str):
    db = get_db()
    res = await db.garden_services.delete_one({"_id": to_object_id(service_id)})
    if not res.deleted_count:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"deleted": True}
