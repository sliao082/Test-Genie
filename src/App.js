import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function UploadFiles() {
  const [selectedFile, setSelectedFile] = useState(null);
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      setSelectedFile(file);
      console.log('PDF selected:', file);
    } else {
      alert('Please select a PDF file.');
    }
  };
  const [checkedItems, setCheckedItems] = useState({
    item1: false,
    item2: false,
  });
  // Handle change for each checkbox
  const handleCheckboxChange = (event) => {
    const { name, checked } = event.target;
    setCheckedItems({
      ...checkedItems,
      [name]: checked,
    });
  };
  const handleSubmit = () => {
    if (selectedFile) {
      // Handle upload logic here
      console.log('Uploading:', selectedFile);
    } else {
      alert('No file selected.');
    }
    const selectedItems = Object.keys(checkedItems).filter(
      (item) => checkedItems[item]
    );
    console.log('Selected items:', selectedItems);
    // Add your submission logic here (e.g., save or send the selected items)
  };

  return (
    <div>
      <div>
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
        />
      </div>
      {/* <button onClick={handleUpload}>Upload PDF</button> */}
      <div style = {{padding: '20px'}}></div>
      <div style={{alignItems: 'left'}}>
        <label style={{fontSize: '20px'}}>
          <input
            type="checkbox"
            name="item1"
            checked={checkedItems.item1}
            onChange={handleCheckboxChange}
          />
          practice test
        </label>
        <label style={{fontSize: '20px', paddingLeft: '30px'}}>
          <input
            type="checkbox"
            name="item2"
            checked={checkedItems.item2}
            onChange={handleCheckboxChange}
          />
          notes summary
        </label>
      </div>
      <div style = {{padding: '20px'}}></div>
      <button className="custom-button" onClick={handleSubmit}> Generate! </button>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
        <label style={{fontSize: '30px', textAlign: 'left', paddingTop: '20px'}}><b> 
          Test Genie </b></label>
        <label style={{padding: '350px'}}></label>
        <label style={{textAlign: 'right', paddingTop: '5px'}}><b> 
          <img src={logo} className="App-logo" alt="logo" />
          Hello Name! </b></label>
        </div>
      </header>

      <header className="App-body">
        <div>
          <p> upload assignments, notes, past exams, etc. </p>
          <UploadFiles/>
        </div>
      </header>
    </div>
  );
}

export default App;
