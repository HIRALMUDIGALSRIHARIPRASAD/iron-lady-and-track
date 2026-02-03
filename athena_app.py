import streamlit as st
import time

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="Athena | Iron Lady Strategy", page_icon="🛡️", layout="centered")

# Iron Lady Theme Colors: Gold, Black, White
css = """
<style>
    .stApp { background-color: #0e0e0e; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #d4af37; color: #000000; border-radius: 0px; 
        font-weight: bold; border: none; padding: 10px 20px;
    }
    .stButton>button:hover { background-color: #f4c430; color: #000000; }
    .chat-message { padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex; }
    .chat-message.user { background-color: #1a1a1a; border-left: 5px solid #d4af37; }
    .chat-message.bot { background-color: #2b2b2b; border-left: 5px solid #ffffff; }
    .bot-name { font-weight: bold; color: #d4af37; margin-bottom: 0.5rem; display: block; }
    .user-name { font-weight: bold; color: #ffffff; margin-bottom: 0.5rem; display: block; }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# --- SIDEBAR & SETUP ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/000000/d4af37?text=IRON+LADY", use_container_width=True)
    st.header("🛡️ Strategy Settings")
    api_key = st.text_input("OpenAI API Key (Optional)", type="password", help="Leave empty to use Demo Mode (Pre-canned responses).")
    mode = st.radio("Select Interface:", ["Glass Ceiling Diagnostic", "The War Room (Chat)"])
    st.markdown("---")
    st.info("**Athena Protocol:**\n\nUnlike standard assistants, I do not offer sympathy. I offer strategy. I am here to help you maximize, not balance.")

# --- MOCK AI (DEMO MODE) ---
def get_demo_response(user_input):
    """Fallback responses if no API key is provided."""
    user_input = user_input.lower()
    if "salary" in user_input or "raise" in user_input:
        return ("**Strategy: Competitor-Centric Valuation.**\n\n"
                "Stop asking for a 'raise' based on your needs. That is weak. "
                "Instead, present a 'Business Case for Resource Allocation.' "
                "Show them that retaining you costs less than the risk of losing your specific "
                "market knowledge to a competitor. \n\n"
                "*Action:* Draft a 1-page memo titled 'Q3 Revenue Acceleration Plan' instead of a resignation letter.")
    elif "interrup" in user_input or "speak" in user_input:
        return ("**Strategy: The Unapologetic Pause.**\n\n"
                "When he interrupts, do not speed up. Stop completely. "
                "Stare silently for 3 seconds. It reclaims the power dynamic. "
                "Then say calmly: *'I wasn't finished. As I was saying...'* \n\n"
                "Do not smile when you say it.")
    else:
        return ("**Observation:** You are operating from a place of hesitation. \n\n"
                "In the Iron Lady philosophy, we do not 'hope' for outcomes; we engineer them using "
                "Business War Tactics. Clarify your objective: Are you trying to be liked, or are you trying to win?")

# --- LIVE AI (OPENAI INTEGRATION) ---
def get_openai_response(messages, api_key):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# --- SYSTEM PROMPT (THE "IRON LADY" BRAIN) ---
SYSTEM_PROMPT = """
You are Athena, the AI strategist for Iron Lady. 
Your Identity: You are NOT a helpful customer support bot. You are a high-level Career Strategist.
Your Tone: Unapologetic, Direct, Strategic, and Empowering. You use "Tough Love."
Your Knowledge Base:
1. "Business War Tactics": Life is a war for leadership. Women must use strategy, not just hard work.
2. "Shameless Pitching": Women must vocalize their achievements without modesty.
3. "Maximization vs. Balance": Reject "work-life balance" (a trap). Embrace "Maximizing" your potential.
4. Programs: 
   - "Leadership Essentials": For early managers needing confidence.
   - "100 Board Members": For mid-level women stuck at a plateau.
   - "Master of Business Warfare": For senior leaders aiming for C-Suite/1Cr+ salary.

