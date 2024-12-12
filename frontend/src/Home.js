import './App.css';
import { Link } from 'react-router-dom';
function Home() {
  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p style={{ fontSize: '50px', paddingTop: '60px' }} ><b> TEST GENIE </b></p>
          <p> Test Genie analyzes the textbooks, assignments, and past exams to </p>
          <p> create study materials for students to utilize to study. </p>
          <div style={{ padding: '20px' }}></div>
          <div>
            <Link to="/UploadContent">
              <button className="big-button"> Generate Content </button>
            </Link>
            <label style={{ padding: '20px' }}></label>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Home;
