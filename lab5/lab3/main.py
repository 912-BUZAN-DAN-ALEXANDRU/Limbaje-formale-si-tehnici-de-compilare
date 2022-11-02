from symbol_table import SymbolTable

st = SymbolTable()

st.add_element("a", 1)
st.add_element("length", 5)
st.add_element("cuvant", "mere")
st.add_element("cuvant2", "pere")
st.add_element("z", 3.6)

assert (st.get_element("cuvant") == "mere")
assert (st.get_element("z") == 3.6)


