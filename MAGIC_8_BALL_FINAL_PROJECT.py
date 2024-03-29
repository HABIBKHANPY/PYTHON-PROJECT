import streamlit as st
import random
st.balloons()
st.snow()

# Sidebar menu
st.sidebar.title("Menu")
selected_page = st.sidebar.radio("", ["MAGIC 8 BALL GAME", "About Us", "Contact"])

if selected_page == "MAGIC 8 BALL GAME":
    st.title("BANO QABIL 2.0 PROJECT")
    st.title("MAGIC 8 BALL")
elif selected_page == "About Us":
    st.title("About Us")
    st.write(f"This address book application was created by {name}.")
elif selected_page == "Contact":
    st.title("Contact")
    st.write("For support, please email support@example.com.")
# Magic 8 Ball answers
responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]
def main():
    # Custom CSS to inject into the webpage
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://img.hotimg.com/eight-ball.jpeg');
            background-size: cover;
            color: #ffffff;
        }
        .stTextInput>div>div>input {
    color: #e0e0e0;
    background-color: #333333;
    }
        .stButton>button {
    color: #404040; /* Change text color to DodgerBlue */
    border-radius: 20px; /* Make corners less rounded */
    border-color: #32CD32; /* Change border color to LimeGreen */
    background-color: #FFD700; /* Change background color to Gold */
    font-size: 20px; /* Increase font size */
    padding: 10px 20px; /* Add more padding for a larger button */
    border-width: 2px; /* Make the border thicker */
    border-style: solid; /* Ensure the border is solid */
    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
        }
.stButton>button:hover {
    background-color: #FF69B4; /* Change background color on hover to HotPink */
    color: #FFFFFF; /* Change text color on hover to white */
}
        </style>
        """, unsafe_allow_html=True)

    # Text input for the question
    question = st.text_input("Ask a question:")

    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.markdown(f"<h2 style='text-align: center;'>🔮 {answer}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
