import datetime
import json
import math

import plotly.graph_objects as go
import numpy as np




analysis = {'cylinders': {'0': {'Torque_engine': {'value': 47734.56, 'std': -0.0, 'avg': 47988.11}, 'load': {'value': 31.98, 'std': -0.0, 'avg': 32.07}, 'firing_pressure': {'value': 111.96, 'std': -0.0, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.62, 'std': -0.0, 'avg': 0.62}, 'compression_pressure': {'value': 86.99, 'std': 0.0, 'avg': 86.86}, 'break_power': {'value': 908.48, 'std': 0.0, 'avg': 908.06}, 'imep': {'value': 15.29, 'std': -0.01, 'avg': 15.32}, 'bmep': {'value': 11.38, 'std': 0.01, 'avg': 11.27}, 'injection_timing': {'value': 1.55, 'std': 0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 275.57, 'std': 0.01, 'avg': 272.42}, 'fuel_flow_rate': {'value': 284.71, 'std': 0.01, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '1': {'Torque_engine': {'value': 50055.44, 'std': 0.02, 'avg': 47988.11}, 'load': {'value': 33.43, 'std': 0.02, 'avg': 32.07}, 'firing_pressure': {'value': 112.87, 'std': 0.02, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.65, 'std': 0.02, 'avg': 0.62}, 'compression_pressure': {'value': 87.67, 'std': 0.02, 'avg': 86.86}, 'break_power': {'value': 1069.02, 'std': 0.02, 'avg': 908.06}, 'imep': {'value': 15.43, 'std': 0.02, 'avg': 15.32}, 'bmep': {'value': 11.29, 'std': 0.0, 'avg': 11.27}, 'injection_timing': {'value': 1.54, 'std': 0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 273.46, 'std': -0.0, 'avg': 272.42}, 'fuel_flow_rate': {'value': 286.77, 'std': 0.01, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '2': {'Torque_engine': {'value': 45352.84, 'std': -0.02, 'avg': 47988.11}, 'load': {'value': 30.36, 'std': -0.02, 'avg': 32.07}, 'firing_pressure': {'value': 111.4, 'std': -0.02, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.59, 'std': -0.03, 'avg': 0.62}, 'compression_pressure': {'value': 85.46, 'std': -0.03, 'avg': 86.86}, 'break_power': {'value': 710.25, 'std': -0.02, 'avg': 908.06}, 'imep': {'value': 15.19, 'std': -0.03, 'avg': 15.32}, 'bmep': {'value': 11.36, 'std': 0.01, 'avg': 11.27}, 'injection_timing': {'value': 1.52, 'std': -0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 272.03, 'std': 0.0, 'avg': 272.42}, 'fuel_flow_rate': {'value': 278.07, 'std': -0.02, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '3': {'Torque_engine': {'value': 49010.19, 'std': 0.01, 'avg': 47988.11}, 'load': {'value': 33.06, 'std': 0.01, 'avg': 32.07}, 'firing_pressure': {'value': 112.4, 'std': 0.01, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.62, 'std': 0.0, 'avg': 0.62}, 'compression_pressure': {'value': 87.6, 'std': 0.01, 'avg': 86.86}, 'break_power': {'value': 1033.42, 'std': 0.01, 'avg': 908.06}, 'imep': {'value': 15.29, 'std': -0.0, 'avg': 15.32}, 'bmep': {'value': 11.46, 'std': 0.01, 'avg': 11.27}, 'injection_timing': {'value': 1.55, 'std': 0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 277.96, 'std': 0.02, 'avg': 272.42}, 'fuel_flow_rate': {'value': 286.51, 'std': 0.01, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '4': {'Torque_engine': {'value': 49793.36, 'std': 0.02, 'avg': 47988.11}, 'load': {'value': 33.26, 'std': 0.02, 'avg': 32.07}, 'firing_pressure': {'value': 112.55, 'std': 0.01, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.64, 'std': 0.01, 'avg': 0.62}, 'compression_pressure': {'value': 87.12, 'std': 0.0, 'avg': 86.86}, 'break_power': {'value': 1018.96, 'std': 0.01, 'avg': 908.06}, 'imep': {'value': 15.39, 'std': 0.01, 'avg': 15.32}, 'bmep': {'value': 11.4, 'std': 0.01, 'avg': 11.27}, 'injection_timing': {'value': 1.53, 'std': 0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 275.44, 'std': 0.01, 'avg': 272.42}, 'fuel_flow_rate': {'value': 284.67, 'std': 0.01, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '5': {'Torque_engine': {'value': 49777.68, 'std': 0.02, 'avg': 47988.11}, 'load': {'value': 33.35, 'std': 0.02, 'avg': 32.07}, 'firing_pressure': {'value': 113.03, 'std': 0.02, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.64, 'std': 0.01, 'avg': 0.62}, 'compression_pressure': {'value': 87.27, 'std': 0.01, 'avg': 86.86}, 'break_power': {'value': 1050.71, 'std': 0.02, 'avg': 908.06}, 'imep': {'value': 15.4, 'std': 0.02, 'avg': 15.32}, 'bmep': {'value': 11.19, 'std': 0.0, 'avg': 11.27}, 'injection_timing': {'value': 1.52, 'std': -0.0, 'avg': 1.53}, 'exhaust_temperature': {'value': 269.53, 'std': -0.0, 'avg': 272.42}, 'fuel_flow_rate': {'value': 284.24, 'std': 0.0, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '6': {'Torque_engine': {'value': 45541.72, 'std': -0.02, 'avg': 47988.11}, 'load': {'value': 30.16, 'std': -0.03, 'avg': 32.07}, 'firing_pressure': {'value': 111.05, 'std': -0.02, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.62, 'std': -0.0, 'avg': 0.62}, 'compression_pressure': {'value': 86.54, 'std': -0.01, 'avg': 86.86}, 'break_power': {'value': 691.16, 'std': -0.03, 'avg': 908.06}, 'imep': {'value': 15.24, 'std': -0.01, 'avg': 15.32}, 'bmep': {'value': 10.89, 'std': -0.04, 'avg': 11.27}, 'injection_timing': {'value': 1.52, 'std': -0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 265.92, 'std': -0.02, 'avg': 272.42}, 'fuel_flow_rate': {'value': 283.54, 'std': -0.0, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}, '7': {'Torque_engine': {'value': 46639.06, 'std': -0.01, 'avg': 47988.11}, 'load': {'value': 30.97, 'std': -0.02, 'avg': 32.07}, 'firing_pressure': {'value': 111.78, 'std': -0.01, 'avg': 112.13}, 'scavenging_pressure': {'value': 0.62, 'std': -0.01, 'avg': 0.62}, 'compression_pressure': {'value': 86.22, 'std': -0.01, 'avg': 86.86}, 'break_power': {'value': 782.47, 'std': -0.01, 'avg': 908.06}, 'imep': {'value': 15.3, 'std': -0.01, 'avg': 15.32}, 'bmep': {'value': 11.19, 'std': -0.01, 'avg': 11.27}, 'injection_timing': {'value': 1.52, 'std': -0.01, 'avg': 1.53}, 'exhaust_temperature': {'value': 269.48, 'std': -0.01, 'avg': 272.42}, 'fuel_flow_rate': {'value': 281.33, 'std': -0.01, 'avg': 283.73}, 'engine_speed_mean': {'value': 49.08, 'std': 0.0, 'avg': 49.08}}}, 'insights': [{'type': 'alert', 'location': 'cylinder #3', 'description': 'Scavenging Air Pressure at -0.03 std away from best performance', 'labels': {'Average Scavenging Air Pressure': 0.62, 'Scavenging Air Pressure': 0.59}}, {'type': 'alert', 'location': 'cylinder #3', 'description': 'Compression Pressure at -0.03 std away from best performance', 'labels': {'Average Compression Pressure': 86.86, 'Compression Pressure': 85.46}}, {'type': 'alert', 'location': 'cylinder #3', 'description': 'IMEP at -0.03 std away from best performance', 'labels': {'Average IMEP': 15.32, 'IMEP': 15.19}}, {'type': 'alert', 'location': 'cylinder #7', 'description': 'Load at -0.03 std away from best performance', 'labels': {'Average Load': 32.07, 'Load': 30.16}}, {'type': 'alert', 'location': 'cylinder #7', 'description': 'Break Power at -0.03 std away from best performance', 'labels': {'Average Break Power': 908.06, 'Break Power': 691.16}}, {'type': 'alert', 'location': 'cylinder #7', 'description': 'BMEP at -0.04 std away from best performance', 'labels': {'Average BMEP': 11.27, 'BMEP': 10.89}}]}
ais_reports = [{'MMSI': '428041000', 'STATUS': '0', 'SPEED': '153', 'LON': '34.533620', 'LAT': '32.018000', 'COURSE': '19', 'HEADING': '16', 'TIMESTAMP': '2020-02-19T14:42:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '273', 'WIND_SPEED': '17', 'WIND_TEMP': '18'}, {'MMSI': '428041000', 'STATUS': '0', 'SPEED': '151', 'LON': '34.615350', 'LAT': '32.263010', 'COURSE': '13', 'HEADING': '12', 'TIMESTAMP': '2020-02-19T15:42:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '287', 'WIND_SPEED': '12', 'WIND_TEMP': '17'}, {'MMSI': '428041000', 'STATUS': '0', 'SPEED': '154', 'LON': '34.704140', 'LAT': '32.508280', 'COURSE': '17', 'HEADING': '17', 'TIMESTAMP': '2020-02-19T16:42:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '346', 'WIND_SPEED': '10', 'WIND_TEMP': '17'}, {'MMSI': '428041000', 'STATUS': '0', 'SPEED': '160', 'LON': '34.782640', 'LAT': '32.754320', 'COURSE': '20', 'HEADING': '18', 'TIMESTAMP': '2020-02-19T17:41:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '350', 'WIND_SPEED': '10', 'WIND_TEMP': '17'}, {'MMSI': '428041000', 'STATUS': '0', 'SPEED': '112', 'LON': '34.959960', 'LAT': '32.889200', 'COURSE': '95', 'HEADING': '94', 'TIMESTAMP': '2020-02-19T18:41:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '350', 'WIND_SPEED': '9', 'WIND_TEMP': '17'}, {'MMSI': '428041000', 'STATUS': '1', 'SPEED': '1', 'LON': '34.997550', 'LAT': '32.894200', 'COURSE': '316', 'HEADING': '272', 'TIMESTAMP': '2020-02-19T19:46:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '333', 'WIND_SPEED': '10', 'WIND_TEMP': '18'}, {'MMSI': '428041000', 'STATUS': '1', 'SPEED': '1', 'LON': '34.997600', 'LAT': '32.893420', 'COURSE': '354', 'HEADING': '292', 'TIMESTAMP': '2020-02-19T20:46:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '333', 'WIND_SPEED': '10', 'WIND_TEMP': '18'}, {'MMSI': '428041000', 'STATUS': '1', 'SPEED': '1', 'LON': '34.997480', 'LAT': '32.892780', 'COURSE': '244', 'HEADING': '307', 'TIMESTAMP': '2020-02-19T21:46:00', 'SHIP_ID': '659948', 'WIND_ANGLE': '333', 'WIND_SPEED': '10', 'WIND_TEMP': '18'}]
metadata = {'vessel': 'ZIM Tarragona', 'm_e': 'MAN 8K90MC-C6', 'displacement_engine': 11705.6, 'Number of cylinders': 8, 'Stroke/bore ratio': 'k', 'Diameter of piston in cm': 90, 'Concept': 'c', 'Design': 'c', 'AIS Vessel Type': 'Container Ship', 'Year Built': 2010, 'Length Overall': 261.06, 'Breadth Extreme': 32.3, 'Deadweight': 50088, 'Gross Tonnage': 40542, 'imo': 9471214, 'date': datetime.datetime(2020, 2, 19, 17, 34, 28, 458000)}

params = json.loads(open('params.json').read())


def log_function(p, curve):
    x = math.log(p)/(1+math.log(curve))

    return x

def get_pressure_angular(p_comp,p_fire,angle):

    data = [p_comp,p_fire]

    curve = (np.max(data) - np.min(data) /2)

    curve = curve / 10

    burst = int(np.degrees(angle * 2))
    t1 = np.linspace(0, log_function(p_comp,curve),burst)
    y1 = [math.pow(math.e * curve,x ) for x in t1]

    t2 = np.linspace(t1[-1], log_function(0.975*p_comp, curve), 185-burst)
    y2 = [(math.pow(math.e * curve, x)) for x in t2]

    t3 = np.linspace(t2[-1], log_function(p_fire, curve), 5)
    y3 = [(math.pow(math.e * curve, x)) for x in t3]

    t4 = np.linspace(t3[-1], log_function(1, curve), 170)
    y4 = [(math.pow(math.e * curve, x)) for x in t4]


    graph = y1+y2+y3+y4

    import plotly.graph_objects as go

    x = np.linspace(0,359, 360)

    #fig = go.Figure(data=go.Scatter(x=x, y=graph))
    #fig.show()


    return x, graph


def plot_map(analysis,metadata,args,ais_reports):
    plot = None
    # MAP
    fig = go.Figure()

    lat = []
    lon = []
    text = []
    for ais_report in ais_reports:
        lat.append(float(ais_report["LAT"]))
        lon.append(float(ais_report["LON"]))
        text.append({
            'SPEED': ais_report["SPEED"],
            'LON': ais_report["LON"],
            'LAT': ais_report["LAT"],
             'COURSE': ais_report["COURSE"],
            'HEADING': ais_report["HEADING"],
            'TIMESTAMP': ais_report["TIMESTAMP"],
            'WIND_ANGLE': ais_report["WIND_ANGLE"],
            'WIND_SPEED': ais_report["WIND_SPEED"],
            'WIND_TEMP': ais_report["WIND_TEMP"]
        })
    fig.add_trace(go.Scattermapbox(
        mode="markers+lines",
        lon=lon,
        lat=lat,
        text=text,
        marker={'size': 10})
    )
    fig.update_layout(
        mapbox={
            'center': {'lon': int((lon[0] + lon[-1]) / 2),
                       'lat': int((lat[0] + lon[-1]) / 2)},
            'style': "stamen-terrain",
            'zoom': 8})
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="LightSteelBlue",
    )
    fig.write_html("plots/"+args["type"]+".html")
    return "plots/"+args["type"]+".html"

def plot_quick_view(analysis,metadata,args):
    fig = go.Figure()


    # QUICK VIEW



    types = []
    descriptions = []
    locations = []
    colors = []
    dates = []
    labels = []
    for insight in analysis["insights"]:
        types.append(insight["type"])
        dates.append(str(metadata["date"]))
        descriptions.append(insight["description"])
        locations.append(insight["location"])
        labels.append(', '.join([key+": "+str(value) for key,value in insight["labels"].items()]))
        if insight["type"] == "alert":
            colors.append(["rgb(255, 200, 200)",'white','white','white'])

    fig.add_trace(
        go.Table(
            header=dict(
                values=["TYPE","DATE","LOCATION", "DESCRIPTION","DATA"],
                line_color='white', fill_color='white',
                align='center', font=dict(color='black', size=20)
            ),
            cells=dict(
                values=[types, dates,locations,descriptions,labels],
                fill_color=np.array(colors).T,
                height=30,
                align=['center','center','center','left'], font=dict(color='black', size=16)
            ))
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="LightSteelBlue",
    )
    fig.write_html("plots/"+args["type"]+".html")
    return "plots/plot.html"

def plot_snapshot(analysis,metadata,args):
    fig = go.Figure()


    # SnapShot
    names = []
    values = {x:[] for x in analysis["cylinders"]["1"].keys()}
    parameters = list(values.keys())
    parameters = [params["targets_names_refactor"][x] + " " + params["targets_measure"][x] for x in parameters]
    for cylinder_index in analysis["cylinders"].keys():
        names.append("Cylinder # "+str(int(cylinder_index)+1))
        for key,value in analysis["cylinders"][cylinder_index].items():
            values[key].append(value["value"])





    fig.add_trace(
        go.Table(
            header=dict(
                values=["PARAMETER"] + names,
                line_color='white', fill_color='white',
                align='center', font=dict(size=20)
            ),
            cells=dict(
                values=[parameters] + list(np.array([val for val in values.values()]).T),
                height=30,
                font=dict( size=16)
            ))
    )



    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="LightSteelBlue",
    )
    fig.write_html("plots/"+args["type"]+".html")
    return "plots/"+args["type"]+".html"

def plot_cylinder(analysis,metadata,args):




    counter = int(args["cylinder_num"]) - 1

    fig = go.Figure()
    x,graph = get_pressure_angular(analysis["cylinders"][str(counter)]['compression_pressure']["value"],analysis["cylinders"][str(counter)]['firing_pressure']["value"],analysis["cylinders"][str(counter)]["injection_timing"]["value"])
    fig.add_trace(
        go.Barpolar(theta=x, r=graph)
    )


    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="LightSteelBlue",
    )
    fig.write_html("plots/"+args["type"]+" - "+str(args["cylinder_num"])+".html")
    return "plots/"+args["type"]+" - "+str(args["cylinder_num"])+".html"

def plot_pressure_angular(analysis,metadata,args):
    fig = go.Figure()
    counter = 0
    for i in range(len(list(analysis["cylinders"].keys()))):
        x,graph = get_pressure_angular(analysis["cylinders"][str(counter)]['compression_pressure']["value"],analysis["cylinders"][str(counter)]['firing_pressure']["value"],analysis["cylinders"][str(counter)]["injection_timing"]["value"])
        counter += 1
        # PREESURE ANGULAR
        fig.add_trace(
            go.Scatter(x=x, y=graph,name="CYLINDER # "+str(counter))
        )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="LightSteelBlue",
    )
    fig.write_html("plots/"+args["type"]+".html")
    return "plots/"+args["type"]+".html"


def get_plot(args):
    plot = None
    if args["type"] == "map":
        plot = plot_map(analysis,metadata,args,ais_reports)
    elif args["type"] == "quick_view":
        plot = plot_quick_view(analysis, metadata, args)
    elif args["type"] == "snapshot":
        plot = plot_snapshot(analysis, metadata, args)
    elif args["type"] == "cylinder":
        plot = plot_cylinder(analysis, metadata, args)
    elif args["type"] == "pressure_angular":
        plot = plot_pressure_angular(analysis, metadata, args)
    return plot

if __name__ == "__main__":
    types = ["map","quick_view","snapshot","cylinder","pressure_angular"]
    for tp in types:
        args = {
            "type":tp,
            "fromdate":"202002191600",
            "todate":"202002192000",
            "imo":9471214
        }
        if tp == "cylinder":
            for i in range(len(list(analysis["cylinders"].keys()))):
                args["cylinder_num"] = i + 1
                get_plot(args)
        else:
            get_plot(args)