from flask import Flask, render_template, request

import qrng

app = Flask(__name__)


@app.get("/")
def index():
    args = request.args
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
    return render_template("index.html", **ctx)
