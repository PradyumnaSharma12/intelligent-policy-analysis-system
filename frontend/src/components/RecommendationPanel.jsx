export default function RecommendationPanel({
  policyData,
}) {
  if (!policyData) return null;

  return (
    <div className="bg-white border border-gray-200 rounded-2xl p-6">
      <h2 className="text-2xl font-bold mb-4">
        AI Recommendations
      </h2>

      <div className="whitespace-pre-wrap">
        {policyData.ai_recommendations}
      </div>
    </div>
  );
}