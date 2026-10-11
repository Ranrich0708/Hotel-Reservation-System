#WIN CHECKER
WinC = [
((1, 2, 3), (4, 5, 6), (7, 8, 9)), # rows
((1, 4, 7), (2, 5, 8), (3, 6, 9)), # cols
((1, 5, 9), (3, 5, 7), (3, 5, 7)) # diagonals
]

def Check (LLL):
ttt = -1
for iii in WinC:
ttt +=1
for ppp in iii:
if tuple((LLL[ppp[0]-1],LLL[ppp[1]-1],LLL[ppp[2]-1])) in
[('X','X','X')]:
return 'X'
check +=1
break
elif tuple((LLL[ppp[0]-1],LLL[ppp[1]-1],LLL[ppp[2]-1])) in
[('O','O','O')]:
return 'O'
check +=1
break

MODULE 2: AI Brain

# Winning lines
winning_lines = [
[0,1,2], [3,4,5], [6,7,8], # rows
[0,3,6], [1,4,7], [2,5,8], # columns
[0,4,8], [2,4,6] # diagonals
]
# Function to check if a player can win in next move
def can_win(board, player):
for line in winning_lines:
values = []
for i in line:
values.append(board[i])
if values.count(player) == 2 and values.count('#') == 1:
return line[values.index('#')]
return None
# Function to generate AI's best move
def generate_best_ai_move(board, Ai_as):
new_board = board.copy()
# Set opponent based on AI symbol
if Ai_as == 'X':
Opp = 'O'
else:
Opp = 'X'
# 1. Win if possible
win_pos = can_win(board, Ai_as)
if win_pos is not None:
new_board[win_pos] = Ai_as
return new_board
# 2. Block opponent if they can win
block_pos = can_win(board, Opp)
if block_pos is not None:
new_board[block_pos] = Ai_as
return new_board
# 3. Take center if empty
if board[4] == '#':
new_board[4] = Ai_as
return new_board

# 4. Take opposite corner
opposite_corners = [(0,8),(2,6),(6,2),(8,0)]
for oc in opposite_corners:
if board[oc[0]] == Opp and board[oc[1]] == '#':
new_board[oc[1]] = Ai_as
return new_board
# 5. Take any empty corner
for pos in [0,2,6,8]:
if board[pos] == '#':
new_board[pos] = Ai_as
return new_board
# 6. Take any empty side
for pos in [1,3,5,7]:
if board[pos] == '#':
new_board[pos] = Ai_as
return new_board
# 7. Fallback (should never happen)
for i in range(9):
if board[i] == '#':
new_board[i] = Ai_as
return new_board
'''
# Example usage
Ai_as = 'X'
current_board = ['#','#','#','#','X','#','O','#','#']
new_board = generate_best_ai_move(current_board, Ai_as)
print(current_board, new_board)
'''

APP MANAGER:

"APP_MANAGER"
from tkinter import *
import Win_Checker
import AIbrain
import mysql.connector

# -------------GLOBAL_VARIABLES--------------------
AiMove = 0
MyLIST = ['#'] * 9
YYY = 2
TTT = ""
Player1_AS, Player2_AS, AI_AS = "", "", ""

# Player name holders used by backend
Player1 = "" # player1 name (PVP mode)
Player2 = "" # player2 name (PVP mode)
PlayerX = "" # saved copy of Player1 for DB usage
PlayerO = "" # saved copy of Player2 / "AI"
Player = "" # single player name (AI mode)

def reset():
global MyLIST, YYY, Player1_AS, Player2_AS
MyLIST = ['#'] * 9
YYY = 2
TTT = ""
Player1_AS = ""
Player2_AS = ""

def WinCheck(mode):
# prefer checking winner first, then tie
winner = Win_Checker.Check(MyLIST)
if winner == 'X':
print('X wins')
return 'X'
if winner == 'O':
print('O wins')
return 'O'
if '#' not in MyLIST:
print('Game over - tie')
return 'K'
return None

def Home_Screen():
def PVPM():
Window.destroy()
PVP_Phase_1()

