from flask import Flask
from pyhelm.repo import from_repo
from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller    
app = Flask(__name__)

@app.route("/")
def hello():
   return "hello world"

@app.route("/enter")
def deploy():
   chart_path = from_repo('https://kubernetes-charts.storage.googleapis.com/', 'mariadb')
   #print(chart_path)
   chart = ChartBuilder({'name': 'mongodb', 'source': {'type': 'directory', 'location': '/tmp/pyhelm-dMLypC/mariadb'}})
   tiller_ins = Tiller('10.102.187.89', '44134') 
   tiller_ins.install_release(chart.get_helm_chart(), dry_run=False, namespace='default') 
   return "hello kuber"
if __name__ == '__main__':
  app.run(host='0.0.0.0',port=33000,debug='True')
