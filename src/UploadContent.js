import React, { useState } from 'react';
import './App.css';
// import PracticeTest from './PracticeTest';
// import Home from './Home';
import { Link } from 'react-router-dom';


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
  // const [checkedItems, setCheckedItems] = useState({
  //   item1: false,
  //   item2: false,
  // });
  // Handle change for each checkbox
  // const handleCheckboxChange = (event) => {
  //   const { name, checked } = event.target;
  //   setCheckedItems({
  //     ...checkedItems,
  //     [name]: checked,
  //   });
  // };
  const handleSubmit = () => {
    if (selectedFile) {
      // Handle upload logic here
      console.log('Uploading:', selectedFile);
    } else {
      alert('No file selected.');
    }
    // const selectedItems = Object.keys(checkedItems).filter(
    //   (item) => checkedItems[item]
    // );
    // console.log('Selected items:', selectedItems);
    // submission logic here (e.g., save or send the selected items)
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
      {/* <div style={{alignItems: 'left'}}>
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
      </div> */}
      <label style = {{padding: '20px'}}></label>
      <Link to="/PracticeTest"> 
        <button className="custom-button" onClick={handleSubmit}> generate practice test </button>
      </Link>
      <label style = {{padding: '20px'}}></label>
      <Link to="/NotesSummary"> 
        <button className="custom-button" onClick={handleSubmit}> generate notes summary </button>
      </Link>
    </div>
  );
}

function UploadContent() {
  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p style = {{paddingTop: '100px'}}> upload assignments, notes, past exams, etc. </p>
          <UploadFiles/>
        </div>
      </header>
    </div>
  );
}

export default UploadContent;
