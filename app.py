import streamlit as st



# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.score = {"X": 0, "O": 0, "Draw": 0}
    st.session_state.move_history = []
    st.session_state.ai_mode = False
    st.session_state.theme = "Light"

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        background-image: url('https://images.unsplash.com/photo-1593112097178-7e5b0697b3d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }
    .overlay {
        background: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
        min-height: 100vh;
    }
    .stButton>button {
        font-size: 28px;
        height: 80px;
        width: 80px;
        border-radius: 8px;
        margin: 5px;
        background-color: transparent;
        color: #fff;
        border: 3px solid #fff;
        transition: all 0.3s;
        font-family: 'Chalkduster', 'Comic Sans MS', cursive;
        
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: rgba(255, 255, 255, 0.2);
       
    }
    .stButton>button:active {
        background: radial-gradient(circle, rgba(255,255,255,0.3) 10%, transparent 10%);
        background-size: 1000%;
        animation: chalkDust 0.4s ease-out;
    }
    @keyframes chalkDust {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    .dark-theme .main {
        background-image: url('https://images.unsplash.com/photo-1593112097178-7e5b0697b3d6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80');
        color: #ffffff;
    }
    .dark-theme .stButton>button {
        border-color: #ccc;
        color: #ccc;
    }
    .score-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        color: #000;
        font-family: 'Chalkduster', cursive;
    }
    h1, h2, h3 {
        font-family: 'Chalkduster', 'Comic Sans MS', cursive;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .footer {
        text-align: center;
        font-family: 'Chalkduster', cursive;
        color: #fff;
        font-size: 18px;
        margin-top: 20px;
        text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
        animation: glow 2s ease-in-out infinite;
    }
    
    </style>
""", unsafe_allow_html=True)

# Winner check function
def check_winner(board):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i, j, k in win_conditions:
        if board[i] and board[i] == board[j] == board[k]:
            return board[i]
    if "" not in board:
        return "Draw"
    return None

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": return 10 - depth
    if winner == "X": return depth - 10
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if not board[i]:
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if not board[i]:
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if not st.session_state.board[i]:
            st.session_state.board[i] = "O"
            score = minimax(st.session_state.board, 0, False)
            st.session_state.board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        st.session_state.board[best_move] = "O"
        st.session_state.move_history.append(("AI (O)", best_move))
        st.session_state.winner = check_winner(st.session_state.board)
        if st.session_state.winner:
            st.session_state.score[st.session_state.winner] += 1
        else:
            st.session_state.current_player = "X"

# Reset game
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.move_history = []

# Reset scores
def reset_all():
    reset_game()
    st.session_state.score = {"X": 0, "O": 0, "Draw": 0}

# Title and theme selection
st.title("🎮 Ultimate Tic Tac Toe Game")
st.write("Made & Designed by ❤️ **Saad** ")
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"], index=0)
if theme != st.session_state.theme:
    st.session_state.theme = theme
    st.markdown(f'<div class="{theme.lower()}-theme">', unsafe_allow_html=True)

# AI mode toggle
st.session_state.ai_mode = st.checkbox("Play against AI (O)", value=st.session_state.ai_mode)

# Scoreboard
st.subheader("🏆 Scoreboard")
col1, col2, col3 = st.columns(3)
col1.metric("Player X", st.session_state.score["X"], delta_color="normal")
col2.metric("Player O" if not st.session_state.ai_mode else "AI (O)", st.session_state.score["O"], delta_color="normal")
col3.metric("Draws", st.session_state.score["Draw"], delta_color="normal")

# Game board UI
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        label = "🔵 X" if st.session_state.board[i] == "X" else "🔴 O" if st.session_state.board[i] == "O" else " "
        if st.button(label, key=f"cell_{i}", use_container_width=True):
            if not st.session_state.board[i] and not st.session_state.winner:
                st.session_state.board[i] = st.session_state.current_player
                st.session_state.move_history.append((f"Player {st.session_state.current_player}", i))
                st.session_state.winner = check_winner(st.session_state.board)
                if st.session_state.winner:
                    st.session_state.score[st.session_state.winner] += 1
                    st.balloons()
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                    if st.session_state.ai_mode and st.session_state.current_player == "O" and not st.session_state.winner:
                        ai_move()

# Game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a Draw!")
    else:
        st.success(f"🎉 {'AI (O)' if st.session_state.winner == 'O' and st.session_state.ai_mode else f'Player {st.session_state.winner}'} Wins!")
        st.balloons()
else:
    st.info(f"👥 Current Turn: {'AI (O)' if st.session_state.current_player == 'O' and st.session_state.ai_mode else f'Player {st.session_state.current_player}'}")

# Move history
st.subheader("📜 Move History (Last 5)")
for move in st.session_state.move_history[-5:]:
    player, pos = move
    st.write(f"{player} placed at position {pos + 1}")



# Reset buttons
col4, col5 = st.columns(2)
if col4.button("🔄 Reset Game"):
    reset_game()
if col5.button("🗑️ Reset Scores"):
    reset_all()

# Replay last move (undo)
if st.session_state.move_history and not st.session_state.winner:
    if st.button("Undo Last Move"):
        last_move = st.session_state.move_history.pop()
        st.session_state.board[last_move[1]] = ""
        st.session_state.current_player = "X" if st.session_state.current_player == "O" else "O"
        st.session_state.winner = None 