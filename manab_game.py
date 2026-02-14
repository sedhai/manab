import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Manab's Universe", page_icon="🎮", layout="centered")

# --- CUSTOM CSS FOR GAMER VIBES ---
st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #ffffff; }
    h1 { color: #e94560; font-family: 'Courier New', Courier, monospace; text-align: center; }
    .story-text { font-size: 20px; background-color: #16213e; padding: 20px; border-radius: 10px; border: 2px solid #0f3460; }
    .stButton>button { width: 100%; background-color: #e94560; color: white; border: 2px solid #fff; border-radius: 10px; font-weight: bold; font-size: 18px; transition: 0.3s; }
    .stButton>button:hover { background-color: #0f3460; border-color: #e94560; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- THE 50-PAGE GAME UNIVERSE (STATE MACHINE) ---
# Each number is a page. It contains the title, story, and buttons that link to other pages.
GAME_DATA = {
    1: {"title": "🏠 The Home Page: Manab's Hub", "text": "Welcome to Manab Sedhai's gaming universe! To prove you are worthy to join the squad, you must survive. Choose your path:", "choices": {"Enter the Roblox Obby (Action)": 2, "Enter the Tycoon (Strategy)": 20, "Enter the Horror Maze (Scary)": 35}},
    
    # --- OBBY PATH (Pages 2 - 19) ---
    2: {"title": "🏃 The Obby: Level 1", "text": "You spawn on a green block. A massive lava pit is in front of you. There is a narrow bridge and a floating platform.", "choices": {"Take the narrow bridge": 3, "Jump to the floating platform": 4}},
    3: {"title": "💀 OOF!", "text": "The bridge was a troll! It disappeared when you stepped on it. You fell into the lava.", "choices": {"Respawn (Go to Start)": 1}},
    4: {"title": "🏃 The Obby: Level 2", "text": "Perfect jump! Now you face spinning lasers.", "choices": {"Run fast!": 5, "Wait and time it": 6}},
    5: {"title": "💀 OOF!", "text": "You got zapped. Patience is a virtue, noob.", "choices": {"Respawn": 1}},
    6: {"title": "🏃 The Obby: Level 3", "text": "You timed it perfectly. You reach a checkpoint! A locked door blocks your path.", "choices": {"Search for a key": 7, "Try to glitch through the wall": 8}},
    7: {"title": "🔑 The Key Room", "text": "You found a glowing blue key guarded by a sleeping Noob.", "choices": {"Sneak past": 9, "Attack the Noob": 10}},
    8: {"title": "💀 Anti-Cheat!", "text": "Manab's anti-cheat system caught you glitching. BANNED (Just kidding, but you died).", "choices": {"Respawn": 1}},
    9: {"title": "🏃 The Obby: Level 4", "text": "You got the key and unlocked the door. You enter a dark cave with two tunnels.", "choices": {"Left Tunnel": 11, "Right Tunnel": 12}},
    10: {"title": "💀 OOF!", "text": "The Noob woke up and hit you with a ban hammer.", "choices": {"Respawn": 1}},
    11: {"title": "🏃 The Obby: Level 5", "text": "The left tunnel is safe! You find a jetpack.", "choices": {"Equip Jetpack": 13, "Leave it, it might be a trap": 14}},
    12: {"title": "💀 Cave In!", "text": "The right tunnel collapsed!", "choices": {"Respawn": 1}},
    13: {"title": "🚀 The Obby: Boss Room", "text": "You fly up to the final platform. The Mega-Bacon-Hair Boss appears!", "choices": {"Shoot laser from jetpack": 15, "Fly circles around him": 16}},
    14: {"title": "💀 The Floor is Lava", "text": "You should have taken the jetpack. The floor drops out.", "choices": {"Respawn": 1}},
    15: {"title": "💥 Boss Fight Phase 2", "text": "Direct hit! The boss shrinks into a tiny bacon hair. He begs for mercy.", "choices": {"Spare him": 17, "Oof him": 18}},
    16: {"title": "💀 Ran out of fuel", "text": "Your jetpack ran out of gas. You fell.", "choices": {"Respawn": 1}},
    17: {"title": "🏆 Obby Victory!", "text": "You showed mercy! The bacon hair gives you the Code of Legends. YOU WIN THE OBBY!", "choices": {"Return to Main Hub": 1}},
    18: {"title": "💀 Karma!", "text": "When you tried to oof him, he used a reverse Uno card.", "choices": {"Respawn": 1}},
    19: {"title": "Secret Room", "text": "You found Manab's secret stash of Robux.", "choices": {"Take some": 1, "Leave it": 1}}, # Buffer page
    
    # --- TYCOON PATH (Pages 20 - 34) ---
    20: {"title": "🏗️ Tycoon: The Beginning", "text": "You claim a blank Tycoon base. You have $10.", "choices": {"Buy a Dropper ($10)": 21, "Buy Walls ($10)": 22}},
    21: {"title": "🏗️ Tycoon: Cash Flow", "text": "The dropper makes $1 a second. You wait and get $50.", "choices": {"Buy Upgrade ($50)": 23, "Buy a Sword ($50)": 24}},
    22: {"title": "💀 Raided!", "text": "You bought walls but had no income. Another player broke in and took your base.", "choices": {"Respawn": 1}},
    23: {"title": "🏗️ Tycoon: Empire", "text": "Your tycoon is huge! You are making $1000 a second.", "choices": {"Build the Mega Laser": 25, "Build a Forcefield": 26}},
    24: {"title": "🗡️ Tycoon: The Warrior", "text": "You bought a sword and attacked a neighbor.", "choices": {"Attack the Pro": 27, "Attack the Noob": 28}},
    25: {"title": "💥 Mega Laser Fired", "text": "You blasted the whole server. You are the king of the Tycoon!", "choices": {"Claim Victory": 29}},
    26: {"title": "🛡️ The Turtle", "text": "You sit in your base forever doing nothing. Boring.", "choices": {"Go outside": 24}},
    27: {"title": "💀 OOF!", "text": "The Pro had admin commands. You were destroyed.", "choices": {"Respawn": 1}},
    28: {"title": "⚔️ Victory?", "text": "You beat the noob, but his big brother joined the server.", "choices": {"Run away": 1, "Fight the brother": 27}},
    29: {"title": "🏆 Tycoon Victory!", "text": "You are the richest player in Manab's server!", "choices": {"Return to Main Hub": 1}},
    30: {"title": "Bank", "text": "Your money is stored here.", "choices": {"Withdraw": 20}},
    31: {"title": "Shop", "text": "Buy cool hats.", "choices": {"Buy Fedora": 20}},
    32: {"title": "Glitch", "text": "You fell through the map.", "choices": {"Respawn": 1}},
    33: {"title": "AFK", "text": "You went AFK and got disconnected.", "choices": {"Reconnect": 1}},
    34: {"title": "Admin Room", "text": "You aren't supposed to be here.", "choices": {"Leave before Manab sees": 1}},

    # --- HORROR PATH (Pages 35 - 49) ---
    35: {"title": "🔦 Horror Maze: Entrance", "text": "It's pitch black. You hear a weird noise down the hall.", "choices": {"Turn on flashlight": 36, "Walk in the dark": 37}},
    36: {"title": "🚪 The Doors", "text": "You see two doors. Door 1 has blood on it. Door 2 smells like pizza.", "choices": {"Enter Door 1": 38, "Enter Door 2": 39}},
    37: {"title": "💀 Jump Scare!", "text": "A monster was right in front of you. OOF.", "choices": {"Respawn": 1}},
    38: {"title": "🔦 Safe Room!", "text": "Reverse psychology! Door 1 was a safe room. You find a medkit.", "choices": {"Heal up": 40, "Save for later": 41}},
    39: {"title": "💀 The Pizza Trap", "text": "The pizza was a lie. A giant monster ate you.", "choices": {"Respawn": 1}},
    40: {"title": "🔦 The Generator", "text": "You find the power generator, but it needs a code.", "choices": {"Enter 1234": 42, "Look for clues": 43}},
    41: {"title": "💀 Infection", "text": "You should have healed. You turned into a zombie.", "choices": {"Respawn": 1}},
    42: {"title": "💀 Wrong Code", "text": "The alarm sounds. The monsters find you.", "choices": {"Respawn": 1}},
    43: {"title": "📝 The Clue", "text": "You find a note: 'Manab's favorite number'. It's 7777!", "choices": {"Enter 7777": 44}},
    44: {"title": "💡 Power On!", "text": "The lights turn on! A secret elevator opens.", "choices": {"Get in": 45}},
    45: {"title": "🚪 The Final Chase", "text": "The elevator breaks. You have to run! A monster is right behind you!", "choices": {"Slide under the obstacle": 46, "Jump over it": 47}},
    46: {"title": "🏃 You Escaped!", "text": "You slid to safety and locked the blast doors.", "choices": {"See your reward": 48}},
    47: {"title": "💀 Tripped!", "text": "You didn't jump high enough.", "choices": {"Respawn": 1}},
    48: {"title": "🏆 Horror Victory!", "text": "You survived Manab's haunted maze. You are fearless.", "choices": {"Return to Main Hub": 1}},
    49: {"title": "The Void", "text": "You are lost in the horror void.", "choices": {"Wake up": 1}},

    # --- THE ULTIMATE ENDING (Page 50) ---
    50: {"title": "👑 MANAB'S INNER CIRCLE", "text": "You found the secret 50th page! You have completed all paths. You are officially in Manab's elite squad.", "choices": {"Restart the Fun": 1}}
}

# --- SESSION STATE MANAGEMENT ---
# This keeps track of what page the user is currently on.
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

# Function to change the page
def go_to_page(page_number):
    st.session_state.current_page = page_number

# --- RENDER THE CURRENT PAGE ---
current_data = GAME_DATA[st.session_state.current_page]

# Display Title and Text
st.markdown(f"<h1>{current_data['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<div class='story-text'>{current_data['text']}</div><br>", unsafe_allow_html=True)

# Secret logic for Page 50 (If they win the main paths, give them a chance to go to 50)
if st.session_state.current_page in [17, 29, 48]:
    st.balloons()
    st.success("🎉 You completed a path! But wait... a secret button appeared.")
    if st.button("Unlock The Ultimate Secret", key="secret_btn"):
        go_to_page(50)
        st.rerun()

# Display Choices (Buttons)
col1, col2 = st.columns(2) # Try to put buttons side by side
button_cols = [col1, col2]

for i, (choice_text, target_page) in enumerate(current_data["choices"].items()):
    # We use modulo to alternate between column 1 and column 2
    with button_cols[i % 2]:
        if st.button(choice_text, key=f"{st.session_state.current_page}_{i}"):
            go_to_page(target_page)
            st.rerun()

# --- PROGRESS BAR ---
st.markdown("---")
progress = min((st.session_state.current_page / 50.0), 1.0)
st.progress(progress, text=f"Exploring Manab's Universe (Page {st.session_state.current_page}/50)")