from fastapi import (
    FastAPI,
    BackgroundTasks,
    status,
    Depends,
    HTTPException,
)
from pydantic import BaseModel
from rcr_adapter import command_log_to_rcr_adapter
from db import RCRDB, RCRStatus, get_db
from model import BuildRCRMapRequest, BuildRCRMapResult

app = FastAPI()


class AddCommnadsInput(BaseModel):
    commands: list[str]


@app.post("/commands", status_code=status.HTTP_201_CREATED)
async def add_commands(
    commands: AddCommnadsInput,
    background_tasks: BackgroundTasks,
    db: RCRDB = Depends(get_db),
):
    background_tasks.add_task(compute_rcr, commands.commands, db)
    return {"message": "Command log recorded"}


def compute_rcr(commands: list[str], db: RCRDB):
    build_map_request = BuildRCRMapRequest(commands=commands)
    db.status = RCRStatus.IN_PROGRESS

    result: BuildRCRMapResult = command_log_to_rcr_adapter(build_map_request)

    db.rcr = result.rcr_map
    db.status = RCRStatus.READY


@app.get("/rcrs/{command}")
async def get_rcr(command: str, db: RCRDB = Depends(get_db)):
    if db.status == RCRStatus.NO_DATA:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No commands log provided yet"
        )

    if db.status == RCRStatus.IN_PROGRESS:
        await db.wait_for_ready()

    if db.status == RCRStatus.READY:
        rcr = db.rcr.get(command)
        if rcr is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unknown command")

        return {"rcr": rcr}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
