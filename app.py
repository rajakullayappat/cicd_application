# Python file (app.py)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>Deployment of Application using GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="hhttps://github.com/rajakullayappat/cicd_application/blob/main/itsworking.jpeg?raw=true">
</center>
</body>
</html>
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
