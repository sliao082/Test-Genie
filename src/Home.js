import './App.css';
import { Link } from 'react-router-dom';
// import UploadContent from './UploadContent';
// import DisplayContent from './DisplayContent';
import React, { useEffect } from 'react';

function Home() {
  
  async function handleGenerateResponse() {
    const systemMessage = "Give me 1 paragraph.";
    const userMessage = "How do I use Gauss-Newton Algorithm to find the Conditional LS estimate?";
    const response = await fetchOllamaResponse(systemMessage, userMessage);
    console.log("Generated Response:", response);
  }

  async function fetchOllamaResponse(systemMessage, userMessage) {
    const response = await fetch("http://127.0.0.1:8000/api/generate-response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            system_message: systemMessage,
            user_message: userMessage,
            model: "llama3.2"
        })
    });
    const data = await response.json();
    console.log(data.response);
    return data.response;
  }

  useEffect(() => {
    handleGenerateResponse();
  }, []);

  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p style = {{fontSize: '50px', paddingTop: '60px'}} ><b> TEST GENIE </b></p>
          <p> Test Genie analyzes the textbooks, assignments, and past exams to </p>
          <p> create study materials for students to utilize to study. </p>
          <div style = {{padding: '20px'}}></div>
          <div>
            <Link to="/UploadContent"> 
                <button className="custom-button"> Generate New Content </button>
            </Link>
            <label style = {{padding: '20px'}}></label>
            <Link to="/DisplayContent"> 
                <button className="custom-button"> Previous Materials </button>
            </Link>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Home;
