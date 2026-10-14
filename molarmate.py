import streamlit as st

st.set_page_config(
    page_title="For My Favorite Grandmaster 🦷♟️",
    page_icon="💌",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f4f7f6;
    }
    .letter-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 2.5rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border: 2px solid #e2e8f0;
        text-align: center;
        max-width: 520px;
        margin: 2rem auto;
    }
    .envelope-header {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
    }
    .title-text {
        color: #2c7a7b;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        font-size: 1.6rem;
        margin-bottom: 0.25rem;
    }
    .subtitle-text {
        color: #718096;
        font-size: 0.95rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .message-body {
        color: #2d3748;
        font-size: 1.15rem;
        line-height: 1.7;
        text-align: left;
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #319795;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

if "opened" not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    st.markdown("""
        <div class="letter-card">
            <div class="envelope-header">✉️</div>
            <div class="title-text">Confidential Patient File</div>
            <div class="subtitle-text">For the Dentist & Grandmaster's Eyes Only</div>
            <p style="color: #4a5568; font-size: 1rem;">
                There is a mandatory treatment note waiting for you.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Open Letter 💌", type="primary", use_container_width=True):
            st.session_state.opened = True
            st.rerun()

else:
    st.balloons()
    
    st.markdown("""
        <div class="letter-card">
            <div class="envelope-header">🩺♟️</div>
            <div class="title-text">Case Notes: A Quick Reminder</div>
            <div class="subtitle-text">Status: Checkmate 💖</div>
            
            <div class="message-body">
                Whether you’re carefully analyzing a tricky root canal or calculating a 10-move checkmate on the board, you do it all with so much precision and grace.<br><br>
                Just a little note to say you’re easily my favorite Grandmaster, in and out of the clinic. Ready whenever you are for our next date! 😊
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Close Letter ✉️", use_container_width=True):
            st.session_state.opened = False
            st.rerun()