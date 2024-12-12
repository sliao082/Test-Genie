import React, { useState, useContext } from "react";
import { TextContext } from "./TextContext";
import './App.css';
import { useNavigate } from "react-router-dom";

function UploadFiles() {
  const [selectedFile, setSelectedFile] = useState(null);
  const { setExtractedText, setLectureNotes } = useContext(TextContext);
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      setSelectedFile(file);
    } else {
      alert('Please select a PDF file.');
    }
  };

  const handleSubmit = async (targetPath) => {
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch("http://127.0.0.1:8000/api/upload/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setExtractedText(data.text);
      if (targetPath === "/NotesSummary") {
        setLectureNotes(data.text);
      }
      navigate(targetPath);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div>
      <div>
        <input type="file" accept="application/pdf" onChange={handleFileChange} />
      </div>
      <div style={{ padding: '20px' }}></div>
      <label style={{ padding: '20px' }}></label>
      <button className="custom-button" onClick={() => handleSubmit("/PracticeTest")}> Generate Practice Test </button>
      <label style={{ padding: '20px' }}></label>
      <button className="custom-button" onClick={() => handleSubmit("/NotesSummary")}> Generate Notes Summary </button>
    </div>
  );
}

function UploadContent() {
  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p style={{ paddingTop: '100px' }}> upload assignments, notes, past exams, etc. </p>
          <UploadFiles />
        </div>
      </header>
    </div>
  );
}

export default UploadContent;