def PAIM():
Window.destroy()
AI_Phase_1()

Window = Tk()
Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

Button1 = Button(Window, bg="#eb5454", padx=25, pady=7,
text="PVP Match",

font=("Arial", 45, "bold"), fg="white",

command=PVPM)
Button1.place(x=30, y=300)

Button2 = Button(Window, bg="#eb5454", padx=60, pady=7,
text="AI Match",

font=("Arial", 45, "bold"), fg="white",

command=PAIM)
Button2.place(x=730, y=300)

Label1 = Label(Window, padx=20, pady=20, bg="#2b292b",
text=("""TICTACTOE GAME"""), fg="white",

font=("Arial", 40, "bold"))
Label1.place(x=410, y=20)

def PVP_Phase_1():
global PlayerX, PlayerO, Player1, Player2
Window = Tk()

def Entrr(Input1, Input2, Input3):
global YYY, Player1, Player2, PlayerX, PlayerO
Player1 = Input1.get()
Player2 = Input2.get()
# set who plays first based on Input3
if Input3.get().upper() == 'X':
YYY = 2
else:

YYY = 3

# minimal validation — keep your original style
if Player1 != "" and Player2 != "" and Input3.get() != "" and
Input3.get().upper() in ('X', 'O'):
# IMPORTANT: save names into PlayerX/PlayerO so
backend can read AFTER windows destroy
PlayerX = Player1
PlayerO = Player2
Window.destroy()
PVP_Phase_2()
print('Condition satisfied')
else:
print('Etho thappu irruku')

Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

MainLabel = Label(Window, bg="#ccc2c2", padx=350,
pady=160, font=("Arial", 45, "bold"), fg="white")
MainLabel.place(x=240, y=140)

SubLabel1 = Label(Window, bg="#eb5454", padx=255,
pady=20, fg="black",

text="ENTER PLAYER1 NAME:", font=("Arial", 20,

"bold"), width=10, anchor="e")
SubLabel1.place(x=250, y=150)

SubLabel2 = Label(Window, bg="#eb5454", padx=255,
pady=20, fg="black",

text="ENTER PLAYER2 NAME:", font=("Arial", 20,

"bold"), width=10, anchor="e")
SubLabel2.place(x=250, y=260)

SubLabel3 = Label(Window, bg="#eb5454", padx=255,
pady=20, fg="black",

text="ENTER PLAYER1 AS(X/0):", font=("Arial",

20, "bold"), width=10, anchor="e")
SubLabel3.place(x=250, y=370)

Input1 = Entry(Window, fg="black", bg="white", font=("Arial",
20, "bold"))
Input1.place(x=680, y=158, width=245, height=60)

Input2 = Entry(Window, fg="black", bg="white", font=("Arial",
20, "bold"))
Input2.place(x=680, y=268, width=245, height=60)

Input3 = Entry(Window, fg="black", bg="white", font=("Arial",
20, "bold"))
Input3.place(x=680, y=378, width=245, height=60)

Enter = Button(Window, fg="black", bg="white", padx=50,
pady=10, text="ENTER",

font=("Arial", 30, "bold"), command=lambda:

Entrr(Input1, Input2, Input3))
Enter.place(x=450, y=455, height=70)

# PlayerX and PlayerO will be set in Entrr when users press
ENTER

def PVP_Phase_2():
Window = Tk()

def BACK():
Window.destroy()
Home_Screen()

Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

Label1 = Label(Window, bg="white", relief=RAISED, bd=5,
padx=170, pady=176)
Label1.place(x=697, y=168)

exit_button = Button(Window, bg="#f7f779", padx=15,
pady=10, text="EXIT",

font=('Arial', 20, 'bold'), command=BACK)

exit_button.place(x=1050, y=550)

def Clicked(x):
global MyLIST, YYY
if YYY % 2 == 0:
MyLIST[x - 1] = 'X'
YYY += 1

print(MyLIST)
return 'X'
else:
MyLIST[x - 1] = 'O'
YYY += 1
print(MyLIST)
return 'O'

