from flask import Flask, render_template, make_response, redirect,session,request
import time
from flask_socketio import SocketIO, send, emit
import os
from random import randint

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key="hello@123"

@app.route('/')
def home():
    return "<center><h1>Welcome to Just Google It</h1></center>"

session_id = 0
@app.route('/<user>')
def index(user):
    global user_data
    if user=="Host":
        user_data = {}
        return render_template('index.html', name=user)
    else:
        return render_template('404.html')

@app.route('/join/member/<member_id>')
def start(member_id):

    current_member = None
    for key, value in user_data.items(): 
        if member_id == str(value): 
            current_member = key
    return render_template("index.html",name="user",member=current_member)


@app.route('/join/<id>')
def user(id):
 
    if(session_id == 0):
        return render_template('404.html')
    elif(id==str(session_id)):
        return render_template("index.html",name="join")
    else:
        return render_template('404.html')

users_dict ={}

@socketio.on("password")
def handlePassword(data):
    if(data=="hello@123"):
        global session_id,initial_member_id
        session_id = randint(100000,999999)
        initial_member_id = randint(100000,999999)
        data = session_id
    else:
        data="Invalid credentals"
    emit("new_password",data,broadcast=True)

initial_member_id = 0
user_data = {}
@socketio.on("username")
def handleUsername(data):
    global session_id,initial_member_id
    print(user_data)
    if data not in user_data.keys():
        user_data[data] = initial_member_id
        initial_member_id = initial_member_id+1
        emit("append_user",data,broadcast = True)
        time.sleep(1)
    emit("new_username",user_data[data])
        
        

@socketio.on("startgame")
def startgame(data):
    global session_id
    session_id = 0
    emit("new_game",data,broadcast=True)

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)

@socketio.on("reset")
def reset(data):
    emit("new_reset",data,broadcast=True)
    

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5004)

#-----------------------------------------------------------------------------

