from flask import Flask, render_template, request, jsonify
import test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reverse_name', methods=['POST'])
def reverse_name():
    data = request.json
    password = data.get('password', '')
    username = data.get('username', '')
    rank, feedback1, feedback2, feedback3, feedback4, feedback5, indicators, info_list = test.main(password, username)  # Reverse the name
    response = {"rank": rank, "feedback1": feedback1, "feedback2": feedback2, "feedback3": feedback3,
                "feedback4": feedback4, "feedback5": feedback5, "indicators": indicators, "info_list":info_list}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)