def replace_button_with_text(button, text, index):
x = button.winfo_x()
y = button.winfo_y()
button.destroy()
Label(button.master, text= Clicked(index), bg="white",
fg="black", font=("Arial", 70, "bold")).place(x=x+10, y=y)
if WinCheck('PVPM') != None:
Window.destroy()
Final(WinCheck('PVPM'))

button1 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '1')
button1.place(x=710, y=180)
button1.config(command=lambda:
replace_button_with_text(button1, "X",1))

button2 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '2')
button2.place(x=820, y=180)
button2.config(command=lambda:
replace_button_with_text(button2, "X",2))

button3 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '3')
button3.place(x=930, y=180)
button3.config(command=lambda:
replace_button_with_text(button3, "X",3))

button4 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '4')
button4.place(x=710, y=300)
button4.config(command=lambda:
replace_button_with_text(button4, "X",4))

button5 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '5')
button5.place(x=820, y=300)
button5.config(command=lambda:
replace_button_with_text(button5, "X",5))

button6 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '6')
button6.place(x=930, y=300)
button6.config(command=lambda:
replace_button_with_text(button6, "X",6))

button7 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '7')
button7.place(x=710, y=420)
button7.config(command=lambda:

replace_button_with_text(button7, "X",7))

button8 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '8')
button8.place(x=820, y=420)
button8.config(command=lambda:
replace_button_with_text(button8, "X",8))

button9 = Button(Window, bg="#eb5454", padx=45, pady=43,
text = '9')
button9.place(x=930, y=420)
button9.config(command=lambda:
replace_button_with_text(button9, "X",9))

MainLabel = Label(Window, bg="#ccc2c2", padx = 180, pady
= 290)
MainLabel.place(x=10,y=20)

Label1 = Label(Window, bg="#ccc2c2", padx = 52, pady = 20,
text= Player1, font=("Arial",20,"bold"), width=15)
Label1.place(x=10,y=25)

Label2 = Label(Window, bg="#52cf42", padx = 45, pady = 20,
text="{SCORE OF PLAYER1}", font=("Arial",20,"bold"),
width=15)
Label2.place(x=16,y=125)

Label3 = Label(Window, bg="#ccc2c2", padx = 52, pady = 20,

text= Player2, font=("Arial",20,"bold"), width=15)
Label3.place(x=10,y=220)

Label4 = Label(Window, bg="#52cf42", padx = 45, pady = 20,
text="{SCORE OF PLAYER2}", font=("Arial",20,"bold"),
width=15)
Label4.place(x=16,y=305)

HeadLabel = Label(Window, bg="#eb5454", padx = 150, pady
= 10, text="{Name of the player who has to play now}",
font=("Arial",20,"bold"), width=15)
HeadLabel.place(x=580,y=15)

def AI_Phase_1():
Window = Tk()
global Player, PlayerX, PlayerO
def Entrr(Input1, Input2):
global Player1_AS, AI_AS, YYY, Player, PlayerX, PlayerO
Player = Input1.get()
# set player choice
if Input2.get().upper() == 'X':
YYY = 2
Player1_AS = 'X'
AI_AS = 'O'
else:
YYY = 3
Player1_AS = 'O'
AI_AS = 'X'

# Save player names so Final() can use them after this
window is destroyed.
PlayerX = Player
PlayerO = "AI"

if Player != "" and Input2.get() != "" and Input2.get().upper()
in ('X','O'):
Window.destroy()
AI_Phase_2()
print('Condition satisfied')
else:
print('Entho thappu irruku')

Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

MainLabel = Label(Window, bg="#ccc2c2", padx = 350, pady
= 120, font=("Arial",45,"bold"), fg="white")
MainLabel.place(x=240,y=140)

SubLabel1 = Label(Window, bg="#eb5454", padx = 255, pady
= 20, fg="black", text="ENTER PLAYER1 NAME:",
font=("Arial",20,"bold"), width=10, anchor="e")
SubLabel1.place(x=250,y=150)

