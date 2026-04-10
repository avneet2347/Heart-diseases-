import React, { useState } from 'react';
import {
  Container,
  Paper,
  Typography,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
  Box,
  Alert,
  Card,
  CardContent,
  Grid,
  Chip,
  LinearProgress
} from '@mui/material';
import { Favorite, HeartBroken, Assessment } from '@mui/icons-material';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    age: '',
    sex: '',
    cp: '',
    trestbps: '',
    chol: '',
    fbs: '',
    restecg: '',
    thalach: '',
    exang: '',
    oldpeak: '',
    slope: '',
    ca: '',
    thal: ''
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // Convert string values to appropriate types
      const dataToSend = {
        age: parseInt(formData.age),
        sex: parseInt(formData.sex),
        cp: parseInt(formData.cp),
        trestbps: parseInt(formData.trestbps),
        chol: parseInt(formData.chol),
        fbs: parseInt(formData.fbs),
        restecg: parseInt(formData.restecg),
        thalach: parseInt(formData.thalach),
        exang: parseInt(formData.exang),
        oldpeak: parseFloat(formData.oldpeak),
        slope: parseInt(formData.slope),
        ca: parseInt(formData.ca),
        thal: parseInt(formData.thal)
      };

      const response = await axios.post('/predict', dataToSend);
      setPrediction(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred during prediction');
    } finally {
      setLoading(false);
    }
  };

  const getRiskColor = (riskLevel) => {
    switch (riskLevel) {
      case 'High Risk': return 'error';
      case 'Medium Risk': return 'warning';
      case 'Low Risk': return 'success';
      default: return 'default';
    }
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h3" component="h1" gutterBottom align="center" color="primary">
        <Favorite sx={{ mr: 1, verticalAlign: 'middle' }} />
        Heart Disease Prediction
      </Typography>
      <Typography variant="h6" align="center" color="text.secondary" sx={{ mb: 4 }}>
        Enter patient information to predict heart disease risk
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper elevation={3} sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              <Assessment sx={{ mr: 1, verticalAlign: 'middle' }} />
              Patient Information
            </Typography>

            <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
              <Grid container spacing={2}>
                <Grid item xs={12} sm={6}>
                  <TextField
                    fullWidth
                    label="Age"
                    name="age"
                    type="number"
                    value={formData.age}
                    onChange={handleChange}
                    required
                    inputProps={{ min: 1, max: 120 }}
                  />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Sex</InputLabel>
                    <Select
                      name="sex"
                      value={formData.sex}
                      onChange={handleChange}
                      label="Sex"
                    >
                      <MenuItem value={0}>Female</MenuItem>
                      <MenuItem value={1}>Male</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Chest Pain Type</InputLabel>
                    <Select
                      name="cp"
                      value={formData.cp}
                      onChange={handleChange}
                      label="Chest Pain Type"
                    >
                      <MenuItem value={1}>Typical Angina</MenuItem>
                      <MenuItem value={2}>Atypical Angina</MenuItem>
                      <MenuItem value={3}>Non-anginal Pain</MenuItem>
                      <MenuItem value={4}>Asymptomatic</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField
                    fullWidth
                    label="Resting Blood Pressure (mm Hg)"
                    name="trestbps"
                    type="number"
                    value={formData.trestbps}
                    onChange={handleChange}
                    required
                    inputProps={{ min: 80, max: 200 }}
                  />
                </Grid>

                <Grid item xs={12} sm={6}>
                  <TextField
                    fullWidth
                    label="Cholesterol (mg/dl)"
                    name="chol"
                    type="number"
                    value={formData.chol}
                    onChange={handleChange}
                    required
                    inputProps={{ min: 100, max: 600 }}
                  />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Fasting Blood Sugar > 120 mg/dl</InputLabel>
                    <Select
                      name="fbs"
                      value={formData.fbs}
                      onChange={handleChange}
                      label="Fasting Blood Sugar > 120 mg/dl"
                    >
                      <MenuItem value={0}>No</MenuItem>
                      <MenuItem value={1}>Yes</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>

                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>EKG Results</InputLabel>
                    <Select
                      name="restecg"
                      value={formData.restecg}
                      onChange={handleChange}
                      label="EKG Results"
                    >
                      <MenuItem value={0}>Normal</MenuItem>
                      <MenuItem value={1}>ST-T Wave Abnormality</MenuItem>
                      <MenuItem value={2}>Left Ventricular Hypertrophy</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField
                    fullWidth
                    label="Maximum Heart Rate"
                    name="thalach"
                    type="number"
                    value={formData.thalach}
                    onChange={handleChange}
                    required
                    inputProps={{ min: 60, max: 220 }}
                  />
                </Grid>

                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Exercise Induced Angina</InputLabel>
                    <Select
                      name="exang"
                      value={formData.exang}
                      onChange={handleChange}
                      label="Exercise Induced Angina"
                    >
                      <MenuItem value={0}>No</MenuItem>
                      <MenuItem value={1}>Yes</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField
                    fullWidth
                    label="ST Depression"
                    name="oldpeak"
                    type="number"
                    step="0.1"
                    value={formData.oldpeak}
                    onChange={handleChange}
                    required
                    inputProps={{ min: 0, max: 6.2, step: 0.1 }}
                  />
                </Grid>

                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Slope of ST Segment</InputLabel>
                    <Select
                      name="slope"
                      value={formData.slope}
                      onChange={handleChange}
                      label="Slope of ST Segment"
                    >
                      <MenuItem value={1}>Upsloping</MenuItem>
                      <MenuItem value={2}>Flat</MenuItem>
                      <MenuItem value={3}>Downsloping</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <FormControl fullWidth required>
                    <InputLabel>Number of Vessels</InputLabel>
                    <Select
                      name="ca"
                      value={formData.ca}
                      onChange={handleChange}
                      label="Number of Vessels"
                    >
                      <MenuItem value={0}>0</MenuItem>
                      <MenuItem value={1}>1</MenuItem>
                      <MenuItem value={2}>2</MenuItem>
                      <MenuItem value={3}>3</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>

                <Grid item xs={12}>
                  <FormControl fullWidth required>
                    <InputLabel>Thallium Test</InputLabel>
                    <Select
                      name="thal"
                      value={formData.thal}
                      onChange={handleChange}
                      label="Thallium Test"
                    >
                      <MenuItem value={3}>Normal</MenuItem>
                      <MenuItem value={6}>Fixed Defect</MenuItem>
                      <MenuItem value={7}>Reversible Defect</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>

                <Grid item xs={12}>
                  <Button
                    type="submit"
                    variant="contained"
                    size="large"
                    fullWidth
                    disabled={loading}
                    sx={{ mt: 2, py: 1.5 }}
                  >
                    {loading ? 'Analyzing...' : 'Predict Heart Disease Risk'}
                  </Button>
                </Grid>
              </Grid>
            </Box>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Prediction Results
              </Typography>

              {loading && (
                <Box sx={{ width: '100%', mt: 2 }}>
                  <LinearProgress />
                  <Typography variant="body2" sx={{ mt: 1 }}>
                    Analyzing patient data...
                  </Typography>
                </Box>
              )}

              {error && (
                <Alert severity="error" sx={{ mt: 2 }}>
                  {error}
                </Alert>
              )}

              {prediction && (
                <Box sx={{ mt: 2 }}>
                  <Alert
                    severity={prediction.prediction === 1 ? "error" : "success"}
                    sx={{ mb: 2 }}
                    icon={prediction.prediction === 1 ? <HeartBroken /> : <Favorite />}
                  >
                    <Typography variant="h6">
                      {prediction.result}
                    </Typography>
                  </Alert>

                  <Box sx={{ mb: 2 }}>
                    <Typography variant="body2" color="text.secondary">
                      Confidence: {prediction.confidence}%
                    </Typography>
                    <Chip
                      label={prediction.risk_level}
                      color={getRiskColor(prediction.risk_level)}
                      size="small"
                      sx={{ mt: 1 }}
                    />
                  </Box>

                  <Typography variant="body2" color="text.secondary">
                    {prediction.prediction === 1
                      ? "Please consult with a healthcare professional for proper diagnosis and treatment."
                      : "This is a preliminary assessment. Regular check-ups are recommended for maintaining heart health."
                    }
                  </Typography>
                </Box>
              )}

              {!prediction && !loading && !error && (
                <Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
                  Fill out the form and click "Predict" to get your heart disease risk assessment.
                </Typography>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;