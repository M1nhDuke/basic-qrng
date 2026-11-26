"""Run: python test_qrng.py"""

import qrng

for backend in qrng.BACKENDS:
    for n in (1, 8, "16"):  # "16": web forms send strings
        bits = qrng.generate(backend, n)
        assert len(bits) == int(n) and set(bits) <= {"0", "1"}, (backend, n, bits)
    bits = qrng.generate(backend, qrng.MAX_BITS)
    # All-equal 1024 bits has probability 2**-1023: failing here means the circuit is broken.
    assert len(bits) == qrng.MAX_BITS and set(bits) == {"0", "1"}, (backend, bits)

for bad in [("qiskit", 0), ("qiskit", 1025), ("qiskit", "abc"), ("qiskit", "2.5"), ("qiskit", None), ("nope", 8)]:
    try:
        qrng.generate(*bad)
    except ValueError:
        continue
    raise AssertionError(f"accepted bad input {bad}")

print("all ok")
