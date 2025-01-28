import streamlit as st
import sympy as s
from sympy import symbols, S, oo, limit
from sympy.calculus.util import continuous_domain
import numpy as np
from sympy import E
class AnalyzeApp:
    def __init__(self):
        self.e = E
        self.x = s.symbols('x')
        if "step" not in st.session_state:
            st.session_state.step = 0

    def definition(self):
        e=E
        y = self.input_text
        yf = s.sympify(y)
        D = continuous_domain(yf, self.x, S.Reals)
        st.session_state['x'] = self.x
        st.session_state['D'] = D
        st.session_state['yf'] = yf
        st.write("The field of definition:", D)
        self.vertical_asymptote(yf, D, self.x)

    def vertical_asymptote(self, yf, D, x):
        e=E
        va = []
        undefined = S.Reals - D
        for i in undefined:
            lim_left = i - (1e-15)
            lim_right = i + (1e-15)
            lim_left_val = yf.subs(x, lim_left)
            lim_right_val = yf.subs(x, lim_right)
            if abs(lim_left_val) > 1e6 or abs(lim_right_val) > 1e6:
                va.append(i)
        st.write("Vertical asymptotes: "+"x=",str(va))
        self.horizontal_asymptote(yf, D, x)

    def horizontal_asymptote(self, yf, D, x):
        e=E
        oo_limit = limit(yf, x, oo)
        st.write("Horizontal asymptotes: "+"y=",str(oo_limit))
        self.xyi(x,yf,D)
    def xyi(self,x,yf,D):
        e=E
        xi=s.Eq(yf,0)
        xix=s.solve(xi,x)
        for i in range(len(xix)):
         xix[i]="("+str(xix[i])+",0)"
        yi=yf.subs(x,0)
        if s.S.Zero in D:
         yi="(0,"+str(yi)+")"
         xix.append(str(yi))
        st.write("Intersection with the axes: ", str(xix))
    def derivative(self,yf,D,x): #ניגזרת
        e=E
        f=s.diff(yf,x)
        f=s.simplify(f)
        st.write("The derivative of the function: ", str(f))
        self.sextreme(yf,f,D,x)
    def sextreme(self,yf,f,D,x):#חשד לקיצון
        e=E
        ep0=s.Eq(f,0)
        ex=s.solve(ep0,x)
        if len(ex)>0:
         st.write("y'= 0   (solutions): ", str(ex))
        if len(ex)==0:
         st.write("There are no extreme points")
    # def table(self, instance): #טבלה  
    #               if len(ex)>0:
    #                 ea=(len(ex))
    #                 tc=2*ea+1
    #                 t=np.empty((3,tc+1),dtype=object)
    #                 t[0,0]='X'
    #                 t[1,0]='Y'
    #                 t[2,0]="Y'"
    #                 for i in range(1,len(ex)+1):
    #                   t[0,2*i]=ex[i-1]
    #                   if i<1 or i>1:
    #                     aex=ex[i-2]+ex[i-1]
    #                     aex=aex/2
    #                     t[0,2*i-1]=aex
    #                 t[0,tc]=ex[-1]+1
    #                 t[0,1]=ex[0]-1

    #                 ey=[]
    #                 for i in range(len(ex)):
    #                   ey.append(yf.subs(x,ex[i]))
    #                 for i in range(1,len(ey)+1):
    #                   t[1,2*i]=ey[i-1]
    #                 yf1=s.sympify(f)
    #                 yf1=s.simplify(yf1)
    #                 for i in range(1,tc+1):
    #                   t[2,i]=yf1.subs(x,t[0,i])
    #                   if t[2,i]>0:
    #                     t[1,i]="U"
    #                   if t[2,i]<0:
    #                     t[1,i]="D"

    #                   u=""
    #                   d=""
    #                   if t[1,1]=="U":
    #                     u+="x<"+str(t[0,2])
    #                   if t[1,1]=="D":
    #                     d="x<"+str(t[0,2])
    #                   if t[1,-1]=="U":
    #                     u+=", "+"x>"+str(t[0,-2])
    #                   if t[1,-1]=="D":
    #                     d+=", "+"x>"+str(t[0,-2])
    #                 for i in range(3,tc-1):
    #                     if t[1,i]=="U":
    #                       u+=", "+str(t[0,i-1])+"<x<"+str(t[0,i+1])
    #                     if t[1,i]=="D":
    #                       d+=", "+str(t[0,i-1])+"<x<"+str(t[0,i+1])
    #                     if d=="":
    #                      u="x כל"
    #                      d="אין"
    #                     if u=="":
    #                      d="x כל"
    #                      u="אין "

    #                 exy=[]
    #                 for i in range(len(ex)):
    #                     i="("+str(ex[i])+","+str(ey[i])+")"
    #                     exy.append(i)
                    
    def run(self):
        st.title("Function Analyzing App")
        self.input_text = st.text_input("Enter a function:", "")
        st.session_state.next_button=self.definition
        if st.session_state.step==0:
           if st.button("Next"):
                self.definition()
                st.session_state.step = 1
        elif st.session_state.step==1:
            if st.button("Next"):
                x = st.session_state.get('x')
                yf = st.session_state.get('yf')
                D = st.session_state.get('D')
                self.derivative(yf,D,x)

        
def app():
    analyze_app=AnalyzeApp()
    analyze_app.run()
