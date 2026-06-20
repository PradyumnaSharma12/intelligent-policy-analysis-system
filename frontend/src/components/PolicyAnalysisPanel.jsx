export default function PolicyAnalysisPanel({
  policyData,
}) {
  if (!policyData) return null;

  return (
    <div className="bg-white border border-gray-200 rounded-2xl p-6">
      <h2 className="text-2xl font-bold mb-4">
        Policy Analysis
      </h2>

      <div className="whitespace-pre-wrap">
        {policyData.policy_analysis}
      </div>
    </div>
  );
}