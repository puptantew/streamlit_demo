import streamlit as st
# streamlit run app.py
st.title("แฮมรักช้าง ช้างรักแฮม")
st.header("แฮมรักบ้านของช้างกับแฮม")
st.subheader("แฮมน่าร้ากกกก")
st.text("เจ้าแฮม")

st.success("Success")
st.warning("warning")
st.info("information")
st.error("Error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favorite Color ?", 
("Red",'Green',"yellow"))

if state == 'Green':
    st.success("Thats my favorite color as well")

occupation = st.selectbox("What do you do ?",
["Student","Vlogger","Engineer"])

st.text(f"selected option is {occupation}")

if st.button("Example Button"):
    st.error("You clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Puptantew")