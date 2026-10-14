
function QuestionsList({questions, selectedId, onSelect}) {
    return (
        <ul>
            {questions.map((q) => (
                <li
                key={q.id}
                onClick={() => onSelect(q.id)}
                style={{fontWeight: q.id === selectedId ? "bold" : "normal"}}
                >
                    {q.text}
                </li>
            ))}
        </ul>
    );
}

export default QuestionsList