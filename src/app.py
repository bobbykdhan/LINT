from flask import Flask, request, render_template
import machine_request
app = Flask(__name__)

validBuildingNames = ["Gleason", "Sol", "Gibson", "Ellingson"]

@app.route("/ticket", methods=["GET", "POST"])
async def ticket():
    if request.method == "GET":
        building = request.args.get('building')
        machineNum = request.args.get('machineNum')

        if building in validBuildingNames:
            if int(machineNum) < 40:
                report_info = ReportInfo(building, "_", "Washer", machineNum, "_")
                machine_request.api_request(report_info)

        return render_template("ticket.html", building=building, machineNum=machineNum)
    else:
        try:
            return "Thanks!", 200
        except ValueError as value_err:
            return str(value_err), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
