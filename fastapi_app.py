from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

import qrng

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


# Plain def: FastAPI runs it in a threadpool, so a slow simulation doesn't block the event loop.
@app.get("/")
def index(request: Request):
    # Raw query strings, not typed params, so bad input shows on the page instead of a 422.
    args = request.query_params
    ctx = {
        "backends": qrng.BACKENDS,
        "backend": args.get("backend", "qiskit"),
        "bits": args.get("bits", "8"),
        "min_bits": qrng.MIN_BITS,
        "max_bits": qrng.MAX_BITS,
    }
    if "backend" in args:
        try:
            ctx["result"] = qrng.generate(ctx["backend"], ctx["bits"])
            ctx["number"] = int(ctx["result"], 2)
        except ValueError as e:
            ctx["error"] = str(e)
    return templates.TemplateResponse(request, "index.html", ctx)
