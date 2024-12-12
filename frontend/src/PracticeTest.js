import { TextContext } from "./TextContext";
import React, { useState, useEffect, useContext, useRef } from 'react';
import ReactMarkdown from "react-markdown";
import './App.css';

function PracticeTest() {
  const { extractedText, lectureNotes } = useContext(TextContext);
  const [response, setResponse] = useState("*The model is generating your practice questions...*");
  const effectRan = useRef(false);

  useEffect(() => {
    const fetchResponse = async () => {
      if (!effectRan.current) {
        if (extractedText) {
          const systemMessage = "Based on the sample questions seen, generate 10 diverse questions that: 1. Cover different aspects of the topics 2. Use varied question structures 3. Include both theoretical and practical elements Please keep each question concise and clear.";
          const userMessage = extractedText;
          const ollama_response = await fetch("http://127.0.0.1:8000/api/generate-test-response", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              system_message: systemMessage,
              user_message: userMessage,
              model: "llama3.2",
            }),
          });
          const data = await ollama_response.json();
          setResponse(data.response);
        }
      }
    };
    fetchResponse();

    return () => effectRan.current = true;
  }, [extractedText, lectureNotes]);

  return (
    <div className="App">
      <header className="App-body">
        <div>
          <div style={{ textAlign: "left", fontSize: "20px", paddingLeft: "100px", paddingRight: "50px", paddingBottom: "50px" }}> <ReactMarkdown>{response}</ReactMarkdown> </div>
        </div>
      </header>
    </div>
  );
}

export default PracticeTest;