Rules:
- Never apologize (e.g., don't say "I'm sorry to hear that").
- Challenge the user's limiting beliefs.
- Always end with a specific "Tactical Move" or specific Iron Lady program recommendation.
"""

# --- UI: HEADER ---
st.title("ATHENA")
st.markdown("### *The Iron Lady Strategy Companion*")
st.markdown("---")

# --- UI: MODE 1 - DIAGNOSTIC ---
if mode == "Glass Ceiling Diagnostic":
    st.subheader("🎯 Career Trajectory Analysis")
    st.write("Let's identify which 'Invisible Wall' is stopping you.")
    
    with st.form("diagnostic_form"):
        role = st.selectbox("Current Role", ["Individual Contributor", "Manager/Team Lead", "Director/VP", "C-Suite/Founder"])
        struggle = st.selectbox("Biggest Frustration", [
            "I work hard but don't get recognized.",
            "I'm stuck at the same salary/level for 3+ years.",
            "I struggle to speak up in male-dominated meetings.",
            "I want to join a Board but don't know how."
        ])
        ambition = st.radio("What is your honest goal?", ["To be respected and stable.", "To dominate my industry and double my income."])
        submitted = st.form_submit_button("Analyze My Profile")

    if submitted:
        st.markdown("### 🔍 Athena's Analysis")
        time.sleep(1) # Simulate thinking
        
        # Logic for recommendation
        program = ""
        diagnosis = ""
        
        if role in ["Individual Contributor", "Manager/Team Lead"]:
            program = "**Leadership Essentials Program**"
            diagnosis = "You are currently stuck in the 'Execution Trap'. You are waiting for permission to lead. You need to learn **Shameless Pitching** to turn your hard work into visibility."
        elif "Board" in struggle or role == "Director/VP":
            program = "**100 Board Members Program**"
            diagnosis = "You have the skills, but you lack the **Strategic Network**. You are playing a game of 'Merit' while your peers are playing a game of 'Warfare'. It is time to fast-track."
        else:
            program = "**Master of Business Warfare**"
            diagnosis = "You are ready for the top, but you are likely negotiating like an employee, not a peer. You need **Competitor-Centric** strategies."

        st.success(f"**Recommendation:** {program}")
        st.info(f"**The Truth:** {diagnosis}")
        st.markdown(f"> *\"The world does not pay you for what you know. It pays you for the value you can shamelessly pitch.\"*")

# --- UI: MODE 2 - WAR ROOM CHAT ---
elif mode == "The War Room (Chat)":
    st.subheader("⚔️ Tactical War Room")
    st.caption("Describe a workplace situation. Athena will give you a Business War Tactic to handle it.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.session_state.display_messages = [{"role": "assistant", "content": "I am ready. What challenge are you facing in the arena today?"}]

    # Display chat history
    for msg in st.session_state.display_messages:
        role_class = "user" if msg["role"] == "user" else "bot"
        name = "YOU" if msg["role"] == "user" else "ATHENA"
        st.markdown(f'<div class="chat-message {role_class}"><span class="{role_class}-name">{name}:</span>{msg["content"]}</div>', unsafe_allow_html=True)

    # User Input
    if prompt := st.chat_input("Ex: 'My boss keeps stealing credit for my ideas...'"):
        # Add user message to state
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.display_messages.append({"role": "user", "content": prompt})
        
        # Rerun to show user message immediately
        st.rerun()

    # Generate Response (if last message was user)
    if st.session_state.display_messages[-1]["role"] == "user":
        with st.spinner("Formulating strategy..."):
            if api_key:
                # Live API Call
                bot_reply = get_openai_response(st.session_state.messages, api_key)
            else:
                # Demo Mode
                time.sleep(1.5)
                bot_reply = get_demo_response(prompt)
        
        # Add bot message to state
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.session_state.display_messages.append({"role": "assistant", "content": bot_reply})
        st.rerun()