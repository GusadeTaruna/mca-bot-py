import json
from flask import Flask, request, make_response, jsonify
import mysql.connector
from mysql.connector import Error
import datetime
import calendar

app = Flask(__name__)
if __name__ == '__main__':
    app.run()

@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the Banking Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('result').get('action')
    except AttributeError:
        return 'json error'

    if action == 'percakpan':
        res = 'Webnya mau'

    return make_response(jsonify({"speech": res}))


