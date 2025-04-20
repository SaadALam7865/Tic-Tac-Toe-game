# # # import streamlit as st

# # # #✅ Step 2: Initialize the Game State
# # # if 'board'  not in st.session_state:
# # #     st.session_state.board = [''] * 9
# # #     st.session_state.current_player = 'X'
# # #     st.session_state.winner = None

# # # # ✅ Step 3: Game Title
# # # st.title("🎯 Tic Tac Toe Game (Python + Streamlit)")

# # # # ✅ Step 4: Game Logic — Check for Winner
# # # def check_winner(board):
# # #     # All possible winning combinations
# # #     win_conditions = [
# # #         (0,1,2) (3,4,5) (6,7,8)  # Rows
# # #         (0,3,6)(1,4,7)(2,5,8)    # columns
# # #         (0,4,8)(2,4,6)  # Diagonals
# # #     ]
# # #     for condition in win_conditions:
# # #         a, b, c = condition
# # #         if board[a] == board[b] == board[c] != '':
# # #             return board[a] # return 'X' or 'O'
# # #     if '' not in board:
# # #         return 'Draw'
# # #     return None

# # # #  Step 5: Displaying Game Board (3x3 Grid)
# # # for i in range(3):
# # #     cols = st.columns(3)
# # #     for j in range(3):
# # #         index = 3 * i + j

                                                                                                                                      

# #     # Remainder value

# # # def cal():
# # #     even_num = []
# # #     odd_num = []
# # #     for i in range(1, 21):
# # #         if i % 2 == 0:
# # #             even_num.append(i)
# # #         else:
# # #             odd_num.append(i)
# # #     print("Even numbers:", even_num)
# # #     print("Odd numbers:", odd_num)

# # # # Call the function
# # # cal()

# # import streamlit as st

# # # Initialize session state (for keeping game data persistent between reruns)
# # if "board" not in st.session_state:
# #     st.session_state.board = [""] * 9
# #     st.session_state.current_player = "X"
# #     st.session_state.winner = None

# # # Game Logic
# # def check_winner(board):
# #     win_conditions = [
# #         (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
# #         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
# #         (0, 4, 8), (2, 4, 6)              # diagonals
# #     ]
# #     for i, j, k in win_conditions:
# #         if board[i] and board[i] == board[j] == board[k]:
# #             return board[i]
# #     if "" not in board:
# #         return "Draw"
# #     return None

# # def reset_game():
# #     st.session_state.board = [""] * 9
# #     st.session_state.current_player = "X"
# #     st.session_state.winner = None

# # # UI Layout
# # st.title("🎮 Tic Tac Toe Game")
# # st.write("Built with Python + Streamlit by Saad 😎")

# # # Game Board
# # cols = st.columns(3)
# # for i in range(9):
# #     if cols[i % 3].button(st.session_state.board[i] or " ", key=i):
# #         if not st.session_state.board[i] and not st.session_state.winner:
# #             st.session_state.board[i] = st.session_state.current_player
# #             st.session_state.winner = check_winner(st.session_state.board)
# #             if not st.session_state.winner:
# #                 st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# # # Game Status
# # if st.session_state.winner:
# #     if st.session_state.winner == "Draw":
# #         st.success("It's a Draw! 🤝")
# #     else:
# #         st.success(f"🎉 Player {st.session_state.winner} Wins!")
# # else:
# #     st.info(f"Current Turn: Player {st.session_state.current_player}")

# # # Reset
# # if st.button("🔄 Reset Game"):
# #     reset_game()
# import streamlit as st
# import random

# # -------------------- Styling --------------------
# st.markdown("""
# <style>
# .main {
#     background: linear-gradient(120deg, #f0f2f6, #f3f0f6, #f6f0f3);
# }
# .stButton>button {
#     font-size: 24px;
#     height: 80px;
#     width: 80px;
#     border-radius: 10px;
#     margin: 5px;
#     transition: all 0.3s;
# }
# .stButton>button:hover {
#     transform: scale(1.1);
#     box-shadow: 0 4px 8px rgba(0,0,0,0.2);
# }
# .score-box {
#     background-color: #e3f2fd;
#     padding: 10px;
#     border-radius: 8px;
#     margin-bottom: 10px;
#     color: black;
      
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------- State Init --------------------
# if "board" not in st.session_state:
#     st.session_state.board = [""] * 9
#     st.session_state.current_player = "X"
#     st.session_state.winner = None
#     st.session_state.player_score = 0
#     st.session_state.ai_score = 0
#     st.session_state.draws = 0
#     st.session_state.play_mode = "Player vs Player"
#     st.session_state.player1 = "Player X"
#     st.session_state.player2 = "Player O"