SubLabel2 = Label(Window, bg="#eb5454", padx = 255, pady
= 20, fg="black", text="ENTER PLAYER CHOICE(X/O):",

font=("Arial",20,"bold"), width=10, anchor="e")
SubLabel2.place(x=250,y=260)

Input1 = Entry(Window, fg="black", bg="white",
font=("Arial",20,"bold"))
Input1.place(x=680,y=158,width=245,height=60)

Input2 = Entry(Window, fg="black", bg="white",
font=("Arial",20,"bold"))
Input2.place(x=680,y=268,width=245,height=60)

Enter = Button(Window, fg="black", bg="white", padx=50,
pady=10, text="ENTER", font=("Arial",30,"bold"),
command=lambda: Entrr(Input1,Input2))
Enter.place(x=450,y=365,height=70)

def AI_Phase_2():
global AiMove, AI_AS
Window = Tk()

def BACK():
Window.destroy()
Home_Screen ()

Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

Label1 = Label(Window, bg="white", relief=RAISED, bd = 5,

padx = 170, pady = 176)
Label1.place(x =697,y = 168)

exit_button = Button(Window,bg="#f7f779", padx=15,pady=10,
text = "EXIT", font = ('Arial',20,'bold'), command = lambda :
BACK())
exit_button.place(x=1050,y=550)

def Ai_Moves ():
global MyLIST,AiMove
copylist = list(MyLIST)
MyLIST = AIbrain.generate_best_ai_move(MyLIST, AI_AS)
print('called')
print (MyLIST)
print(copylist)
for place in range(9):
if copylist[place] != MyLIST[place]:
AiMove = place + 1
print(f'AiMove: {AiMove} {AI_AS}')
return AiMove
return None
def Clicked (x):
# Player's move being counted
global MyLIST, YYY, AI_AS,AiMove
print(x)
if Player1_AS == 'X':
MyLIST[x-1] = 'X'
YYY += 1
if WinCheck('PAIM') != None:

Window.destroy()
Final(WinCheck('PAIM'))
#AI's turn:
Ai_Moves()
AIBUTTON (AiMove)
if WinCheck('PAIM') != None:
Window.destroy()
Final(WinCheck('PAIM'))
return 'X'
else:
MyLIST[x-1] = 'O'
YYY += 1
if WinCheck('PAIM') != None:
Window.destroy()
Final(WinCheck('PAIM'))
#AI's turn:
Ai_Moves()
AIBUTTON (AiMove)
if WinCheck('PAIM') != None:
Window.destroy()
Final(WinCheck('PAIM'))
return 'O'
def replace_button_with_text2(button, text, index):
x = button.winfo_x()
y = button.winfo_y()
button.destroy()
Label(button.master, text= text, bg="white", fg="black",
font=("Arial", 70, "bold")).place(x=x+10, y=y)
def replace_button_with_text(button, text, index):

x = button.winfo_x()
y = button.winfo_y()
button.destroy()
Label(button.master, text= Clicked(index), bg="white",
fg="black", font=("Arial", 70, "bold")).place(x=x+10, y=y)

button1 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '1')
button1.place(x=710,y=180)
button1.config(command=lambda:
replace_button_with_text(button1, "X",1))

button2 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '2')
button2.place(x=820,y=180)
button2.config(command=lambda:
replace_button_with_text(button2, "X",2))

button3 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '3')
button3.place(x=930,y=180)
button3.config(command=lambda:
replace_button_with_text(button3, "X",3))

button4 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '4')
button4.place(x=710,y=300)
button4.config(command=lambda:

replace_button_with_text(button4, "X",4))

button5 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '5')
button5.place(x=820,y=300)
button5.config(command=lambda:
replace_button_with_text(button5, "X",5))

button6 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '6')
button6.place(x=930,y=300)
button6.config(command=lambda:
replace_button_with_text(button6, "X",6))

button7 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '7')
button7.place(x=710,y=420)
button7.config(command=lambda:
replace_button_with_text(button7, "X",7))

button8 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '8')
button8.place(x=820,y=420)
button8.config(command=lambda:
replace_button_with_text(button8, "X",8))

button9 = Button(Window,bg="#eb5454",
padx=45,pady=43,text = '9')
button9.place(x=930,y=420)

