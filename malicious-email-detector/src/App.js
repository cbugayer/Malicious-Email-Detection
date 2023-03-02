import React from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

class EmailText extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Please insert url here for scrutiny',
      phishingURL: '',
      phishingPrediction: '',
      confidence: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
    console.log(this.state.value);
  }

  handleSubmit(event) {
    const requestOptions = {
      method: 'POST',
      headers: {'Accept': 'application/json','Content-Type': 'application/json'},
      body: JSON.stringify({"urls": [this.state.value]})
    };
    alert('Scanning Email...');
    event.preventDefault();
    const port = 8000
    const serverAddress = 'http://127.0.0.1:' + port + '/phishing-prediction'
    console.log(this.state.value);
    fetch(serverAddress, requestOptions)
      .then(async response => {
        if (!response.ok){
          alert(response.statusText)
        }
        const data = await response.json();
        this.setState({phishingPrediction: data['predictions'][0]['prediction']})
        this.setState({confidence: data['predictions'][0]['phishing_probability']})
        this.setState({phishingURL: data['predictions'][0]['url']})
      })
  }

  render() {
    return (
      <div>
        <Form onSubmit={this.handleSubmit}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Insert URL:</Form.Label>
          <Form.Control onChange={this.handleChange} />
        </Form.Group>
        <Button type="submit">
          Submit
        </Button>
        </Form>
        <div>
          <p>Phishing Prediction: {this.state.phishingPrediction}</p>
          <p>Confidence: {this.state.confidence} %</p>
          <p>URL: {this.state.phishingURL}</p>
        </div>
      </div>
    );
  }
}

export default EmailText;
