export default function AnalysisCards({
  policyData,
}) {
  if (!policyData) return null;

  const cards = [
    {
      title: "Category",
      value: policyData.predicted_category,
    },
    {
      title: "Characters",
      value: policyData.characters_extracted,
    },
    {
      title: "Status",
      value: "Indexed",
    },
    {
      title: "File",
      value: policyData.filename,
    },
  ];

  return (
    <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-white border border-gray-200 rounded-2xl p-6"
        >
          <h3 className="text-gray-500">
            {card.title}
          </h3>

          <p className="text-xl font-bold mt-2">
            {card.value}
          </p>
        </div>
      ))}
    </div>
  );
}