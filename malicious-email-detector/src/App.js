import React from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import gmailApi from "react-gmail";

class scrapeEmail extends React.Component {
  state = {
    messages: [],
  };

  getMessages = () => {
    gmailApi.get.messages(true, 10).then((res) => {
      this.setState({ messages: gmailApi.normalizeData(res) });
    });
  }

  render() {
    return (
      <div className="App">
        <h1>Malicious Email Detector</h1>
        <h2>Scrape Email</h2>
        <Button onClick={this.getMessages}>Scrape Email</Button>
        <div>
          {this.state.messages.map((message) => (
            <div>
              <span>
                {message.subject}: {message.snippet}
              </span>
              <p>{message.date}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

class EmailText extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "Please insert url here for scrutiny",
      phishingURL: "",
      phishingPrediction: "",
      confidence: "",
    };

    

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
    console.log(this.state.value);
  }

  handleSubmit(event) {
    const requestOptions = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ urls: [this.state.value] }),
    };
    alert("Scanning Email...");
    event.preventDefault();
    const port = 8000;
    const serverAddress = "http://127.0.0.1:" + port + "/phishing-prediction";
    console.log(this.state.value);
    fetch(serverAddress, requestOptions).then(async (response) => {
      if (!response.ok) {
        alert(response.statusText);
      }
      const data = await response.json();
      this.setState({
        phishingPrediction: data["predictions"][0]["prediction"],
      });
      this.setState({
        confidence: data["predictions"][0]["phishing_probability"],
      });
      this.setState({ phishingURL: data["predictions"][0]["url"] });
    });
  }

  render() {
    return (
      <div className="form-container">
        <Form className="form" onSubmit={this.handleSubmit}>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label className="form-label">Insert Email:</Form.Label>
            <Form.Control
              className="form-control"
              onChange={this.handleChange}
            />
          </Form.Group>
          <Button className="form-button" type="submit">
            Submit
          </Button>
        </Form>
        <div class="summary">
          <p class="prediction">
            Phishing Prediction: {this.state.phishingPrediction}
          </p>
          <p class="confidence">Confidence: {this.state.confidence} %</p>
          <p class="url">URL: {this.state.phishingURL}</p>
        </div>


      </div>
    );
  }
}

export default EmailText;
