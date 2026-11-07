import streamlit as st
st.title("Helping Hands🤝")
st.markdown("""
<style>
.stApp{background-color:#D6E4FF}
div.stButton > button {
font-size: 16px;
padding: 8px 14px;
border-radius: 20px;
 border: 2px solid #white;
 background: #fade82; 
color: #9d174d;
div.stButton > button:
hover { background: #A4CF97; 
border-color: #A4CF97; } 
}
div.stButton > button:hover {
background: #A4CF97;
border-color: #A4CF97;
}


@media (max-width: 640px) {
    div[data-testid="stHorizontalBlock"] {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    div[data-testid="stColumn"], div[data-testid="column"] {
        min-width: 0 !important;
        flex: 1 1 0 !important;
        width: auto !important;
    }
}


</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_shared_requests():
    return []


requests = get_shared_requests()

if "requests" not in st.session_state:
    st.session_state.requests = []
# filter har insaan ka apna hai, isliye session_state mein hi rehta hai
if "filter" not in st.session_state:
    st.session_state.filter = []
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
name = st.text_input("write your name!")
user = st.text_input("what do you need help with?? ")
#helper_name = st.text_input("write your name if you are ofering help!!")
helper_name=name
col1, col2 = st.columns(2)
if col1.button("📚math"):
    if "📚math" not in st.session_state.filter:
        st.session_state.filter.append("📚math")
    if name:
        requests.append({"text": f"{name} needs help with 📚math", "helpers": []})
if col2.button("Art🧶"):
    if "Art🧶" not in st.session_state.filter:
        st.session_state.filter.append("Art🧶")
    if name:
        requests.append({"text": f"{name} needs help with Art🧶", "helpers": []})

col3, col4 = st.columns(2)
if col3.button("reading📖"):
    if "reading📖" not in st.session_state.filter:
        st.session_state.filter.append("reading📖")
    if name:
        requests.append({"text": f"{name} needs help with reading📖", "helpers": []})

if col4.button("coding💻"):
    if "coding💻" not in st.session_state.filter:
        st.session_state.filter.append("coding💻")
    if name:
        requests.append({"text": f"{name} needs help with coding💻", "helpers": []})
col5, col6 = st.columns(2)
if col5.button("swimming🏊🏻"):
    if "swimming🏊🏻" not in st.session_state.filter:
        st.session_state.filter.append("swimming🏊🏻")
    if name:
        requests.append({"text": f"{name} needs help with swimming🏊🏻", "helpers": []})

if col6.button("biking🚴🏻"):
    if "biking🚴🏻" not in st.session_state.filter:
        st.session_state.filter.append("biking🚴🏻")
    if name:
        requests.append({"text": f"{name} needs help with biking🚴🏻", "helpers": []})

col7, col8 = st.columns(2)
if col7.button("music🎶"):
    if "music🎶" not in st.session_state.filter:
        st.session_state.filter.append("music🎶")
    if name:
        requests.append({"text": f"{name} needs help with music🎶", "helpers": []})

if col8.button("dancing💃🏻"):
    if "dancing💃🏻" not in st.session_state.filter:
        st.session_state.filter.append("dancing💃🏻")
    if name:
        requests.append({"text": f"{name} needs help with dancing💃🏻", "helpers": []})
# st.write(st.session_state.filter)
# user=st.text_input("what do need help with??:")
# st.write("Filter list:", st.session_state.filter)
if st.button("+I need help with:"):
    if user and name:
        requests.append({"text": f"{name} needs help with {user}", "helpers": []})

# if st.session_state.filter:
# st.session_state.requests.append(st.session_state.filter[-1])

st.subheader(f"{', '.join(st.session_state.filter)} requests:")

for i in range(len(requests)):
    col_a, col_b, col_c = st.columns([4, 1, 1])

    col_a.write(requests[i]["text"])

    # I'll help button
    if col_b.button("I'll help 🙂", key="help" + str(i)):
        if name:
            if name not in requests[i]["helpers"]:
                requests[i]["helpers"].append(name)
        else:
            st.warning("please type your name first")

    if len(requests[i]["helpers"]) > 0:
        col_a.write("✅ Helping: " + ", ".join(requests[i]["helpers"]))

    if col_c.button("🗑️", key="delete" + str(i)):
        requests.pop(i)
        st.rerun()
