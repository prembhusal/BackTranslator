from flask import Flask, render_template, request
import sqlite3 as sql
from seqTranslate import ntSeqInGCrange

app = Flask(__name__)

database = "./testData.db"

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/addrecord',methods = ['POST', 'GET'])
def addrecord():
   if request.method == 'POST':
      try:
         seq = request.form['seq']#input nucleotide sequence
         gcRange = request.form['gc'] # gc range eg. 40-60
         
         
         with sql.connect(database) as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS inputseq (aaseq TEXT PRIMARY KEY NOT NULL)")
            print "Table created successfully"
            # check in inputseq table if entry already exists
            record = cur.execute("SELECT * FROM  inputseq WHERE aaseq='%s'" %seq ).fetchone()
            

            if record is None:
               #insert amino acid sequence into the inputseq table
               cur.execute("INSERT INTO inputseq (aaseq) VALUES (?)", (seq,))

               #convert amino acid and get the one having specified gc range
               ntSeq,gc = ntSeqInGCrange(seq,gcRange)
               print ntSeq,gc

               #insert amino acid sequence and  nucleotide sequence into outputSequence table 
               cur.execute("CREATE TABLE IF NOT EXISTS outputSequence (aaseq TEXT PRIMARY KEY NOT NULL, ntseq TEXT NOT NULL)")
               
               cur.execute("INSERT INTO outputSequence (aaseq,ntseq) VALUES (?,?)", (seq,ntSeq))
               
               con.commit()
               msg = " Nucleotide Sequence : "+ntSeq+", GC content: " +str(gc)
            else:
               #display warning message
               msg = " record already exists"

            #con.commit()

      except:
         con.rollback()
         msg = "error "
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
@app.route('/showtable')
def list():
   con = sql.connect(database)
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from outputSequence")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')
