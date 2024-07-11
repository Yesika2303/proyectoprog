import streamlit as st
st.html("<center> <h1> ¡Bienvenido!  </h1> </center>")
st.write("En este aplicativo podrá hallar la medida del tercer lado de un triángulo rectángulo a partir de las medidas de dos lados conocidos, aplicando el teorema de Pitágoras.")
st.divider()
st.title("Teorema de Pitágoras")
with st.container(border=True):
    st.markdown("La suma de los cuadrados de los catetos es igual al cuadrado de la hipotenusa.")
st.image("https://www.smartick.es/blog/wp-content/uploads/2024/02/teorema-de-Pitagoras-2-768x619.png")
with st.container(border=True):
    st.markdown("En un triángulo rectángulo, los lados menores son los que forman el ángulo recto y se llaman **catetos** y el lado mayor se llama **hipotenusa**. En el triángulo rectángulo de la imagen a y b son los catetos y c es la hipotenusa.")
st.subheader("Demostración gráfica del teorema de Pitágoras (por Perigal)")
st.video("https://www.smartick.es/blog/wp-content/uploads/2024/02/Video-demostracion-Perigal.mp4?_=2")
st.write("Seleccione los lados cuyas medidas conoce:")
opc = st.selectbox("", ["El cateto a y la hipotenusa (c)","El cateto b y la hipotenusa (c)", "Ambos catetos (a y b)"])
st.write("Digite las medidas en las casillas correspondientes:")
if opc == "El cateto a y la hipotenusa (c)":
    a= float(st.number_input("a"))
    c= float(st.number_input("c"))
    if a<=0 or c<=0 or a>=c:
        st.write("No es un triángulo rectángulo.")
    else:
        b= (c**2 - a**2)**0.5
        st.latex(f"b=\\sqrt{{c^2-a^2}}=\\sqrt{{{c}^2-{a}^2}}={b}")
elif opc == "El cateto b y la hipotenusa (c)":
    b= float(st.number_input("b"))
    c= float(st.number_input("c"))
    if b<=0 or c<=0 or b >= c:
        st.write("No es un triángulo rectángulo.")
    else:
        a= (c**2 - b**2)**0.5
        st.latex(f"a=\\sqrt{{c^2-b^2}}=\\sqrt{{{c}^2-{b}^2}}={a}")
elif opc == "Ambos catetos (a y b)":
    a= float(st.number_input("a"))
    b= float(st.number_input("b"))
    if a<=0 or b<=0:
        st.write("No es un triángulo rectángulo.")
    else:
        c= (a**2 + b**2)**0.5
        st.latex(f"c=\\sqrt{{a^2+b^2}}=\\sqrt{{{a}^2+{b}^2}}={c}")
        







