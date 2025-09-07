from flask import Flask, render_template_string, request
import joblib
import numpy as np

# تهيئة تطبيق Flask
app = Flask(__name__)

model = joblib.load('xgb_model.joblib')
    # قواميس الترميز للقيم النصية
crop_type_encoding = {
    'BANANA': 0, 'SOYABEAN': 1, 'CABBAGE': 2, 'POTATO': 3, 'RICE': 4,
    'MELON': 5, 'MAIZE': 6, 'CITRUS': 7, 'BEAN': 8, 'WHEAT': 9,
    'MUSTARD': 10, 'COTTON': 11, 'SUGARCANE': 12, 'TOMATO': 13, 'ONION': 14
}
soil_type_encoding = {'DRY': 0, 'WET': 1, 'MOIST': 2}
region_encoding = {'DESERT': 0, 'SEMI ARID': 1, 'SEMI HUMID': 2, 'HUMID': 3}
weather_condition_encoding = {'NORMAL': 0, 'SUNNY': 1, 'WINDY': 2, 'RAINY': 3}


# قالب HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Crop Water Requirement Prediction</title>
</head>
<body>
    <h1>Crop Water Requirement Prediction</h1>
    <form action="/predict" method="POST">

        <label for="crop_type">CROP TYPE:</label>
        <select name="crop_type" required>
            <option value="BANANA">BANANA</option>
            <option value="SOYABEAN">SOYABEAN</option>
            <option value="CABBAGE">CABBAGE</option>
            <option value="POTATO">POTATO</option>
            <option value="RICE">RICE</option>
            <option value="MELON">MELON</option>
            <option value="MAIZE">MAIZE</option>
            <option value="CITRUS">CITRUS</option>
            <option value="BEAN">BEAN</option>
            <option value="WHEAT">WHEAT</option>
            <option value="MUSTARD">MUSTARD</option>
            <option value="COTTON">COTTON</option>
            <option value="SUGARCANE">SUGARCANE</option>
            <option value="TOMATO">TOMATO</option>
            <option value="ONION">ONION</option>
        </select><br><br>

        <label for="soil_type">SOIL TYPE:</label>
        <select name="soil_type" required>
            <option value="DRY">DRY</option>
            <option value="WET">WET</option>
            <option value="MOIST">MOIST</option>
        </select><br><br>

        <label for="region">REGION:</label>
        <select name="region" required>
            <option value="DESERT">DESERT</option>
            <option value="SEMI ARID">SEMI ARID</option>
            <option value="SEMI HUMID">SEMI HUMID</option>
            <option value="HUMID">HUMID</option>
        </select><br><br>

        <label for="weather_condition">WEATHER CONDITION:</label>
        <select name="weather_condition" required>
            <option value="NORMAL">NORMAL</option>
            <option value="SUNNY">SUNNY</option>
            <option value="WINDY">WINDY</option>
            <option value="RAINY">RAINY</option>
        </select><br><br>

        <label for="temp_min">TEMP_MIN:</label>
        <input type="number" name="temp_min" step="0.1" required><br><br>

        <label for="temp_max">TEMP_MAX:</label>
        <input type="number" name="temp_max" step="0.1" required><br><br>

        <button type="submit">SUBMIT</button>
    </form>
    {% if prediction_text %}
    <h2>{{ prediction_text }}</h2>
    {% endif %}
</body>
</html>
"""

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template_string(html_template)

# نقطة التنبؤ
@app.route('/predict', methods=['POST'])
def predict():
    # الحصول على المدخلات من المستخدم
    crop_type = request.form['crop_type']
    soil_type = request.form['soil_type']
    region = request.form['region']
    weather_condition = request.form['weather_condition']
    temp_min = float(request.form['temp_min'])
    temp_max = float(request.form['temp_max'])

    # تحويل المدخلات النصية إلى قيم عددية
    crop_type_encoded = crop_type_encoding[crop_type]
    soil_type_encoded = soil_type_encoding[soil_type]
    region_encoded = region_encoding[region]
    weather_condition_encoded = weather_condition_encoding[weather_condition]

    # تحويل المدخلات إلى مصفوفة مناسبة للنموذج (بإجمالي 13 ميزة)
    input_features = np.array([[crop_type_encoded, soil_type_encoded, region_encoded, weather_condition_encoded, temp_min, temp_max, 0, 0, 0, 0, 0, 0, 0]])

    # التنبؤ باستخدام النموذج
    prediction = model.predict(input_features)[0]

    # عرض النتيجة على المستخدم
    return render_template_string(html_template, prediction_text=f'Water Required: {prediction:.2f} units')

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
