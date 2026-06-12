import streamlit as st

st.title("Hello, Streamlit! :wave:")
st.subheader("This is a simple Streamlit app.")
st.write("You can use Streamlit to create interactive web applications with Python.")
st.text("Here's an example of a simple input form:")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!") 
st.write("You can also add more complex components, such as charts, maps, and more!")  

game_of_the_year = st.selectbox("Choose Game of the Year:", ["The Last of Us Part II", "Hades", "Ghost of Tsushima", "Animal Crossing: New Horizons"])
st.write(f"You selected: {game_of_the_year}")

st.success("Thank you for using this Streamlit app! :tada:")

if st.button("Click me!"):
    st.balloons()
  
st.slider("Select a value:", 0, 100,10)

st.checkbox("Check me!")

st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])

st.number_input("Enter a number:", min_value=0, max_value=100, value=50)

st.date_input("Select a Birthdate:")

col1, col2 = st.columns(2)
with col1:
    st.header("Cat ")
    st.image("https://images.pexels.com/photos/4961908/pexels-photo-4961908.jpeg", width=200)
    vote1=st.radio("Vote for cat:", ["cat"])
    st.success("Thank you for voting for cat!")
    
with col2:
    st.header("Dog")
    st.image("https://images.pexels.com/photos/8545347/pexels-photo-8545347.jpeg", width=170)
    vote2=st.radio("Vote for dog:", ["dog"])
    st.success("Thank you for voting for dog!")

name = st.sidebar.text_input("Enter your name in the sidebar:")
if name:
    st.sidebar.write(f"Hello, {name}! Welcome to the sidebar!")
    st.sidebar.success("You can add more components to the sidebar as well!")