button9.config(command=lambda:
replace_button_with_text(button9, "X",9))

def AIBUTTON (AiMove):
if True:
if AiMove == 1:
# Use button1 for AiMove 1
button1.config(command=lambda:
replace_button_with_text2(button1, AI_AS, 1))

button1.invoke()
elif AiMove == 2:
# Use button2 for AiMove 2
button2.config(command=lambda:
replace_button_with_text2(button2, AI_AS, 2))

button2.invoke()
elif AiMove == 3:
# Use button3 for AiMove 3
button3.config(command=lambda:
replace_button_with_text2(button3, AI_AS, 3))

button3.invoke()
elif AiMove == 4:
# Use button4 for AiMove 4
button4.config(command=lambda:
replace_button_with_text2(button4, AI_AS, 4))

button4.invoke()
elif AiMove == 5:
# Use button5 for AiMove 5
print('Vantaen SIR!!!')
button5.config(command=lambda:

replace_button_with_text2(button5, AI_AS, 5))

button5.invoke()
elif AiMove == 6:
# Use button6 for AiMove 6
button6.config(command=lambda:
replace_button_with_text2(button6, AI_AS, 6))

button6.invoke()
elif AiMove == 7:
# Use button7 for AiMove 7
button7.config(command=lambda:
replace_button_with_text2(button7, AI_AS, 7))

button7.invoke()
elif AiMove == 8:
# Use button8 for AiMove 8
button8.config(command=lambda:
replace_button_with_text2(button8, AI_AS, 8))

button8.invoke()
elif AiMove == 9:
print('KAKAKA')
# Use button9 for AiMove 9
button9.config(command=lambda:
replace_button_with_text2(button9, AI_AS, 9))

button9.invoke()

MainLabel = Label(Window,bg="#ccc2c2", padx = 180, pady =
290)
MainLabel.place(x=10,y=20)

Label1 = Label(Window,bg="#ccc2c2", padx = 52, pady =

20,text= Player,font=("Arial",20,"bold"),width=15)
Label1.place(x=10,y=25)

Label2 = Label(Window,bg="#52cf42", padx = 45, pady =
20,text="{SCORE OF
PLAYER1}",font=("Arial",20,"bold"),width=15)
Label2.place(x=16,y=125)

Label3 = Label(Window,bg="#ccc2c2", padx = 52, pady =
20,text= "AI",font=("Arial",20,"bold"),width=15)
Label3.place(x=10,y=220)

Label4 = Label(Window,bg="#52cf42", padx = 45, pady =
20,text="{SCORE OF
PLAYER2}",font=("Arial",20,"bold"),width=15)
Label4.place(x=16,y=305)

HeadLabel = Label(Window,bg="#eb5454", padx = 150, pady
= 10,text="{THE AI IS PLAYING
AS(X/O)}",font=("Arial",20,"bold"),width=15)
HeadLabel.place(x=580,y=15)

def KKK():
if AI_AS == 'X':
print('Aiitean')
Ai_Moves()
AIBUTTON (AiMove)
Window.after(3000, KKK())

def Final(Info):
global TTT, PlayerX, PlayerO
TTT = Info
Window = Tk()
Window.geometry("1188x648")
Window.title("")
Window.config(background="#2b292b")

Label2 = Label(Window, padx=20, pady=20, bg="#2b292b",
text=(f"""PLAYAR {TTT} WINS BABY!!!!!"""),
fg="white", font=("Arial", 40, "bold"))

# Determine result strings per player for a single match
# Default values
X_result_str = "Draw"
O_result_str = "Draw"

# If X wins
if TTT == "X":
X_result_str = "XWins"
O_result_str = "OLost"
elif TTT == "O":
X_result_str = "XLost"
O_result_str = "OWins"
elif TTT == "K": # tie
X_result_str = "Draw"
O_result_str = "Draw"

Label2.place(x=300, y=200)

