import clearbit, requests

from flask import Flask,render_template,request

clearbit.key = ''  # your api key goes here
app = Flask(__name__)


def scrap_info(company):
    try:
        response = clearbit.Company.find(domain=company, stream=True)
    except:
        response= None

    url = "https://prospector.clearbit.com/v1/people/search&domain={}".format(company)

    try:
        people = clearbit.Prospector.search(domain=company)['results']
    except:
        people= None

    Keypeople = []
    try:
        Name = response['name']
    except:
        Name = 'NA'

    try:
        Address = response['location']
    except:
        Address = 'NA'

    try:
        Phoneno = response['phone']
    except:
        Phoneno = 'NA'

    try:
        for person in people:
            Keypeople.append(person['name']['fullName'])

    except:
        Keypeople = 'NA'

    return {'Name': Name, 'Address': Address, 'Phone no': Phoneno, 'Key people': Keypeople}


@app.route('/company', methods = ['POST', 'GET'])
def scrapper():
    if request.method == 'POST':
        company = request.form['cname']
        detail= scrap_info(company)
        return render_template('result.html', detail=detail)
    else:

        return render_template('company.html')


#print(datas)

# main driver function
if __name__ == '__main__':
	app.run(debug=True)
