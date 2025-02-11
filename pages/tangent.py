import streamlit as st
import sympy as s
from sympy import symbols, S, oo, limit
from sympy.calculus.util import continuous_domain
import numpy as np
from sympy import E 
class tangent:
    def __init__(self):
        self.x = s.symbols('x')
    def tangent(self,x,function_input_t,x_value_input,y_value_input): #ניגזרת
        e=E
        y=function_input_t
        yf=s.sympify(y)
        f=s.diff(yf,x)
        f=s.simplify(f)
        st.write("f'(x) = ", str(f))
        xv = (x_value_input)
        yv = (y_value_input)
        # xv = sympify(xv)
        # yf = sympify(yv)
        # if xv.lstrip('-').isdigit():
        #     xv=int(xv)
        # if yv.lstrip('-').isdigit():
        #     yf=int(yv)
        # if not(xv.has(E,log)):
        #     xv=float(xv)
        # if not(yf.has(E,log)):
        #     yf=float(xv)
        m = f.subs(x, xv)
        st.write("m = ",float(m))
        st.write("y-y₁=m(x-x₁)")
        st.write("y-",yv,"=",float(m),"(x-",xv,")")
        t="y-",yv,"=",float(m),"x"+"+("+str(float(m)*float(xv)*-1)+")"
        st.write(t)
        t="y="+str(m)+"x"+"+("+str((float(m)*float(xv)*-1)+float(yv))+")"
        st.write(t)






    def run(self):
        st.title("Tangent equation finding App")

        # Inputs
        function_input_t = st.text_input("Enter the function:", key="tangent_function_input")
        x_value_input = st.text_input("Enter the x value of the point:", key="x_value")
        y_value_input = st.text_input("Enter the y value of the point:", key="y_value")

        # Submit Button
        if st.button("Next"):
            if function_input_t:
                x = s.symbols('x')
                self.tangent(x, function_input_t, x_value_input, y_value_input)
            else:
                st.error("Please enter a function.")

# Run the app
def app():
    tangent_app = tangent()
    tangent_app.run()

app()
