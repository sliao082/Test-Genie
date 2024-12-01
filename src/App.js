import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UploadContent from './UploadContent';
import DisplayContent from './DisplayContent';
import Home from './Home';

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
          Hello Guest! </b></label>
        </div>
      </header>
      <Router> 
        <Routes> 
          <Route path="/" element={<Home/>} /> 
          <Route path="/UploadContent" element={<UploadContent/>} /> 
          <Route path="/DisplayContent" element={<DisplayContent/>} /> 
        </Routes> 
      </Router>
    </div>
  );
}

export default App;
