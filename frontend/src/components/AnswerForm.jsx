import { useEffect, useState } from "react";

function AnswerForm({question, onSave, answers}) {
    const [text, setText] = useState("");
    const canSubmit = text.trim() !== "";

    function handleSubmit(e) {
        e.preventDefault();
        onSave(text);
        setText("");
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>{question.text}</h2>
            <textarea value={text} onChange={(e) => setText(e.target.value)}></textarea>
            <button disabled={!canSubmit}>Save</button>
        </form>
    )

}

export default AnswerForm