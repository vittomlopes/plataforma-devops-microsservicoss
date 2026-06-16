@app.route("/user-info")
def user_info():
    response = requests.get("http://user-service:5000/users")
    return response.json()