'''
teams = ['Tech_keys--01', 
            'wolfs--02', 
            'Idealet--03', 
            'Friends--04', 
            'Trio--05', 
            'Power_Riot--06', 
            'TechHeads--07',
            'Three_idiots--08',
            'Bale_Puri--09',
            'HP--10',
            'Leuca_Legends--11',
            'BEAUTIFUL_DATA--12',
            'Jigirthanda_dhost--13',
            'Chumma_Kizhi--14',
            'Simple--15',
            'Archons--16',
            'Candy--17',
            'Code_breakers--18',
            'Petta_parak--19',
            'StarBois--20',
            'NGK--21',
            'Wolf_Boyz--22',
            'Why_nots--23',
            'Team_Solo--24',
            'Team_Fore--25',
            'The_Alpha--26',
            'Fab_4--27',
            'Skanda_Gurunathan_R--28',
            'Find_out--29',
            'Rule_Breakers--30',
            'Jubilee--31',
            'Pirates--32',
            'TEAM_MECH--33',
            'Phoenix--34',
            'Team_MECHANICAL--35',
            'RUPESH_KUMAR_S--36',
            'The_Inevitables--37',
            'Team_Valient--38',
            'Night_Riders--39',
            'Error404--40',
            'Msec_girls--41']
host = 'Just-Google-It-Buzzer-Host'

<tr>
                        <td><center>02 - wolfs</center></td>
                        <td><center><button id="add" value="+" onclick="add_1()">+</button></center></td>
                        <td><center><span id="score_1">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>03 - Idealet</center></td>
                            <td><center><button id="add" value="+" onclick="add_2()">+</button></center></td>
                            <td><center><span id="score_2">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>04 - Friends</center></td>
                            <td><center><button id="add" value="+" onclick="add_3()">+</button></center></td>
                            <td><center><span id="score_3">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>05 - Trio</center></td>
                            <td><center><button id="add" value="+" onclick="add_4()">+</button></center></td>
                            <td><center><span id="score_4">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>06 - Power Riot</center></td>
                            <td><center><button id="add" value="+" onclick="add_5()">+</button></center></td>
                            <td><center><span id="score_5">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>07 - TechHeads</center></td>
                            <td><center><button id="add" value="+" onclick="add_6()">+</button></center></td>
                            <td><center><span id="score_6">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>08 - 3 idiots</center></td>
                            <td><center><button id="add" value="+" onclick="add_7()">+</button></center></td>
                            <td><center><span id="score_7">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>09 - Bale Puri</center></td>
                            <td><center><button id="add" value="+" onclick="add_8()">+</button></center></td>
                            <td><center><span id="score_8">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>10 - HP</center></td>
                            <td><center><button id="add" value="+" onclick="add_9()">+</button></center></td>
                            <td><center><span id="score_9">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>11 - Leuca Legends</center></td>
                            <td><center><button id="add" value="+" onclick="add_10()">+</button></center></td>
                            <td><center><span id="score_10">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>12 - BEAUTIFUL DATA</center></td>
                            <td><center><button id="add" value="+" onclick="add_11()">+</button></center></td>
                            <td><center><span id="score_11">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>13 - Jigirthanda dhost</td>
                            <td><center><button id="add" value="+" onclick="add_12()">+</button></center></td>
                            <td><center><span id="score_12">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>14 - Chumma Kizhi</center></td>
                            <td><center><button id="add" value="+" onclick="add_13()">+</button></center></td>
                            <td><center><span id="score_13">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>15 - Simple</center></td>
                            <td><center><button id="add" value="+" onclick="add_14()">+</button></center></td>
                            <td><center><span id="score_14">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>16 - Archons</center></td>
                            <td><center><button id="add" value="+" onclick="add_15()">+</button></center></td>
                            <td><center><span id="score_15">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>17 - Candy</center></td>
                            <td><center><button id="add" value="+" onclick="add_16()">+</button></center></td>
                            <td><center><span id="score_16">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>18 - Code breakers</center></td>
                            <td><center><button id="add" value="+" onclick="add_17()">+</button></center></td>
                            <td><center><span id="score_17">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>19 - Petta parak</center></td>
                            <td><center><button id="add" value="+" onclick="add_18()">+</button></center></td>
                            <td><center><span id="score_18">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>20 - StarBois</center></td>
                            <td><center><button id="add" value="+" onclick="add_19()">+</button></center></td>
                            <td><center><span id="score_19">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>21 - NGK</center></td>
                            <td><center><button id="add" value="+" onclick="add_20()">+</button></center></td>
                            <td><center><span id="score_20">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>22 - Wolf Boyz</center></td>
                            <td><center><button id="add" value="+" onclick="add_21()">+</button></center></td>
                            <td><center><span id="score_21">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>23 - Why nots</center></td>
                            <td><center><button id="add" value="+" onclick="add_22()">+</button></center></td>
                            <td><center><span id="score_22">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>24 - Team Solo</center></td>
                            <td><center><button id="add" value="+" onclick="add_23()">+</button></center></td>
                            <td><center><span id="score_23">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>25 - Team Fore</center></td>
                            <td><center><button id="add" value="+" onclick="add_24()">+</button></center></td>
                            <td><center><span id="score_24">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>26 - The Alpha</center></td>
                            <td><center><button id="add" value="+" onclick="add_25()">+</button></center></td>
                            <td><center><span id="score_25">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>27 - Fab 4</center></td>
                            <td><center><button id="add" value="+" onclick="add_26()">+</button></center></td>
                            <td><center><span id="score_26">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>28 - Skanda Gurunathan R</center></td>
                            <td><center><button id="add" value="+" onclick="add_27()">+</button></center></td>
                            <td><center><span id="score_27">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>29 - Find out</center></td>
                            <td><center><button id="add" value="+" onclick="add_28()">+</button></center></td>
                            <td><center><span id="score_28">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>30 - Rule Breakers</center></td>
                            <td><center><button id="add" value="+" onclick="add_29()">+</button></center></td>
                            <td><center><span id="score_29">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>31 - Jubilee</center></td>
                            <td><center><button id="add" value="+" onclick="add_30()">+</button></center></td>
                            <td><center><span id="score_30">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>32 - Pirates</center></td>
                            <td><center><button id="add" value="+" onclick="add_31()">+</button></center></td>
                            <td><center><span id="score_31">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>33 - TEAM MECH</center></td>
                            <td><center><button id="add" value="+" onclick="add_32()">+</button></center></td>
                            <td><center><span id="score_32">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>34 - Phoenix</center></td>
                            <td><center><button id="add" value="+" onclick="add_33()">+</button></center></td>
                            <td><center><span id="score_33">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>35 - Team MECHANICAL</center></td>
                            <td><center><button id="add" value="+" onclick="add_34()">+</button></center></td>
                            <td><center><span id="score_34">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>36 - RUPESH KUMAR S</center></td>
                            <td><center><button id="add" value="+" onclick="add_35()">+</button></center></td>
                            <td><center><span id="score_35">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>37 - The Inevitables</center></td>
                            <td><center><button id="add" value="+" onclick="add_36()">+</button></center></td>
                            <td><center><span id="score_36">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>38 - Team Valient</center></td>
                            <td><center><button id="add" value="+" onclick="add_37()">+</button></center></td>
                            <td><center><span id="score_37">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>39 - Night Riders</center></td>
                            <td><center><button id="add" value="+" onclick="add_38()">+</button></center></td>
                            <td><center><span id="score_38">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>40 - Error404</center></td>
                            <td><center><button id="add" value="+" onclick="add_39()">+</button></center></td>
                            <td><center><span id="score_39">0</span></center></td>
                        </tr>
                        <tr>
                            <td><center>41 - Msec girls</center></td>
                            <td><center><button id="add" value="+" onclick="add_40()">+</button></center></td>
                            <td><center><span id="score_40">0</span></center></td>
                        </tr>
'''