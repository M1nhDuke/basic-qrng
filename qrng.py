"""Random bits from a 1-qubit circuit (Hadamard, then measure), one shot per bit.

All three backends are local simulators: outcomes come from a classical PRNG.
"""

import cirq
import pennylane as qml
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

MIN_BITS, MAX_BITS = 1, 1024


def _qiskit(n):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    result = StatevectorSampler().run([qc], shots=n).result()
    return "".join(result[0].data.c.get_bitstrings())


def _cirq(n):
    q = cirq.LineQubit(0)
    circuit = cirq.Circuit(cirq.H(q), cirq.measure(q, key="m"))
    bits = cirq.Simulator().run(circuit, repetitions=n).measurements["m"].ravel()
    return "".join(str(int(b)) for b in bits)


def _pennylane(n):
    @qml.set_shots(n)
    @qml.qnode(qml.device("default.qubit", wires=1))
    def circuit():
        qml.Hadamard(0)
        return qml.sample(wires=0)

    return "".join(str(int(b)) for b in qml.math.ravel(circuit()))


BACKENDS = {"qiskit": _qiskit, "cirq": _cirq, "pennylane": _pennylane}


def generate(backend, n_bits):
    """Return a string of n_bits '0'/'1' characters. n_bits may be a str (from a web form)."""
    if backend not in BACKENDS:
        raise ValueError(f"Unknown backend {backend!r}. Choose one of: {', '.join(BACKENDS)}.")
    try:
        n = int(n_bits)
    except (TypeError, ValueError):
        raise ValueError("Number of bits must be a whole number.") from None
    if not MIN_BITS <= n <= MAX_BITS:
        raise ValueError(f"Number of bits must be between {MIN_BITS} and {MAX_BITS}.")
    return BACKENDS[backend](n)
