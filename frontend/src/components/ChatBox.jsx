import { useState } from "react";
import api from "../services/api";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);

  const askQuestion = async () => {
    if (!question.trim()) return;

    const userQuestion = question;

    setMessages((prev) => [
      ...prev,
      {
        type: "user",
        text: userQuestion,
      },
    ]);

    setQuestion("");

    try {
      const response = await api.post(
        "/ask-policy",
        {
          question: userQuestion,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          type: "ai",
          text: response.data.answer,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          type: "ai",
          text: "Unable to generate response.",
        },
      ]);
    }
  };

  return (
    <div className="bg-white border border-gray-200 rounded-2xl p-6">
      <h2 className="text-2xl font-bold mb-4">
        Policy Chat
      </h2>

      <div className="h-80 overflow-y-auto border rounded-xl p-4 mb-4 bg-gray-50">
        {messages.length === 0 && (
          <p className="text-gray-500">
            Ask questions about the uploaded policy.
          </p>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`mb-4 flex ${
              msg.type === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >
            <div
              className={`max-w-[80%] px-4 py-3 rounded-xl ${
                msg.type === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-white border"
              }`}
            >
              {msg.text}
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-3">
        <input
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
          placeholder="Ask about uploaded policy..."
          className="flex-1 border rounded-lg p-3"
        />

        <button
          onClick={askQuestion}
          className="bg-blue-600 text-white px-6 rounded-lg"
        >
          Send
        </button>
      </div>
    </div>
  );
}