# Ensure PlayerX and PlayerO are available — fallback to
Player1/Player2 or Player/A "AI"
if PlayerX == "":
try:
PlayerX = Player1
except Exception:
PlayerX = Player # for AI mode
if PlayerO == "":
try:
PlayerO = Player2
except Exception:
PlayerO = "AI"

# Call SAVE_USER_INFO with the proper parameters (two
player entries)
try:
# Each entry: (player_name, side, result_string)
save_list = [(PlayerX, "X", X_result_str), (PlayerO, "O",
O_result_str)]
SAVE_USER_INFO(save_list)
except Exception as e:
print("Error saving score to DB:", e)

def BACK():
Window.destroy()
Home_Screen()

exit_button = Button(Window, bg="#f7f779", padx=15,

pady=10, text="EXIT",

font=('Arial', 20, 'bold'), command=BACK)

exit_button.place(x=1050, y=550)
reset()

Home_Screen()

# ---------------- DATABASE PART ----------------
def MySQL_Python_Connect():
"""
Returns (connection, cursor).
Ensures database and SCORE_TABLE exist.
"""
# change if you wish
try:
# connect to server (no DB specified)
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Ramana@123",
database="TICTACTOE",
autocommit=False
)
except Exception as e:
# fail early with helpful message
raise RuntimeError("Could not connect to MySQL server: "
+ str(e))

mycursor = mydb.cursor()

