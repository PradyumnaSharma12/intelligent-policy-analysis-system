import {
  Brain,
  FileText,
  Search,
  Sparkles,
} from "lucide-react";

export default function Features() {
  const features = [
    {
      title: "Policy Summarization",
      icon: <FileText size={40} />,
      desc: "Generate concise summaries instantly."
    },
    {
      title: "AI Classification",
      icon: <Brain size={40} />,
      desc: "Categorize policies using ML models."
    },
    {
      title: "RAG Question Answering",
      icon: <Search size={40} />,
      desc: "Ask questions directly from policy documents."
    },
    {
      title: "Recommendations",
      icon: <Sparkles size={40} />,
      desc: "Receive AI-powered policy recommendations."
    }
  ];

  return (
    <section
      id="features"
      className="max-w-7xl mx-auto px-8 py-20"
    >
      <h2 className="text-4xl font-bold text-center mb-14">
        Features
      </h2>

      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
        {features.map((feature) => (
          <div
            key={feature.title}
            className="bg-white border border-gray-200 rounded-2xl p-8 shadow-sm"
          >
            <div className="text-blue-600 mb-4">
              {feature.icon}
            </div>

            <h3 className="font-semibold text-xl mb-2">
              {feature.title}
            </h3>

            <p className="text-gray-600">
              {feature.desc}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}