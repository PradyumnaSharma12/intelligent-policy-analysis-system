export default function SummaryPanel({ summary }) {
  if (!summary) return null;

  return (
    <div className="bg-white border border-gray-200 rounded-2xl p-6">
      <h2 className="text-2xl font-bold mb-4">
        Executive Summary
      </h2>

      <div className="whitespace-pre-wrap text-gray-700 leading-relaxed">
        {summary}
      </div>
    </div>
  );
}
