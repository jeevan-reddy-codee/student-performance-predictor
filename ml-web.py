from flask import Flask, render_template, request, jsonify
import pickle
import warnings
print("RUNNING NEW CODE")
warnings.filterwarnings("ignore")

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        hours = float(data['hours'])

        
        prediction = model.predict([[hours]])[0][0]
        prediction = max(0, min(100, prediction))
        print("PRED VALUE:", prediction)

        return jsonify({'prediction': round(prediction, 2)})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({'prediction': 0})

if __name__ == "__main__":
    app.run(debug=True)

