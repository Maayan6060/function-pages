import streamlit as st
import sympy as s
from sympy import symbols, S, oo, limit
from sympy.calculus.util import continuous_domain
import numpy as np
class integral:
    def __init__(self):
        self.x = s.symbols('x')

    def integrate(self, x, function_input, low_bound_input, high_bound_input):
        y = function_input
        yf = s.sympify(y)
        I=s.integrate(yf,x)
        I2=str(I)
        I2=I2.replace("log(", "ln(")
        I2=str(I2)+"+C"
        st.session_state['function'] = yf
        st.session_state['integral'] = I
        st.write("The general integral of the function: ")
        st.write(str(I2))
        self.input_text=""

#low integral bound

        low_integral_bound=low_bound_input
        low_integral_bound=(low_integral_bound)
        st.session_state['low_integral_bound'] = low_integral_bound 
        self.input_text=""
        
#high integral bound

        high_integral_bound=high_bound_input
        high_integral_bound=(high_integral_bound)
        st.session_state['high_integral_bound'] = high_integral_bound
        st.session_state['step'] = 'surface' 
        self.input_text=""
    
#surface

        yf= st.session_state['function']
        low_integral_bound = st.session_state['low_integral_bound']
        high_integral_bound = st.session_state['high_integral_bound']
        surface=s.integrate(yf,(x,high_bound_input,low_integral_bound))
        surface=str(surface)
        surface=surface.replace("log(","ln(")
        st.write("The surface between the function and the axes: ", str(surface))


    def run(self):
        st.title("Function Integrating App")

        # Inputs
        function_input = st.text_input("Enter the function to integrate:")
        low_bound_input = st.text_input("Enter the lower integral bound:")
        high_bound_input = st.text_input("Enter the upper integral bound:")

        # Submit Button
        if st.button("Next"):
            if function_input:
                x = s.symbols('x')
                self.integrate(x, function_input, low_bound_input, high_bound_input)
            else:
                st.error("Please enter a function to integrate.")

# Run the app
def app():
    integral_app = integral()
    integral_app.run()

app()

