# basic-qrng

A basic quantum random number generator website. Pick a backend (**Qiskit**, **Cirq** or **PennyLane**)
and a number of bits (1–1024); you get the random bitstring and its integer value.

Every backend runs the same circuit: one qubit, a Hadamard gate, a measurement, repeated once per bit.

> **Simulated, not truly random.** All three backends are local simulators, which draw measurement
> outcomes from a classical pseudo-random generator. This is a demo of the idea, not a source of
> true quantum randomness. That would need real quantum hardware.

The same site is built three ways, all calling `qrng.generate(backend, n_bits)`:

| App | Run | Open |
|---|---|---|
| Flask | `flask --app flask_app run` | http://127.0.0.1:5000 |
| FastAPI | `uvicorn fastapi_app:app` | http://127.0.0.1:8000 |
| Streamlit | `streamlit run streamlit_app.py` | http://localhost:8501 |

Flask and FastAPI share `templates/index.html`. You can link straight to a result, e.g. `/?backend=cirq&bits=16`.

## Setup

Python 3.13:

```sh
python -m venv .venv
.venv\Scripts\activate        # Windows; on macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Test

```sh
python test_qrng.py
```
