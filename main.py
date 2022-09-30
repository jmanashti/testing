import os
import pymssql
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    print('hello table')
    try:
        #import pymssql
        conn = pymssql.connect(host=r'35.226.107.0',user=r'sqlserver',password=r'!Rankworks',database='rankworksgoogle')
        cursor = conn.cursor()
        cursor.execute('SELECT  (select count(*) from dbo.Twitter ) AS Total_Twitter_ID,  (select count(*) from dbo.Twitter_Metrics ) AS Total_Twitter_Metrics')
        data = cursor.fetchall()
        test='Total_Twitter_ID='+str(data[0][0])
        test=test +'    Total_Twitter_Metrics='+ str(data[0][1])
         #['Total_Twitter_Metrics=',srt(data[0][1])]]
        cursor.close()
        conn.close()
    except:
        print('error loading data')
        test='error loading data'
    return test




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
#%%
