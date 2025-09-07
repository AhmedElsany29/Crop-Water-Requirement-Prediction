# 🌱 Crop Water Requirement Prediction (Flask + XGBoost)

A Flask web application that predicts **crop water requirements** based
on crop type, soil type, region, weather conditions, and temperature
values.\
The app uses a pre-trained **XGBoost model** (`xgb_model.joblib`) to
make predictions and displays the results in a simple web interface.

------------------------------------------------------------------------

## ✨ Features

-   User-friendly web interface built with **Flask**.\
-   Dropdown menus for crop type, soil type, region, and weather
    conditions.\
-   Input fields for **minimum and maximum temperature**.\
-   Real-time prediction of water requirements.\
-   Powered by a pre-trained **XGBoost machine learning model**.

------------------------------------------------------------------------

## 🛠️ Requirements

Before running the app, install the required dependencies:

``` bash
pip install flask joblib numpy
```

Make sure you have the trained model file saved as:

    xgb_model.joblib

------------------------------------------------------------------------

## ▶️ Usage

1.  Clone the repository:

    ``` bash
    git clone https://github.com/username/crop-water-prediction.git
    cd crop-water-prediction
    ```

2.  Run the Flask app:

    ``` bash
    python app.py
    ```

3.  Open the app in your browser:

        http://127.0.0.1:5000/

------------------------------------------------------------------------

## ⚙️ Input Parameters

-   **Crop Type**: (e.g., RICE, WHEAT, POTATO, BANANA, etc.)\
-   **Soil Type**: (DRY, WET, MOIST)\
-   **Region**: (DESERT, SEMI ARID, SEMI HUMID, HUMID)\
-   **Weather Condition**: (NORMAL, SUNNY, WINDY, RAINY)\
-   **Temp Min / Temp Max**: Minimum and maximum temperature values.

------------------------------------------------------------------------

## 📊 Model

-   The application loads a trained **XGBoost regression/classification
    model** from `xgb_model.joblib`.\
-   Encoded categorical values (`crop_type`, `soil_type`, `region`,
    `weather_condition`) are mapped into integers before prediction.\
-   Input features are passed as a 13-dimensional NumPy array.

------------------------------------------------------------------------

## 📌 Notes

-   Make sure the model file (`xgb_model.joblib`) exists in the project
    directory.\
-   The app runs in **debug mode** by default for development.\
-   You can deploy the app on **Heroku, Render, or Docker** for
    production use.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Improve UI with **Bootstrap** or **Tailwind CSS**.\
-   Add more environmental features (humidity, rainfall, etc.).\
-   Enable saving prediction results to a database.
