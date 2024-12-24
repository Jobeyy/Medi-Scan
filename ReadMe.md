
# MediScan: Skin Cancer & Brain Cancer Detection Application

MediScan is a Skin Cancer and Brain MRI detection web application designed to analyze uploaded skin images and provide a preliminary assessment using machine learning models. This project uses a simple and user-friendly interface, leveraging modern web technologies and backend services to offer accurate predictions.

---

## Features

- **User-Friendly Interface**: Upload skin images in a few clicks.
- **Machine Learning Integration**: Detect skin cancer using state-of-the-art models.
Detect Brain MRI cancer using state-of-the-art models (YOLO).
- **Real-Time Results**: Get predictions, including cancer likelihood and confidence scores.
- **Responsive Design**: Accessible on desktops, tablets, and mobile devices.

---

## Technologies Used

### **Frontend**
- **React.js**: For building the dynamic and interactive user interface.
- **Tailwind CSS**: For styling and responsive design.

### **Backend**
- **Node.js / Python Flask**: Backend services to process images and interact with the ML model.
- **Machine Learning Models**: TensorFlow and PyTorch-based skin cancer detection model and Brain MRI Model respectively.

### **Other Tools**
- **Fetch API**: For sending HTTP requests from the frontend to the backend.
- **FormData**: For handling image uploads.


## Installation and Setup

### Prerequisites
- **Node.js** (for running the frontend)
- **Python** (for backend/ML service)
- **Package Manager**: npm or yarn
- **Flask** (for backend server, if using Python)

### Frontend Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Jobeyy/Medi-Scan.git]
   cd medi-scan
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `server/` folder:
   ```bash
   cd server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```bash
   python app.py
   ```

4. Ensure the backend is running on `http://127.0.0.1:5000`.

---

## How to Use

1. Launch the application by running the frontend and backend servers.
2. On the **Skin Cancer Page**:
   - Click **"Choose File"** to upload a clear image of your skin.
   - Click **"Submit"** to analyze the image.
2. On the **MRI Cancer Page**:
   - Click **"Choose File"** to upload a Brain MRI image.
   - Click **"Submit"** to analyze the image.
3. View the prediction results, which include:
   - The likelihood of cancer.
   - Confidence scores.
   - Segmented regions (if applicable).

---

## Example Response
Upon successful image analysis, the system displays the following:
- **Name**: Image name or identifier.
- **Cancer Prediction**: Yes/No or likelihood percentage.
- **Hash**: Unique hash for the file.
- **Image**: Segmented skin image or result URL.



## Future Improvements

- Enhance the model accuracy using additional datasets.
- Add support for more skin conditions.
- Implement a database to store user results.
- Add a progress bar for file uploads.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For questions or feedback, reach out to [JobeyFarias01@gmail.com](JobeyFarias01@gmail.com).

---

Let me know if you want to tweak any section or add more details!
