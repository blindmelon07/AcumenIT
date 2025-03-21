from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
   greet_urls = url_for("greet"),
   wave_url = url_for("wave", name="bryan")
   dance_url = url_for("dance")

   html = f"""
   <a href="{greet_urls}">Greet</a>
   <a href="{wave_url}">Wave</a>
   <a href="{dance_url}">Dance</a>
   """
   return html
    



# @app.route('/')
# def hello_world():
#     # 1 / 0
#     return 'Hello, World! mother dipota ka gud <br /> i am bryan'


@app.route("/wave/<name>")
def wave(name):
    name = name.capitalize()
    return f"I am waving at {name}"
@app.route("/dance")
@app.route("/dance/<int:dance_no>")
def dance(dance_no=0):
        dances = ["waltz", "tango", "foxtrot", "cha cha", "samba", "rumba"]
        dance = dances[dance_no]
        html = f"<h1>Let's dance {dance}</h1>"
        return html


# @app.route("/profile/<name>/get/<int:index>")
# def get_profile(name, index):
#     return f"Hello {name}, your index is {index}"

    # $ flask --app exercise64 run
    # $ flask --app exercise64 run --debug
    # $ flask --app exercise64 run --host=0.0.0.0