# create database if not exists and use it
try:
mycursor.execute("CREATE DATABASE IF NOT EXISTS
TICTACTOE;")
mydb.database = "TICTACTOE"
except Exception as e:
raise RuntimeError("Could not create/use database: " +
str(e))

# create table if not exists
create_table_sql = """
CREATE TABLE IF NOT EXISTS SCORE_TABLE (
NAME VARCHAR(255) PRIMARY KEY,
TOTAL_MATCHES INT DEFAULT 0,
PLAYED_AS_X INT DEFAULT 0,
PLAYED_AS_O INT DEFAULT 0,
TOTAL_WINS INT DEFAULT 0,
WINS_AS_X INT DEFAULT 0,
WINS_AS_O INT DEFAULT 0,
TOTAL_LOST INT DEFAULT 0,
LOST_AS_X INT DEFAULT 0,
LOST_AS_O INT DEFAULT 0,
WIN_LOSE_RATIO DOUBLE DEFAULT 0
);
"""
mycursor.execute(create_table_sql)
mydb.commit()

return mydb, mycursor

def SAVE_USER_INFO(APAJ):
"""
APAJ: list of tuples for the match:
[(player_name, side('X'/'O'), resultString), ...]
Example: [("Alice","X","XWins"), ("Bob","O","OLost")]
This function inserts new rows or updates existing rows by
adding stats for this match.
"""
# defensive
if not APAJ:
print("SAVE_USER_INFO called with empty APAJ; nothing
to save.")
return

mydb, mycursor = MySQL_Python_Connect()

print("DEBUG: Connected to DB. APAJ:", APAJ)

for entry in APAJ:
try:
player_name, side, result = entry
except Exception as e:
print("DEBUG: malformed APAJ entry, skipping:", entry,
e)
continue

# Normalize

player_name = str(player_name).strip()
side = str(side).upper().strip()
result = str(result).strip()

if player_name == "":
print("DEBUG: empty player name, skipping entry:",
entry)
continue

# Stats for this single match
played_as_x = 1 if side == 'X' else 0
played_as_o = 1 if side == 'O' else 0
won_as_x = 0
won_as_o = 0
lost_as_x = 0
lost_as_o = 0
total_matches = 1
total_wins = 0
total_lost = 0

# Interpret result (robust checks)
low = result.lower()
if side == 'X':
if 'xwin' in low or ('win' in low and 'x' in low) or ('wins' in
low and 'x' in low):
won_as_x = 1
total_wins = 1
elif 'xlost' in low or ('lost' in low and 'x' in low):
lost_as_x = 1

total_lost = 1
elif 'draw' in low or 'tie' in low:
pass
elif side == 'O':
if 'owin' in low or ('win' in low and 'o' in low) or ('wins' in
low and 'o' in low):
won_as_o = 1
total_wins = 1
elif 'olost' in low or ('lost' in low and 'o' in low):
lost_as_o = 1
total_lost = 1
elif 'draw' in low or 'tie' in low:
pass

# Check if player exists
try:
mycursor.execute("SELECT NAME, TOTAL_MATCHES,
PLAYED_AS_X, PLAYED_AS_O, TOTAL_WINS, WINS_AS_X,
WINS_AS_O, TOTAL_LOST, LOST_AS_X, LOST_AS_O FROM
SCORE_TABLE WHERE NAME = %s", (player_name,))
row = mycursor.fetchone()
except Exception as e:
print("DB select error for", player_name, e)
continue

if row is None:
# Insert a new row
insert_sql = """
INSERT INTO SCORE_TABLE

(NAME, TOTAL_MATCHES, PLAYED_AS_X,
PLAYED_AS_O, TOTAL_WINS, WINS_AS_X, WINS_AS_O,
TOTAL_LOST, LOST_AS_X, LOST_AS_O, WIN_LOSE_RATIO)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
wins_x = won_as_x
wins_o = won_as_o
lost_x = lost_as_x
lost_o = lost_as_o
total_wins_val = total_wins
total_lost_val = total_lost
played_x_val = played_as_x
played_o_val = played_as_o
total_matches_val = total_matches

win_lose_ratio = (total_wins_val / total_lost_val) if
total_lost_val != 0 else float(total_wins_val)

try:
mycursor.execute(insert_sql, (player_name,

total_matches_val, played_x_val, played_o_val, total_wins_val,
wins_x, wins_o, total_lost_val, lost_x, lost_o, win_lose_ratio))

mydb.commit()
print(f"DEBUG: Inserted new player {player_name}")
except Exception as e:
print("DB insert error for", player_name, e)
mydb.rollback()
continue
else:

# Update existing player by adding this match's stats
# row fields: NAME, TOTAL_MATCHES, PLAYED_AS_X,
PLAYED_AS_O, TOTAL_WINS, WINS_AS_X, WINS_AS_O,
TOTAL_LOST, LOST_AS_X, LOST_AS_O
_, cur_total_matches, cur_played_as_x,
cur_played_as_x, cur_total_wins, cur_wins_as_x,
cur_wins_as_o, cur_total_lost, cur_lost_as_x, cur_lost_as_o =
row

new_total_matches = cur_total_matches + total_matches
new_played_as_x = cur_played_as_x + played_as_x
new_played_as_o = cur_played_as_o + played_as_o
new_total_wins = cur_total_wins + total_wins
new_wins_as_x = cur_wins_as_x + won_as_x
new_wins_as_o = cur_wins_as_o + won_as_o
new_total_lost = cur_total_lost + total_lost
new_lost_as_x = cur_lost_as_x + lost_as_x
new_lost_as_o = cur_lost_as_o + lost_as_o

if new_total_lost != 0:
new_ratio = new_total_wins / new_total_lost
else:
new_ratio = float(new_total_wins)

update_sql = """
UPDATE SCORE_TABLE
SET TOTAL_MATCHES = %s,
PLAYED_AS_X = %s,
PLAYED_AS_O = %s,

TOTAL_WINS = %s,
WINS_AS_X = %s,
WINS_AS_O = %s,
TOTAL_LOST = %s,
LOST_AS_X = %s,
LOST_AS_O = %s,
WIN_LOSE_RATIO = %s
WHERE NAME = %s
"""
try:
mycursor.execute(update_sql, (
new_total_matches,
new_played_as_x,
new_played_as_o,
new_total_wins,
new_wins_as_x,
new_wins_as_o,
new_total_lost,
new_lost_as_x,
new_lost_as_o,
new_ratio,
player_name
))
mydb.commit()
print(f"DEBUG: Updated player {player_name}")
except Exception as e:
print("DB update error for", player_name, e)
mydb.rollback()
continue

# final debug
try:
print("DEBUG: SAVE_USER_INFO finished, closing DB
connection.")
mycursor.close()
mydb.close()
except:
pass

# END OF FILE