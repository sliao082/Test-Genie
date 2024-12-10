import './App.css';
// import UploadContent from './UploadContent';
// import Home from './Home';

// const PDFView = ({ pdfUrl }) => {
//   return (
//     <div>
//       <iframe
//         src={pdfUrl}
//         width="1000px"
//         height="700px"
//         title="PDFView"
//       ></iframe>
//     </div>
//   );
// };

function PracticeTest() {
  // default reponse
  const response = "Q:What is the primary purpose of a git branch? S:To isolate separate streams of work S:To save small snapshots of code as you work on your project S:To store code about to be committed S:To keep a history of commits A:To isolate separate streams of work Q:How often should you commit? S:Once for every 25-50 lines of code S:Once per day S:Once per week S:Once every time you make a small amount of progress or have work to save A:Once every time you make a small amount of progress or have work to save Q:What is the best way you and your teammate could avoid merge conflicts? S:Only commit on separate branches and never merge S:Only commit on master S:Use Subversion instead of Git S:Don’t edit the same files on different branches A:Don’t edit the same files on different branches Q:Which of the following is the correct command to check out a new branch? S:git add -b new_branch S:git branch new_branch S:git switch to new_branch S:git checkout -b new_branch A:git checkout -b new_branch Q:Which of the following is the correct command to check out an existing branch? S:git branch -e existing_branch S:git switch to existing_branch S:git checkout existing_branch S:git checkout -b existing_branch A:git checkout existing_branch Q:What is a commit? S:A command used to terminate a software development project S:A snapshot/record of changes to code metadata (author, timestamp, etc.) that were in the staging area S:A snapshot/record of changes to code and its metadata (author, timestamp, etc.) that were in the staging area S:A measurement of the complexity of a software project, calculated based on the number of files and lines of code changed. A:A snapshot/record of changes to code and its metadata (author, timestamp, etc.) that were in the staging area Q:Which of the following commands adds all files in the src/ folder to the staging area and creates a commit? (we recommend double checking with Git docs!) S:cd src/ && git add . && git commit -m “some message” S:git commit src/ -am “some message” S:git add src/ && git commit -m “some message” S:cd src/ && git add -A && git commit src/ -m “some message” A:git add src/ && git commit -m “some message” A:cd src/ && git add . && git commit -m “some message”";
  const questions = response.split("Q:");

  const questionElements = questions.filter((q) => q.trim()).map((question, index) => {
    const parts = question.split(/(S:|A:)/).filter((part) => part.trim()); 
    return (
      <div key={index}>
        <p>&nbsp;</p>
        <p>Q: {parts[0].trim()}</p>
        {parts.slice(1).map((part, subIndex, arr) => {
          if (part === "S:") {
            return <p key={subIndex}>- {arr[subIndex + 1]?.trim()}</p>;
          } else if (part === "A:") {
            return <p key={subIndex}>{part} {arr[subIndex + 1]?.trim()}</p>;
          } else {
            return null;
          }
        })}
      </div>
    );
  });

  return (
    <div className="App">
      <header className="App-body">
        <div>
          <div style = {{textAlign: "left", fontSize: "20px", paddingLeft: "100px", paddingRight: "50px", paddingBottom: "50px"}}> {questionElements} </div>
        </div>
      </header>
    </div>
  );
}

export default PracticeTest;
