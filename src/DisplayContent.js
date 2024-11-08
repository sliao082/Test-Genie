import './App.css';
import UploadContent from './UploadContent';
import Home from './Home';

const PDFView = ({ pdfUrl }) => {
  return (
    <div>
      <iframe
        src={pdfUrl}
        width="1000px"
        height="700px"
        title="PDFView"
      ></iframe>
    </div>
  );
};

function DisplayContent() {
  const pdfUrl = "/testPDFs/testPDF1.pdf";
  return (
    <div className="App">
      <header className="App-body">
        <div>
          <p> previously generated content: </p>
          {/* <PDFView pdfUrl={pdfUrl} /> */}
          <PDFView pdfUrl={"/testPDFs/testPDF1.pdf"} />
          <PDFView pdfUrl={"/testPDFs/testPDF2.pdf"} />
          <PDFView pdfUrl={"/testPDFs/testPDF3.pdf"} />
        </div>
      </header>
    </div>
  );
}

export default DisplayContent;
