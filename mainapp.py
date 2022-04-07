from flask import Flask, render_template, send_from_directory, request
from logging import FileHandler, WARNING
from flask import abort

app = Flask(__name__)
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == "POST":
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        source = request.form.get("source")
        date = year+month+day
        return send_from_directory(f"./datasheets/{source}_Api", date+"_"+source+"_All_Data.csv", as_attachment=True)
    return render_template("index.html")


@app.route('/googleadmob/<path:path>', methods=['GET'])
def fetch_admob(path):
    try:
        return send_from_directory("./datasheets/Google_Admob_Api/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/googleads/<path:path>', methods=['GET'])
def fetch_ads(path):
    try:
        return send_from_directory("./datasheets/Google_Ads_Api/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/facebookads/<path:path>', methods=['GET'])
def fetch_facebook(path):
    try:
        return send_from_directory("./datasheets/Facebook_Ads_Api/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/googleanalytics/<path:path>', methods=['GET'])
def fetch_analytics(path):
    try:
        return send_from_directory("./datasheets/Google_Analytics_Api/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/combinedbyapp/<path:path>', methods=['GET'])
def combine_by_app(path):
    print(path)
    try:
        return send_from_directory("./datasheets/Combined_Data_By_App/", path, as_attachment=True)
    except FileNotFoundError:
        print("File not found")
        abort(404)


@app.route('/combinedbycountry/<path:path>', methods=['GET'])
def combine_by_country(path):
    try:
        return send_from_directory("./datasheets/Combined_Data_By_Country/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/playconsoledata/<path:path>', methods=['GET'])
def playconsole_by_country(path):
    try:
        return send_from_directory("./datasheets/PlayConsole_Api/", path, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/combinedappdatabydate/<path:path>', methods=['GET'])
def fetch_app_by_date(path):
    try:
        return send_from_directory("./datasheets/Combined_Data_By_App/", path, as_attachment=True)
    except:
        abort(404)


@app.route('/combinedcountrydatabydate/<path:path>', methods=['GET'])
def fetch_country_by_date(path):
    try:
        return send_from_directory("./datasheets/Combined_Data_By_Country/", path, as_attachment=True)
    except:
        abort(404)


@app.route('/combinedalldatabydate/<path:path>', methods=['GET'])
def all_data_by_date(path):
    try:
        return send_from_directory("./datasheets/Combined_Data_By_Date/", path, as_attachment=True)
    except:
        abort(404)


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1')
