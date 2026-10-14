import { useEffect, useState } from "react";
import QuestionsList from "./components/QuestionsList";
import AnswerForm from "./components/AnswerForm.jsx";

function App() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [answers, setAnswers] = useState([])
  const selectedQuestion = questions.find((q) => q.id == selectedId)
  const selectedAnswers = answers.filter((a) => a.question_id == selectedId)
    function saveAnswer(text) {
      fetch("api/answers", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({"question_id": selectedId, "text": text} )
      })
          .then((res) => {
              if (!res.ok) throw new Error(`HTTP ${res.status}`);
              return res.json();
          })
          .then((saved) => setAnswers([...answers, saved]))
          .catch((err) => setError((err.message)));
    }

  useEffect(() => {
    fetch("/api/questions")
        .then((res) => {
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          return res.json();
        })
        .then((data) => setQuestions(data))
        .catch((err) => setError(err.message))
        .finally(() => setLoading(false));
  }, []);

    useEffect(() => {
        fetch("/api/answers")
            .then((res) => {
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                return res.json();
            })
            .then((data) => setAnswers(data))
            .catch((err) => setError((err.message)))

    }, []);
    if (loading) return <p>Loading questions...</p>;
    if (error) return <p>Error: {error}</p>;


  return (
      <main>
        <h1>Interview Coach</h1>
          <QuestionsList
              questions={questions}
              selectedId={selectedId}
              onSelect={setSelectedId}
          />
          {selectedQuestion && <AnswerForm
         question={selectedQuestion}
         onSave={saveAnswer}/>}
          {selectedQuestion && <ul>
              {selectedAnswers.map((a) => (
                  <li
                      key={a.id}
                      style={{fontWeight: a.id === selectedId ? "bold" : "normal"}}
                  >
                      {a.text}
                  </li>
              ))}
          </ul>}
      </main>
  );
}

export default App;