// import React, { useState } from 'react';
import './App.css';
import { Link } from 'react-router-dom';
import UploadContent from './UploadContent';
import DisplayContent from './DisplayContent';

function Home() {
  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p style = {{fontSize: '50px'}} ><b> TEST GENIE </b></p>
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
