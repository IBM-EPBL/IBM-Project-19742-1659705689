from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas
import os
app=Flask (__name__)
model = pickle.load(open ('Linear_Regression.pkl', 'rb'))  
@app.route('/') # rendering the html template 
def form1(): 
    return render_template('form1.html')
@app.route('/prediction',methods=["POST","GET"])  


@app.route('/predict', methods = [ "POST","GET"])# route to show the predictions in a web UI def 
def predict():
   input_feature=[int(x) for x in request.form.values() ]
    #input_feature = np.transpose(input_feature)
   input_feature=[np.array(input_feature)]
   print(input_feature)
   names = ['GRE SCORE', 'TOFEL SCORE', 'SOP SCORE', 'LOR SCORE', 'CGPA', 'RESEARCH PAPER', 'UNIVERSITY RANK']
   data = pandas.DataFrame(input_feature, columns=names) 
   print(data)
   #data_scaled = scale.fit_transform(data) #data = pandas.DataFrame(, columns=names)
   # predictions using the loaded model file prediction=model.predict(data)
   prediction=model.predict(data)
   print (prediction)
   prediction = int(prediction)
   print(type(prediction))
   if (prediction >= 60):
      return render_template("sucess.html", prediction_text = prediction)
   else:
    #showing the prediction results in a UI
      return render_template("failure.html",  prediction_text = prediction)

  
    
  
if __name__=="__main__":
# app.run(host='0.0.0.0', port=8000, debug=True) 
  port=int(os.environ.get('PORT',5000)) 
  app.run(debug=False)