# # -------------------- Functions --------------------
# def check_winner(board):
#     win_conditions = [
#         (0,1,2), (3,4,5), (6,7,8),
#         (0,3,6), (1,4,7), (2,5,8),
#         (0,4,8), (2,4,6)
#     ]
#     for i,j,k in win_conditions:
#         if board[i] and board[i] == board[j] == board[k]:
#             return board[i]
#     if "" not in board:
#         return "Draw"
#     return None

# def reset_game():
#     st.session_state.board = [""] * 9
#     st.session_state.current_player = "X"
#     st.session_state.winner = None

# def reset_scores():
#     st.session_state.player_score = 0
#     st.session_state.ai_score = 0
#     st.session_state.draws = 0

# def ai_move():
#     empty = [i for i, val in enumerate(st.session_state.board) if val == ""]
#     if empty:
#         move = random.choice(empty)
#         st.session_state.board[move] = "O"
#         st.session_state.winner = check_winner(st.session_state.board)

# # -------------------- UI --------------------
# st.title("🎮 Tic Tac Toe - Pro Edition")
# st.write("Created with ❤️ by **Saad Alam**")

# st.session_state.play_mode = st.sidebar.radio("Choose Game Mode:", ["Player vs Player", "Player vs AI"])

# # Player Names (PvP mode)
# if st.session_state.play_mode == "Player vs Player":
#     st.session_state.player1 = st.text_input("Enter name for Player X:", st.session_state.player1)
#     st.session_state.player2 = st.text_input("Enter name for Player O:", st.session_state.player2)

# # Score Display
# st.markdown("### 📊 Scores:")
# score_display = f"<div class='score-box'>👤 {st.session_state.player1}: {st.session_state.player_score} | "
# score_display += f"🤖 {st.session_state.player2 if st.session_state.play_mode == 'Player vs Player' else 'AI'}: {st.session_state.ai_score} | 🤝 Draws: {st.session_state.draws}</div>"
# st.markdown(score_display, unsafe_allow_html=True)

# # -------------------- Game Board --------------------
# cols = st.columns(3)
# for i in range(9):
#     if cols[i % 3].button(st.session_state.board[i] or " ", key=i):
#         if not st.session_state.board[i] and not st.session_state.winner:
#             st.session_state.board[i] = st.session_state.current_player
#             st.session_state.winner = check_winner(st.session_state.board)

#             if not st.session_state.winner:
#                 if st.session_state.play_mode == "Player vs Player":
#                     st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
#                 else:
#                     ai_move()

# # -------------------- Winner Check --------------------
# if st.session_state.winner:
#     if st.session_state.winner == "Draw":
#         st.success("🤝 It's a Draw!")
#         st.session_state.draws += 1
#     else:
#         name = ""
#         if st.session_state.play_mode == "Player vs Player":
#             name = st.session_state.player1 if st.session_state.winner == "X" else st.session_state.player2
#         else:
#             name = "You" if st.session_state.winner == "X" else "AI"
#         st.balloons()
#         st.success(f"🎉 {name} wins!")

#         if st.session_state.play_mode == "Player vs AI":
#             if st.session_state.winner == "X":
#                 st.session_state.player_score += 1
#             else:
#                 st.session_state.ai_score += 1
#         else:
#             if st.session_state.winner == "X":
#                 st.session_state.player_score += 1
#             else:
#                 st.session_state.ai_score += 1

# print('### --------------------------')
# # -------------------- Buttons --------------------
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("🔄 Reset Game"):
#         reset_game()
# with col2:
#     if st.button("♻️ Reset Scores"):
#         reset_scores()
