# 🛑 Driver Drowsiness Detection System

A real-time driver drowsiness detection system using deep learning and OpenCV. The system detects signs of fatigue by analyzing eye and mouth states using custom and pre-built CNN models.


## 🚀 How to Run

1. **Install Dependencies**

   Make sure Python 3.7+ is installed. Then run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**

   ```bash
   python launcher_file.py
   ```

3. **Choose from the Popup Menu**

   You'll be presented with a GUI to choose:
   - **Model**:
     - Custom
     - VGG16
     - VGG19
   - **Input Type**:
     - Only Eyes
     - Only Mouth
     - Both Eyes and Mouth

4. **Allow Camera Access**

   The system will activate your webcam and start detecting drowsiness based on the selected configuration.

---

## 🧠 Models Used

### ✅ Custom CNN

A lightweight custom-built convolutional neural network trained from scratch on the dataset.

### ✅ VGG16

A transfer learning model using the VGG16 architecture with fine-tuning.

### ✅ VGG19

Another transfer learning approach using the deeper VGG19 model.

---

## 👁️‍🗨️ Detection Methods

- **Eyes Only**: Classifies eye states as Open or Closed.
- **Mouth Only**: Detects yawning based on mouth state.
- **Both**: Uses combined eye and mouth inputs to determine drowsiness more accurately.

---

## 🔔 Alert Mechanism

If the model detects prolonged eye closure or frequent yawning:
- The system will trigger a **sound alarm** using `alarm.wav`
- A red rectangle will flash around the screen as a visual alert

---

## 🧪 Training (Optional)

If you'd like to retrain the models or experiment with new data:

```bash
cd Training
Model3Training.ipynb    # For the custom CNN
Vgg16Vgg19Training.ipynb           # For VGG16 and VGG19-based model
```

## 📸 Example

When launched, the webcam feed will appear with real-time drowsiness analysis. Alerts are raised when drowsiness is detected.

---

