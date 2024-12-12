import './App.css';
import { TextContext } from "./TextContext";
import React, { useState, useEffect, useContext, useRef } from 'react';
import ReactMarkdown from "react-markdown";

function NotesSummary() {
  const { extractedText } = useContext(TextContext);
  const [response, setResponse] = useState("*The model is reading your lecture notes...*");
  const effectRan = useRef(false);

  useEffect(() => {
    const fetchResponse = async () => {
      if (!effectRan.current) {
        if (extractedText) {
          const systemMessage = "Give me a comprehensive and detailed summary of the content.";
          const ollama_response = await fetch("http://127.0.0.1:8000/api/generate-summary-response", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              system_message: systemMessage,
              user_message: extractedText,
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
  }, [extractedText]);

  return (
    <div className="App">
      <header className="App-body">
        <div>
          <div style={{ textAlign: "left", fontSize: "20px", paddingLeft: "100px", paddingRight: "50px", paddingBottom: "50px", lineHeight: "2" }}>
            <ReactMarkdown>{response}</ReactMarkdown>
          </div>
        </div>
      </header>
    </div>
  );
}

export default NotesSummary;
