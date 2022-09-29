import os
import pymssql
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    conn = pymssql.connect(host=r'35.226.107.0',user=r'sqlserver',password=r'!Rankworks',database='rankworksgoogle')
    Engagement_Rates='1';UI_Score='1';Last_Update=str(date.today())
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM dbo.Twitter')
    data = cursor.fetchall()
    print('Number of Twitter Id Collected=',data)
    conn.close()
    return data




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
#%%
