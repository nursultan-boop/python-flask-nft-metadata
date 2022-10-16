from flask import Flask, request
import requests
import psycopg2
# create the Flask app
app = Flask(__name__)

def check_in_db(address):
    conn = psycopg2.connect("dbname=nft_py user=postgres password='123'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM nfts where nft_address='"+address+"'")
    if(cur.rowcount==0):
        return False
    return True

@app.route('/query-example')
def query_example():
    return 'Query String Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'
    
@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        returnValue=""
        address = request.form.get('address')
        if(check_in_db(address)):
            conn = psycopg2.connect("dbname=nft_py user=postgres password='123'")
            cur = conn.cursor()
            cur.execute("SELECT nft_metadata FROM nfts where nft_address='"+address+"'")
            records = cur.fetchall()
            returnValue=records[0][0]
        else:            
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address)
            headers = {
                "accept": "application/json",
                "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z"
            }
            returnValue = requests.get(url, headers=headers).text
            conn = psycopg2.connect("dbname=nft_py user=postgres password='123'")
            cur = conn.cursor()
            cur.execute("insert into nfts(nft_address,nft_metadata) values('{}','{}')".format(address, returnValue))
            conn.commit()
        return '''
                <h1>{}</h1>
                  '''.format(returnValue)
    
    # otherwise handle the GET request   
    return '''
           <form method="POST"style="margin: auto; width: 220px; text-align: center;">
               <div><label>address: <input type="text" name="address"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)


