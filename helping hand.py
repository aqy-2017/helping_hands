import streamlit as st
st.title("Helping Hands🤝")
st.markdown("""
      <style>
      div.stButton > button {
          font-size: 4px;
          padding: 1px 4px;
      }
      </style>
  """, unsafe_allow_html=True)
if "requests" not in st.session_state:
  st.session_state.requests = []
if "filter" not in st.session_state:

    st.session_state.filter = []
col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)
name=st.text_input("write your name!")
user=st.text_input("what do you need help with??  ")
helper_name=st.text_input("write your name if you are ofering help!!")

if col1.button("📚math"):
    if "📚math" not in st.session_state.filter:

      st.session_state.filter.append("📚math")
    if name:
        st.session_state.requests.append(f"{name} needs help with 📚math")


   # st.session_state.requests.append("📚math")




if col2.button("Art🧶"):

    if "Art🧶" not in st.session_state.filter:
        st.session_state.filter.append("Art🧶")
    if name:
        st.session_state.requests.append(f"{name} needs help with Art🧶")



if col3.button("reading📖"):
    if "reading📖" not in st.session_state.filter:
        st.session_state.filter.append("reading📖")
    if name:
        st.session_state.requests.append(f"{name} needs help with reading")

if col4.button("coding💻"):
    if "coding💻" not in st.session_state.filter:
        st.session_state.filter.append("coding💻")
    if name:
        st.session_state.requests.append(f"{name} needs help with coding")

if col5.button("swimming🏊🏻"):
    if "swimming🏊🏻" not in st.session_state.filter:
        st.session_state.filter.append("swimming🏊🏻")
    if name:
        st.session_state.requests.append(f"{name} needs help with swimming")
if col6.button("biking🚴🏻"):
    if "biking🚴🏻" not in st.session_state.filter:
        st.session_state.filter.append("biking🚴🏻")

    if name:
        st.session_state.requests.append(f"{name} needs help with biking")

if col7.button("music🎶"):
    if "music🎶" not in st.session_state.filter:
        st.session_state.filter.append("music🎶")

    if name:
        st.session_state.requests.append(f"{name} needs help with music")

if col8.button("dancing💃🏻"):
    if "dancing💃🏻" not in st.session_state.filter:
        st.session_state.filter.append("dancing💃🏻")

    if name:
        st.session_state.requests.append(f"{name} needs help with dancing")
#st.write(st.session_state.filter)
#user=st.text_input("what do need help with??:")
#st.write("Filter list:", st.session_state.filter)
if st.button("+I need help with:"):
    if user and name:
        st.session_state.requests.append(f"{name} needs help with {user}")


   # if st.session_state.filter:
        #st.session_state.requests.append(st.session_state.filter[-1])

st.subheader(f"{', '.join(st.session_state.filter)} requests:")

for i in range(len(st.session_state.requests)):
    col_a, col_b = st.columns([4, 1])

    col_a.write(st.session_state.requests[i])
    if col_b.button("I'll help 🙂", key=i): #key=a unique number or word like an id for button
        if helper_name:
            st.success(f"{helper_name} will help with {st.session_state.requests [i]} ")
        else:
            st.warning("please type you name first")





















