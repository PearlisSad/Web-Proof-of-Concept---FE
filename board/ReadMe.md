Activate venv if not already active

Windows run: 

venv\Scripts\activate

To run(IN ROOT FOLDER):

python -m flask --app board run --port 8000 --debug
or
python -m board


To add pages:
in posts.py add a route "/<page name>"
create html file in /pages