from flask import Flask, request, render_template,jsonify
import api



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('playlist.html')

@app.route('/player',methods=['GET', 'POST'])
def player():
    return render_template('player.html')


historylist=api.get_history(17)
recommendlist=api.get_results(17)

#get all history
@app.route('/post0', methods=['GET','POST'])
def Get_history_0():
    # get login information
    useridinput = request.form['userid']
    result = {
        "output": historylist[0]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post1', methods=['GET','POST'])
def Get_history_1():
    result = {
        "output": historylist[1]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post2', methods=['GET','POST'])
def Get_history_2():
    result = {
        "output": historylist[2]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post3', methods=['GET','POST'])
def Get_history_3():
    result = {
        "output": historylist[3]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post4', methods=['GET','POST'])
def Get_history_4():
    result = {
        "output": historylist[4]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post5', methods=['GET','POST'])
def Get_history_5():
    result = {
        "output": historylist[5]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post6', methods=['GET','POST'])
def Get_history_6():
    result = {
        "output": historylist[6]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post7', methods=['GET','POST'])
def Get_history_7():
    result = {
        "output": historylist[7]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post8', methods=['GET','POST'])
def Get_history_8():
    result = {
        "output": historylist[8]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/post9', methods=['GET','POST'])
def Get_history_9():
    result = {
        "output": historylist[9]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

#get all recommendations
@app.route('/postrec0', methods=['GET','POST'])
def Get_recommend_0():
    # get login information
    useridinput = request.form['userid']
    result = {
        "output": recommendlist[0]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec1', methods=['GET','POST'])
def Get_recommend_1():
    result = {
        "output": recommendlist[1]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec2', methods=['GET','POST'])
def Get_recommend_2():
    result = {
        "output": recommendlist[2]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec3', methods=['GET','POST'])
def Get_recommend_3():
    result = {
        "output": recommendlist[3]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec4', methods=['GET','POST'])
def Get_recommend_4():
    result = {
        "output": recommendlist[4]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec5', methods=['GET','POST'])
def Get_recommend_5():
    result = {
        "output": recommendlist[5]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec6', methods=['GET','POST'])
def Get_recommend_6():
    result = {
        "output": recommendlist[6]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec7', methods=['GET','POST'])
def Get_recommend_7():
    result = {
        "output": recommendlist[7]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec8', methods=['GET','POST'])
def Get_recommend_8():
    result = {
        "output": recommendlist[8]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/postrec9', methods=['GET','POST'])
def Get_recommend_9():
    result = {
        "output": recommendlist[9]
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
