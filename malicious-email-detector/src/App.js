import React from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

class EmailText extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: 'Please insert url here for scrutiny',
      phishingPrediction: ''
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
      body: JSON.stringify({"urls": this.state.value})
    };
    alert('Scanning Email...');
    event.preventDefault();
    const port = 8080
    const serverAddress = 'http://127.0.0.1:' + port + '/phishing-prediction'
    console.log(this.state.value);
    fetch(serverAddress, requestOptions)
      .then(async response => {
        if (!response.ok){
          alert(response.statusText)
        }
        console.log(response);
        const data = await response.json();
        this.setState({phishingPrediction: data['predictions'][3]})
      })
  }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Insert URL:</Form.Label>
        <Form.Control onChange={this.handleChange} />
      </Form.Group>
      <Button type="submit">
        Submit
      </Button>
    </Form>
    );
  }
}

export default EmailText;
