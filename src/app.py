from flask import Flask, request, render_template
from machine_request import ReportInfo, api_request
app = Flask(__name__)

validBuildingNames = ["Gleason", "Sol", "Gibson", "Ellingson"]

@app.route("/ticket", methods=["GET", "POST"])
async def ticket():
    if request.method == "GET":
        building = request.args.get('b')
        machineNum = request.args.get('m')

        return render_template("ticket.html", building=building, machineNum=machineNum)
    else:
        try:
            building = request.form.get('building')
            machineNum = request.form.get('machineNum')
            issue = request.form.get('issue')

            if building in validBuildingNames:
                if int(machineNum) < 40:
                    report = ReportInfo(building, machineNum, issue)
                    api_request(report)

            return "Thanks!", 200
        except ValueError as value_err:
            return str(value_err), 400




@app.route('/debug/<path:url_param>')
async def get_url(url_param):
    driver = create_driver()
    print("Driver Created")
    print("Submitting report for: debugging")
    make_request(driver, ReportInfo(url_param, "-","-"), True)
    driver.quit()
    return f'The URL parameter is: {url_param}'




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
