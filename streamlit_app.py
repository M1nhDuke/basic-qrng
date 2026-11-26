import streamlit as st

import qrng

st.title("Quantum Random Number Generator")
st.caption(
    "Each bit is one measurement of a qubit after a Hadamard gate. Runs on a local simulator, "
    "which draws outcomes from a classical pseudo-random generator: a demo, not true quantum randomness."
)

backend = st.selectbox("Backend", list(qrng.BACKENDS))
bits = st.number_input("Bits", min_value=qrng.MIN_BITS, max_value=qrng.MAX_BITS, value=8, step=1)

if st.button("Generate"):
    try:
        result = qrng.generate(backend, bits)
    except ValueError as e:
        st.error(str(e))
    else:
        st.subheader(f"Result ({backend}, {len(result)} bits)")
        st.write("Bits:")
        st.code(result, language=None, wrap_lines=True)
        st.write("Integer:")
        st.code(str(int(result, 2)), language=None, wrap_lines=True)
