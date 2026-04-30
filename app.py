import pandas as pd
import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS

scaler = pickle.load(open('components/scaler.pkl', 'rb'))
model = pickle.load(open('components/xgb-model.pkl', 'rb'))

app = Flask(__name__)
CORS(app) # enable the react front app to access this API

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/endpoint', methods=['POST'])
def handle_json():
    data = request.get_json()

    # persoItems = float(data.get('persoItems'))
    # assetQuality = float(data.get('assetQuality'))
    # arrearRiskScore = float(data.get('arrearRiskScore'))
    # loanAccount = float(data.get('loanAccount'))
    # creditDiversity = float(data.get('assetQuality'))
    # productCount = float(data.get('productCount'))
    # activityScore = float(data.get('activityScore'))
    # age = float(data.get('age'))
    # educationLevel = float(data.get('educationLevel'))
    # loanDuration = float(data.get('loanDuration'))
    # loanAmount = float(data.get('loanAmount'))
    # workingExperience = float(data.get('workingExperience'))
    # jobTitle = float(data.get('jobTitle'))
    # durationCompany = float(data.get('durationCompany'))
    # industry = float(data.get('industry'))
    # secondaryType = float(data.get('secondaryType'))
    # income = float(data.get('income'))
    # maritalStatus = float(data.get('maritalStatus'))
    # writesOff = float(data.get('writesOff'))
    # arrears = float(data.get('arrears'))
    # lastArrears = float(data.get('lastArrears'))
    # cardHistory = float(data.get('cardHistory'))
    # creditUtilisation = float(data.get('creditUtilisation'))
    # creditLastYear = float(data.get('creditLastYear'))
    # purchaseLastYear = float(data.get('purchaseLastYear'))
    # loanLastYear = float(data.get('loanLastYear'))
    # debtRatio = float(data.get('debtRatio'))
    # emis = float(data.get('emis'))

    data_dico = {
        'Total_Personal_Items': float(data.get('persoItems')),
        'Asset_Quality': float(data.get('assetQuality')),
        'Arrears_Risk_Score': float(data.get('arrearRiskScore')),
        'Total_Loan_Accounts': float(data.get('loanAccount')),
        'Credit_Diversity': float(data.get('creditDiversity')),
        'Credit_Product_Count': float(data.get('productCount')),
        'Credit_Activity_Score': float(data.get('activityScore')),
        'Age': float(data.get('age')),
        'Education_Level': float(data.get('educationLevel')),
        'Loan_Duration_Years': float(data.get('loanDuration')),
        'Loan_Amount': float(data.get('loanAmount')),
        'Working_Experience': float(data.get('workingExperience')),
        'Current_Job_Title': float(data.get('jobTitle')),
        'Duration_Current_Company': float(data.get('durationCompany')),
        'Industry': float(data.get('industry')),
        'Employment_Secondary_Type': float(data.get('secondaryType')),
        'Disposable_Income': float(data.get('income')),
        'Marital_Status': float(data.get('maritalStatus')),
        'Write_Offs': float(data.get('writesOff')),
        'Arrears': float(data.get('arrears')),
        'Last_Year_Arrears': float(data.get('lastArrears')),
        'Credit_Card_History_Hire_Purchase': float(data.get('cardHistory')),
        'Credit_Utilisation': float(data.get('creditUtilisation')),
        'Credit_Cards_Last_Year': float(data.get('creditLastYear')),
        'Hire_Purchase_Last_Year': float(data.get('purchaseLastYear')),
        'Loans_Last_Year': float(data.get('loanLastYear')),
        'Debt_Ratio': float(data.get('debtRatio')),
        'Active_EMIs': float(data.get('emis'))
    }

    data_pd = pd.DataFrame(data_dico, index=[0])

    scaled_data = scaler.transform(data_pd)
    risk_level = model.predict(scaled_data)
    
    return jsonify({"received": risk_level[0].item()})


# ensures the development server only starts if you run the script directly,
# preventing it from launching accidentally if the file is imported elsewhere
if __name__ == "__main__":
    app.run(debug=True, port=5000)
